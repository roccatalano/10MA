r"""Chapter 9 (C10) slide deck: the locked template + new 'New learning' slides (animated / interactive).
   python3 tools/slides/ch9.py 9A 9B        -> lessons/10MAG Univariate Statistics - Slides (9A-9B sample).html
New learning slides use only the book's Key ideas / Building understanding / Lesson starter content (cited)."""
import os,sys,json,html,re
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import build as B, ch9_data
B.DATA=ch9_data.S;B.UNIT='Univariate Statistics'
BOOK=B.BOOK
B.KI_END.update({'9A':767,'9B':773,'9C':782,'9D':790,'9E':796})
B.EX_START.update({'9A':769,'9B':777,'9C':785,'9D':793,'9E':799})
B.ANS.update({'9A':1070,'9B':1070,'9C':1070,'9D':1071,'9E':1071})
CK='Chapter 9 checklist'

def slide_li(sub,c,d):
    st=f'{sub} {c["title"]}'
    lis=''.join(f'<li>{html.escape(x)}</li>' for x in c['learning_intentions'])
    sc=''.join(f'<li>☐ {html.escape(x["text"])}</li>' for x in c['success_criteria'])
    seq=['Do Now','Activating prior knowledge','Key ideas','New learning']+[f'Example {e["n"]} · You try {e["n"]} — {B.card_ex_title(c,e["n"])}' for e in d['ex']]+['Exit tasks','Coursework']
    ns=[x['n'] for x in c['success_criteria']]
    return (f'<section class="slide li">{B.bar(sub,"Learning intentions",st)}<div class="cols" style="grid-template-columns:1.05fr 1fr .95fr">'
            f'<div class="col"><h2>Learning intentions</h2><ul>{lis}</ul></div><div class="col"><h2>Success criteria</h2><ul class="ck">{sc}</ul></div>'
            f'<div class="col"><h2>Lesson sequence</h2><ol class="seq">{"".join(f"<li>{x}</li>" for x in seq)}</ol></div></div>'
            +B.foot(f'{BOOK}, {sub} Learning intentions (p. {c["printed_page"]}); success criteria = {CK} items {ns[0]}–{ns[-1]} (p. 853)')+'</section>')

def slides_exit(sub,c,d):
    st=f'{sub} {c["title"]}';cells=[]
    for e,sc in zip(d['exit'],c['success_criteria']):
        cells.append(f'<div class="part"><div class="skill ck"><span class="box"></span><span>{html.escape(sc["text"])}</span></div><div class="qtxt"><b>{sc["n"]}.</b> {B.q_html("!"+e["q"].lstrip("!"))}</div><div class="work">{B.lines_html(e["w"])}</div></div>')
    ns=[x['n'] for x in c['success_criteria']]
    return [B.grid_slide('exit',sub,st,cells,f'{BOOK}, {CK} items {ns[0]}–{ns[-1]} (p. 853). Working by teacher.','Tick each skill in your checklist when you can do it.')]

# ---------------------------------------------------------------- New learning slides
def nl(sub,title,body,src,cls=''):
    st=f'{sub} {B.card("C10-"+sub)["title"]}'
    return f'<section class="slide nl {cls}">{B.bar("New learning",title,st)}{body}{B.foot(src)}</section>'

