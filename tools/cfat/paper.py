"""Build a real CFAT paper (+ solutions copy) from subchapter blocks, in the house CFAT layout
(title box with code + Name + score box; Section A multiple choice in a 2-column grid; Section B short answer).
   python3 tools/cfat/paper.py 10MAA 1 "Algebra and Linear Relations"
Stream levels: 10MAG = L1 + L2, 10MAA = L2 + L3. Which subchapters = courses/lessons.json cfats[stream|unit][n-1]."""
import json,sys,os
HERE=os.path.dirname(os.path.abspath(__file__));ROOT=os.path.join(HERE,'..','..')
LEVELS={'10MAG':('L1','L2'),'10MAA':('L2','L3')}

CSS="""*{box-sizing:border-box}body{font-family:Arial,"Liberation Sans",Helvetica,sans-serif;font-size:9.8pt;line-height:1.28;color:#000;margin:0}
.sheet>*:last-child{margin-bottom:0}
@page{size:A4;margin:0}
.sheet{width:210mm;height:297mm;padding:11mm 12mm 12mm;background:#fff;overflow:hidden;position:relative;break-after:page}
.sheet:last-child{break-after:auto}.sheet .pno{position:absolute;bottom:6mm;left:0;right:0;text-align:center;font-size:8.5pt;color:#444}
@media screen{html{background:#8a8a8a}.sheet{margin:8mm auto;box-shadow:0 2px 14px rgba(0,0,0,.45)}}
#flow{width:186mm}
.title{display:flex;align-items:center;gap:4mm;border:2px solid #000;padding:2mm 4mm;margin-bottom:2mm}
.title .code{font-size:15pt;line-height:1.1;text-align:center;font-weight:bold;border-right:2px solid #000;padding-right:4mm}
.title h1{font-size:16pt;margin:0;flex:1}.title h1 div{font-size:10pt;font-weight:normal;margin-top:1mm}
.title .who{font-size:10.5pt;white-space:nowrap;display:flex;flex-direction:column;gap:2mm;align-items:flex-end}
.title .who i{display:inline-block;border-bottom:1px solid #000;width:52mm;height:5mm;vertical-align:bottom}
.title .who .scb{display:inline-block;border:1.5px solid #000;width:26mm;height:9mm;text-align:right;padding:1mm 2mm;font-size:12pt;font-weight:bold}
.secthd{font-weight:bold;text-transform:uppercase;letter-spacing:.4px;font-size:10.5pt;margin:0 0 1.5mm;display:flex;justify-content:space-between}
.secthd span{text-transform:none;letter-spacing:0;font-weight:normal;font-size:9.5pt}
.qgrid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:2.5mm;margin-bottom:2.5mm}
.box{border:1.2px solid #000;break-inside:avoid;display:flex;flex-direction:column}
.box>.hd{font-weight:bold;font-size:10.5pt;text-transform:uppercase;letter-spacing:.4px;border-bottom:1.2px solid #000;padding:1mm 3mm;background:#eee;display:flex;justify-content:space-between;white-space:nowrap}
.box>.hd span{text-transform:none;font-weight:normal;letter-spacing:0}
.box>.bd{padding:2mm 3mm;flex:1;display:flex;flex-direction:column}
.q{margin:0 0 1.5mm}.mc{display:grid;grid-template-columns:1fr;gap:1.6mm;margin:1mm 0}.mc div{display:flex;gap:1mm}.mc b{flex:none;width:5mm}
.blank{flex:1}
.cite{font-size:8pt;font-style:italic;color:#444;text-align:right;margin-top:auto;padding-top:1mm}
.skill{font-size:8pt;color:#555;font-weight:normal}
svg.fig{display:block;margin:1mm 0 1mm 2mm;max-width:100%;height:auto}
.ans{display:none;color:#c00}.sol .ans{display:block}.sol .mc .ok{color:#c00;font-weight:bold}
.ans>div{margin:1mm 0}
.brk{break-before:page}
table.sk{break-inside:avoid;border-collapse:collapse;margin:3mm 0 0 auto;font-size:9pt}table.sk td,table.sk th{border:1px solid #000;padding:1mm 2.5mm;text-align:center}table.sk th{background:#eee}
table.sk td:first-child{text-align:left}"""

def card_tenA(lib,cid):
    return any(x['id']==cid and x.get('tenA') for c in lib['chapters'] for x in c.get('subchapters',[]))

def load(card): return json.load(open(os.path.join(HERE,f'{card}.json')))

