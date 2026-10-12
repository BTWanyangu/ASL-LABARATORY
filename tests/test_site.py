import json,re,unittest
from pathlib import Path
from content.data import SERVICES, SERVICE_GROUPS, VALCAMBI_SERVICE_NAMES
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/'dist'
class SiteAudit(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.routes=json.loads((DIST/'route-manifest.json').read_text())['routes']
  cls.html=[(r,BeautifulSoup((DIST/r.strip('/')/'index.html' if r.strip('/') else DIST/'index.html').read_text(),'html.parser')) for r in cls.routes]
 def test_service_routes_and_not_found(self):
  self.assertEqual(len(self.routes),30)
  self.assertIn("/trade/",self.routes)
  for service in SERVICES:
   self.assertIn("/services/"+service["slug"]+"/",self.routes)
  self.assertTrue((DIST/'404.html').exists())
 def test_single_heading_and_unique_metadata(self):
  titles=[];desc=[]
  for route,soup in self.html:
   self.assertEqual(len(soup.select('main h1')),1,route)
   self.assertTrue(soup.select_one('meta[name=description]')['content'],route)
   titles.append(soup.title.text);desc.append(soup.select_one('meta[name=description]')['content'])
  self.assertEqual(len(titles),len(set(titles)))
  self.assertEqual(len(desc),len(set(desc)))
 def test_every_local_hyperlink_is_real(self):
  for route,soup in self.html:
   for a in soup.find_all('a',href=True):
    href=a['href'];parsed=urlsplit(href)
    if parsed.scheme or href.startswith('#'):continue
    if not href.startswith('/'):continue
    path=parsed.path.strip('/')
    file=DIST/path
    valid=file.is_file() or (file.is_dir() and (file/'index.html').is_file())
    self.assertTrue(valid,f'Broken internal link in {route}: {href}')
 def test_image_paths_and_alt_attributes(self):
  for route,soup in self.html:
   for im in soup.find_all('img'):
    src=im.get('src','')
    self.assertTrue(src.startswith('/'))
    self.assertTrue((DIST/src.lstrip('/')).is_file(),f'Missing image {src} on {route}')
    self.assertTrue(im.has_attr('alt'),f'Image missing alt in {route}')
 def test_service_categories_and_trade_links(self):
  expected={"Transportation":"transportation","Reception":"reception","Assaying":"assaying","Refining":"refining","Manufacturing":"manufacturing","Financing":"financing","Storage":"storage"}
  self.assertEqual(len(SERVICES),15)
  self.assertEqual(VALCAMBI_SERVICE_NAMES,list(expected))
  self.assertTrue(all(any(s["slug"]==slug for s in SERVICES) for slug in expected.values()))
  self.assertEqual(sum(len(items) for _,items in SERVICE_GROUPS),15)
  home=dict(self.html)['/'];services=dict(self.html)['/services/'];trade=dict(self.html)['/trade/']
  for slug in ['mineral-buying','mineral-trading']:
   self.assertTrue(services.select_one(f'a[href="/services/{slug}/"]'))
   self.assertTrue(trade.select_one(f'a[href="/services/{slug}/"]'))
   self.assertTrue(home.select_one(f'a[href="/services/{slug}/"]'))
  for slug in expected.values():
   self.assertTrue(services.select_one(f'a[href="/services/{slug}/"]'))
   self.assertTrue(home.select_one(f'a[href="/services/{slug}/"]'))
 def test_service_pages_substantive(self):
  for s in SERVICES:
   html=(DIST/'services'/s['slug']/'index.html').read_text()
   soup=BeautifulSoup(html,'html.parser')
   self.assertGreaterEqual(len(soup.select('.narrative-section')),3,s['slug'])
   self.assertGreaterEqual(len(soup.select('.check-list li')),5,s['slug'])
   self.assertGreaterEqual(len(soup.select('.faq-list details')),2,s['slug'])
   self.assertIn('/contact/?service='+s['slug'],html)
 def test_resources_are_true_pdf_files(self):
  for p in (DIST/'downloads').glob('*.pdf'):
   self.assertEqual(p.read_bytes()[:4],b'%PDF')
  self.assertEqual(len(list((DIST/'downloads').glob('*.pdf'))),3)
 def test_contact_never_claims_unverified_delivery(self):
  doc=(DIST/'contact/index.html').read_text()
  self.assertIn('Prepare enquiry',doc)
  self.assertNotIn('Your enquiry has been sent',doc)
  self.assertIn('Your enquiry has not been sent',doc)
 def test_no_placeholder_domain_or_legacy_names(self):
  for route,soup in self.html:
   text=soup.get_text(' ',strip=True)
   for term in ['RockValle','RockVale','WiseWastes','CombiBar','Lorem ipsum','ISO 17025 certified']:
    self.assertNotIn(term,text,route)
 def test_assets_manifest_matches_actual(self):
  manifest=json.loads((ROOT/'IMAGE_MANIFEST.json').read_text())
  self.assertEqual(len(manifest),14)
  for entry in manifest:
   self.assertTrue((DIST/entry['path'].lstrip('/')).exists())
if __name__=='__main__':unittest.main()