def L_types(sub):
    leaf=lambda t,d,k:f'<div class="tn leaf st" style="--d:{k}"><b>{t}</b><span>{d}</span></div>'
    tree=('<div class="tree">'
          '<div class="tn root">Data</div>'
          '<div class="tl2"><div class="tn st cat">Categorical<span>words / categories</span></div><div class="tn st num">Numerical<span>numbers</span></div></div>'
          '<div class="tl3">'+leaf('Nominal','Categories have no order; e.g. colours: red, blue, yellow',0)+leaf('Ordinal','Categories can be ordered; e.g. low, medium, high',1)
          +leaf('Discrete','Data can take on only a limited number of values; e.g. number of children in a family',2)+leaf('Continuous','Data can take on any value in a given range; e.g. time taken to complete a race',3)+'</div></div>')
    a=nl(sub,'Types of data',f'<p class="lead">Statistical data can be divided into subgroups. <span class="hint">Click to build the diagram.</span></p>{tree}',f'{BOOK}, 9A Key ideas (p. 767)')
    items=[('4.7, 3.8, 1.6, 9.2, 4.8','N'),('red, blue, yellow, green, blue, red','C'),('low, medium, high, low, low, medium','C'),
           ('How many times do you eat at your favourite fast-food place in a typical week?','N'),('How much do you usually spend buying your favourite fast food?','N'),
           ('How many items did you buy last time you went to your favourite fast-food place?','N'),('Which is your favourite fast-food?','C')]
    cards=''.join(f'<div class="card ix" data-a="{k}"><div class="ct">{t}</div><div class="cb"><button data-v="C">Categorical</button><button data-v="N">Numerical</button></div></div>' for t,k in items)
    b=nl(sub,'Sort it: categorical or numerical?',f'<p class="lead">Classify each set of data, or the data each survey question would generate. <span class="hint">Click a button on each card.</span></p><div class="cards">{cards}</div><div class="score ix">Score: <b>0</b> / {len(items)} <button class="reset">Reset</button></div>',
           f'{BOOK}, 9A Building understanding Q3 and Q4 (p. 768); answers p. 1070','sort')
    return [a,b]

def L_sample(sub):
    body=('<div class="cols" style="grid-template-columns:1fr 1.25fr"><div class="col"><h2>Key ideas</h2>'
          '<p>A <b>population</b> is a group of people, animals or objects with something in common, e.g. <i>all the students in your school</i>.</p>'
          '<p>A <b>sample</b> is a group that has been chosen from a population. Sometimes information from a sample is used to describe the whole population, so it is important to choose the sample carefully.</p>'
          '<div class="out ix" id="sout">Choose a sample →</div></div>'
          '<div class="col pop"><h2>All the students in your school (240)</h2><div class="dots ix"></div><div class="btns ix"><button data-s="rand">Random sample of 24</button><button data-s="lib">24 students in the library</button><button data-s="y12">24 students from one Year 12 class</button><button data-s="clr">Clear</button></div></div></div>')
    return [nl(sub,'Population and sample',body,f'{BOOK}, 9A Key ideas (p. 767); library sample from Example 2 · Now you try (p. 769)','popn')]

