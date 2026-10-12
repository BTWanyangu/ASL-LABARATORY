"""Chromium rendering and interaction tests using inlined local assets.
Site navigation in this sandbox is restricted by browser administrator policy; HTML
is loaded with set_content, while a separate HTTP smoke test verifies deep URLs.
"""
import base64,subprocess,time,requests,mimetypes,re
from pathlib import Path
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]; DIST=ROOT/'dist'
CSS=(DIST/'styles.css').read_text()
CSS=re.sub(r'@import url\(.*?\);','',CSS)
JS=(DIST/'app.js').read_text()
def page_markup(route):
 loc=DIST/route.strip('/')/'index.html' if route.strip('/') else DIST/'index.html'
 soup=BeautifulSoup(loc.read_text(),'html.parser')
 for link in soup.find_all('link',rel='stylesheet'):
  tag=soup.new_tag('style');tag.string=CSS;link.replace_with(tag)
 for script in soup.find_all('script',src=True):
  tag=soup.new_tag('script');tag.string=JS;script.decompose();soup.body.append(tag)
 for image in soup.find_all('img',src=True):
  file=DIST/image['src'].lstrip('/');mime=mimetypes.guess_type(str(file))[0]
  image['src']='data:'+mime+';base64,'+base64.b64encode(file.read_bytes()).decode()
 return str(soup)

def run():
 with sync_playwright() as pw:
  b=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  screen=ROOT/'tests/screenshots';screen.mkdir(exist_ok=True)
  for width in [320,375,768,1024,1440]:
   p=b.new_page(viewport={'width':width,'height':900},device_scale_factor=1)
   errors=[];p.on('pageerror',lambda err:errors.append(str(err)))
   p.set_content(page_markup('/'),wait_until='domcontentloaded',timeout=30000)
   p.wait_for_timeout(80)
   res=p.evaluate('''()=>({doc:document.documentElement.scrollWidth,win:innerWidth,heading:!!document.querySelector('h1')})''')
   assert res['doc']<=width+1,(width,res)
   assert not errors,(width,errors)
   if width in [375,1440]:
    p.evaluate('''async()=>{await Promise.all([...document.images].map(async i=>{i.loading='eager';try{await i.decode()}catch(e){}}))}''')
    p.screenshot(path=str(screen/f'home-{width}.png'),full_page=True)
   if width==375:
    p.locator('.nav-toggle').click();assert p.locator('.mobile-navigation').is_visible()
    p.keyboard.press('Escape');assert p.locator('#mobile-navigation').is_hidden()
   if width==1440:
    p.locator('.menu-trigger').click();assert p.locator('.dropdown').is_visible()
    p.keyboard.press('Escape');assert p.locator('.dropdown').is_hidden()
   print('viewport',width,'PASS',res)
   p.close()
  p=b.new_page(viewport={'width':1440,'height':900})
  routes=__import__('json').loads((DIST/'route-manifest.json').read_text())['routes']
  for route in routes:
   p.set_content(page_markup(route),wait_until='domcontentloaded',timeout=30000)
   assert p.locator('h1').count()==1,route
   assert p.title().strip(),route
  print('routes PASS',len(routes))
  # Because set_content() does not navigate, service preselection needs location
  # mocking. Form submit, validation and honest draft can still be exercised.
  p.set_content(page_markup('/contact/'),wait_until='domcontentloaded')
  p.locator('.form-submit').click();assert p.locator('#form-status').inner_text().strip()
  p.locator('#name').fill('Website Tester')
  p.locator('#email').fill('tester@example.com')
  p.locator('#material').fill('A gold sample weighing approximately 10 g')
  p.locator('#message').fill('Please advise about possible assay scope.')
  p.locator('#service').select_option('mineral-trading')
  p.locator('#consent').check()
  p.locator('.form-submit').click()
  assert p.locator('#enquiry-output').is_visible()
  assert 'has not been sent' in p.locator('#enquiry-output').inner_text()
  assert 'Mineral trading' in p.locator('#enquiry-draft').inner_text()
  p.screenshot(path=str(screen/'contact-desktop.png'),full_page=True)
  print('form PASS validation, draft generation, non-transmission claim')
  b.close()
  for pdf in ['sample-submission-checklist.pdf','material-enquiry-guide.pdf','understanding-results.pdf']:
   f=DIST/'downloads'/pdf
   assert f.is_file() and f.read_bytes()[:4]==b'%PDF'
  print('downloads PASS')
  server=subprocess.Popen(['python3','-m','http.server','4181','--directory',str(DIST)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
  try:
   for _ in range(30):
    try:
     if requests.get('http://127.0.0.1:4181/').status_code==200:break
    except Exception:time.sleep(.2)
   for route in routes:
    response=requests.get('http://127.0.0.1:4181'+route,timeout=5)
    assert response.status_code==200,(route,response.status_code)
   print('HTTP deep routes PASS',len(routes))
  finally:server.terminate();server.wait()
if __name__=='__main__':run()
