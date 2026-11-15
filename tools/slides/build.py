r"""Build a unit slide deck from the shared subchapter data.
   python3 tools/slides/build.py "10MAA|Algebra and Linear Relations"
Order = Lesson planning (courses/lessons.json). Design = lessons/slides-template.html (CSS/JS copied here).
"""
import json,re,sys,os,html
from bs4 import BeautifulSoup
HERE=os.path.dirname(os.path.abspath(__file__));ROOT=os.path.join(HERE,'..','..')
sys.path.insert(0,HERE)
import ch1_data
DATA=ch1_data.S
BOOK='Cambridge Essential Mathematics 10 &amp; 10A 3rd Ed'
# first page of each Exercise (printed), read off the book
EX_START={'1A':8,'1B':15,'1C':21,'1D':27,'1E':36,'1F':42,'1G':49,'1H':54,'1I':62,'1J':68,'1K':72,'1L':79}
# page of the Now you try answers
ANS={'1A':956,'1B':957,'1C':958,'1D':959,'1E':960,'1F':965,'1G':966,'1H':967,'1I':968,'1J':968,'1K':968,'1L':969}
# last page of Key ideas (= Building understanding page)
KI_END={'1A':5,'1B':12,'1C':19,'1D':25,'1E':30,'1F':39,'1G':47,'1H':52,'1I':58,'1J':66,'1K':71,'1L':76}

def esc_money(h): return h.replace('\\$','<span class="nomath">$</span>')
def pp(a,b): return f'p. {a}' if a==b else f'pp. {a}–{b}'

def card(sub):
    lib=json.load(open(os.path.join(ROOT,'library/C10.json')))
    for ch in lib['chapters']:
        for s in ch.get('subchapters',[]):
            if s['id']==sub: return s

def worksheet(sub):
    return BeautifulSoup(open(os.path.join(ROOT,f'lessons/C10-{sub} worksheet.html')).read(),'html.parser')

def ws_box(ws,title):
    for b in ws.select('div.box'):
        hd=b.select_one('.hd')
        if hd and hd.get_text().strip().startswith(title): return b.select_one('.bd')

def tex_line(t,final):
    if t.startswith('<svg'): return f'<div class="st fig">{t}</div>'
    if t.startswith('!'): return f'<div class="st{" final" if final else ""}">{esc_money(t[1:])}</div>'
    if final: return f'<div class="st final">$\\boldsymbol{{{t}}}$</div>'
    return f'<div class="st">${t}$</div>'

def lines_html(lines):
    marked=any(isinstance(l,str) and l.startswith('*') for l in lines)
    texidx=[i for i,l in enumerate(lines) if not l.startswith('<svg') and not l.startswith('!')]
    last=texidx[-1] if texidx else -1
    o=[]
    for i,l in enumerate(lines):
        f=l.startswith('*') if marked else (i==last)
        o.append(tex_line(l[1:] if l.startswith('*') else l,f))
    return ''.join(o)

def q_html(q):
    if not q: return ''
    return esc_money(q[1:]) if q.startswith('!') else f'${q}$'

def bar(tag,h1,sub):
    return f'<div class="bar"><span class="tag">{tag}</span><h1>{h1}</h1><span class="sub">{sub}</span></div>'
def foot(src): return f'<div class="foot"><span>{src}</span><span class="pg"></span></div>'

def slide_title(sub,c,unit):
    return (f'<section class="slide title" data-sec="{sub}"><div class="code">{sub}</div><h1>{c["title"]}</h1><div class="unit">{unit}</div>'
            f'<div class="pp">{BOOK} · {pp(c["printed_page"],c["printed_end"])}</div><span class="pg" style="display:none"></span></section>')

def slide_donow(label):
    return (f'<section class="slide title dn" data-sec="donow"><div class="code">Do Now</div><h1>Complete the Do Now sheet in front of you.</h1>'
            f'<div class="unit">Work on your own and in silence. Show your working.</div><div class="pp">{label}</div><span class="pg" style="display:none"></span></section>')

