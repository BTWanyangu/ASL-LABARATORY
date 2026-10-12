from pathlib import Path
import zipfile,subprocess,tempfile,hashlib,os
ROOT=Path(__file__).resolve().parents[1]
TARGET=ROOT.parent.parent/'ASL-Website-Expanded-Services.zip'
EXCLUDES={'__pycache__','node_modules','.git','.pytest_cache'}
with zipfile.ZipFile(TARGET,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7) as z:
 for f in sorted(ROOT.rglob('*')):
  if not f.is_file() or any(p in EXCLUDES for p in f.relative_to(ROOT).parts) or f.suffix=='.pyc':continue
  z.write(f,arcname='asl-website/'+str(f.relative_to(ROOT)))
with zipfile.ZipFile(TARGET) as z:
 bad=z.testzip()
 assert bad is None,bad
 files=set(z.namelist())
 for needed in ['package.json','render.yaml','README.md','HANDOVER.md','QA_REPORT.md','IMAGE_MANIFEST.md','SERVICE_SCOPE_AND_REFERENCES.md','dist/trade/index.html','dist/services/mineral-buying/index.html','dist/services/mineral-trading/index.html','dist/services/refining/index.html','dist/index.html','dist/contact/index.html','dist/downloads/sample-submission-checklist.pdf','public/images/brand/asl-original-logo.png']:
  assert 'asl-website/'+needed in files,needed
 with tempfile.TemporaryDirectory() as temp:
  z.extractall(temp)
  ext=Path(temp)/'asl-website'
  for cmd in [['npm','ci','--offline'],['npm','run','build'],['npm','test'],['npm','run','typecheck']]:
   res=subprocess.run(cmd,cwd=ext,capture_output=True,text=True,timeout=90)
   if res.returncode:
    raise RuntimeError(f'Clean ZIP check failed for {cmd}: '+res.stdout+'\n'+res.stderr)
  print('Clean extraction/build/tests/typecheck: PASS')
print('ZIP verified:',TARGET,'files:',len(files),'bytes:',TARGET.stat().st_size,'sha256:',hashlib.sha256(TARGET.read_bytes()).hexdigest())