def build(stream,n,unit):
    lp=json.load(open(os.path.join(ROOT,'courses/lessons.json')))
    cards=[x['id'] for x in lp['cfats'][f'{stream}|{unit}'][n-1]['items']]
    lv=LEVELS[stream];subs=[c.split('-')[1] for c in cards]
    lib=json.load(open(os.path.join(ROOT,'library/C10.json')))
    A=[];B=[];skills=[]
    for c in cards:
        b=load(c);sub=c.split('-')[1]
        for s in b['skills']:
            tag=f'{sub}.{s["n"]}';skills.append([tag,s['skill'],0])
            # one question per skill: alternate the stream's two levels within a subchapter (10A subchapters take the harder level)
            want=lv[1] if (card_tenA(lib,c) or s['n']%2==0) else lv[0]
            it=[x for x in s['items'] if x['level']==want][0]
            it=dict(it,tag=tag);(A if it['type']=='mc' else B).append(it);skills[-1][2]+=it['marks']
    tot=sum(s[2] for s in skills);ma=sum(i['marks'] for i in A);mb=sum(i['marks'] for i in B)
    qn=[0]
    def hd(it):
        qn[0]+=1;return f'<div class="hd">Question {qn[0]} <span><span class="skill">{it["tag"]} · {it["level"]}</span> &nbsp; {it["marks"]} mark{"s" if it["marks"]>1 else ""}</span></div>'
    def ans(it): return '<div class="ans">'+''.join(f'<div>{x}</div>' for x in it['sol'])+'</div>'
    def cite(it): return f'<div class="cite">{it["src"]}</div>'
    def mcbox(it):
        o=''.join(f'<div class="{"ok" if "ABCDE"[k]==it["answer"] else ""}"><b>{"ABCDE"[k]}.</b><span>{x}</span></div>' for k,x in enumerate(it['options']))
        cols=3 if max(len(x) for x in it["options"])<16 else 2
        return f'<div class="box">{hd(it)}<div class="bd"><p class="q">{it["q"]}</p><div class="mc" style="grid-template-columns:repeat({cols},1fr)">{o}</div>{ans(it)}{cite(it)}</div></div>'
    def sabox(it):
        h=24 if it['marks']==1 else 32
        return f'<div class="box">{hd(it)}<div class="bd" style="min-height:{h}mm"><p class="q">{it["q"]}</p>{ans(it)}<div class="blank"></div>{cite(it)}</div></div>'
    def rows(items,f): return ''.join(f'<div class="qgrid">{"".join(f(x) for x in items[k:k+2])}</div>' for k in range(0,len(items),2))
    title={1:'Algebra review, equations &amp; inequalities'}.get(n,unit)
    body=(f'<div class="title"><div class="code">CFAT<br>1.{n}</div><h1>{title}<div>{", ".join(subs)} · {stream} · 20 minutes · Show all working</div></h1>'
          f'<div class="who"><div>Name <i></i></div><div class="scb">/{tot}</div></div></div>'
          f'<div class="secthd">Section A · Multiple choice<span>Circle one answer. {ma} marks</span></div>{rows(A,mcbox)}'
          f'<div class="secthd">Section B · Short answer<span>Show your working. {mb} marks</span></div>{rows(B,sabox)}'
          )
    os.makedirs(os.path.join(ROOT,'assessments'),exist_ok=True)
    base=f'CFAT 1.{n} - {stream} - {subs[0]}-{subs[-1]}'
    for sol in (False,True):
        name=base+(' - Solutions' if sol else '')
        html=(f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>{name}</title>'
          '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">'
          '<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>'
          '<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>'
          f'<style>{CSS}</style></head><body class="{"sol" if sol else ""}"><div id="flow">'
          + body.replace('Show all working','Worked solutions' if sol else 'Show all working') +
          """<script>renderMathInElement(document.body,{delimiters:[{left:'$',right:'$',display:false}],throwOnError:false});
document.fonts.ready.then(()=>{const flow=document.getElementById('flow');const items=[...flow.children];const H=297-23-6;const mm=v=>v*96/25.4;
let sh,used=0,n=0;const newSheet=()=>{sh=document.createElement('div');sh.className='sheet';document.body.appendChild(sh);used=0;n++};newSheet();
items.forEach((el,k)=>{const h=el.getBoundingClientRect().height+parseFloat(getComputedStyle(el).marginBottom||0);
 const keep=el.classList.contains('secthd')&&items[k+1]?items[k+1].getBoundingClientRect().height:0;
 if(used>0&&used+h+keep>mm(H))newSheet();sh.appendChild(el);used+=h});
flow.remove();document.querySelectorAll('.sheet').forEach((x,k,a)=>{const p=document.createElement('div');p.className='pno';p.textContent='Page '+(k+1)+' of '+a.length;x.appendChild(p)});document.body.dataset.ready=1})</script></body></html>""")
        p=os.path.join(ROOT,'assessments',name+'.html');open(p,'w').write(html);print(p,f'{len(A)} MC + {len(B)} SA = {tot} marks')

if __name__=='__main__':
    build(sys.argv[1],int(sys.argv[2]),sys.argv[3] if len(sys.argv)>3 else 'Algebra and Linear Relations')