def slide_li(sub,c,d,donow):
    st=f'{sub} {c["title"]}'
    lis=''.join(f'<li>{html.escape(x)}</li>' for x in c['learning_intentions'])
    sc=''.join(f'<li>☐ {html.escape(x["text"])}</li>' for x in c['success_criteria'])
    seq=(['Do Now'] if donow else [])+['Activating prior knowledge','Key ideas and formulas']
    seq+=[f'Example {e["n"]} · You try {e["n"]} — {card_ex_title(c,e["n"])}' for e in d['ex']]+['Exit tasks','Coursework']
    ns=[x['n'] for x in c['success_criteria']]
    items=f'{ns[0]}–{ns[-1]}' if len(ns)>1 else f'{ns[0]}'
    ck='p. 88' if ns[-1]<=17 else ('p. 89' if ns[0]>=18 else 'pp. 88–89')
    return (f'<section class="slide li">{bar(sub,"Learning intentions",st)}<div class="cols" style="grid-template-columns:1.05fr 1fr .95fr">'
            f'<div class="col"><h2>Learning intentions</h2><ul>{lis}</ul></div>'
            f'<div class="col"><h2>Success criteria</h2><ul class="ck">{sc}</ul></div>'
            f'<div class="col"><h2>Lesson sequence</h2><ol class="seq">{"".join(f"<li>{x}</li>" for x in seq)}</ol></div></div>'
            +foot(f'{BOOK}, {sub} Learning intentions (p. {c["printed_page"]}); success criteria = Chapter 1 checklist item{"s" if len(ns)>1 else ""} {items} ({ck})')+'</section>')

def card_ex_title(c,n):
    for e in c['examples']:
        if e['n']==n:
            t=e['title']
            if t.endswith('in the form'): t+=' y = mx + c'
            return t

def grid_slide(kind,sub,st,cells,src,note):
    tag,h1=('APK','Activating prior knowledge') if kind=='apk' else ('Exit','Exit tasks')
    n=len(cells);cls='g22' if n>=3 else ('g21' if n==2 else 'g11')
    return (f'<section class="slide ex4">{bar(tag,h1,st)}<p class="q" style="margin:16px 4px 10px">{note}</p>'
            f'<div class="parts {cls}">{"".join(cells)}</div>{foot(src)}</section>')

def slides_apk(sub,c,d):
    st=f'{sub} {c["title"]}'
    if 'apk_src' in d: src=d['apk_src']
    else:
        ws=worksheet(sub);b=ws_box(ws,'Activating prior knowledge')
        src=b.select_one('p.src').get_text().strip().replace('for the Victorian Curriculum ','')+'. Working by teacher.'
    cells=[]
    for i,(a,cd) in enumerate(zip(d['apk'],c['apk']),1):
        yr=cd['book'][1]
        cells.append(f'<div class="part"><div class="skill">Year {yr} · {html.escape(cd["skill"])}</div><div class="qtxt"><b>{i}.</b> {q_html("!"+a["q"].lstrip("!"))}</div><div class="work">{lines_html(a["w"])}</div></div>')
    if any('<svg' in x for x in cells) and len(cells)>2:
        return ''.join(grid_slide('apk',sub,st,cells[k:k+2],src,'Answer each question.') for k in range(0,len(cells),2))
    return grid_slide('apk',sub,st,cells,src,'Answer each question.')

def slides_exit(sub,c,d):
    st=f'{sub} {c["title"]}';out=[]
    items=list(zip(d['exit'],c['exit_tasks'],c['success_criteria']))
    svg=any('<svg' in str(e) for e,_,_ in items)
    k=2 if svg else 4
    groups=[items[i:i+k] for i in range(0,len(items),k)]
    for g in groups:
        cells=[]
        for e,et,sc in g:
            cells.append(f'<div class="part"><div class="skill ck"><span class="box"></span><span>{html.escape(sc["text"])}</span></div><div class="qtxt"><b>{sc["n"]}.</b> {q_html("!"+e["q"].lstrip("!"))}</div><div class="work">{lines_html(e["w"])}</div></div>')
        ns=[x[2]['n'] for x in g];pg='p. 88' if ns[-1]<=17 else 'p. 89'
        items_s=f'items {ns[0]}–{ns[-1]}' if len(ns)>1 else f'item {ns[0]}'
        out.append(grid_slide('exit',sub,st,cells,f'{BOOK}, Chapter 1 checklist {items_s} ({pg}). Working by teacher.','Tick each skill in your checklist when you can do it.'))
    return out

