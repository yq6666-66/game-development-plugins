"""Exercise copied-package independence, not model reasoning or engine behavior."""
from pathlib import Path
import importlib.util
import shutil
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('package_validator',ROOT/'scripts/validate_package.py')
validator=importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)
class PortableSkillTests(unittest.TestCase):
    def test_each_skill_can_be_copied_without_outer_repository(self):
        for source in (ROOT/'skills').iterdir():
            if not source.is_dir(): continue
            with self.subTest(skill=source.name), tempfile.TemporaryDirectory() as tmp:
                root=Path(tmp)
                shutil.copytree(source,root/'skills'/source.name)
                self.assertEqual(validator.validate(root),[])
    def test_removed_english_reference_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);target=root/'skills'/'game-ui-design'
            shutil.copytree(ROOT/'skills'/'game-ui-design',target)
            (target/'references/workflow.en.md').unlink()
            self.assertTrue(any('missing reference' in e for e in validator.validate(root)))
