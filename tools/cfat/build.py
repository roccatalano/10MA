"""Test build: one subchapter CFAT block -> preview page with the block grid and the two stream papers.
   python3 tools/cfat/build.py C10-1A
10MAG = L1 + L2, 10MAA = L2 + L3. MC first (Section A), then short answer (Section B)."""
import json,sys,os
HERE=os.path.dirname(os.path.abspath(__file__));ROOT=os.path.join(HERE,'..','..')
STREAMS={'10MAG':('L1','L2'),'10MAA':('L2','L3')}
LV={'L1':'L1','L2':'L2','L3':'L3'}

def items(block,levels):
    out=[]
    for s in block['skills']:
        for it in s['items']:
            if it['level'] in levels: out.append(dict(it,skill=s['n'],skilltext=s['skill']))
    return out

def sol(it):
    return '<div class="sol">'+''.join(f'<div>{x}</div>' for x in it['sol'])+'</div>'

def mc(it,qn):
    opts=''.join(f'<li class="{"ok" if "ABCDE"[k]==it["answer"] else ""}"><b>{"ABCDE"[k]}</b> {o}</li>' for k,o in enumerate(it['options']))
    return (f'<div class="cell"><div class="qh"><b>Question {qn}</b><span class="tagl">{it["level"]} · skill {SUB}.{it["skill"]}</span></div>'
            f'<p>{it["q"]}</p><ol class="mc">{opts}</ol>{sol(it)}<div class="src">{it["src"]} · {it["vc2"]}</div></div>')

def sa(it,qn):
    h=22 if it['marks']==1 else 34
    return (f'<div class="cell"><div class="qh"><b>Question {qn}</b><span class="tagl">{it["level"]} · skill {SUB}.{it["skill"]}</span><span class="mk">({it["marks"]} mark{"s" if it["marks"]>1 else ""})</span></div>'
            f'<p>{it["q"]}</p><div class="ws" style="min-height:{h}mm">{sol(it)}</div><div class="src">{it["src"]} · {it["vc2"]}</div></div>')

def paper(block,stream):
    lv=STREAMS[stream];its=items(block,lv)
    A=[i for i in its if i['type']=='mc'];B=[i for i in its if i['type']=='sa']
    qn=0;a='';b=''
    for i in A: qn+=1;a+=mc(i,qn)
    for i in B: qn+=1;b+=sa(i,qn)
    tot=sum(i['marks'] for i in its)
    by={}
    for i in its: by[i['skill']]=by.get(i['skill'],0)+i['marks']
    score=''.join(f'<td>{SUB}.{k}<br><span>/{v}</span></td>' for k,v in sorted(by.items()))
    return (f'<section class="page" data-tab="{stream}"><div class="title"><div class="code">CFAT</div><h1>{SUB} {TITLE}</h1><div class="pg">{stream} · {" + ".join(lv)} · test build</div></div>'
            f'<div class="name"><b>Name:</b> <span class="line"></span> <b>Class:</b> {stream}</div>'
            + (f'<div class="band">Section A · Multiple choice <span>Circle one answer</span></div><div class="grid">{a}</div>' if A else '')
            + f'<div class="band">Section B · Short answer <span>Show your working</span></div><div class="grid">{b}</div>'
            f'<table class="score"><tr><td><b>Skill</b><br><span>marks</span></td>{score}<td><b>Total</b><br><span>/{tot}</span></td></tr></table></section>')

def grid(block):
    rows=''
    for s in block['skills']:
        cells=''.join(f'<td><div class="ty">{"Multiple choice" if it["type"]=="mc" else "Short answer"} · {it["marks"]} mk</div><p>{it["q"]}</p>'
                      +(('<ol class="mc sm">'+''.join(f'<li class="{"ok" if "ABCDE"[k]==it["answer"] else ""}"><b>{"ABCDE"[k]}</b> {o}</li>' for k,o in enumerate(it["options"]))+'</ol>') if it['type']=='mc' else '')
                      +f'{sol(it)}<div class="src">{it["src"]}</div></td>' for it in s['items'])
        rows+=f'<tr><th>{SUB}.{s["n"]}<br><span>{s["skill"]}</span></th>{cells}</tr>'
    return (f'<section class="page wide" data-tab="block"><div class="title"><div class="code">Block</div><h1>{block["card"]} · {TITLE}</h1><div class="pg">{len(block["skills"])} skills × 3 levels</div></div>'
            f'<p class="note">One block per subchapter. <b>10MAG</b> papers take the L1 + L2 columns; <b>10MAA</b> papers take L2 + L3. The L2 column is shared, so both streams can be compared on the same questions.</p>'
            f'<table class="blk"><thead><tr><th>Skill (checklist)</th><th>L1 · Level 9 review</th><th>L2 · Level 10</th><th>L3 · extension</th></tr></thead><tbody>{rows}</tbody></table></section>')

