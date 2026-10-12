(()=>{
'use strict';
const toggle=document.querySelector('.nav-toggle');
const mobile=document.getElementById('mobile-navigation');
const menu=document.querySelector('.has-menu');
const menuButton=menu?.querySelector('.menu-trigger');
const closeMobile=()=>{if(!toggle||!mobile)return;toggle.setAttribute('aria-expanded','false');toggle.setAttribute('aria-label','Open navigation');mobile.hidden=true;};
const closeDesktop=()=>{if(!menu)return;menu.classList.remove('is-open');menu.classList.add('is-suppressed');menuButton?.setAttribute('aria-expanded','false');};
menu?.addEventListener('pointerleave',()=>menu.classList.remove('is-suppressed'));
menuButton?.addEventListener('focus',()=>menu?.classList.remove('is-suppressed'));
toggle?.addEventListener('click',()=>{const next=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(next));toggle.setAttribute('aria-label',next?'Close navigation':'Open navigation');mobile.hidden=!next;if(next){closeDesktop();mobile.querySelector('a')?.focus();}});
menuButton?.addEventListener('click',()=>{const next=!menu.classList.contains('is-open');closeMobile();menu.classList.remove('is-suppressed');menu.classList.toggle('is-open',next);menuButton.setAttribute('aria-expanded',String(next));});
document.addEventListener('keydown',(ev)=>{if(ev.key==='Tab'&&mobile&&!mobile.hidden){const targets=[...mobile.querySelectorAll('a,summary,button,[tabindex]:not([tabindex="-1"])')].filter(el=>el.getClientRects().length);if(targets.length){const first=targets[0],last=targets[targets.length-1];if(ev.shiftKey&&document.activeElement===first){ev.preventDefault();last.focus();}else if(!ev.shiftKey&&document.activeElement===last){ev.preventDefault();first.focus();}}}if(ev.key==='Escape'){const wasOpen=toggle?.getAttribute('aria-expanded')==='true';closeMobile();closeDesktop();if(wasOpen)toggle?.focus();}});
document.addEventListener('pointerdown',(ev)=>{if(menu&&!menu.contains(ev.target))closeDesktop();if(mobile&&!mobile.hidden&&!document.querySelector('.site-header')?.contains(ev.target))closeMobile();});
window.addEventListener('resize',()=>{if(innerWidth>1130)closeMobile();});
const form=document.getElementById('enquiry-form');if(!form)return;
const urlParams=new URLSearchParams(location.search);
const serviceSelect=form.querySelector('[name=service]');const requested=urlParams.get('service');
if(requested&&Array.from(serviceSelect.options).some(o=>o.value===requested))serviceSelect.value=requested;
const status=document.getElementById('form-status');const output=document.getElementById('enquiry-output');const draftNode=document.getElementById('enquiry-draft');const copy=document.getElementById('copy-enquiry');const copyStatus=document.getElementById('copy-status');const mailto=document.getElementById('mailto-enquiry');
const officialEmail=document.querySelector('meta[name="asl-contact-email"]')?.content||'';
function draftData(){let data=new FormData(form);return `AURUM STANDARD LABORATORIES — SERVICE ENQUIRY\n\nFull name: ${data.get('name')}\nEmail: ${data.get('email')}\nTelephone: ${data.get('phone')||'Not supplied'}\nLocation: ${data.get('location')||'Not supplied'}\nService of interest: ${serviceSelect.selectedOptions[0]?.textContent||''}\n\nMATERIAL / SPECIMEN\n${data.get('material')}\n\nQUESTION OR REQUEST\n${data.get('message')}\n\nPrepared using the ASL website enquiry form. This text is an enquiry draft, not a sample record or assay report.`;}
form.addEventListener('submit',(ev)=>{ev.preventDefault();status.textContent='';output.hidden=true;form.querySelectorAll('[aria-invalid]').forEach(i=>i.removeAttribute('aria-invalid'));
 const honeypot=form.querySelector('[name=organisation_url]');if(honeypot?.value)return;
 const invalid=Array.from(form.querySelectorAll('[required]')).filter(el=>!el.checkValidity());
 if(invalid.length){invalid.forEach(el=>el.setAttribute('aria-invalid','true'));status.textContent='Please complete all required fields and enter a valid email address.';invalid[0].focus();return;}
 const draft=draftData();draftNode.textContent=draft;output.hidden=false;copyStatus.textContent='';
 if(officialEmail){mailto.hidden=false;mailto.href=`mailto:${encodeURIComponent(officialEmail)}?subject=${encodeURIComponent('ASL service enquiry — '+serviceSelect.selectedOptions[0].textContent)}&body=${encodeURIComponent(draft)}`;}else{mailto.hidden=true;}
 output.scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'start'});
});
copy?.addEventListener('click',async()=>{const draft=draftNode.textContent||'';try{await navigator.clipboard.writeText(draft);copyStatus.textContent='Enquiry text copied to clipboard. Your message has not been sent.';}catch(_){const range=document.createRange();range.selectNodeContents(draftNode);const sel=window.getSelection();sel.removeAllRanges();sel.addRange(range);copyStatus.textContent='Enquiry text selected. Use Copy (Ctrl+C / Cmd+C) to copy it. Your message has not been sent.';}});
})();
