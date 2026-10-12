"""Original ASL-facing content for the expanded services portfolio.

Valcambi category structure was used as a reference, not its business claims,
operating terms, proprietary processes, credentials or branded products.
Each item is informational and enquiry-led pending owner confirmation of scope.
"""
EXPANDED_SERVICES = [
 {
  'slug':'transportation','title':'Precious materials transportation','short':'Transportation','eyebrow':'07 / TRANSPORTATION','image':'sample-handling',
  'lead':'Plan the movement of valuable materials with care.','summary':'Explore shipment preparation, secure movement considerations and documented handover.',
  'intro':'The movement of mineral samples, gold and precious stones requires more than a shipping label. Packaging, declarations, identity checks and a clearly agreed handover matter from collection through delivery. Begin a conversation about the transportation arrangements appropriate to your material.',
  'sections':[
   ('A shipment begins with a sound plan','Material form, value, destination, packaging requirements and any relevant safety classification affect the transport approach. Before any movement, parties should agree on who prepares the shipment, who arranges carriage and how receipt is confirmed.'),
   ('Documentation that travels with the material','Accurate consignor and consignee details, item descriptions, counts or weights and suitable supporting documentation make it easier to reconcile what was dispatched with what is received. Regulatory declarations and cross-border permits, where relevant, need to be addressed through authorised channels.'),
   ('Security and handover points','High-value goods may call for secure carriers, tamper-evident packaging, insurance discussions, tracked transfers and clearly defined responsibilities. Transport arrangements should be confirmed case by case; an online enquiry does not book collection or insure a shipment.')],
  'prepare':['Material description and approximate value or quantity','Collection and destination areas','Packaging, piece count and approximate gross weight','Any relevant customs or ownership documentation','Preferred timeline and special handling considerations'],
  'faq':[('Can I request collection through the website?','The enquiry form starts a discussion. Collection is not scheduled without a separately confirmed arrangement.'),('Will my shipment automatically be insured?','No. Insurance and liability terms must be specifically reviewed and agreed for any transport arrangement.')],
  'related':['reception','storage','sample-handling']
 },
 {
  'slug':'reception','title':'Material reception & intake','short':'Reception','eyebrow':'08 / RECEPTION','image':'sample-handling',
  'lead':'A clear intake creates a traceable beginning.','summary':'Understand how identification, declared weight, condition and specimen records fit together.',
  'intro':'The first point of receipt is where a material description becomes an identifiable consignment or specimen record. A thoughtful reception plan considers what is expected, what physically arrives and what information should follow the material.',
  'sections':[
   ('Before material arrives','An advance description can include the sender, declared material type, packaging, sample count, approximate weight, intended work and supporting documents. For sensitive materials, parties should discuss acceptance conditions before dispatch.'),
   ('Inspection, reconciliation and identification','At the point of receipt, the condition of seals and packaging, piece count and identifying marks can be checked against supplied information. Any differences should be documented and clarified before subsequent processing.'),
   ('Weighing, sampling and next steps','Appropriate weighing, sample separation and unique identifiers can support a coherent chain of records. The path thereafter may involve examination, processing, storage, return or commercial discussion, depending on an agreed scope.')],
  'prepare':['Sender and authorised recipient details','Material category, form and approximate weight','Number of packages and sample identifiers','Packaging and seal information, if relevant','Prior analyses, consignment records or safety notes'],
  'faq':[('Is reception the same as an assay?','No. Reception establishes what was received and how it is identified; analysis or examination is a separate activity.'),('Should I ship material before speaking to ASL?','Contact ASL first to agree on suitability, any acceptance conditions and handover arrangements.')],
  'related':['sample-handling','assaying','transportation']
 },
 {
  'slug':'assaying','title':'Precious metals assaying','short':'Assaying','eyebrow':'09 / ASSAYING','image':'gold-assay',
  'lead':'Measured composition begins with the right specimen.','summary':'Explore sampling, precious-metal content, method suitability and assay interpretation.',
  'intro':'Assaying is the examination or measurement of a material to answer defined questions about composition or content. For precious metals, the relationship between the material, the sampling plan and the analytical technique is central to interpreting the result.',
  'sections':[
   ('Understanding what an assay measures','An assay may focus on the proportion of a precious metal, relevant accompanying constituents or characteristics required for a particular decision. Different sample forms call for different preparation and evaluation considerations.'),
   ('Selecting methods for the actual question','Industry methods can include fire assay, X-ray fluorescence and instrumental chemical analysis. These are examples rather than a list of instruments operated by ASL; the appropriate technique depends on material, required analytes, sensitivity and agreed scope.'),
   ('From test portion to useful result','A report needs to link each stated result to the particular specimen examined, its identity and measurement units. When results inform a larger lot, sampling representativeness and any technical limitations should also be considered.')],
  'prepare':['Precious-metal type or suspected composition','Material form and approximate mass','Known source and sampling method, if applicable','Existing results or supporting documents','Measurements or fineness questions to resolve'],
  'faq':[('Can appearance alone establish fineness?','No. A reliable assessment relies on appropriate evidence rather than colour or visual appearance.'),('Is an assay the same as a valuation?','No. Composition is one possible input to valuation; market price and commercial settlement involve additional factors.')],
  'related':['gold-assay','mineral-assay','reporting']
 },
 {
  'slug':'refining','title':'Precious metals refining','short':'Refining','eyebrow':'10 / REFINING','image':'refining',
  'lead':'From metal-bearing input to a defined output.','summary':'Learn how feedstock characterization, recovery options and product specification shape refining discussions.',
  'intro':'Refining refers to processes used to separate, recover or improve the purity of metals. The most relevant route depends on the incoming material, its composition, impurities and the intended output. Use this service area to discuss a potential refining requirement and the technical information needed to assess it.',
  'sections':[
   ('Assessing the feedstock','The material may arrive as doré, alloy, scrap, concentrated intermediate product or another metal-bearing form. Composition and likely contaminants determine which process questions matter before any refining decision is made.'),
   ('Understanding process routes','Industry refining approaches can involve thermal, electrochemical or wet-chemical methods, often combined in stages. Their suitability depends on the metals present and the desired recovery or specification. No particular plant, throughput or achievable purity is implied by this overview.'),
   ('Yield, reconciliation and documentation','Material balance, loss accounting, recovery basis, output form and the treatment of residues can all affect a commercial refining agreement. Parties should discuss testing, ownership, processing terms and delivery arrangements before work begins.')],
  'prepare':['Material type and approximate quantity','Previous assay or compositional data','Known contaminants or handling restrictions','Target product or required specification','Ownership, documentation and desired next step'],
  'faq':[('Does refining mean all impurities can be removed?','Each refining route has technical and commercial limits; achievable output specifications require assessment.'),('Can I receive a confirmed recovery quote online?','No. Processing terms and feasibility depend on verified material details and a separately agreed proposal.')],
  'related':['assaying','manufacturing','reporting']
 },
 {
  'slug':'manufacturing','title':'Precious metal manufacturing','short':'Manufacturing','eyebrow':'11 / MANUFACTURING','image':'manufacturing',
  'lead':'Consider the form and function of finished metal.','summary':'Explore how refined metal may be transformed into bars, grain or other agreed product forms.',
  'intro':'Precious-metal manufacturing connects metal specification to the physical form needed for its intended use. Understanding product type, material input, dimensional requirements and marking expectations is the starting point for a useful manufacturing enquiry.',
  'sections':[
   ('Define the intended product','Cast forms, granules, fabricated components and other industrial metal formats can present different requirements. The finished format should follow from practical use, quantity and agreed specifications rather than an assumed catalogue.'),
   ('Control material and specifications','A manufacturing discussion should consider incoming purity, permitted alloying elements, dimensional tolerances, handling, finished weights and any quality checks required by the intended application.'),
   ('Presentation, records and delivery','Packaging, product identification, documentation and agreed release conditions may be important for subsequent distribution or use. Branded minting, legal hallmarks or exchange accreditation must not be assumed without separate evidence and approval.')],
  'prepare':['Desired product form and intended application','Material supplied or input metal requirements','Approximate quantity and weight per item','Dimensions, finish or marking expectations','Any technical specifications or design drawings'],
  'faq':[('Can a custom product be ordered directly here?','This page starts a discussion of requirements; it is not an online factory order system.'),('Are produced bars automatically exchange-approved?','No. Exchange acceptance and authorised hallmarks have specific conditions and are not implied by a material description.')],
  'related':['refining','assaying','transportation']
 },
 {
  'slug':'financing','title':'Precious metals financing enquiries','short':'Financing','eyebrow':'12 / FINANCING','image':'reporting',
  'lead':'Clarify the commercial structure around the material.','summary':'Understand how ownership, verification, settlement and financing requirements may connect.',
  'intro':'Commercial activity involving valuable materials may require working-capital planning, settlement arrangements or a discussion with regulated financial providers. A financing enquiry begins with the structure of the proposed transaction and the parties involved, not an assumption that a facility is available.',
  'sections':[
   ('Map the underlying transaction','The material type, location, ownership, intended buyer or counterparty and proposed timing help define the commercial context. These facts matter whether someone is exploring inventory finance, advance settlement or another arrangement.'),
   ('Independent information and documentation','Accurate material descriptions, supporting assay documents, ownership evidence and trade paperwork can support due diligence. Financial terms must be reviewed separately by appropriately authorised parties.'),
   ('Evaluate terms and responsibility','Any actual offer would need to specify provider, eligibility, costs, security, settlement timing and legal terms. This website does not issue loans, promise credit, arrange regulated finance automatically or accept payment instructions.')],
  'prepare':['Proposed transaction and purpose of funding','Material description and quantity','Proof of ownership and counterparties, where relevant','Available test or valuation documents','Preferred transaction currency, timeframe and structure'],
  'faq':[('Can I apply for a loan on this page?','No. This is an enquiry area for discussing requirements; no credit application or approval process is provided by the site.'),('Does an assay guarantee financing?','No. Financing depends on the responsible provider’s independent eligibility and risk assessments.')],
  'related':['mineral-trading','assaying','storage']
 },
 {
  'slug':'storage','title':'Precious materials storage','short':'Storage','eyebrow':'13 / STORAGE','image':'lab-detail',
  'lead':'Preserve material identity while planning custody.','summary':'Explore inventory identification, segregation, authorised access and release records.',
  'intro':'Storage of gold, precious metals and valuable specimens involves questions about identity, security, inventory records, access and the circumstances under which material can be released. Begin with the actual item and custody requirement.',
  'sections':[
   ('Identify the holdings','A suitable record should distinguish material description, item count, weight, distinguishing marks and any available identifiers. Whether items require segregation or sealed packaging depends on agreed custody arrangements.'),
   ('Understand the custody arrangement','Location, access controls, security, record reconciliation, permitted inspections and responsibility for loss are contractual matters. No vault facilities, insured custody or particular storage jurisdiction are asserted by this page.'),
   ('Release and transfer controls','Any release process should define authorised instructions, recipient verification, handover evidence and connection to transport or reporting records. Storage enquiry submission does not constitute a deposit or transfer instruction.')],
  'prepare':['Material type, form, quantity and approximate value','Preferred duration and custody objective','Packaging or segregation needs','Access and release-authorisation requirements','Relevant insurance, ownership or transport questions'],
  'faq':[('Does ASL provide an insured vault automatically?','Custody arrangements and insurance, if relevant, require a separately confirmed service agreement.'),('Can I deposit material by completing this form?','No. An enquiry is not a custody agreement or an instruction to receive assets.')],
  'related':['transportation','reception','mineral-trading']
 },
 {
  'slug':'mineral-buying','title':'Mineral buying','short':'Mineral buying','eyebrow':'14 / MINERAL BUYING','image':'mineral-assay',
  'lead':'Begin a mineral purchase with clear information.','summary':'Explore sourcing enquiries, material descriptions, due diligence and purchase considerations.',
  'intro':'Mineral buying begins with knowing what material is on offer, the seller’s right to sell, how quantity and composition are documented and what commercial terms require agreement. ASL’s enquiry pathway helps organise the initial discussion without implying a standing purchase offer.',
  'sections':[
   ('Describe what is being offered','Material type, grade or assay evidence, volume, physical form and location help establish whether a buying discussion can be meaningful. Different minerals have different handling and market requirements.'),
   ('Verify the counterparty and material','Responsible purchasing discussions involve seller identification, provenance and ownership documentation, applicable permits, export status where relevant and a defensible understanding of the material offered.'),
   ('Agree commercial terms separately','Pricing basis, sampling rights, delivery point, settlement, acceptance criteria and liability need written agreement between the actual parties. Displaying this service is not a commitment to purchase material at any price.')],
  'prepare':['Mineral type and physical form','Available quantity and location','Grade/assay results and sample information','Seller identity, ownership and licence documents','Expected pricing basis and delivery terms'],
  'faq':[('Can I sell minerals instantly through the site?','No. The website starts a buying enquiry; it is not a live marketplace or binding offer.'),('Does ASL buy every mineral listed?','Material interest, eligibility and commercial terms must be reviewed for each proposed transaction.')],
  'related':['mineral-trading','mineral-assay','reception']
 },
 {
  'slug':'mineral-trading','title':'Mineral trading','short':'Mineral trading','eyebrow':'15 / MINERAL TRADING','image':'mineral-assay',
  'lead':'Connect mineral opportunities to informed decisions.','summary':'Explore trade enquiries, specification alignment, transaction documentation and responsible sourcing.',
  'intro':'Mineral trading involves aligning what a seller can reliably supply with the grade, quality, volume, documentation and delivery requirements of a potential buyer. A clear transaction framework is as important as the material itself.',
  'sections':[
   ('Understand the material and the market requirement','A prospective trade should define mineral species or commodity, grade, tolerances, quantity, available supply, packing and destination requirements. Assay and representative sampling information can support product specifications.'),
   ('Responsible counterparties and traceable sourcing','Buyers and sellers should examine licensing, ownership, source information, compliance obligations and applicable sanctions or export controls before making commitments. The relevant legal requirements depend on the countries and commodities involved.'),
   ('From commercial discussion to documented terms','A transaction may require agreed quotations, payment terms, inspection rights, Incoterms where applicable, risk transfer, shipment documentation and dispute procedures. The enquiry form does not execute contracts, handle escrow or provide shipment tracking.')],
  'prepare':['Mineral or commodity and grade/specification','Buy or sell interest and target quantity','Country or area of origin and intended destination','Assay, ownership and regulatory documents available','Preferred transaction, delivery and payment framework'],
  'faq':[('Can this website execute a mineral trade?','No. Commercial agreements and payments require separately verified arrangements.'),('Can an existing assay be used in a trade discussion?','It can help, provided the parties agree that it describes a suitably representative specimen and meets their requirements.')],
  'related':['mineral-buying','transportation','financing']
 }
]

# Editorial groups also drive the mega-menu, services index and enquiry pathways.
SERVICE_GROUPS = [
 ('Material examination', ['mineral-assay','gold-assay','diamonds','gemstones','assaying']),
 ('Processing & production', ['refining','manufacturing']),
 ('Logistics & custody', ['reception','transportation','storage','sample-handling']),
 ('Buying, trading & finance', ['mineral-buying','mineral-trading','financing']),
 ('Results & documentation', ['reporting']),
]
VALCAMBI_SERVICE_NAMES = ['Transportation','Reception','Assaying','Refining','Manufacturing','Financing','Storage']
