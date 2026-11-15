"""Build the 10MAG Modified unit workbook: house-style cover + per lesson (Lesson planning order) the modified worksheet,
then that lesson's Freefall sheets (courses/modified.json; each sheet once per unit).
Freefall is licensed to the school: the output goes to G: only and is NEVER written inside this repo.
   python3 tools/worksheets/workbook_m.py "Univariate Statistics" <Freefall folder> <out folder>
Freefall 8 copy = Teacher Edition: each topic is notes, worksheet, answers (, worksheet, answers ...): answer pages are left out."""
import json,subprocess,sys,html,os
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
sys.path.insert(0,os.path.dirname(__file__));_w=open(os.path.join(os.path.dirname(__file__),'workbook.py')).read();CSS=_w[_w.index("CSS='''")+7:_w.index("'''",_w.index("CSS='''")+7)]   # cover CSS from workbook.py
unit,FFDIR,OUT=sys.argv[1],sys.argv[2],sys.argv[3]
assert not os.path.abspath(OUT).startswith(ROOT),'Freefall pages must never be written into the repo'
U=json.load(open(f'{ROOT}/courses/units.json'));L=json.load(open(f'{ROOT}/courses/lessons.json'));M=json.load(open(f'{ROOT}/courses/modified.json'))
FF=json.load(open(f'{ROOT}/courses/freefall.json'));SH={s['id']:s for s in FF['sheets']};BOOK={k:os.path.join(FFDIR,v['file']) for k,v in FF['books'].items()}
IDX={s['id']:s for ch in json.load(open(f'{ROOT}/library/C10.json'))['chapters'] for s in ch['subchapters']}
key='10MAG|'+unit;us=[u for u in U['units'] if u['stream']=='10MAG'];num='G'+str(next(i for i,u in enumerate(us,1) if u['name']==unit))
pages=lambda f:int(subprocess.run(['pdfinfo',f],capture_output=True,text=True).stdout.split('Pages:')[1].split()[0])
def _yellow(book,p):
    # FF8 notes pages have a yellow background; worksheets and answer pages are white
    from PIL import Image;o=f'/tmp/ffchk_{p}';subprocess.run(['pdftoppm','-r','12','-png','-f',str(p),'-l',str(p),'-singlefile',book,o],capture_output=True)
    im=Image.open(o+'.png').convert('RGB');w,h=im.size;r,g,b=im.getpixel((w//2,h-3));return b<200 and r>200 and g>200
def ffpages(s):
    r=list(range(s['start'],s['end']+1))
    if s['book']!='FF8':return r
    # FF8 = Teacher Edition: notes (yellow, 1-2 pages), worksheet (white), answers (white, straight after its worksheet), repeated.
    # Keep yellow pages and the first white page of each run of white pages; drop the answer page that follows it.
    out=[];prev_white=False
    for p in r:
        if _yellow(BOOK['FF8'],p):out.append(p);prev_white=False
        elif not prev_white:out.append(p);prev_white=True
        else:prev_white=False
    return out
plan=L['plans'][key];cf=L['cfats'][key];seen_ff=set();cnt={};seen={};parts=[];rows='';pno=2;last=None
for l in plan:
    if l['kind']=='teach':[cnt.__setitem__(x['id'],cnt.get(x['id'],0)+1) for x in l['items']]
for k,l in enumerate(plan,1):
    if l['kind']!='teach':continue
    week=next((i+1 for i,c in enumerate(cf) if any(x['id'] in [y['id'] for y in c['items']] for x in l['items'])),None)
    if week!=last:last=week;ch=''.join(c for c in IDX[cf[week-1]['items'][0]['id']]['sub'] if c.isdigit());rows+=f'<tr class="cf"><td colspan="3">CFAT {num[1:]}.{ch}.{week}M · Week {week}</td></tr>'
    for x in l['items']:
        sub=IDX[x['id']]['sub'];seen[x['id']]=seen.get(x['id'],0)+1
        ws=f'{ROOT}/lessons/C10-{sub} modified worksheet'+(f' (part {seen[x["id"]]})' if cnt[x['id']]>1 else '')+'.pdf'
        n=pages(ws);rows+=f'<tr><td class="n">L{k}</td><td>{sub} modified worksheet</td><td class="p">{pno}</td></tr>';parts.append((ws,f'1-{n}'));pno+=n
        for fid in M['sheets'].get(x['id'],[]):
            if fid in seen_ff:continue
            seen_ff.add(fid);s=SH[fid];pp=ffpages(s)
            rows+=f'<tr><td class="n"></td><td>&nbsp;&nbsp;Freefall: {html.escape(s["title"])} <small>({fid})</small></td><td class="p">{pno}</td></tr>'
            parts.append((BOOK[s['book']],','.join(map(str,pp))));pno+=len(pp)
doc=f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="pg">
<div class="title"><div class="code">{num}M</div><div><h1>{html.escape(unit)}</h1><div class="sub">Year 10 Mathematics · 10MAG Modified · Unit workbook</div></div></div>
<div class="big">Modified unit workbook</div>
<div class="who"><b>Name</b><i></i><b>Class</b><i></i><b>Teacher</b><i></i></div>
<div class="box"><div class="hd">Contents</div><table><tr><th>Lesson</th><th>Worksheet / Freefall sheet</th><th class="p">Page</th></tr>{rows}</table></div>
<div class="foot"><span>Cambridge Essential Mathematics 7, 8 &amp; 9 (3rd Ed.) · Freefall Mathematics (licensed to EKC, not for distribution)</span><span>Bring this workbook to every lesson</span></div></div></body></html>'''
os.makedirs(OUT,exist_ok=True);cov='/tmp/mcover.html';open(cov,'w').write(doc)
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b=pw.chromium.launch();pg=b.new_page();pg.goto('file://'+cov);pg.emulate_media(media='print');pg.pdf(path='/tmp/mcover.pdf',prefer_css_page_size=True,print_background=True)
out=os.path.join(OUT,f'10MAG Modified {unit} - Unit workbook.pdf')
args=['qpdf','--empty','--pages','/tmp/mcover.pdf','1']
for f,r in parts:args+=[f,r]
subprocess.run(args+['--',out],check=True);print(out,pages(out),'pages')
