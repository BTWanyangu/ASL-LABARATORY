#!/usr/bin/env python3
"""Dependency-free, prerendered static build. Every URL has its own index.html."""
from pathlib import Path
import json,os,shutil,re,sys,html
from urllib.parse import urljoin
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from content.data import SITE,SERVICES,ARTICLES
from templates.components import header,footer
from templates import pages
PUB=ROOT/'public';DEST=ROOT/'dist'
BASE=(os.environ.get('ASL_SITE_URL') or '').strip().rstrip('/')
EMAIL=(os.environ.get('ASL_PUBLIC_EMAIL') or '').strip()
if BASE and not BASE.startswith(('https://','http://')):raise ValueError('ASL_SITE_URL must be an http(s) origin')
if EMAIL and not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+',EMAIL):raise ValueError('ASL_PUBLIC_EMAIL must be a valid email address')
if DEST.exists():shutil.rmtree(DEST)
shutil.copytree(PUB,DEST)

def write_page(route,title,description,body,img='home-hero',noindex=False):
 route=route.strip('/')
 path=('/'+route+'/' if route else '/')
 page_dir=DEST/route if route else DEST
 page_dir.mkdir(parents=True,exist_ok=True)
 canonical=(f'<link rel="canonical" href="{html.escape(BASE+path)}">' if BASE else '')
 social=(html.escape(BASE+'/images/generated/'+img+'.webp') if BASE else '/images/generated/'+img+'.webp')
 page=f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><meta name="theme-color" content="#101f36"><title>{html.escape(title)}</title><meta name="description" content="{html.escape(description,quote=True)}"><meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title,quote=True)}"><meta property="og:description" content="{html.escape(description,quote=True)}"><meta property="og:image" content="{social}"><meta name="twitter:card" content="summary_large_image">{canonical}<meta name="robots" content="{'noindex,follow' if noindex else 'index,follow'}"><meta name="asl-contact-email" content="{html.escape(EMAIL,quote=True)}"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon.png" type="image/png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="/styles.css"><script src="/app.js" defer></script></head><body>{header(path)}<main id="main">{body}</main>{footer()}</body></html>'''
 (page_dir/'index.html').write_text(page,encoding='utf-8')
 return path
ROUTES=[]
def add(*args,**kw):ROUTES.append(write_page(*args,**kw))
add('','Aurum Standard Analytical Laboratories | Minerals, Gold, Diamonds & Gemstones','Explore analytical services, assaying, refining, transportation, storage and mineral buying and trading.',pages.home())
add('about','About Aurum Standard Analytical Laboratories | ASL','Understand the identity, focus and guiding principles of Aurum Standard Analytical Laboratories.',pages.about(),'about')
add('services','Material Assay & Examination Services | Aurum Standard Analytical Laboratories','Explore sixteen services covering analytical testing enquiries, assay, refining, manufacturing, transport, storage and mineral trading.',pages.services_index(),'mineral-assay')
add('trade','Mineral Buying & Trading | Aurum Standard Analytical Laboratories','Discover information about mineral buying, mineral trade, responsible sourcing and how to begin a commercial enquiry.',pages.trade_index(),'mineral-assay')
for s in SERVICES:
 desc=f"Explore {s['title'].lower()} questions, material preparation, reporting considerations and useful next steps at Aurum Standard Analytical Laboratories."
 add('services/'+s['slug'],s['title']+' | Aurum Standard Analytical Laboratories',desc,pages.service_detail(s),s['image'])
add('process','Our Laboratory Enquiry Process | Aurum Standard Analytical Laboratories','Understand the stages from a material enquiry and sample identification to relevant examination, review and reporting.',pages.process(),'lab-detail')
add('quality','Quality & Responsibility | Aurum Standard Analytical Laboratories','Explore the principles of specimen identity, method suitability, traceability, interpretation and confidentiality.',pages.quality(),'quality')
add('knowledge','Knowledge & Insights | Aurum Standard Analytical Laboratories','Read educational articles about assays, representative sampling, diamond and gemstone examination, and laboratory reports.',pages.knowledge_index(),'stone-detail')
for a in ARTICLES:
 add('knowledge/'+a['slug'],a['title']+' | Aurum Standard Analytical Laboratories',a['excerpt'],pages.article_detail(a),a['image'])
add('resources','Sample Guidance & Downloadable Resources | Aurum Standard Analytical Laboratories','Download real educational PDF guides on specimen preparation, material enquiries and understanding laboratory results.',pages.resources(),'reporting')
add('contact','Contact & Enquiries | Aurum Standard Analytical Laboratories','Prepare an enquiry about analytical services, assay, precious materials, buying, trading, refining or custody at ASL.',pages.contact(),'contact')
add('privacy','Privacy Notice | Aurum Standard Analytical Laboratories','How the ASL website handles enquiry-drafting information and site privacy.',pages.privacy(),'home-hero')
add('terms','Website Terms | Aurum Standard Analytical Laboratories','Terms for the informational ASL website and downloadable reference resources.',pages.terms(),'home-hero')
# Dedicated 404 document with the right metadata, not a modified copy of home.
write_page('404','Page not found | Aurum Standard Analytical Laboratories','The page you requested could not be found. Return to ASL services or the homepage.',pages.not_found(),noindex=True)
shutil.copyfile(DEST/'404/index.html',DEST/'404.html')
(DEST/'robots.txt').write_text('User-agent: *\nAllow: /\n'+('Sitemap: '+BASE+'/sitemap.xml\n' if BASE else ''),encoding='utf-8')
if BASE:
 from xml.sax.saxutils import escape
 urls='\n'.join('  <url><loc>'+escape(BASE+route)+'</loc></url>' for route in ROUTES)
 (DEST/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+urls+'\n</urlset>',encoding='utf-8')
# Site-manifest is useful for QA and routes, not a fabricated results database.
(DEST/'route-manifest.json').write_text(json.dumps({'routes':ROUTES,'generatedAt':datetime.now(timezone.utc).isoformat(),'baseUrl':BASE or None},indent=2))
print(f'Build complete: {len(ROUTES)} HTML routes + 404, {len(list((DEST/"downloads").glob("*.pdf")))} PDF guides, {len(list((DEST/"images/generated").glob("*.webp")))} images in {DEST}')
