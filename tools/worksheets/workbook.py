"""Build '<stream> <unit> - Unit workbook.pdf' = house-style cover + subchapter worksheet PDFs in Lesson planning order.
Run from the repo root:  python3 tools/worksheets/workbook.py "10MAA|Algebra and Linear Relations" ..."""
import json,subprocess,sys,html,os
from playwright.sync_api import sync_playwright
U=json.load(open('courses/units.json'));L=json.load(open('courses/lessons.json'))
IDX={s['id']:s for b in ('C10','G11') for ch in json.load(open(f'library/{b}.json'))['chapters'] for s in ch['subchapters']}
pages=lambda f:int(subprocess.run(['pdfinfo',f],capture_output=True,text=True).stdout.split('Pages:')[1].split()[0])
CSS='''@page{size:A4;margin:0}*{box-sizing:border-box}body{margin:0;font-family:Arial,Helvetica,sans-serif;color:#000}
.pg{width:210mm;height:297mm;padding:16mm 16mm 14mm;display:flex;flex-direction:column}
.title{display:flex;align-items:center;gap:5mm;border:2.5px solid #000;padding:5mm 6mm}
.title .code{font-size:34pt;font-weight:bold;border-right:2.5px solid #000;padding-right:6mm}
.title h1{font-size:26pt;margin:0;line-height:1.1}.title .sub{font-size:12pt;margin-top:1.5mm}
.big{margin:7mm 0 6mm;font-size:15pt;font-weight:bold;letter-spacing:.5px;text-transform:uppercase;border-bottom:1.5px solid #000;padding-bottom:2mm}
.who{display:grid;grid-template-columns:auto 1fr;gap:6mm 4mm;font-size:12pt;margin-bottom:8mm}.who i{border-bottom:1px solid #000}
.box{border:1.2px solid #000}.box>.hd{font-weight:bold;font-size:11pt;text-transform:uppercase;letter-spacing:.4px;border-bottom:1.2px solid #000;padding:1.5mm 3mm;background:#eee}
table{width:100%;border-collapse:collapse;font-size:11pt}td,th{padding:1.6mm 3mm;border-bottom:1px solid #bbb;text-align:left}th{font-size:9.5pt;text-transform:uppercase;color:#333}
td.n{width:14mm;font-weight:bold}td.p,th.p{width:16mm;text-align:right}tr.cf td{background:#f3f3f3;font-size:9.5pt;font-weight:bold;letter-spacing:.3px;border-bottom:1px solid #000}
.foot{margin-top:auto;font-size:9pt;color:#333;display:flex;justify-content:space-between;border-top:1px solid #000;padding-top:2mm}
@media screen{html{background:#8a8a8a}body{padding:8mm 0}.pg{margin:0 auto;background:#fff;box-shadow:0 2px 14px rgba(0,0,0,.45)}}'''
def build(key):
  st,name=key.split('|');us=[u for u in U['units'] if u['stream']==st];u=next(x for x in us if x['name']==name);num=('A' if st=='10MAA' else 'G')+str(us.index(u)+1)
  order=[]
  for l in L['plans'][key]:
    for x in l['items']:
      if x['id'] not in order:order.append(x['id'])
  cf={x['id']:i+1 for i,c in enumerate(L.get('cfats',{}).get(key,[])) for x in c['items']}
  files=[f'lessons/{i} worksheet.pdf' for i in order];missing=[f for f in files if not os.path.exists(f)]
  if missing:sys.exit('missing worksheets: '+', '.join(missing))
  p=2;rows='';last=None
  for i,f in zip(order,files):
    if cf.get(i)!=last:last=cf.get(i);rows+=f'<tr class="cf"><td colspan="3">CFAT {last} · Week {last}</td></tr>' if last else ''
    s=IDX[i];rows+=f'<tr><td class="n">{s["sub"]}</td><td>{html.escape(s["title"])}{" <b>(10A)</b>" if s.get("tenA") else ""}</td><td class="p">{p}</td></tr>';p+=pages(f)
  doc=f'''<!DOCTYPE html><html><head><meta charset="utf-8"><title>{st} {num} {html.escape(name)} – Unit workbook</title><style>{CSS}</style></head><body><div class="pg">
  <div class="title"><div class="code">{num}</div><div><h1>{html.escape(name)}</h1><div class="sub">Year 10 Mathematics · {st} · Unit workbook</div></div></div>
  <div class="big">Unit workbook</div>
  <div class="who"><b>Name</b><i></i><b>Class</b><i></i><b>Teacher</b><i></i><b>Coursework option</b><span>Good &nbsp;/&nbsp; Better &nbsp;/&nbsp; Best &nbsp;<small>(circle the one your teacher sets)</small></span></div>
  <div class="box"><div class="hd">Contents</div><table><tr><th>Sub</th><th>Subchapter</th><th class="p">Page</th></tr>{rows}</table></div>
  <div class="foot"><span>Cambridge Essential Mathematics for the Victorian Curriculum 10 &amp; 10A, 3rd Ed.</span><span>Bring this workbook to every lesson</span></div></div></body></html>'''
  cover=f'lessons/{st} {name} - Unit workbook cover.html';open(cover,'w').write(doc)
  with sync_playwright() as pw:
    b=pw.chromium.launch();pg=b.new_page();pg.goto('file://'+os.path.abspath(cover));pg.emulate_media(media='print');pg.pdf(path='/tmp/cover.pdf',prefer_css_page_size=True,print_background=True)
  out=f'lessons/{st} {name} - Unit workbook.pdf'
  subprocess.run(['qpdf','--empty','--pages','/tmp/cover.pdf',*files,'--',out],check=True)
  print(out,pages(out),'pages')
for k in sys.argv[1:]:build(k)