CSS="""*{box-sizing:border-box}body{margin:0;background:#8a8a8a;font-family:Arial,Helvetica,sans-serif;font-size:10.5pt;color:#000}
.bar{position:sticky;top:0;z-index:5;background:#222;color:#fff;padding:8px 14px;display:flex;gap:8px;align-items:center;font:14px system-ui}
.bar button{font:inherit;border:1px solid #888;background:#333;color:#fff;padding:4px 12px;border-radius:4px;cursor:pointer}.bar button.on{background:#fff;color:#000}
.bar label{margin-left:auto}
.page{width:210mm;min-height:297mm;margin:8mm auto;padding:11mm 12mm;background:#fff;box-shadow:0 2px 14px rgba(0,0,0,.45);display:none}
.page.wide{width:297mm;min-height:210mm}.page.on{display:block}
.title{display:flex;align-items:center;gap:12px;border:2px solid #000;padding:6px 12px}.title .code{font-size:20pt;font-weight:bold;border-right:2px solid #000;padding-right:12px}.title h1{font-size:15pt;margin:0;flex:1}.title .pg{font-size:9pt;color:#333}
.name{margin:8px 0}.name .line{display:inline-block;width:80mm;border-bottom:1px solid #000;margin-right:14px}
.band{background:#eee;border:1.5px solid #000;padding:3px 10px;font-weight:bold;text-transform:uppercase;font-size:9.5pt;letter-spacing:.4px;margin-top:8px;display:flex;justify-content:space-between}.band span{font-weight:normal;text-transform:none}
.grid{display:grid;grid-template-columns:1fr 1fr;border:1.5px solid #000;border-top:0}
.cell{padding:7px 10px;border-top:1px solid #000;border-left:1px solid #000;display:flex;flex-direction:column}.cell:nth-child(odd){border-left:0}.cell:nth-child(-n+2){border-top:0}
.qh{display:flex;gap:8px;align-items:baseline}.qh .tagl{font-size:8pt;color:#666}.qh .mk{margin-left:auto;font-size:9pt}
.cell p{margin:5px 0}
ol.mc{list-style:none;padding:0;margin:2px 0 0 4px}ol.mc li{margin:3px 0}ol.mc li b{display:inline-block;width:18px}
.sol,.src{display:none}.showsol .sol{display:block;color:#c00000;margin-top:4px}.showsol .src{display:block;color:#c00000;font-size:7.5pt;margin-top:auto;padding-top:4px;text-align:right}
.showsol ol.mc li.ok{color:#c00000;font-weight:bold}
.ws{flex:1}.cell p svg.fig,table.blk svg.fig{display:block;margin:4px 0;max-width:100%;height:auto}.sol svg{display:block;max-width:100%;height:auto}
table.score{border-collapse:collapse;margin-top:10px;margin-left:auto}table.score td{border:1.5px solid #000;padding:4px 10px;text-align:center;font-size:9pt}table.score span{display:inline-block;min-width:28px;text-align:right;padding-top:8px}
.note{font-size:10pt}
table.blk{border-collapse:collapse;width:100%;font-size:9.5pt}table.blk th,table.blk td{border:1.5px solid #000;padding:6px 8px;vertical-align:top;text-align:left}
table.blk thead th{background:#eee;font-size:9pt;text-transform:uppercase}table.blk tbody th{width:19%}table.blk tbody th span{font-weight:normal;font-size:9pt}
table.blk td p{margin:3px 0}.ty{font-size:7.5pt;color:#666;text-transform:uppercase}ol.mc.sm li{margin:5px 0;font-size:9pt}.sol>div{margin:5px 0}
table.blk .src{display:block;font-size:7.5pt;color:#555;margin-top:4px}table.blk .sol{display:block;color:#c00000}
@media print{body{background:#fff}.bar{display:none}.page{box-shadow:none;margin:0;display:none}.page.on{display:block}}"""

def build(card):
    global SUB,TITLE
    b=json.loads(open(os.path.join(HERE,f'{card}.json')).read().replace('\\\\$','<span class=\\"nomath\\">$</span>'));SUB=card.split('-')[1]
    lib=json.load(open(os.path.join(ROOT,'library/C10.json')))
    TITLE=[x for c in lib['chapters'] for x in c.get('subchapters',[]) if x['id']==card][0]['title']
    plans=json.load(open(os.path.join(ROOT,'courses/lessons.json')))['plans']
    taught=[st for st in STREAMS if any(it['id']==card for k,v in plans.items() if k.startswith(st+'|') for l in v for it in l['items'])]
    out=os.path.join(ROOT,f'lessons/{card} CFAT block - test build.html')
    html=(f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>{card} CFAT block · test build</title>'
      '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">'
      '<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>'
      '<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>'
      f'<style>{CSS}</style></head><body>'
      '<div class="bar"><button data-t="block" class="on">Block</button>'+''.join(f'<button data-t="{st}">{st} paper ({" + ".join(STREAMS[st])})</button>' for st in taught)+(f'<span style="opacity:.7">{SUB} is not taught in {", ".join(x for x in STREAMS if x not in taught)}</span>' if len(taught)<len(STREAMS) else '')+'<label><input type="checkbox" id="sol"> Show solutions + sources</label></div>'
      + grid(b) + ''.join(paper(b,st) for st in taught) +
      """<script>renderMathInElement(document.body,{delimiters:[{left:'$',right:'$',display:false}],ignoredClasses:['nomath'],throwOnError:false});
const tab=t=>{document.querySelectorAll('.page').forEach(p=>p.classList.toggle('on',p.dataset.tab===t));document.querySelectorAll('.bar button').forEach(b=>b.classList.toggle('on',b.dataset.t===t))};
document.querySelectorAll('.bar button').forEach(b=>b.onclick=()=>tab(b.dataset.t));tab(new URLSearchParams(location.search).get('t')||'block');
const S=document.getElementById('sol');S.onchange=()=>document.body.classList.toggle('showsol',S.checked);if(new URLSearchParams(location.search).get('sol')){S.checked=true;S.onchange()}
document.body.dataset.ready=1</script></body></html>""")
    open(out,'w').write(html);print(out)

if __name__=='__main__':
    for c in (sys.argv[1:] or ['C10-1A']): build(c)
