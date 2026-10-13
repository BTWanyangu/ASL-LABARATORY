from html import escape as esc
from urllib.parse import quote
from content.data import SITE,SERVICES,ARTICLES,STEPS,SERVICE_GROUPS,SERVICE_BY_SLUG

def e(v):return esc(str(v),quote=True)
def a(href,text,klass='',icon=False,attrs=''):
 return f'<a href="{e(href)}" class="{e(klass)}" {attrs}>{text}{"<span aria-hidden=\"true\"> ↗</span>" if icon else ""}</a>'
def img(name,alt='',klass='',loading='lazy',sizes='(max-width: 720px) 100vw, 50vw'):
 return f'<img class="{klass}" src="/images/generated/{e(name)}.webp" alt="{e(alt)}" loading="{loading}" decoding="async" sizes="{sizes}">'
def button(href,text,outline=False,light=False):
 return a(href,e(text)+' <span class="button-arrow" aria-hidden="true">↗</span>', 'btn '+('btn-outline ' if outline else 'btn-gold ')+('btn-light' if light else ''))
def eyebrow(text):return f'<div class="eyebrow">{e(text)}</div>'
def section_head(kicker,title,desc='',center=False):
 return f'<div class="section-heading {"center" if center else ""}">{eyebrow(kicker)}<h2>{title}</h2>{f"<p>{e(desc)}</p>" if desc else ""}</div>'
def masthead(title,kicker,lead,image=None,crumbs=None,klass=''):
 if image:
  return f'''<section class="page-hero dark-hero {klass}"><div class="page-hero-image">{img(image,'',loading='eager')}</div><div class="hero-scrim"></div><div class="container page-hero-content">{breadcrumbs(crumbs) if crumbs else ''}{eyebrow(kicker)}<h1>{title}</h1><p>{e(lead)}</p></div></section>'''
 return f'''<section class="page-hero plain-hero {klass}"><div class="container page-hero-content">{breadcrumbs(crumbs) if crumbs else ''}{eyebrow(kicker)}<h1>{title}</h1><p>{e(lead)}</p></div></section>'''
def breadcrumbs(crumbs):
 if not crumbs:return ''
 return '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a> <span aria-hidden="true">/</span> '+' '.join((f'<a href="{e(link)}">{e(name)}</a> <span aria-hidden="true">/</span>' if link else f'<span aria-current="page">{e(name)}</span>') for name,link in crumbs)+'</nav>'
def service_card(s,compact=False):
 slug=s['slug'];cls='service-card compact' if compact else 'service-card'
 return f'''<a href="/services/{slug}/" class="{cls}"><div class="service-card-media">{img(s['image'],s['summary'])}<span class="service-number">{s['eyebrow'].split(' / ')[0]}</span></div><div class="service-card-body"><span class="card-kicker">{e(s['eyebrow'].split(' / ')[1])}</span><h3>{e(s['title'])}</h3><p>{e(s['summary'])}</p><span class="text-link">Explore service <span aria-hidden="true">↗</span></span></div></a>'''
def article_card(x):
 return f'''<a href="/knowledge/{x['slug']}/" class="article-card"><div class="article-img">{img(x['image'],x['title'])}</div><div class="article-content"><div class="article-meta"><span>{e(x['category'])}</span><span>{x['minutes']} min read</span></div><h3>{e(x['title'])}</h3><p>{e(x['excerpt'])}</p><span class="text-link">Read insight <span aria-hidden="true">↗</span></span></div></a>'''