def slide_ki(sub,c,d):
    st=f'{sub} {c["title"]}';src=f'{BOOK}, {sub} Key ideas ({pp(c["printed_page"],KI_END[sub])})'
    if d.get('ki_html')=='TEMPLATE':
        t=open(os.path.join(ROOT,'lessons/slides-template.html')).read()
        i=t.index('<!-- KEY IDEAS | KEY FORMULAS -->');j=t.index('<!-- WORKED EXAMPLE -->')
        s=t[i:j]; s=re.sub(r'<div class="foot">.*?</div>',foot(src),s,flags=re.S); return s
    ws=worksheet(sub);kd=ws_box(ws,'Key definitions');kf=ws_box(ws,'Key formulas')
    ul=kd.find('ul');ul.attrs={}
    for t in kf.select('table'): t['class']='kt'
    for s in kf.select('svg.figc'): s['style']='display:block;max-height:120px;width:auto'
    return (f'<section class="slide">{bar(sub,"Key ideas",st)}<div class="cols" style="grid-template-columns:1fr 1fr">'
            f'<div class="col sm"><h2>Key ideas</h2>{ul}</div><div class="col sm"><h2>Key formulas</h2>{"".join(str(x) for x in kf.contents)}</div></div>{foot(src)}</section>')

def slide_example(sub,c,e,yt):
    st=f'{sub} {c["title"]}';n=e['n'];title=card_ex_title(c,n)
    parts=e['yt'] if yt else e['parts'];instr=(e.get('yinstr') or e['instr']) if yt else e['instr']
    cols=[]
    for p in parts:
        lab,q,ls=p[0],p[1],p[2];fig=p[3] if len(p)>3 else ''
        head=f'<div class="qq{" qt" if q.startswith("!") and "<svg" not in q else ""}"><span class="lab">{lab}</span>{q_html(q)}</div>' if (lab or q) else ''
        svgs=[l for l in ls if l.startswith('<svg')];txt=[l for l in ls if not l.startswith('<svg')]
        if not txt: txt,svgs=ls,[]
        side=fig+''.join(f'<div class="st fig">{v}</div>' for v in svgs)
        figh=f'<div class="qfig">{side}</div>' if side else ''
        cols.append(f'<div class="part{" wide" if len(parts)==1 else ""}">{head}<div class="pw"><div class="work">{lines_html(txt)}</div>{figh}</div></div>')
    tag=f'You try {n}' if yt else f'Example {n}'
    if yt: src=f'{BOOK}, {sub} Example {n} · Now you try (p. {e["page"]}); working follows Example {n}, answers checked against p. {ANS[sub]}; key idea {e["kp"]}'
    else: src=f'{BOOK}, {sub} Example {n} (p. {e["page"]}); key idea {e["kp"]}'
    return (f'<section class="slide ex{" yt" if yt else ""}" data-id="C10-{sub}-{"yt" if yt else "ex"}{n}">{bar(tag,title,st)}'
            f'<div class="top"><p class="q">{esc_money(instr)}</p><div class="ki"><div class="kh">Key idea</div><div class="kb">{e["ki"]}</div></div></div>'
            f'<div class="parts" style="grid-template-columns:repeat({len(parts)},minmax(0,1fr))">{"".join(cols)}</div>{foot(src)}</section>')

