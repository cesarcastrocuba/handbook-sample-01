"""The edition preview is read-only; release verification checks the actual deployed URL."""
from pathlib import Path
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[2]


class ReleaseWorkflowTests(unittest.TestCase):
    def test_release_verifies_the_deploy_output_without_write_credentials(self):
        jobs = yaml.safe_load((ROOT / '.github/workflows/release.yml').read_text())['jobs']
        self.assertEqual(jobs['deploy']['outputs']['page_url'], '${{ steps.deployment.outputs.page_url }}')
        verify = jobs['verify']
        self.assertEqual(verify['needs'], 'deploy')
        self.assertEqual(verify['permissions'], {'contents': 'read'})
        checkout = next(step for step in verify['steps'] if step.get('uses', '').startswith('actions/checkout@'))
        self.assertIs(checkout['with']['persist-credentials'], False)
        install = next(step for step in verify['steps'] if 'pip install' in step.get('run', ''))
        self.assertIn('-r requirements.txt', install['run'])
        check = next(step for step in verify['steps'] if 'handbook_toolkit.site_check' in step.get('run', ''))
        self.assertEqual(check['env']['PAGE_URL'], '${{ needs.deploy.outputs.page_url }}')
        self.assertEqual(check['run'], 'python3 -m handbook_toolkit.site_check "$PAGE_URL"')

    def test_ci_builds_and_uploads_a_non_release_preview(self):
        workflow = yaml.safe_load((ROOT / '.github/workflows/check.yml').read_text())
        self.assertEqual(workflow['permissions'], {'contents': 'read'})
        steps = workflow['jobs']['check']['steps']
        self.assertTrue(any(step.get('run') == 'make full' for step in steps))
        build = next(step['run'] for step in steps if 'handbook-toolkit build-book' in step.get('run', ''))
        self.assertIn('--preview', build)
        self.assertIn('--require-page-numbers', build)
        self.assertIn('--version "$VERSION-preview"', build)
        upload = next(step for step in steps if step.get('uses', '').startswith('actions/upload-artifact@'))
        self.assertEqual(upload['with']['path'], '${{ runner.temp }}/edition-preview')
        self.assertEqual(upload['with']['if-no-files-found'], 'error')
        for step in steps:
            self.assertNotIn('deploy-pages', step.get('uses', ''))
            self.assertNotIn('gh release', step.get('run', ''))


if __name__ == '__main__':
    unittest.main()