def L_hist(sub):
    data=[('0–',3,15),('10–',5,25),('20–',8,40),('30–40',4,20)]
    W,H,L,R,T,Bm=520,340,60,60,20,50;n=4;w=(W-L-R)/n;h=H-T-Bm;ym=10;y=lambda f:T+h-f/ym*h
    o=[f'<line x1="{L}" y1="{T+h}" x2="{W-R}" y2="{T+h}" stroke="#000" stroke-width="2"/><line x1="{L}" y1="{T-6}" x2="{L}" y2="{T+h}" stroke="#000" stroke-width="2"/>']
    for k in range(0,ym+1,2):o.append(f'<line x1="{L-6}" y1="{y(k)}" x2="{L}" y2="{y(k)}" stroke="#000"/><text x="{L-10}" y="{y(k)+5}" font-size="15" text-anchor="end">{k}</text>')
    for i,(g,f,p) in enumerate(data):
        o.append(f'<g class="st grow" data-row="{i}"><rect x="{L+i*w}" y="{y(f)}" width="{w}" height="{T+h-y(f)}" fill="#d00000" fill-opacity=".25" stroke="#d00000" stroke-width="2"/><text x="{L+i*w+w/2}" y="{y(f)-8}" font-size="16" text-anchor="middle" fill="#d00000" font-weight="bold">{f}</text></g>')
    for i,lab in enumerate(['0','10','20','30','40']):o.append(f'<text x="{L+i*w}" y="{T+h+20}" font-size="15" text-anchor="middle">{lab}</text>')
    o.append(f'<text x="{(L+W-R)/2}" y="{H-6}" font-size="16" text-anchor="middle">Score</text><text x="18" y="{T+h/2}" font-size="16" text-anchor="middle" transform="rotate(-90 18 {T+h/2})">Frequency</text>')
    pa=[f'<line x1="{W-R}" y1="{T-6}" x2="{W-R}" y2="{T+h}" stroke="#000" stroke-width="2"/>']+[f'<line x1="{W-R}" y1="{y(k)}" x2="{W-R+6}" y2="{y(k)}" stroke="#000"/><text x="{W-R+10}" y="{y(k)+5}" font-size="15">{k*5}</text>' for k in range(0,ym+1,2)]+[f'<text x="{W-14}" y="{T+h/2}" font-size="16" text-anchor="middle" transform="rotate(90 {W-14} {T+h/2})">% Frequency</text>']
    o.append(f'<g class="st">{"".join(pa)}</g>')
    svg=f'<svg viewBox="0 0 {W} {H}" style="width:100%;height:100%">{"".join(o)}</svg>'
    rows=''.join(f'<tr class="row" data-row="{i}"><td>{g}</td><td>{f}</td><td>{p}</td></tr>' for i,(g,f,p) in enumerate(data))
    tbl=f'<table class="ft"><tr><th>Class interval</th><th>Frequency</th><th>Percentage frequency</th></tr>{rows}<tr class="row tot" data-row="9"><td>Total</td><td>20</td><td>100</td></tr></table>'
    body=(f'<div class="cols" style="grid-template-columns:.9fr 1.1fr"><div class="col"><h2>Frequency table</h2>{tbl}'
          '<p class="sm2">The interval $10–$ includes all numbers from $10$ (including $10$) to fewer than $20$.</p>'
          '<p class="sm2 after">Percentage frequency $= \\dfrac{\\text{frequency}}{\\text{total}} \\times 100$, e.g. $\\dfrac{8}{20} \\times 100 = 40$</p>'
          '<p class="sm2 after">The bars sit across the class boundaries and there are <b>no gaps</b> between bars.</p></div>'
          f'<div class="col"><h2>Histogram <span class="hint" style="text-transform:none">click to build</span></h2><div style="flex:1;min-height:0">{svg}</div></div></div>')
    return [nl(sub,'From frequency table to histogram',body,f'{BOOK}, 9B Key ideas (p. 773); notes on bars from Example 3 (p. 775)','hist')]

def L_shape(sub):
    body=('<div class="cols" style="grid-template-columns:1.35fr .65fr"><div class="col"><h2>Shape of the data <span class="hint" style="text-transform:none">drag the slider</span></h2>'
          '<svg class="shp ix" viewBox="0 0 640 300" style="width:100%;flex:1;min-height:0"></svg>'
          '<div class="ix sl"><span>Tail to the left</span><input type="range" min="-100" max="100" value="0" class="skew"><span>Tail to the right</span></div></div>'
          '<div class="col"><h2>What changes?</h2><div class="shape-name">Symmetrical</div>'
          '<div class="mm"><div><i class="ln med"></i>Median <b class="vmed"></b></div><div><i class="ln mean"></i>Mean <b class="vmean"></b></div></div>'
          '<ul class="rules"><li data-k="sym"><b>Symmetrical</b>: the mean and median will be equal.</li><li data-k="pos"><b>Positively skewed</b>: the median will be less than the mean.</li><li data-k="neg"><b>Negatively skewed</b>: the median will be greater than the mean.</li></ul></div></div>')
    return [nl(sub,'Symmetrical or skewed?',body,f'{BOOK}, 9B Key ideas (p. 773). Data in the demonstration made up by the teacher.','shape')]

