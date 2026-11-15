"""Build a real CFAT paper (+ solutions copy) from subchapter blocks, in the house CFAT layout
(title box with code + Name + score box; Section A multiple choice in a 2-column grid; Section B short answer).
   python3 tools/cfat/paper.py 10MAA 1 "Algebra and Linear Relations"
Stream levels: 10MAG = L1 + L2, 10MAA = L2 + L3. Which subchapters = courses/lessons.json cfats[stream|unit][n-1]."""
import json,sys,os,re
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
.eqs{display:block;margin:1mm 0 1mm 8mm}.eqs>span{display:block;margin:.6mm 0}
.qgrid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:2.5mm;margin-bottom:2.5mm}
.box{border:1.2px solid #000;break-inside:avoid;display:flex;flex-direction:column}
.box>.hd{font-weight:bold;font-size:10.5pt;text-transform:uppercase;letter-spacing:.4px;border-bottom:1.2px solid #000;padding:1mm 3mm;background:#eee;display:flex;justify-content:space-between;white-space:nowrap}
.box>.hd span{text-transform:none;font-weight:normal;letter-spacing:0}
.box>.bd{padding:2mm 3mm;flex:1;display:flex;flex-direction:column}
.q{margin:0 0 1.5mm}.mc{display:grid;grid-template-columns:1fr;gap:1.2mm;margin:1mm 0}.mc div{display:flex;gap:1mm;align-items:center}.mc b{flex:none;width:5mm}
.blank{flex:1}.sarow{margin-bottom:2.5mm}.sarow .box{min-height:0}
.cite{font-size:8pt;font-style:italic;color:#444;text-align:right;margin-top:auto;padding-top:1mm;visibility:hidden}.sol .cite{visibility:visible}
.skill{font-size:8pt;color:#555;font-weight:normal}
svg.fig{display:block;margin:1mm 0 1mm 2mm;max-width:100%;height:auto}
.ans{display:block;visibility:hidden;color:#c00}.sol .ans{visibility:visible}.sol .mc .ok{color:#c00}
.ans>div{margin:.3mm 0}.ans svg.fig{height:30mm;width:auto;max-width:100%;display:block;margin:2mm auto 0}.ans svg.fig[viewBox^="0 -6"]{height:15mm}.q svg.fig{height:14mm;width:auto}
.brk{break-before:page}.eqs{margin:1.5mm 0 1.5mm 6mm;line-height:1.7}.sol .stu{display:none}body:not(.sol) .ans svg{display:none}.stu svg.ax.nl{height:15mm!important}.skb{flex-direction:row!important;padding:0!important}.skl{flex:1;display:flex;flex-direction:column;padding:2mm 3mm;border-right:1.2px solid #000}.skr{flex:1;display:flex;align-items:center;justify-content:center;padding:2mm}.skr>div{width:100%}.skr svg{width:100%;height:auto;max-height:var(--gh,66mm);display:block;margin:0 auto}.skr .ans svg.fig{margin:0 auto!important;height:auto}.sol .skr .stu{display:none}body:not(.sol) .skr .ans{display:none}.stu svg.ax{display:block;margin:0;height:30mm;width:auto;max-width:100%}
.pg{margin-top:2mm}.pg svg{display:block;height:62mm;width:auto;max-width:100%;margin:0 auto}.pg .ans svg.fig{height:62mm;width:auto;margin:0 auto}.sol .pg .stu{display:none}body:not(.sol) .pg .ans{display:none}
table.sk{break-inside:avoid;border-collapse:collapse;margin:3mm 0 0 auto;font-size:9pt}table.sk td,table.sk th{border:1px solid #000;padding:1mm 2.5mm;text-align:center}table.sk th{background:#eee}
table.sk td:first-child{text-align:left}"""

def card_tenA(lib,cid):
    return any(x['id']==cid and x.get('tenA') for c in lib['chapters'] for x in c.get('subchapters',[]))

def load(card): return json.loads(open(os.path.join(HERE,f'{card}.json')).read().replace('\\\\$','<span class=\\"nomath\\">$</span>'))

import re
def build(stream,n,unit):
    lp=json.load(open(os.path.join(ROOT,'courses/lessons.json')))
    cards=[x['id'] for x in lp['cfats'][f'{stream}|{unit}'][n-1]['items']]
    lv=LEVELS[stream];subs=[c.split('-')[1] for c in cards]
    lib=json.load(open(os.path.join(ROOT,'library/C10.json')))
    A=[];B=[];skills=[]
    nsk=sum(len(load(c)['skills']) for c in cards);FEW=nsk<6   # short week: test both of the stream's levels
    fills=[]
    for c in cards:
        b=load(c);sub=c.split('-')[1]
        for s in b['skills']:
            tag=f'{sub}.{s["n"]}';skills.append([tag,s['skill'],0])
            # one question per skill: alternate the stream's two levels within a subchapter (10A subchapters take the harder level)
            want=lv[1] if (card_tenA(lib,c) or s['n']%2==0) else lv[0]
            pick=[x for x in s['items'] if not x.get('fill') and (x['level'] in lv if FEW else x['level']==want)]
            fills+=[dict(x,tag=tag) for x in s['items'] if x.get('fill') and x['level'] in lv]
            for it in pick:
                it=dict(it,tag=tag);(A if it['type']=='mc' else B).append(it);skills[-1][2]+=it['marks']
    while len(A)==1 and fills:   # never a lone multiple-choice question
        f=fills.pop(0);A.append(f);[sk.__setitem__(2,sk[2]+f['marks']) for sk in skills if sk[0]==f['tag']]
    nsk_=sum(1 for i in B if any(str(x).startswith('<svg') and 'viewBox="0 -6' not in x for x in i['sol']))
    GH='66mm' if nsk_<=2 else ('54mm' if nsk_==3 else '46mm')
    tot=sum(s[2] for s in skills);ma=sum(i['marks'] for i in A);mb=sum(i['marks'] for i in B)
    qn=[0]
    def hd(it):
        qn[0]+=1;return f'<div class="hd">Question {qn[0]} <span><span class="skill">{it["tag"]} · {it["level"]}</span> &nbsp; {it["marks"]} mark{"s" if it["marks"]>1 else ""}</span></div>'
    def ans(it): return '<div class="ans">'+''.join(f'<div>{x}</div>' for x in it['sol'])+'</div>'
    def cite(it): return f'<div class="cite">{it["src"]}</div>'
    REL=re.compile(r'(=|<|>|\\le|\\ge|\\leq|\\geq|\\leqslant|\\geqslant)')
    def eqlines(q):
        # agreed rule: two equations/inequalities in a stem go one per line, labelled [1], [2]
        m=re.search(r'\$([^$]+)\$(?: \[1\])? and \$([^$]+)\$(?: \[2\])?',q)
        if not m or not (REL.search(m.group(1)) and REL.search(m.group(2))): return q
        if all(re.fullmatch(r'\s*[a-z]\s*=\s*-?[\d.]+\s*',g) for g in m.groups()): return q   # substitution values, not equations
        e=f'<span class="eqs"><span>${m.group(1)}$ &nbsp;[1]</span><span>${m.group(2)}$ &nbsp;[2]</span></span>'
        rest=q[m.end():].lstrip(' ');rest=rest[1:] if rest.startswith('.') else rest
        return q[:m.start()]+e+rest
    def mcbox(it):
        it=dict(it,q=eqlines(it['q']))
        o=''.join(f'<div class="{"ok" if "ABCDE"[k]==it["answer"] else ""}"><b>{"ABCDE"[k]}.</b><span>{x}</span></div>' for k,x in enumerate(it['options']))
        return f'<div class="box">{hd(it)}<div class="bd"><p class="q">{it["q"]}</p><div class="mc">{o}</div>{cite(it)}</div></div>'
    def blank(v):
        v=re.sub(r'<(polygon|polyline|circle|text|path|line)[^>]*(#d00000|#f4b6b6)[^>]*/?>(</text>)?','',v)
        return re.sub(r'<text[^>]*fill="#d00000"[^<]*</text>','',v)
    def grid10():
        u=6;o=[]
        for k in range(-10,11):
            c='#bbb' if k else '#000';w=.5 if k else 1.2
            o.append(f'<line x1="{(k+10)*u}" y1="0" x2="{(k+10)*u}" y2="{20*u}" stroke="{c}" stroke-width="{w}"/>')
            o.append(f'<line x1="0" y1="{(k+10)*u}" x2="{20*u}" y2="{(k+10)*u}" stroke="{c}" stroke-width="{w}"/>')
        for k in (-10,-5,5,10):
            o.append(f'<text x="{(k+10)*u}" y="{10*u+7}" font-size="5" text-anchor="middle">{k}</text><text x="{10*u-2}" y="{(10-k)*u+2}" font-size="5" text-anchor="end">{k}</text>')
        o.append(f'<text x="{20*u+3}" y="{10*u+2}" font-size="6" font-style="italic" font-family="Times New Roman">x</text><text x="{10*u+2}" y="-2" font-size="6" font-style="italic" font-family="Times New Roman">y</text>')
        return f'<svg class="g10" viewBox="-4 -8 132 136">{"".join(o)}</svg>'
    def sabox(it):
        it=dict(it,q=eqlines(it['q']))
        figs=[x for x in it['sol'] if x.startswith('<svg')]
        nl=figs and 'viewBox="0 -6' in figs[-1]
        h=12
        if figs and not nl:
            txt=dict(it,sol=[x for x in it['sol'] if not x.startswith('<svg')])
            return (f'<div class="box sa" data-m="{it["marks"]}">{hd(it)}<div class="bd skb" style="min-height:{h}mm"><div class="skl"><p class="q">{it["q"]}</p>{ans(txt)}<div class="blank"></div>{cite(it)}</div>'
                    f'<div class="skr"><div class="stu">{grid10()}</div><div class="ans">{figs[-1]}</div></div></div></div>')
        if nl: it=dict(it,q=it['q']+'<div class="stu">'+re.sub(r'<(polygon|polyline|circle|text|path|line)[^>]*#d00000[^>]*/?>(</text>)?','',figs[-1]).replace('class="fig"','class="fig ax nl"')+'</div>')
        return f'<div class="box sa" data-m="{it["marks"]}">{hd(it)}<div class="bd" style="min-height:{h}mm"><p class="q">{it["q"]}</p>{ans(it)}<div class="blank"></div>{cite(it)}</div></div>'
    def pbox(it):
        # sketch question in a side-by-side pair: question on top, big grid underneath
        it=dict(it,q=eqlines(it['q']))
        figs=[x for x in it['sol'] if x.startswith('<svg')];txt=dict(it,sol=[x for x in it['sol'] if not x.startswith('<svg')])
        return (f'<div class="box sa" data-m="{it["marks"]}">{hd(it)}<div class="bd" style="min-height:12mm"><p class="q">{it["q"]}</p>{ans(txt)}<div class="blank"></div>'
                f'<div class="pg"><div class="stu">{grid10()}</div><div class="ans">{figs[-1]}</div></div>{cite(it)}</div></div>')
    def isk(it):
        f=[x for x in it['sol'] if str(x).startswith('<svg')];return bool(f) and 'viewBox="0 -6' not in f[-1]
    AUTO_PAIR=stream=='10MAG'   # 10MAG: adjacent sketch questions go side by side with big grids underneath
    def sarows():
        out=[];k=0;q0=len(A)
        while k<len(B):
            if AUTO_PAIR and k+1<len(B) and isk(B[k]) and isk(B[k+1]):
                out.append(f'<div class="qgrid pair">{pbox(B[k])}{pbox(B[k+1])}</div>');k+=2
            else: out.append(f'<div class="sarow">{sabox(B[k])}</div>');k+=1
        return ''.join(out)
    def rows(items,f): return ''.join(f'<div class="qgrid">{"".join(f(x) for x in items[k:k+2])}</div>' for k in range(0,len(items),2))
    title={'10MAA':{1:'Algebra review, equations &amp; inequalities',2:'Graphing and finding straight lines',3:'Length, midpoint, parallel lines and regions',4:'Simultaneous equations'},
           '10MAG':{1:'Algebra review, equations &amp; inequalities',2:'Graphing and finding straight lines',3:'Length, midpoint, parallel and perpendicular lines',4:'Simultaneous equations',5:'Simultaneous equations in context and regions'}}.get(stream,{}).get(n,unit)
    body=(f'<div class="title"><div class="code">CFAT<br>1.{n}</div><h1>{title}<div>{", ".join(subs)} · {stream} · 20 minutes · Show all working</div></h1>'
          f'<div class="who"><div>Name <i></i></div><div class="scb">/{tot}</div></div></div>'
          +(f'<div class="secthd">Section A · Multiple choice<span>Circle one answer. {ma} marks</span></div>{rows(A,mcbox)}' if A else '')
          +f'<div class="secthd">Section B · Short answer<span>Show your working. {mb} marks</span></div>'+sarows()
          )
    os.makedirs(os.path.join(ROOT,'assessments'),exist_ok=True)
    base=f'CFAT 1.{n} - {stream} - {subs[0]}-{subs[-1]}'
    for sol in (False,True):
        name=base+(' - Solutions' if sol else '')
        html=(f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>{name}</title>'
          '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">'
          '<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>'
          '<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>'
          f'<style>{CSS}body{{--gh:{GH}}}</style></head><body class="{"sol" if sol else ""}" data-cap="{22 if stream=='10MAG' else 999}"><div id="flow">'
          + body.replace('Show all working','<b style="color:#c00">Solutions</b>' if sol else 'Show all working') +
          """</div><script>renderMathInElement(document.body,{delimiters:[{left:'$',right:'$',display:false}],ignoredClasses:['nomath'],throwOnError:false});
document.fonts.ready.then(()=>{const flow=document.getElementById('flow');const items=[...flow.children];const H=297-23-6;const CAP=+document.body.dataset.cap;const mm=v=>v*96/25.4;
let sh,used=0,n=0;const newSheet=()=>{sh=document.createElement('div');sh.className='sheet';document.body.appendChild(sh);used=0;n++};newSheet();
items.forEach((el,k)=>{const h=el.getBoundingClientRect().height+parseFloat(getComputedStyle(el).marginBottom||0);
 const keep=el.classList.contains('secthd')&&items[k+1]?items[k+1].getBoundingClientRect().height:0;
 if(used>0&&used+h+keep>mm(H))newSheet();sh.appendChild(el);used+=h});
flow.remove();
document.querySelectorAll('.sheet').forEach(x=>{const sa=[...x.querySelectorAll('.box.sa')];if(!sa.length)return;
 const kids=[...x.children];const last=kids[kids.length-1];const free=x.getBoundingClientRect().bottom-mm(12+6)-last.getBoundingClientRect().bottom;
 if(free<=0)return;const tm=sa.reduce((a,b)=>a+ +b.dataset.m,0);
 const hs=sa.map(b=>b.querySelector('.bd').getBoundingClientRect().height);sa.forEach((b,i)=>{b.querySelector('.bd').style.minHeight=(hs[i]+Math.min(free*(+b.dataset.m)/tm,mm(CAP*(+b.dataset.m))))+'px'})});
document.querySelectorAll('.sheet').forEach((x,k,a)=>{const p=document.createElement('div');p.className='pno';p.textContent='Page '+(k+1)+' of '+a.length;x.appendChild(p)});document.body.dataset.ready=1})</script></body></html>""")
        p=os.path.join(ROOT,'assessments',name+'.html');open(p,'w').write(html);print(p,f'{len(A)} MC + {len(B)} SA = {tot} marks')

if __name__=='__main__':
    build(sys.argv[1],int(sys.argv[2]),sys.argv[3] if len(sys.argv)>3 else 'Algebra and Linear Relations')