def slide_cw(sub,c):
    st=f'{sub} {c["title"]}';cw=c['coursework']
    rows=''
    for k,lab in (('good','Good<span>Minimum for your coursework tick</span>'),('better','Better'),('best','Best')):
        r=cw[k];rows+=f'<tr><th>{lab}</th>'+''.join(f'<td>{("Q"+r[x]) if r[x] not in ("–","") else "–"}</td>' for x in ('Fluency','Problem-solving','Reasoning','Enrichment'))+'</tr>'
    return (f'<section class="slide cwk">{bar(sub,f"Coursework · Exercise {sub} ({pp(EX_START[sub],c["printed_end"])})",st)}'
            f'<table class="cw"><thead><tr><th>Option</th><th>Fluency</th><th>Problem-solving</th><th>Reasoning</th><th>Enrichment</th></tr></thead><tbody>{rows}</tbody></table>'
            f'<p class="note"><b>(½)</b> = every second part (a, c, e, …) · <b>(⅓)</b> = every third part (a, d, g, …). Your teacher will tell you which row to do. Tick it off on your worksheet.</p>'
            +foot(f'{BOOK}, Exercise {sub} pathways (Foundation / Standard / Advanced)')+'</section>')

def simple(t,sub_t):
    return f'<section class="slide title" data-sec="x"><div class="code">{t}</div><h1>{sub_t}</h1><span class="pg" style="display:none"></span></section>'

def subchapter(sub,donow,split_at=None,split_label=None):
    c=card('C10-'+sub);d=DATA[sub];o=[]
    o.append(slide_title(sub,c,UNIT));o.append(slide_li(sub,c,d,donow));o.append(slides_apk(sub,c,d));o.append(slide_ki(sub,c,d))
    for k,e in enumerate(d['ex']):
        if split_at is not None and k==split_at: o.append(slide_donow(split_label))
        o.append(slide_example(sub,c,e,False));o.append(slide_example(sub,c,e,True))
    o+=slides_exit(sub,c,d);o.append(slide_cw(sub,c))
    return o

def build(key,out):
    global UNIT
    stream,UNIT=key.split('|')
    plan=json.load(open(os.path.join(ROOT,'courses/lessons.json')))['plans'][key]
    S=[f'<section class="slide title cover"><div class="code">{stream}</div><h1>{UNIT}</h1><div class="unit">Year 10 {"Advanced" if stream=="10MAA" else "General"} Mathematics · Chapter 1 slides</div><div class="pp">{BOOK}</div><span class="pg" style="display:none"></span></section>']
    done={}  # sub -> lessons seen
    seq=[]
    for L,les in enumerate(plan,1):
        if les['kind']=='review': seq.append(('review',L));continue
        if les['kind']=='assess': seq.append(('cat',L));continue
        for i,it in enumerate(les['items']):
            sub=it['id'].split('-')[1];seq.append(('teach',L,sub,i==0))
    i=0
    while i<len(seq):
        s=seq[i]
        if s[0]=='review': S.append(slide_donow(f'Lesson {s[1]}'));S.append(simple('Review','Chapter 1 review'));i+=1;continue
        if s[0]=='cat': S.append(simple('CAT','Algebra and Linear Relations'));i+=1;continue
        _,L,sub,first=s
        # count consecutive lessons that teach this same subchapter (split subchapter)
        j=i+1;Ls=[L]
        while j<len(seq) and seq[j][0]=='teach' and seq[j][2]==sub: Ls.append(seq[j][1]);j+=1
        if first: S.append(slide_donow(f'Lesson {L}'))
        nex=len(DATA[sub]['ex'])
        split=(nex+1)//2 if len(Ls)>1 else None
        S+=subchapter(sub,first,split,f'Lesson {Ls[1]} · {sub} continued' if len(Ls)>1 else None)
        i=j
    t=open(os.path.join(ROOT,'lessons/slides-template.html')).read()
    head=t[:t.index('<div class="stage" id="stage">')]
    head=head.replace('<title>Slide templates · Worked example / You try</title>',f'<title>{stream} {UNIT} · Slides</title>')
    head=head.replace('</style>',EXTRA_CSS+'</style>')
    open(out,'w').write(head+'<div class="stage" id="stage">\n'+'\n'.join(S)+'\n</div>'+NAV_JS)
    print(out,len(S),'slides')

