import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
def module(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/f'{name}.py')
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
G=module('release_gate'); P=module('publish_release')
class GateTests(unittest.TestCase):
    def setUp(self):
        self.r=dict(version='0.2.0',source_sha='a'*40,artifact_sha256='b'*64,approved=True,
                    scope='github-release',reviewer='owner',approved_at='2026-11-15',evidence={})
        self.files={'docs/validation/runtime.log':b'actual test log fixture'}
        for key in G.REQUIRED:
            self.r['evidence'][key]=dict(path=f'docs/validation/{key}.json',sha256=hashlib.sha256(b'evidence').hexdigest(),
                status='PASS',host_version='test-host',platform='test-platform',input='task',observed='result',date='2026-11-15',source_sha='a'*40,version='0.2.0')
            proof=copy.deepcopy(self.r['evidence'][key]);proof.update(operation=key,mode='actual-host-runtime',artifact_sha256='b'*64,update_scope='remote-candidate-end-to-end',log={'path':'docs/validation/runtime.log','sha256':hashlib.sha256(self.files['docs/validation/runtime.log']).hexdigest()})
            body=json.dumps(proof).encode();self.files[proof['path']]=body
            self.r['evidence'][key]['sha256']=hashlib.sha256(body).hexdigest()
    def valid(self,r): return G.validate(r,lambda p:self.files[p],lambda s:True)
    def test_arbitrary_or_synthetic_body(self):
        path=self.r['evidence']['codex-update']['path']
        for body in [b'evidence',json.dumps({'status':'SKIPPED'}).encode()]:
            self.files[path]=body;self.r['evidence']['codex-update']['sha256']=hashlib.sha256(body).hexdigest()
            with self.assertRaises(ValueError): self.valid(self.r)
    def test_local_update_body_rejected(self):
        path=self.r['evidence']['codex-update']['path'];proof=json.loads(self.files[path]);proof['update_scope']='local-synthetic'
        self.files[path]=json.dumps(proof).encode();self.r['evidence']['codex-update']['sha256']=hashlib.sha256(self.files[path]).hexdigest()
        with self.assertRaises(ValueError): self.valid(self.r)
    def test_complete(self): self.assertEqual(self.valid(self.r),('0.2.0','a'*40))
    def test_missing_waived_stale_or_tampered_evidence(self):
        for field,value in [('status','SKIPPED'),('status','structural-pass'),('sha256','b'*64),('source_sha','c'*40),('version','0.1.0'),('path','../secret'),('path','/etc/passwd')]:
            with self.subTest(field=field,value=value):
                r=copy.deepcopy(self.r);r['evidence']['codex-invoke'][field]=value
                with self.assertRaises(ValueError): self.valid(r)
        self.r['evidence'].pop('claude-invoke')
        with self.assertRaises(ValueError): self.valid(self.r)
    def test_invalid_version_approval_sha(self):
        for field,value in [('version','0.1.0'),('version','1.0.0-rc1'),('version','1.0.0\ncommand'),('source_sha','main'),('approved',False),('scope','daily')]:
            r=copy.deepcopy(self.r);r[field]=value
            with self.assertRaises(ValueError): self.valid(r)
    def test_non_ancestor(self):
        with self.assertRaises(ValueError): G.validate(self.r,lambda p:b'evidence',lambda s:False)

class PublisherTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.p=Path(self.tmp.name)
        for n in ['game-development-plugins-0.2.0.zip','SHA256SUMS','RELEASE-NOTES.md']: (self.p/n).write_bytes(b'test')
        self.digest=hashlib.sha256(b'test').hexdigest();self.calls=[]
    def api(self,path,**kw):
        self.calls.append((path,kw))
        if path.startswith('/git/ref/'): return None
        if path.startswith('/releases?'): return []
        if path == '/git/refs': return {}
        if path == '/releases': return dict(id=1,upload_url='https://uploads.github.com/repos/test/assets{?name}')
        if path.startswith('https://'): return dict(digest='sha256:'+self.digest,size=4)
        raise AssertionError(path)
    def test_existing_tag_never_mutates(self):
        with self.assertRaises(ValueError): P.publish(self.p,'0.2.0','a'*40,self.digest,lambda *a,**k:{'object':{}})
    def test_existing_draft_never_mutates(self):
        def api(path,**kw):
            self.calls.append((path,kw));return None if path.startswith('/git/ref/') else [dict(tag_name='v0.2.0')]
        with self.assertRaises(ValueError): P.publish(self.p,'0.2.0','a'*40,self.digest,api)
        self.assertFalse(any(k.get('method') for _,k in self.calls))
    def test_non_increasing_version_rejected(self):
        def api(path,**kw):
            self.calls.append((path,kw)); return None if path.startswith('/git/ref/') else [dict(tag_name='v1.0.0')]
        with self.assertRaises(ValueError): P.publish(self.p,'0.2.0','a'*40,self.digest,api)
        self.assertFalse(any(k.get('method') for _,k in self.calls))
    def test_bad_digest_never_contacts_network(self):
        with self.assertRaises(ValueError): P.publish(self.p,'0.2.0','a'*40,'0'*64,self.api)
        self.assertEqual(self.calls,[])
    def test_failed_upload_leaves_draft_not_public(self):
        def api(path,**kw):
            result=self.api(path,**kw)
            if path.startswith('https://'): result['digest']='sha256:wrong'
            return result
        with self.assertRaises(ValueError): P.publish(self.p,'0.2.0','a'*40,self.digest,api)
        self.assertFalse(any(k.get('method')=='PATCH' for _,k in self.calls))
    def test_mock_success_and_target_binding(self):
        def api(path,**kw):
            if path.startswith('/git/ref/') and any(p=='/git/refs' for p,k in self.calls): return {'object':{'type':'commit','sha':'a'*40}}
            if path=='/releases/1': return dict(draft=False,tag_name='v0.2.0',html_url='mock://release')
            return self.api(path,**kw)
        P.publish(self.p,'0.2.0','a'*40,self.digest,api)
        self.assertIn(('/git/refs',{'method':'POST','data':{'ref':'refs/tags/v0.2.0','sha':'a'*40}}),self.calls)
    def test_workflow_is_main_only_and_pinned(self):
        text=(ROOT/'.github/workflows/release.yml').read_text()
        self.assertIn('branches: [main]',text)
        self.assertNotIn('pull_request_target',text)
        self.assertNotIn('workflow_run',text)
        self.assertEqual(text.count('contents: write'),1)
        for line in text.splitlines():
            if 'uses:' in line: self.assertRegex(line,r'@[0-9a-f]{40} #')
if __name__=='__main__': unittest.main()
