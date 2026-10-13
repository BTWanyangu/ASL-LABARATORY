"""Corporate name rebrand regression, evaluated against a generated dist build."""
import unittest
from pathlib import Path
from bs4 import BeautifulSoup
try:
 from pypdf import PdfReader
except ImportError:
 PdfReader = None
ROOT=Path(__file__).resolve().parents[1]
NEW='Aurum Standard Analytical Laboratories'
OLD='Aurum Standard Laboratories'

class CorporateNameTests(unittest.TestCase):
 def test_brand_identity_and_main_navigation(self):
  from content.data import SITE
  self.assertEqual(SITE['name'],NEW)
  for path in ['','about','services','contact','404']:
   file=ROOT/'dist'/path/'index.html'
   soup=BeautifulSoup(file.read_text(), 'html.parser')
   self.assertIn(NEW,soup.title.text)
   self.assertIn('ANALYTICAL LABORATORIES',soup.select_one('.brand-words strong').get_text(' '))
   self.assertNotIn(OLD,soup.get_text(' ',strip=True))
   self.assertIn(NEW,soup.select_one('footer').get_text(' ',strip=True))
 def test_other_pages_are_updated(self):
  pages=list((ROOT/'dist').rglob('index.html'))
  self.assertGreaterEqual(len(pages),30)
  for p in pages:
   html=p.read_text()
   self.assertNotIn(OLD,html,p)
 def test_download_guides_rebranded(self):
  paths=list((ROOT/'dist/downloads').glob('*.pdf'))
  self.assertEqual(len(paths),3)
  for p in paths:
   self.assertEqual(p.read_bytes()[:4],b'%PDF')
  if PdfReader is None:
   self.skipTest('Install optional pypdf package to inspect PDF branding text')
  for p in paths:
   reader=PdfReader(str(p))
   self.assertIn('AURUM STANDARD ANALYTICAL LABORATORIES',reader.pages[0].extract_text())

if __name__=='__main__':unittest.main()