EXTRA_CSS=r"""
/* ---- deck additions (build.py) ---- */
.foot{margin-top:auto;padding-top:10px}
.slide.cwk .cw{margin-top:22px}
.slide.li .col{font-size:21px;line-height:1.35}
.slide.li .col ul,.slide.li .col ol{flex:1;display:flex;flex-direction:column;justify-content:space-around;margin:4px 0}
.slide.li .col li{margin:0}
.slide.li ul.ck{list-style:none;padding-left:0}
.nomath{}
.col.sm table.kt{table-layout:fixed;width:100%}.col.sm table.kt td:first-child{width:30%;white-space:normal}.col.sm svg.figc,.col.sm td>svg{max-width:100%;height:auto}
.parts.g21 .qtxt svg.fig,.parts.g21 .qtxt svg.figc,.parts.g11 .qtxt svg.fig{max-height:200px}
.parts{grid-template-rows:minmax(0,1fr)}.part{min-height:0;overflow:hidden}
.part .pw{flex:1;display:flex;gap:14px;min-height:0}
.part .pw .work{flex:1;min-width:0;overflow:hidden}
.part .qfig{flex:0 1 auto;max-width:52%;padding-top:8px;display:flex;flex-direction:column;justify-content:flex-start}.part .qfig svg{max-height:100%}
.part .qq{flex:none}.part .qq.qt{white-space:normal;font-size:24px!important;line-height:1.35}
.st.fig{white-space:normal;overflow:visible}.st.fig svg,.qfig svg{max-width:100%;height:auto}
.st .katex{font-size:1em}
.part .work{font-size:28px}.parts.g22 .work,.parts.g21 .work,.parts.g11 .work{font-size:22px}
.parts.g21{grid-template-columns:repeat(2,minmax(0,1fr))}.parts.g11{grid-template-columns:1fr}
.parts.g21 .part{padding:12px 18px}.parts.g21 .st,.parts.g11 .st{margin:0 0 6px!important;font-size:24px}
.qtxt svg.fig,.qtxt svg.figc{display:block;margin:6px 0 0 10px;max-height:150px;width:auto}
.ki .kb .katex{font-size:1.05em}
table.tv{border-collapse:collapse;font-size:20px}table.tv td{border:1.5px solid #d00000;padding:2px 12px;text-align:center}
.slide.cover .code{font-size:90px}
.pg{min-width:30px;text-align:right}
"""

