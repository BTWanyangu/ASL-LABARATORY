"""Focused expanded-services browser and mobile menu smoke test."""
from pathlib import Path
from playwright.sync_api import sync_playwright
from browser_smoke import page_markup, DIST, ROOT

with sync_playwright() as pw:
 b=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 out=ROOT/'tests/screenshots';out.mkdir(exist_ok=True)
 for route in ['/services/','/trade/','/services/refining/','/services/mineral-buying/','/services/mineral-trading/']:
  for width in [320,375,768,1024,1440]:
   p=b.new_page(viewport={'width':width,'height':900})
   errors=[];p.on('pageerror',lambda err:errors.append(str(err)))
   p.set_content(page_markup(route))
   sizes=p.evaluate('''()=>({doc:document.documentElement.scrollWidth,win:innerWidth})''')
   assert sizes['doc']<=sizes['win']+1,(route,width,sizes)
   assert not errors,(route,width,errors)
   if width in [375,1440] and route in ['/services/','/trade/']:
    p.evaluate("""async()=>{await Promise.all([...document.images].map(async i=>{i.loading='eager';try{await i.decode()}catch(e){}}))}""")
   if width==1440 and route in ['/services/','/trade/']:
    p.screenshot(path=str(out/(route.strip('/').replace('/','-')+'-1440.png')),full_page=True)
   if width==375 and route in ['/services/','/trade/']:
    p.screenshot(path=str(out/(route.strip('/').replace('/','-')+'-375.png')),full_page=True)
   if width==375 and route=='/services/':
    p.locator('.nav-toggle').click()
    assert p.locator('.mobile-navigation').is_visible()
    p.locator('.mobile-details summary').first.click()
    group=p.locator('.mobile-service-group').filter(has_text='Buying, trading & finance')
    group.locator('summary').click()
    assert group.locator('a[href="/services/mineral-buying/"]').is_visible()
    assert group.locator('a[href="/services/mineral-trading/"]').is_visible()
    p.keyboard.press('Escape')
    assert p.locator('.mobile-navigation').is_hidden()
   if width==1440 and route=='/services/':
    p.locator('.menu-trigger').click()
    assert p.locator('.dropdown-group').count()==5
    assert p.locator('.dropdown-links a').count()==15
    p.keyboard.press('Escape')
   p.close()
  print(route,'PASS 5 viewports, layout and nav checks')
 b.close()
