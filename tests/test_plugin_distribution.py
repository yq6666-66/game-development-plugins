import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile
import shutil

ROOT = Path(__file__).resolve().parents[1]

class DistributionTests(unittest.TestCase):
    def module(self):
        path = ROOT / 'scripts/build_plugin.py'
        self.assertTrue(path.exists(), 'distribution builder must exist')
        spec = importlib.util.spec_from_file_location('build_plugin', path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    def test_manifests_and_seven_skills(self):
        self.assertEqual(self.module().validate(ROOT), [])

    def test_reproducible_and_self_contained_archive(self):
        mod = self.module()
        with tempfile.TemporaryDirectory() as td:
            a, b = Path(td)/'a.zip', Path(td)/'b.zip'
            mod.build(ROOT, a); mod.build(ROOT, b)
            self.assertEqual(a.read_bytes(), b.read_bytes())
            with zipfile.ZipFile(a) as archive:
                names = archive.namelist()
                self.assertEqual(sum(n.endswith('/SKILL.md') for n in names), 7)
                self.assertIn('plugin.json', names)
                self.assertIn('.claude-plugin/plugin.json', names)
                self.assertNotIn('.git/config', names)
                self.assertNotIn('docs/research/daily/2026-11-15.md', names)
                archive.extractall(Path(td)/'unpacked')
            self.assertEqual(mod.validate(Path(td)/'unpacked'), [])

    def test_rejects_symlinks(self):
        mod = self.module()
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)/'repo'; shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('.git', '__pycache__'))
            (root/'skills/leak').symlink_to('/tmp', target_is_directory=True)
            self.assertTrue(mod.validate(root))

    def test_version_mismatch_rejected(self):
        mod = self.module()
        import json
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)/'repo'; shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('.git', '__pycache__'))
            path = root/'.claude-plugin/plugin.json'; data=json.loads(path.read_text(encoding='utf-8')); data['version']='9.9.9'; path.write_text(json.dumps(data),encoding='utf-8')
            self.assertTrue(mod.validate(root))

    def test_existing_output_preserved(self):
        mod=self.module()
        with tempfile.TemporaryDirectory() as td:
            path=Path(td)/'existing.zip';path.write_bytes(b'user content')
            with self.assertRaises(FileExistsError): mod.build(ROOT,path)
            self.assertEqual(path.read_bytes(),b'user content')

    def test_catalog_escape_rejected(self):
        mod=self.module()
        import json
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)/'repo';shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('.git','__pycache__'))
            path=root/'.agents/plugins/marketplace.json';data=json.loads(path.read_text(encoding='utf-8'));data['plugins'][0]['source']['path']='../outside';path.write_text(json.dumps(data),encoding='utf-8')
            self.assertTrue(mod.validate(root))

    def test_host_catalog_shapes_not_interchangeable(self):
        import json
        mod=self.module()
        for name,source in [('.claude-plugin/marketplace.json', {'source':'local','path':'./'}), ('.agents/plugins/marketplace.json','./')]:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as td:
                root=Path(td)/'repo';shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('.git','__pycache__'))
                path=root/name;data=json.loads(path.read_text(encoding='utf-8'));data['plugins'][0]['source']=source
                path.write_text(json.dumps(data),encoding='utf-8')
                self.assertTrue(mod.validate(root))

if __name__ == '__main__': unittest.main()