NAV_JS=r"""
<div class="nav">→ / click: next line of working, then next slide · ← back · F full screen · type a number + Enter to jump</div>
<script>
renderMathInElement(document.body,{delimiters:[{left:'$',right:'$',display:false}],ignoredClasses:['nomath'],throwOnError:false});
const S=[...document.querySelectorAll('.slide')];let i=0;
S.forEach((s,k)=>s.querySelector('.pg').textContent=(k+1));
const show=k=>{i=Math.max(0,Math.min(S.length-1,k));S.forEach((s,j)=>s.classList.toggle('on',j===i));try{history.replaceState(null,'','#'+(i+1))}catch(e){}};
const fit=()=>{const z=Math.min(innerWidth/1280,innerHeight/720);document.getElementById('stage').style.transform=`translate(-50%,-50%) scale(${z})`};
addEventListener('resize',fit);fit();show((parseInt(location.hash.slice(1))||1)-1);
// fit: maths never wraps (shrink to column width); working that is too tall goes to two columns, then shrinks
const over=e=>e.scrollHeight>e.clientHeight+2;
const wfit=(q,f0)=>{let f=f0;q.style.display='block';q.style.fontSize=f+'px';while(q.scrollWidth>q.clientWidth+1&&f>11){f-=0.5;q.style.fontSize=f+'px'}return f};
const fitWork=w=>{const L=[...w.querySelectorAll('.st:not(.fig)')];if(!L.length&&!over(w))return;
  const f0=parseFloat(getComputedStyle(w).fontSize);
  const run=floor=>{const fi=L.map(q=>wfit(q,f0));let u=Math.min(f0,Math.max(Math.min(...fi,f0),20));
    const ap=()=>L.forEach((q,k)=>q.style.fontSize=Math.min(u,fi[k])+'px');ap();
    while(over(w)&&u>floor){u-=0.5;ap()}};
  run(22);
  const V=[...w.querySelectorAll('.st.fig svg')];let sc=1;
  while(over(w)&&V.length&&sc>0.62){sc*=0.93;V.forEach(v=>{v.style.height=(parseFloat(v.getAttribute('height'))*sc)+'px';v.style.width='auto'})}
  if(over(w)&&w.clientWidth>520){w.style.columnCount=2;w.style.columnGap='30px';L.forEach(q=>q.style.breakInside='avoid');run(15)}
  let g=0;while(over(w)&&g<25){g++;sc*=0.93;V.forEach(v=>{v.style.height=(parseFloat(v.getAttribute('height'))*sc)+'px';v.style.width='auto'});if(g>8)L.forEach(q=>q.style.fontSize=parseFloat(q.style.fontSize)*0.95+'px')}};
const shrink=()=>{S.forEach(s=>{s.classList.add('on');
  s.querySelectorAll('.qq').forEach(q=>wfit(q,parseFloat(getComputedStyle(q).fontSize)));
  s.querySelectorAll('.work').forEach(fitWork);
  s.querySelectorAll('.col').forEach(c=>{let f=parseFloat(getComputedStyle(c).fontSize),g=0;while(over(c)&&f>11&&g<30){g++;f-=0.5;c.style.fontSize=f+'px'}});
  s.querySelectorAll('.parts.g22 .part,.parts.g21 .part').forEach(c=>{let g=0;while(over(c)&&g<20){g++;c.querySelectorAll('.qtxt,.st:not(.fig)').forEach(q=>{q.style.fontSize=(parseFloat(getComputedStyle(q).fontSize)*0.94)+'px'});c.querySelectorAll('svg.fig,svg.figc').forEach(v=>{v.style.height=(v.getBoundingClientRect().height*0.92)+'px';v.style.width='auto'})}});
  s.classList.remove('on')});show(i);document.body.dataset.ready=1};
const fl=['KaTeX_Main','KaTeX_Math','KaTeX_Size1','KaTeX_Size2','KaTeX_AMS'].flatMap(f=>['normal','bold','italic','italic bold'].map(w=>document.fonts.load(w+' 20px '+f).catch(()=>0)));
Promise.all(fl).then(()=>document.fonts.ready).then(()=>setTimeout(shrink,80));
const steps=()=>[...S[i].querySelectorAll('.st')];
const fwd=()=>{const n=steps().find(x=>!x.classList.contains('show'));n?n.classList.add('show'):show(i+1)};
const back=()=>{const sh=steps().filter(x=>x.classList.contains('show'));sh.length?sh.pop().classList.remove('show'):show(i-1)};
let num='';
addEventListener('keydown',e=>{if(/^[0-9]$/.test(e.key)){num+=e.key;return}
  if(e.key==='Enter'&&num){show(parseInt(num)-1);num='';return}num='';
  if(['ArrowRight','PageDown',' '].includes(e.key))fwd();if(['ArrowLeft','PageUp'].includes(e.key))back();
  if(e.key==='Home')show(0);if(e.key==='End')show(S.length-1);if(e.key==='f'||e.key==='F')document.documentElement.requestFullscreen?.()});
addEventListener('click',e=>e.clientX>innerWidth/2?fwd():back());
</script></body></html>"""

if __name__=='__main__':
    key=sys.argv[1] if len(sys.argv)>1 else '10MAA|Algebra and Linear Relations'
    stream,unit=key.split('|')
    build(key,os.path.join(ROOT,f'lessons/{stream} {unit} - Slides.html'))