def steps_grid(short=False):
 data=STEPS[:4] if short else STEPS
 return '<div class="steps-grid '+('short-steps' if short else '')+'">'+''.join(f'<div class="step"><span class="step-index">{n}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for n,t,d in data)+'</div>'
def cta(title='Have a material you would like to discuss?',body='Tell us what you have, what you need to know and which supporting details are already available.',href='/contact/',label='Discuss your sample'):
 return f'''<section class="cta-panel"><div class="container cta-inner"><div>{eyebrow('THE NEXT STEP')}<h2>{e(title)}</h2><p>{e(body)}</p></div>{button(href,label)}</div></section>'''
def faq(items):
 return '<div class="faq-list">'+''.join(f'<details><summary>{e(q)}<span aria-hidden="true">+</span></summary><div class="faq-answer">{e(ans)}</div></details>' for q,ans in items)+'</div>'
def header(current=''):
 def service_links(slugs):
  return ''.join(f'<a href="/services/{slug}/">{e(SERVICE_BY_SLUG[slug]["title"])}<span aria-hidden="true">↗</span></a>' for slug in slugs)
 services_menu=''.join(f'<div class="dropdown-group"><h4>{e(label)}</h4>{service_links(slugs)}</div>' for label,slugs in SERVICE_GROUPS)
 mobile_groups=''.join(f'<details class="mobile-service-group"><summary>{e(label)} <span aria-hidden="true">+</span></summary><div class="mobile-service-links">{service_links(slugs)}</div></details>' for label,slugs in SERVICE_GROUPS)
 navlinks=[('Home','/'),('About','/about/'),('Mineral Trade','/trade/'),('Our Process','/process/'),('Quality','/quality/'),('Knowledge','/knowledge/'),('Resources','/resources/'),('Contact','/contact/')]
 def item(label,href):
  active=(current==href or (href!='/' and current.startswith(href)))
  return f'<a href="{href}" {"aria-current=\"page\"" if active else ""}>{e(label)}</a>'
 desktop=''.join(item(*x) for x in navlinks[:2])+f'''<div class="has-menu"><button class="menu-trigger" type="button" aria-expanded="false" aria-controls="desktop-services">Services <span aria-hidden="true">⌄</span></button><div class="dropdown" id="desktop-services"><div class="dropdown-intro"><span class="card-kicker">A COMPLETE VIEW</span><h3>Explore our service areas</h3><p>From analytical evaluation and assays to refining, logistics and mineral commerce.</p>{a('/services/','View all services','text-link')}</div><div class="dropdown-links">{services_menu}</div></div></div>'''+''.join(item(*x) for x in navlinks[2:])
 mobile=''.join(item(*x) for x in navlinks[:2])+f'''<details class="mobile-details"><summary>Services <span aria-hidden="true">+</span></summary><div class="mobile-sub"><a href="/services/">All services</a>{mobile_groups}</div></details>'''+''.join(item(*x) for x in navlinks[2:])
 return f'''<a href="#main" class="skip-link">Skip to content</a><header class="site-header" id="site-header"><div class="container header-inner"><a href="/" class="brand" aria-label="Aurum Standard Laboratories homepage"><img src="/images/brand/asl-crest.png" alt="" width="60" height="60"><span class="brand-words"><strong>AURUM STANDARD<br>LABORATORIES</strong><small>ASSAY OF MINERALS, GOLD, DIAMONDS & GEMSTONES</small></span></a><nav class="desktop-nav" aria-label="Main navigation">{desktop}</nav><a href="/contact/" class="header-cta">ENQUIRE <span aria-hidden="true">↗</span></a><button class="nav-toggle" aria-expanded="false" aria-controls="mobile-navigation" aria-label="Open navigation" type="button"><span></span><span></span><span></span></button></div><nav id="mobile-navigation" class="mobile-navigation" aria-label="Mobile navigation" hidden><div class="mobile-navigation-inner">{mobile}<a class="mobile-contact" href="/contact/">Request an enquiry ↗</a></div></nav></header>'''
def footer():
 material=['analytical-as-a-service','mineral-assay','gold-assay','diamonds','gemstones','assaying','reporting']
 workflow=['reception','transportation','storage','refining','manufacturing','mineral-buying','mineral-trading','financing']
 def links(slugs):return ''.join(f'<a href="/services/{slug}/">{e(SERVICE_BY_SLUG[slug]["title"])}</a>' for slug in slugs)
 return f'''<footer class="site-footer"><div class="container"><div class="footer-top"><div class="footer-brand"><img src="/images/brand/asl-crest.png" width="94" height="94" alt=""><h2>Aurum Standard<br>Laboratories</h2><p>Assay of Minerals, Gold, Diamonds &amp; Gemstones</p><p class="footer-description">Material understanding, processing conversations, responsible mineral commerce and careful documentation.</p></div><div class="footer-column"><h3>Assaying &amp; examination</h3>{links(material)}<a href="/services/sample-handling/">Sample handling</a></div><div class="footer-column"><h3>Operations &amp; trade</h3>{links(workflow)}<a href="/trade/">Buying &amp; trading overview</a></div><div class="footer-column"><h3>Company &amp; resources</h3><a href="/about/">About ASL</a><a href="/process/">Our process</a><a href="/quality/">Quality &amp; responsibility</a><a href="/knowledge/">Knowledge</a><a href="/resources/">Download guides</a><a href="/contact/">Enquiries</a><a href="/privacy/">Privacy</a><a href="/terms/">Website terms</a></div></div><div class="footer-bottom"><span>© {__import__('datetime').date.today().year} Aurum Standard Laboratories. All rights reserved.</span><span>PRECISION OF PURPOSE. CLARITY OF INFORMATION.</span></div></div></footer>'''
