import importlib.util
from pathlib import Path
import tempfile
import unittest

root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validator', root/'scripts/validate_package.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)

class PackagingTests(unittest.TestCase):
    def build(self, text, files=None):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        skill = root/'skills/example'
        skill.mkdir(parents=True)
        (skill/'SKILL.md').write_text(text)
        for name, content in (files or {}).items():
            path = skill/name; path.parent.mkdir(parents=True, exist_ok=True); path.write_text(content)
        return root
    def test_repository(self):
        self.assertEqual([], validator.validate(root))
    def test_valid_reference(self):
        r = self.build('---\nname: example\ndescription: Test example.\n---\n[Detail](references/detail.md)', {'references/detail.md':'Details'})
        self.assertEqual([], validator.validate(r))
    def test_missing_reference_is_detected(self):
        r = self.build('---\nname: example\ndescription: Test example.\n---\n[Detail](references/missing.md)')
        self.assertTrue(any('missing reference' in e for e in validator.validate(r)))
    def test_bad_frontmatter_is_detected(self):
        r = self.build('# No frontmatter')
        self.assertTrue(any('frontmatter' in e for e in validator.validate(r)))
    def test_mismatched_name_is_detected(self):
        r = self.build('---\nname: another\ndescription: Test example.\n---\n')
        self.assertTrue(any('mismatched name' in e for e in validator.validate(r)))
    def test_external_local_dependency_is_detected(self):
        r = self.build('---\nname: example\ndescription: Test example.\n---\n[Outside](../../outside.md)')
        self.assertTrue(any('escapes' in e for e in validator.validate(r)))

if __name__ == '__main__': unittest.main()
