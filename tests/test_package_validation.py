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

    def test_explicit_and_collapsed_references(self):
        r = self.build('---\nname: example\ndescription: Test example.\n---\n[Full][ Detail ] [detail][]\n[detail]: references/detail.md', {'references/detail.md':'Details'})
        self.assertEqual([], validator.validate(r))
    def test_reference_style_missing_file_is_detected(self):
        r = self.build('---\nname: example\ndescription: Test example.\n---\n[Detail][detail]\n[detail]: references/missing.md')
        self.assertTrue(any('missing reference' in e for e in validator.validate(r)))
    def test_reference_style_external_dependency_is_detected(self):
        r = self.build('---\nname: example\ndescription: Test example.\n---\n[Detail][detail]\n[detail]: ../../outside.md')
        self.assertTrue(any('escapes' in e for e in validator.validate(r)))
    def test_missing_label_and_duplicate_definition(self):
        targets, errors = validator.markdown_targets('[x][absent] [A][]\n[a]: one.md\n[A]: two.md')
        self.assertIn('one.md', targets)
        self.assertTrue(any('undefined' in e for e in errors))
        self.assertTrue(any('duplicate' in e for e in errors))
    def test_code_examples_do_not_create_dependencies(self):
        targets, errors = validator.markdown_targets('`[example][missing]`\n```md\n[Detail](missing.md)\n```\n~~~\n[x][missing]\n~~~\n[Real](#section)')
        self.assertEqual(targets, ['#section'])
        self.assertEqual(errors, [])

    def test_multiline_code_spans_and_exact_delimiters(self):
        for example in ('`example\n[Detail](missing.md)\nend`',
                        '``example ` inner\n[Detail][missing]\nend``'):
            self.assertEqual((['real.md'], []), validator.markdown_targets(example + '\n[Real](real.md)'))
        self.assertEqual((['real.md'], []), validator.markdown_targets('`unclosed [Real](real.md)'))

    def test_escaped_opening_brackets_and_backslash_parity(self):
        for example in (r'\[not-a-link][missing]', r'\[Detail](missing.md)',
                        r'\\\[not-a-link][missing]'):
            self.assertEqual(([], []), validator.markdown_targets(example))
        self.assertEqual((['real.md'], []), validator.markdown_targets(r'\\[Real](real.md)'))

    def test_defined_shortcut_and_ordinary_brackets(self):
        targets, errors = validator.markdown_targets('[Guide] [ordinary text]\n[guide]: references/missing.md')
        self.assertEqual(targets, ['references/missing.md'])
        self.assertEqual(errors, [])
    def test_external_and_fragment_references(self):
        r = self.build('---\nname: example\ndescription: Test example.\n---\n[Site][s] [Here][h]\n[s]: https://example.com/doc\n[h]: #section')
        self.assertEqual([], validator.validate(r))

if __name__ == '__main__': unittest.main()
