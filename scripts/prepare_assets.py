from PIL import Image,ImageOps,ImageEnhance
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.units import inch
import json
ROOT=Path(__file__).resolve().parents[1]
GEN=ROOT/'public/images/generated'; BRAND=ROOT/'public/images/brand'
GEN.mkdir(parents=True,exist_ok=True); BRAND.mkdir(parents=True,exist_ok=True)
logo=Image.open('/mnt/data/image(20261012-071423).png').convert('RGB'); logo.save(BRAND/'asl-original-logo.png',optimize=True)
# Extract gold crest from original; softly remove near-white pixels, keeping the fine gold details.
crest=logo.crop((63,117,715,818)).convert('RGBA')
pixels=crest.load()
for y in range(crest.height):
 for x in range(crest.width):
  r,g,b,a=pixels[x,y]
  brightness=min(r,g,b)
  whitening=min(r,g,b)
  alpha=max(0,min(255,int((255-whitening)*255/36))) if whitening>216 else 255
  pixels[x,y]=(r,g,b,alpha)
crest.thumbnail((450,450),Image.Resampling.LANCZOS)
crest.save(BRAND/'asl-crest.png',optimize=True)
crest2=crest.copy();crest2.thumbnail((96,96),Image.Resampling.LANCZOS); crest2.save(ROOT/'public/favicon.png')
(ROOT/'public/favicon.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#10213b"/><circle cx="32" cy="32" r="25" fill="none" stroke="#c8a159" stroke-width="1.4"/><text x="32" y="41" text-anchor="middle" fill="#e8c77b" font-size="26" font-family="Georgia,serif">ASL</text></svg>''')
sources={
 'home-hero':('/mnt/data/wide_cinematic_shallow_depth_of_field_still_life.png','Gold and precious-material still life at a laboratory bench'),
 'mineral-assay':('/mnt/data/a_dramatic_high_end_macro_style_still_life_close.png','Gold-bearing rock with crystalline mineral specimens'),
 'gold-assay':('/mnt/data/a_realistic_high_resolution_close_up_laboratory_s.png','Gloved hand positioning a gold sample at a precision balance'),
 'diamond-examination':('/mnt/data/a_close_up_high_end_macro_jewelry_still_life_scen.png','Two brilliant-cut diamonds on a velvet examination tray'),
 'gemstone-examination':('/mnt/data/a_close_up_cinematic_still_life_scene_of_a_gem_in.png','Emerald, blue, red and violet gemstones on an inspection surface'),
}
manifest=[]
def asset(name,path,alt,fit=(1400,900),box=None,quality=83,usage=[]):
 im=Image.open(path).convert('RGB')
 if box: im=im.crop(box)
 if fit: im.thumbnail(fit,Image.Resampling.LANCZOS)
 im.save(GEN/(name+'.webp'),'WEBP',quality=quality,method=6)
 manifest.append(dict(path='/images/generated/'+name+'.webp',alt=alt,origin='Original AI-generated conceptual editorial photograph',sourceOriginal=Path(path).name,usage=usage,dimensions=list(im.size)))
