"""Analytical as a Service regression coverage; execute after npm run build."""
import json, unittest
from pathlib import Path
from bs4 import BeautifulSoup
from content.data import SERVICES,SERVICE_BY_SLUG,SERVICE_GROUPS
BASE=Path(__file__).resolve().parents[1]
DIST=BASE/'dist'
class AnalyticalExtensionTests(unittest.TestCase):
 def setUp(self):
  self.slug='analytical-as-a-service'
  self.link='/services/'+self.slug+'/'
 def html(self,route):
  p=DIST/route.strip('/')/'index.html' if route!='/' else DIST/'index.html'
  return BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 def test_analytical_content_and_group(self):
  s=SERVICE_BY_SLUG[self.slug]
  self.assertEqual(s['title'],'Analytical as a Service')
  self.assertGreaterEqual(len(s['sections']),6)
  self.assertGreaterEqual(len(s['prepare']),6)
  self.assertGreaterEqual(len(s['faq']),3)
  self.assertTrue(any(self.slug in slugs for _,slugs in SERVICE_GROUPS))
 def test_route_visible_in_services_home_header_footer(self):
  for route in ['/','/services/','/contact/']:
   soup=self.html(route)
   self.assertTrue(soup.select_one('a[href="'+self.link+'"]'),route)
  self.assertTrue(self.html('/services/').select_one('section .service-card[href="'+self.link+'"]'))
 def test_service_content_and_enquiry_workflow(self):
  soup=self.html(self.link)
  self.assertEqual(len(soup.select('main h1')),1)
  self.assertGreaterEqual(len(soup.select('.narrative-section')),6)
  self.assertEqual(len(soup.select('.analytical-approach-grid article')),4)
  self.assertTrue(soup.select_one('a[href="/contact/?service='+self.slug+'"]'))
  contact=self.html('/contact/')
  self.assertTrue(contact.select_one('select#service option[value="'+self.slug+'"]'))
  self.assertIn('enquiry',contact.get_text().lower())
 def test_image_and_route_manifest(self):
  manifest=json.loads((DIST/'route-manifest.json').read_text())
  self.assertIn(self.link,manifest['routes'])
  self.assertEqual(len(manifest['routes']),31)
  self.assertTrue((DIST/'images/generated/analytical-as-a-service.webp').is_file())
if __name__=='__main__':unittest.main()