def L_stem(sub):
    vals=[1,3,12,15,19,21,24,26,27,30,34]
    chips=''.join(f'<span class="chip" data-i="{k}">{v}</span>' for k,v in enumerate(vals))
    rows='';k=0
    for s in range(4):
        lv=[v for v in vals if v//10==s]
        leaves=''.join(f'<span class="lf st" data-i="{vals.index(v)}">{v%10}</span>' for v in lv)
        rows+=f'<tr><td class="stm">{s}</td><td class="lvs">{leaves}</td></tr>'
    body=(f'<div class="cols" style="grid-template-columns:.8fr 1.2fr"><div class="col"><h2>Data (in order)</h2><div class="chips">{chips}</div>'
          '<p class="sm2">The <b>stem</b> is the tens digit and the <b>leaf</b> is the units digit. Leaves are written in order.</p>'
          '<p class="sm2 after">Always include a key: $2\\,|\\,4$ means $24$.</p></div>'
          f'<div class="col"><h2>Stem-and-leaf plot <span class="hint" style="text-transform:none">click to place each value</span></h2><table class="sl"><tr><th>Stem</th><th>Leaf</th></tr>{rows}</table></div></div>')
    return [nl(sub,'Building a stem-and-leaf plot',body,f'{BOOK}, 9B Key ideas (p. 773)','stem')]

LEARN={'types':L_types,'sample':L_sample,'hist':L_hist,'shape':L_shape,'stem':L_stem}

def subchapter(sub):
    c=B.card('C10-'+sub);d=B.DATA[sub];o=[B.slide_donow(f'{sub}')]
    o+= [B.slide_title(sub,c,B.UNIT),slide_li(sub,c,d),B.slides_apk(sub,c,d),B.slide_ki(sub,c,d)]
    for k in d.get('learn',[]):o+=LEARN[k](sub)
    for e in d['ex']:o+=[B.slide_example(sub,c,e,False),B.slide_example(sub,c,e,True)]
    o+=slides_exit(sub,c,d);o.append(B.slide_cw(sub,c))
    return o

NL_CSS=r"""
.st:has(.tx){white-space:normal}.st .tx{display:block;line-height:1.3}
.kt table td{font-weight:normal!important;white-space:normal!important}.kt table td b{font-weight:bold}
.slide.ex .top .q{min-width:0}
[data-id="C10-9B-ex3"] .top,[data-id="C10-9B-yt3"] .top{margin:10px 0 8px}
[data-id="C10-9B-ex3"] .top .q,[data-id="C10-9B-yt3"] .top .q{font-size:22px}
[data-id="C10-9B-ex3"] .part .qq.qt,[data-id="C10-9B-yt3"] .part .qq.qt{font-size:17px!important;line-height:1.25}
[data-id="C10-9B-ex3"] .part,[data-id="C10-9B-yt3"] .part{padding:8px 12px}
[data-id="C10-9B-ex3"] .work,[data-id="C10-9B-yt3"] .work{padding-top:6px}

/* ---- New learning slides (ch9.py) ---- */
.slide.nl .bar .tag{font-size:22px}
.slide.nl .lead{font-size:24px;margin:16px 4px 10px}
.hint{font-size:15px;color:#777;font-weight:normal}
.tree{flex:1;display:flex;flex-direction:column;align-items:center;gap:26px;padding:8px 0;position:relative}
.tn{border:2.5px solid #000;padding:10px 22px;font-size:26px;font-weight:bold;text-align:center;background:#fff}
.tn span{display:block;font-size:15px;font-weight:normal;color:#444}
.tn.root{font-size:30px}
.tl2{display:grid;grid-template-columns:1fr 1fr;gap:300px}
.tl3{display:grid;grid-template-columns:repeat(4,250px);gap:14px}
.tn.leaf{font-size:20px;font-weight:normal;padding:10px 12px;white-space:normal}.tn.leaf b{display:block;font-size:24px;margin-bottom:4px}.tn.leaf span{font-size:16px;color:#000}
.tn.st{color:#000;white-space:normal}
.tl3 .leaf:nth-child(-n+2){border-color:#1f5fbf}.tl2 .cat{border-color:#1f5fbf}
.tl3 .leaf:nth-child(n+3){border-color:#d00000}.tl2 .num{border-color:#d00000}
.cards{flex:1;display:grid;grid-template-columns:repeat(4,1fr);gap:14px;align-content:start}
.card{border:2px solid #000;padding:12px;display:flex;flex-direction:column;gap:10px;font-size:19px;min-height:120px;transition:background .3s}
.card .ct{flex:1}.card .cb{display:flex;gap:8px}
.card button,.btns button,.score button{font:inherit;font-size:16px;padding:6px 10px;border:2px solid #000;background:#fff;cursor:pointer}
.card button:hover,.btns button:hover{background:#eee}
.card.ok{background:#e3f5e3;border-color:#1a7f1a}.card.no{background:#fde4e4;border-color:#d00000;animation:shake .35s}
@keyframes shake{25%{transform:translateX(-6px)}75%{transform:translateX(6px)}}
.score{font-size:20px;margin-top:10px;display:flex;gap:14px;align-items:center}
.pop .dots{flex:1;display:grid;grid-template-columns:repeat(24,1fr);gap:5px;align-content:center;padding:6px}
.pop .dots i{aspect-ratio:1;border-radius:50%;background:#ccc;transition:background .4s,transform .4s}
.pop .dots i.on{background:#d00000;transform:scale(1.25)}
.pop .dots i.lib{outline:1.5px dashed #888}
.btns{display:flex;gap:8px;flex-wrap:wrap;margin-top:6px}
.out{margin-top:auto;border:2px solid #000;padding:12px;font-size:20px;background:#fafafa;min-height:110px}
.ft{border-collapse:collapse;font-size:21px;margin:6px 0 12px}.ft td,.ft th{border:1.5px solid #000;padding:5px 14px;text-align:center}.ft th{background:#eee;font-size:15px}
.ft tr.row td{color:#fff;transition:color .4s}.ft tr.row.show td{color:#d00000}
.sm2{font-size:19px;margin:4px 0 8px}.after{opacity:0;transition:opacity .4s}.after.show{opacity:1}
g.st.grow{opacity:1;transform:scaleY(0);transform-box:fill-box;transform-origin:bottom;transition:transform .7s cubic-bezier(.3,1.4,.6,1)}
g.st.grow.show{transform:none}
svg g.st{white-space:normal}
.sl{display:flex;gap:14px;align-items:center;font-size:16px;color:#444;padding:4px 10px}.sl input{flex:1;accent-color:#d00000}
.shape-name{font-size:34px;font-weight:bold;margin:6px 0 14px;color:#d00000}
.mm div{display:flex;align-items:center;gap:10px;font-size:22px;margin:6px 0}.mm .ln{display:inline-block;width:34px;height:0;border-top:4px solid #000}.mm .ln.med{border-color:#1f5fbf}.mm .ln.mean{border-top:4px dashed #d00000}
.rules{list-style:none;padding:0;margin-top:16px}.rules li{font-size:18px;padding:8px;border:2px solid transparent;margin-bottom:6px;transition:border-color .3s,background .3s}.rules li.on{border-color:#000;background:#fff7d6}
.chips{display:flex;flex-wrap:wrap;gap:10px;margin:8px 0 16px}.chip{font-size:26px;border:2px solid #000;padding:4px 12px;transition:opacity .4s,transform .4s}.chip.used{opacity:.25;transform:scale(.85)}
table.sl{border-collapse:collapse;font-size:40px;margin:10px 0 0 30px}table.sl th{font-size:18px;padding:4px 16px;border-bottom:3px solid #000}table.sl th:first-child,table.sl td.stm{border-right:3px solid #000;text-align:right;padding:4px 20px}
table.sl td.lvs{padding:4px 18px;min-width:330px}.lf.st{display:inline-block;margin-right:22px;color:#d00000;font-weight:bold}
"""

NL_JS=r"""
<script>
// New learning interactives (ch9.py)
document.querySelectorAll('.slide.sort').forEach(sl=>{const sc=sl.querySelector('.score b');const upd=()=>sc.textContent=sl.querySelectorAll('.card.ok').length;
  sl.querySelectorAll('.card button').forEach(b=>b.onclick=e=>{const c=b.closest('.card');c.classList.remove('ok','no');void c.offsetWidth;c.classList.add(b.dataset.v===c.dataset.a?'ok':'no');upd()});
  sl.querySelector('.reset').onclick=()=>{sl.querySelectorAll('.card').forEach(c=>c.classList.remove('ok','no'));upd()}});
document.querySelectorAll('.slide.popn').forEach(sl=>{const D=sl.querySelector('.dots');for(let k=0;k<240;k++){const i=document.createElement('i');if(k%24>=18&&k<96)i.classList.add('lib');D.appendChild(i)}
  const dots=[...D.children],out=sl.querySelector('#sout');
  const T={rand:'<b>Random sample:</b> every student has the same chance of being chosen, so the sample is spread across the whole school. It is more likely to be <b>representative</b>.',
   lib:'<b>Students in the library:</b> students who study in the library may not reflect a typical group of students. This sample is <b>not representative</b>.',
   y12:'<b>One Year 12 class:</b> only one year level is included, so the views of younger students are missed. This sample is <b>not representative</b>.',clr:'Choose a sample →'};
  sl.querySelectorAll('.btns button').forEach(b=>b.onclick=()=>{dots.forEach(d=>d.classList.remove('on'));const s=b.dataset.s;let pick=[];
   if(s==='rand'){const ix=[...dots.keys()].sort(()=>Math.random()-.5).slice(0,24);pick=ix}
   if(s==='lib')pick=dots.map((d,k)=>d.classList.contains('lib')?k:-1).filter(k=>k>=0).slice(0,24);
   if(s==='y12')pick=[...Array(24).keys()].map(k=>216+k);
   pick.forEach((k,n)=>setTimeout(()=>dots[k].classList.add('on'),n*35));out.innerHTML=T[s]})});
// histogram: table row appears with its bar
new MutationObserver(ms=>ms.forEach(m=>{const g=m.target;if(!g.dataset||g.dataset.row===undefined)return;const sl=g.closest('.slide');const on=g.classList.contains('show');
  sl.querySelectorAll('.ft tr.row[data-row="'+g.dataset.row+'"]').forEach(r=>r.classList.toggle('show',on));
  if(g.dataset.row==='3')sl.querySelector('.ft tr.tot').classList.toggle('show',on)})).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class']});
// '.after' notes appear once the slide's last step is shown
new MutationObserver(ms=>ms.forEach(m=>{const t=m.target;if(!t.classList||!t.classList.contains('st'))return;const sl=t.closest('.slide');const st=[...sl.querySelectorAll('.st')];
  const done=st.length&&st[st.length-1].classList.contains('show');sl.querySelectorAll('.after').forEach(a=>a.classList.toggle('show',done))})).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class']});
// stem-and-leaf: grey out each data chip as its leaf is placed
new MutationObserver(ms=>ms.forEach(m=>{const l=m.target;if(!l.classList||!l.classList.contains('lf'))return;const sl=l.closest('.slide');
  const c=sl.querySelector('.chip[data-i="'+l.dataset.i+'"]');if(c)c.classList.toggle('used',l.classList.contains('show'))})).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class']});
// shape slider: histogram with mean and median
document.querySelectorAll('.slide.shape').forEach(sl=>{const sv=sl.querySelector('svg.shp'),r=sl.querySelector('.skew');
  const draw=()=>{const a=+r.value/100,N=11,W=640,H=300,L=30,B=36,w=(W-2*L)/N;
    let f=[...Array(N).keys()].map(k=>{const x=(k+.5)/N;const p=1+3*Math.max(0,-a)*1.6+2,q=1+3*Math.max(0,a)*1.6+2;return Math.pow(x,p-1)*Math.pow(1-x,q-1)});
    const mx=Math.max(...f);f=f.map(v=>Math.round(v/mx*12));const n=f.reduce((s,v)=>s+v,0);
    let mean=f.reduce((s,v,k)=>s+v*k,0)/n;let c=0,med=0;for(let k=0;k<N;k++){if(c+f[k]>=n/2){med=k-.5+(n/2-c)/f[k];break}c+=f[k]}
    const X=v=>L+(v+.5)*w,Y=v=>H-B-v/12*(H-B-20);
    let s=`<line x1="${L}" y1="${H-B}" x2="${W-L}" y2="${H-B}" stroke="#000" stroke-width="2"/>`;
    f.forEach((v,k)=>{s+=`<rect x="${L+k*w}" y="${Y(v)}" width="${w}" height="${H-B-Y(v)}" fill="#d00000" fill-opacity=".2" stroke="#d00000" stroke-width="1.5"/>`;s+=`<text x="${L+k*w+w/2}" y="${H-B+18}" font-size="14" text-anchor="middle">${k}</text>`});
    s+=`<line x1="${X(med)}" y1="10" x2="${X(med)}" y2="${H-B}" stroke="#1f5fbf" stroke-width="4"/><line x1="${X(mean)}" y1="10" x2="${X(mean)}" y2="${H-B}" stroke="#d00000" stroke-width="4" stroke-dasharray="9 6"/>`;
    sv.innerHTML=s;sl.querySelector('.vmed').textContent=med.toFixed(1);sl.querySelector('.vmean').textContent=mean.toFixed(1);
    const k=Math.abs(a)<.12?'sym':(a>0?'pos':'neg');sl.querySelector('.shape-name').textContent={sym:'Symmetrical',pos:'Positively skewed',neg:'Negatively skewed'}[k];
    sl.querySelectorAll('.rules li').forEach(li=>li.classList.toggle('on',li.dataset.k===k))};
  r.oninput=draw;draw()});
</script>"""

def main(subs):
    S=[f'<section class="slide title cover"><div class="code">10MAG</div><h1>Univariate Statistics</h1><div class="unit">Year 10 General Mathematics · Unit 1 slides ({", ".join(subs)} sample with New learning slides)</div><div class="pp">{BOOK}</div><span class="pg" style="display:none"></span></section>']
    for s in subs:S+=subchapter(s)
    t=open(os.path.join(B.ROOT,'lessons/slides-template.html')).read()
    head=t[:t.index('<div class="stage" id="stage">')].replace('<title>Slide templates · Worked example / You try</title>','<title>10MAG Univariate Statistics · Slides</title>')
    head=head.replace('</style>',B.EXTRA_CSS+NL_CSS+'</style>')
    nav=B.NAV_JS.replace("addEventListener('click',e=>e.clientX>innerWidth/2?fwd():back());","addEventListener('click',e=>{if(e.target.closest('.ix,button,input'))return;e.clientX>innerWidth/2?fwd():back()});")
    nav=nav.replace("addEventListener('keydown',e=>{","addEventListener('keydown',e=>{if(e.target.tagName==='INPUT')return;")
    assert nav!=B.NAV_JS
    nav=nav.replace('</script></body></html>','</script>'+NL_JS+'</body></html>')
    html_=('\n'.join(S))
    for k in ('ex3','yt3'):   # Example 3: wider histogram column
        html_=re.sub(r'(data-id="C10-9B-%s".*?grid-template-columns:)repeat\(3,minmax\(0,1fr\)\)'%k,r'\1minmax(0,.95fr) minmax(0,1.45fr) minmax(0,.7fr)',html_,count=1,flags=re.S)
    S=[html_]
    out=os.path.join(B.ROOT,f'lessons/10MAG Univariate Statistics - Slides ({subs[0]}-{subs[-1]} sample).html')
    open(out,'w').write(head+'<div class="stage" id="stage">\n'+'\n'.join(S)+'\n</div>'+nav);print(out,len(S),'slides')
if __name__=='__main__':main(sys.argv[1:] or ['9A','9B'])