for n,(f,alt) in sources.items(): asset(n,f,alt,fit=(1700,1100),usage=['service illustration','editorial'])
# Distinct crops from original visual scenes; track originals transparently in the asset inventory.
asset('about','/mnt/data/a_realistic_high_resolution_close_up_laboratory_s.png','Laboratory microscope and samples under warm interior light',fit=(1200,1400),box=(0,0,1000,1024),usage=['About page'])
asset('sample-handling','/mnt/data/a_realistic_high_resolution_close_up_laboratory_s.png','Sample containers and a curated mineral tray',fit=(1200,1050),box=(0,130,810,960),usage=['Sample handling service'])
asset('reporting','/mnt/data/a_realistic_high_resolution_close_up_laboratory_s.png','Carefully arranged mineral specimen containers at a work bench',fit=(1200,1050),box=(0,0,900,880),usage=['Reporting service'])
asset('quality','/mnt/data/a_close_up_high_end_macro_jewelry_still_life_scen.png','Close detail of a precisely held diamond',fit=(1200,1050),box=(620,115,1420,915),usage=['Quality page'])
asset('contact','/mnt/data/a_close_up_cinematic_still_life_scene_of_a_gem_in.png','Faceted colored gemstones and examination tools',fit=(1100,1100),box=(650,0,1550,793),usage=['Contact page'])
asset('stone-detail','/mnt/data/a_dramatic_high_end_macro_style_still_life_close.png','Textured gold bearing mineral surface',fit=(1100,1200),box=(400,0,1300,1000),usage=['Knowledge article'])
asset('lab-detail','/mnt/data/a_realistic_high_resolution_close_up_laboratory_s.png','Gold particles beside glassware on a laboratory bench',fit=(1100,1200),box=(550,0,1440,1024),usage=['Process page'])
(ROOT/'IMAGE_MANIFEST.json').write_text(json.dumps(manifest,indent=2))
(ROOT/'IMAGE_MANIFEST.md').write_text('# Image inventory\n\nThe official ASL logo was supplied by the user. All other scene images are original generated conceptual visuals; they **do not depict verified ASL facilities, equipment or personnel**. Several alternate layouts are crops of the same generated originals.\n\n'+'\n'.join(f"- `{x['path']}` — {x['alt']} (original: `{x['sourceOriginal']}`)" for x in manifest)+'\n')
# Genuine practical guidance PDFs: non-certification/reference material.
out=ROOT/'public/downloads'; out.mkdir(exist_ok=True)
NAVY=colors.HexColor('#112440'); GOLD=colors.HexColor('#ad853e'); GREY=colors.HexColor('#485367')
styles=getSampleStyleSheet(); styles.add(ParagraphStyle(name='DocTitleASL',fontName='Times-Bold',fontSize=22,leading=26,textColor=NAVY,spaceAfter=15)); styles.add(ParagraphStyle(name='DocHeadASL',fontName='Helvetica-Bold',fontSize=11,leading=15,textColor=NAVY,spaceBefore=18,spaceAfter=7)); styles.add(ParagraphStyle(name='DocBodyASL',fontName='Helvetica',fontSize=9.7,leading=15,textColor=GREY,spaceAfter=8)); styles.add(ParagraphStyle(name='DocSmallASL',fontName='Helvetica',fontSize=8.5,leading=13,textColor=GREY,spaceAfter=10))
resources=[
('sample-submission-checklist.pdf','Sample submission checklist','A practical guide to preparing descriptions, documents, and packaging before arranging material examination.',[
 ('Before preparing the specimen',['State the material type, approximate amount or piece count, and the purpose of examination.','Record a clear description and any known specimen source or existing identifiers.','Gather available reports, photographs, previous tests, and any questions you want answered.']),
 ('Packaging and identification',['Separate and identify each specimen so individual items cannot be confused.','Use suitable protective packaging for fragile stones, powders, granular samples or sharp material.','Tell the laboratory about known handling hazards before transport or presentation.','Do not send valuable or hazardous materials until receipt and transport arrangements are agreed.']),
 ('Useful enquiry details',['Full name and a return contact channel','Material type, approximate weight or number of pieces','Any relevant prior test, photograph or supporting document','What you need the examination to establish','Desired output and any special handling or return requirements'])]),
('material-enquiry-guide.pdf','Material enquiry guide','Questions that help frame an enquiry about minerals, gold, diamonds or colored gemstones.',[
 ('Minerals',['Which elements or minerals are of interest?','Is the material a single specimen or a sample intended to represent a batch?','What source, collection process or prior analysis can be described?']),
 ('Gold',['Is it jewellery, grain, bar, dust, doré or gold-bearing mineral material?','Is your question about composition, gold content, or fineness?','Does your sample represent a larger amount of material?']),
 ('Diamonds',['Is the specimen rough or polished?','Is the question about identity, observed characteristics, or a particular evaluation issue?','Are there existing photographs, reports or identification records?']),
 ('Gemstones',['Which stone type is suspected?','Is it cut or rough, mounted or loose?','Is the question about identity, observable properties or possible treatment?'])]),
('understanding-results.pdf','Understanding reported results','A concise reference to specimen identifiers, methods, units and interpretation.',[
 ('Know which item was examined',['Identify the unique sample description or reference number and confirm it matches the item in question.','Check whether the result refers to an individual piece, a test portion, or a sample representing a larger lot.']),
 ('Read measurements in context',['Percentages, parts per million, mass fractions and fineness describe different forms of measurement.','A result may be affected by sampling, specimen heterogeneity, preparation and method suitability.','Any reported limits, conditions and observations should be read together with the numeric findings.']),
 ('Understand the scope',['A laboratory observation does not automatically establish geological origin, market value or the contents of an untested shipment.','An assay report is not automatically an independent accreditation, guarantee, or regulatory certificate.','Ask the issuer to explain unclear terminology, method applicability or sample representativeness.'])])]
def render_pdf(filename,title,summary,sections):
 doc=SimpleDocTemplate(str(out/filename),pagesize=(595,842),leftMargin=55,rightMargin=55,topMargin=58,bottomMargin=58,author='Aurum Standard Analytical Laboratories - educational reference',title=title)
 story=[Paragraph('AURUM STANDARD ANALYTICAL LABORATORIES',styles['DocSmallASL']),Paragraph(title,styles['DocTitleASL']),Paragraph(summary,styles['DocBodyASL']),Spacer(1,5)]
 for head,items in sections:
  story.append(Paragraph(head,styles['DocHeadASL']))
  for item in items: story.append(Paragraph('• '+item,styles['DocBodyASL']))
 story.append(Spacer(1,20));story.append(Paragraph('General educational guidance only. Agree the examination scope and any physical sample submission arrangements directly with the service provider.',styles['DocSmallASL']))
 def footer(canvas,doc):
  canvas.setStrokeColor(GOLD);canvas.line(55,45,540,45);canvas.setFont('Helvetica',8);canvas.setFillColor(GREY);canvas.drawString(55,29,'ASL  •  Assay of Minerals, Gold, Diamonds & Gemstones');canvas.drawRightString(540,29,f'{doc.page}')
 doc.build(story,onFirstPage=footer,onLaterPages=footer)
for r in resources:render_pdf(*r)
print('assets',len(manifest),'pdfs',len(resources))
