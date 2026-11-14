"""Navigation contract only; does not execute a host or game."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
NAV = ROOT / 'docs' / 'navigation'
CATEGORIES = (
    '01-design-prototype', '02-architecture-engineering', '03-visual-art',
    '04-gameplay-systems', '05-ui-experience', '06-testing-performance',
    '07-build-collaboration', '08-tools-resources',
)


class NavigationTests(unittest.TestCase):
    def test_eight_categories_are_linked_in_both_indexes(self):
        for suffix in ('', '.en'):
            index = (NAV / f'README{suffix}.md').read_text()
            for slug in CATEGORIES:
                with self.subTest(language=suffix, category=slug):
                    self.assertIn(f'(categories/{slug}{suffix}.md)', index)
                    self.assertTrue((NAV / 'categories' / f'{slug}{suffix}.md').is_file())

    def test_guides_have_routes_evidence_and_language_switch(self):
        for slug in CATEGORIES:
            for suffix in ('', '.en'):
                with self.subTest(language=suffix, category=slug):
                    text = (NAV / 'categories' / f'{slug}{suffix}.md').read_text()
                    other = '' if suffix else '.en'
                    self.assertIn(f'({slug}{other}.md)', text)
                    required = ('## Inputs and output', '**New project:**', '**Existing project:**',
                                '## Available entry', '## Smallest check', 'not another installable Skill') if suffix else (
                                '## 输入与交付', '**从零开发：**', '**接手项目：**',
                                '## 当前可用入口', '## 最小检查', '不是新增可安装 Skill')
                    for item in required:
                        self.assertIn(item, text)

    def test_navigation_local_file_links_exist(self):
        for path in NAV.rglob('*.md'):
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                if '://' in target or target.startswith('#'):
                    continue
                with self.subTest(page=str(path.relative_to(ROOT)), target=target):
                    self.assertTrue((path.parent / target.split('#')[0]).is_file())


if __name__ == '__main__':
    unittest.main()
