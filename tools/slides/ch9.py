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
B.ANS.update({'9A':1070,'9B':1070,'9C':1072,'9D':1073,'9E':1074})
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

def L_tw_read(sub):
    cols=['Strongly agree','Agree','Neutral','Disagree','Strongly disagree','Total']
    rows=[('Junior',[2,10,15,12,7,46]),('Senior',[20,28,16,4,1,69]),('Total',[22,38,31,16,8,115])]
    th=''.join(f'<th>{c}</th>' for c in ['']+cols)
    tb=''.join(f'<tr><th>{r}</th>'+''.join(f'<td class="c{" tot" if (j==5 or i==2) else ""}" data-r="{i}" data-c="{j}">{v}</td>' for j,v in enumerate(vs))+'</tr>' for i,(r,vs) in enumerate(rows))
    body=(f'<p class="lead">Do you think the competition was worthwhile? <span class="hint">Click any number in the table.</span></p>'
          f'<table class="twi ix">{"<tr>"+th+"</tr>"}{tb}</table><div class="twout ix">Click a cell to see what it means.</div>')
    return [nl(sub,'Reading a two-way table',body,f'{BOOK}, 9C Lesson starter (p. 781). Percentages by teacher.','twr')]

def L_tw_build(sub):
    st=lambda v:f'<span class="st big">{v}</span>'
    tbl=('<table class="twi"><tr><th></th><th>Holiday</th><th>No holiday</th><th>Total</th></tr>'
         f'<tr><th>Working</th><td>10</td><td>8</td><td class="tot">{st("18")}<i>a</i></td></tr>'
         '<tr><th>Not working</th><td>6</td><td>12</td><td class="tot">18</td></tr>'
         f'<tr><th>Total</th><td class="tot">16</td><td class="tot">{st("20")}<i>b</i></td><td class="tot">{st("36")}<i>c</i></td></tr></table>')
    steps=('<div class="howto"><div class="st tx2">$a$: add across the row: $10 + 8 = 18$</div>'
           '<div class="st tx2">$b$: add down the column: $8 + 12 = 20$</div>'
           '<div class="st tx2">$c$: total surveyed: $18 + 18 = 36$, and check $16 + 20 = 36$ ✔</div></div>')
    body=(f'<p class="lead">The entries in a two-way table are totalled both vertically and horizontally. <span class="hint">Click to find $a$, $b$ and $c$.</span></p>'
          f'<div class="cols" style="grid-template-columns:1.1fr .9fr"><div class="col" style="justify-content:center">{tbl}</div><div class="col"><h2>Working</h2>{steps}</div></div>')
    return [nl(sub,'Completing a two-way table',body,f'{BOOK}, 9C Key ideas (p. 781) and Building understanding Q1 (p. 782). Working by teacher.','twb')]

def tiles(vals,labels):
    """vals in a grid row; labels = list of (col_start, span, text, row) revealed one by one"""
    n=len(vals);t=''.join(f'<div class="tile" style="grid-column:{k+1}">{v}</div>' for k,v in enumerate(vals))
    l=''.join(f'<div class="st lab r{r}" style="grid-column:{c} / span {sp};grid-row:{r+1}">{x}</div>' for c,sp,x,r in labels)
    return f'<div class="tiles" style="grid-template-columns:repeat({n},1fr)">{t}{l}</div>'
def L_five(sub):
    odd=tiles([1,2,2,3,5,6,6,7,9],[(5,1,'$Q_2 = 5$',1),(1,4,'lower half',2),(6,4,'upper half',2),(2,2,'$Q_1 = 2$',3),(7,2,'$Q_3 = 6.5$',3)])
    even=tiles([2,3,3,4,7,8,8,9,9,9],[(5,2,'$Q_2 = 7.5$',1),(1,5,'lower half',2),(6,5,'upper half',2),(3,1,'$Q_1 = 3$',3),(8,1,'$Q_3 = 9$',3)])
    body=('<div class="cols" style="grid-template-columns:1fr 1fr"><div class="col"><h2>Odd number of values</h2>'+odd+'<div class="st tx2" style="margin-top:auto">$\\text{IQR} = Q_3 - Q_1 = 6.5 - 2 = 4.5$</div></div>'
          '<div class="col"><h2>Even number of values</h2>'+even+'<div class="st tx2" style="margin-top:auto">$\\text{IQR} = Q_3 - Q_1 = 9 - 3 = 6$</div></div></div>'
          '<p class="sm2" style="margin-top:8px"><b>Five-figure summary:</b> min, $Q_1$, $Q_2$ (median), $Q_3$, max. With an odd number of values, leave the median out of the halves. <span class="hint">Click to find each quartile.</span></p>')
    return [nl(sub,'Finding quartiles and the IQR',body,f'{BOOK}, 9D Key ideas (p. 790)','five')]
def L_fence(sub):
    body=('<div class="cols" style="grid-template-columns:1.4fr .6fr"><div class="col"><h2>Number of ducks spotted in eight flocks <span class="hint" style="text-transform:none">drag the slider to change the largest flock</span></h2>'
          '<svg class="fz ix" viewBox="0 0 700 250" style="width:100%;flex:1;min-height:0"></svg>'
          '<div class="ix sl"><span>Largest flock</span><input type="range" min="13" max="40" value="15" class="big"><b class="bv">15</b></div></div>'
          '<div class="col"><h2>Live summary</h2><div class="fsum"></div><p class="sm2" style="margin-top:auto">An outlier does <b>not</b> significantly affect the median. An outlier <b>does</b> significantly affect the mean.</p></div></div>')
    return [nl(sub,'Outliers and fences',body,f'{BOOK}, 9D Key ideas (p. 790); data from Building understanding Q3 (p. 790), largest value changed by the teacher','fence')]
def L_box(sub):
    W,L=900,40;a,b=0,30;x=lambda v:L+(v-a)/(b-a)*(W-2*L);by=120
    o=[f'<line x1="{L-20}" y1="200" x2="{W-L+20}" y2="200" stroke="#000" stroke-width="2"/>']+[f'<line x1="{x(v)}" y1="194" x2="{x(v)}" y2="206" stroke="#000"/><text x="{x(v)}" y="228" font-size="20" text-anchor="middle">{v}</text>' for v in range(0,31,5)]
    marks=[(5,'Minimum value'),(10,'$Q_1$'),(15,'$Q_2$'),(20,'$Q_3$'),(25,'Maximum value')]
    for v,t in marks:o.append(f'<g class="st"><line x1="{x(v)}" y1="{by-40}" x2="{x(v)}" y2="{by+40}" stroke="#d00000" stroke-width="3" stroke-dasharray="6 5"/></g>')
    o.append(f'<g class="st"><rect x="{x(10)}" y="{by-34}" width="{x(20)-x(10)}" height="68" fill="#d00000" fill-opacity=".15" stroke="#000" stroke-width="3"/><line x1="{x(15)}" y1="{by-34}" x2="{x(15)}" y2="{by+34}" stroke="#000" stroke-width="3"/></g>')
    o.append(f'<g class="st"><line x1="{x(5)}" y1="{by}" x2="{x(10)}" y2="{by}" stroke="#000" stroke-width="3"/><line x1="{x(20)}" y1="{by}" x2="{x(25)}" y2="{by}" stroke="#000" stroke-width="3"/><line x1="{x(5)}" y1="{by-16}" x2="{x(5)}" y2="{by+16}" stroke="#000" stroke-width="3"/><line x1="{x(25)}" y1="{by-16}" x2="{x(25)}" y2="{by+16}" stroke="#000" stroke-width="3"/></g>')
    o.append('<g class="st">'+''.join(f'<text x="{(x(p)+x(q))/2}" y="{by-50}" font-size="19" text-anchor="middle" fill="#1f5fbf">approx. 25%</text>' for p,q in ((5,10),(10,15),(15,20),(20,25)))+'</g>')
    svg=f'<svg viewBox="0 0 {W} 240" style="width:100%">{"".join(o)}</svg>'
    lab=''.join(f'<div class="st bl" style="left:{x(v)/W*100:.2f}%">{t}</div>' for v,t in marks)
    body=(f'<p class="lead">A <b>box plot</b> divides the data set into four groups that are approximately equal in size (25%). <span class="hint">Click to build it.</span></p>'
          f'<div class="boxb"><div class="bls">{lab}</div>{svg}</div><p class="sm2 after">The <b>box</b> goes from $Q_1$ to $Q_3$ (its width is the IQR). The <b>whiskers</b> stretch to the lowest and highest data values that are not outliers.</p>')
    return [nl(sub,'Parts of a box plot',body,f'{BOOK}, 9E Key ideas (p. 796); values from Building understanding Q1 (p. 796)','boxs')]
def L_boxlive(sub):
    body=('<div class="cols" style="grid-template-columns:1.45fr .55fr"><div class="col"><h2>Number of cars in 13 families <span class="hint" style="text-transform:none">drag the slider to change the family with the most cars</span></h2>'
          '<svg class="bz ix" viewBox="0 0 760 330" style="width:100%;flex:1;min-height:0"></svg>'
          '<div class="ix sl"><span>Most cars</span><input type="range" min="4" max="15" value="8" class="big"><b class="bv">8</b></div></div>'
          '<div class="col"><h2>Five-figure summary</h2><div class="fsum"></div><p class="sm2" style="margin-top:auto">An outlier is marked with a dot (•). The whisker stops at the highest value that is <b>not</b> an outlier.</p></div></div>')
    return [nl(sub,'Box plots with outliers',body,f'{BOOK}, 9E Key ideas (p. 796); data from 9D Building understanding Q2 (p. 790), largest value changed by the teacher','boxl')]

LEARN={'types':L_types,'sample':L_sample,'hist':L_hist,'shape':L_shape,'stem':L_stem,'tw_read':L_tw_read,'tw_build':L_tw_build,'five':L_five,'fence':L_fence,'box':L_box,'boxlive':L_boxlive}

def subchapter(sub):
    c=B.card('C10-'+sub);d=B.DATA[sub];o=[B.slide_donow(f'{sub}')]
    o+= [B.slide_title(sub,c,B.UNIT),slide_li(sub,c,d),B.slides_apk(sub,c,d),B.slide_ki(sub,c,d)]
    for k in d.get('learn',[]):o+=LEARN[k](sub)
    for e in d['ex']:o+=[B.slide_example(sub,c,e,False),B.slide_example(sub,c,e,True)]
    o+=slides_exit(sub,c,d);o.append(B.slide_cw(sub,c))
    return o

NL_CSS=r"""
.twi{border-collapse:collapse;font-size:24px;margin:8px auto}.twi th,.twi td{border:2px solid #000;padding:8px 14px;text-align:center}.twi th{background:#eee;font-size:17px}
.twi td.c{cursor:pointer;transition:background .25s}.twi td.c:hover{background:#f3f3f3}.twi td.tot{font-weight:bold}
.twi td.hl{background:#ffd9d9!important}.twi td.hl2{background:#fff3c4}.twi td.pick{background:#d00000!important;color:#fff}
.twout{border:2px solid #000;padding:14px 18px;font-size:23px;margin-top:16px;min-height:110px;background:#fafafa}
.twb .twi td{position:relative;min-width:110px;height:56px}.twb .twi td i{position:absolute;left:8px;top:4px;font-size:16px;color:#777}.st.big{font-weight:bold;font-size:28px}
.tx2{font-size:24px;color:#d00000;white-space:normal;margin:10px 0 18px}
.tiles{display:grid;gap:6px 6px;margin:18px 4px 0}.tile{border:2px solid #000;font-size:28px;text-align:center;padding:8px 0;grid-row:1}
.tiles .lab{white-space:normal;text-align:center;font-size:20px;color:#d00000;margin:0}.tiles .lab.r2{border-top:3px solid #1f5fbf;color:#1f5fbf;font-size:17px;padding-top:2px}.tiles .lab.r1,.tiles .lab.r3{font-weight:bold;white-space:nowrap;overflow:visible}
.fsum{font-size:21px;line-height:1.6}.fsum b{color:#d00000}.fsum .ol{color:#d00000;font-weight:bold}
.boxb{position:relative;margin-top:44px}.bls{position:absolute;left:0;right:0;top:-36px;height:30px}.bl{position:absolute;transform:translateX(-50%);font-size:19px;color:#d00000;white-space:nowrap;font-weight:bold}

.st:has(.tx){white-space:normal}.st .tx{display:block;line-height:1.3}
.kt table td{font-weight:normal!important;white-space:normal!important}.kt table td b{font-weight:bold}
.slide.ex .top .q{min-width:0}.slide.ex .top .q table{margin-top:8px}
[data-id="C10-9B-ex3"] .top,[data-id="C10-9B-yt3"] .top,[data-id="C10-9C-ex5"] .top,[data-id="C10-9C-yt5"] .top{margin:10px 0 8px}
[data-id="C10-9B-ex3"] .top .q,[data-id="C10-9B-yt3"] .top .q,[data-id="C10-9C-ex5"] .top .q,[data-id="C10-9C-yt5"] .top .q{font-size:21px}
[data-id="C10-9B-ex3"] .part .qq.qt,[data-id="C10-9B-yt3"] .part .qq.qt,[data-id="C10-9C-ex5"] .part .qq.qt,[data-id="C10-9C-yt5"] .part .qq.qt{font-size:16px!important;line-height:1.25}
[data-id="C10-9B-ex3"] .part,[data-id="C10-9B-yt3"] .part,[data-id="C10-9C-ex5"] .part,[data-id="C10-9C-yt5"] .part{padding:8px 12px}
[data-id="C10-9B-ex3"] .work,[data-id="C10-9B-yt3"] .work,[data-id="C10-9C-ex5"] .work,[data-id="C10-9C-yt5"] .work{padding-top:6px}

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

// 9C reading a two-way table
document.querySelectorAll('.slide.twr').forEach(sl=>{const T=sl.querySelector('.twi'),O=sl.querySelector('.twout');const rn=['junior','senior','all'],cn=['Strongly agree','Agree','Neutral','Disagree','Strongly disagree','in total'];
  const cell=(r,c)=>T.querySelector(`td[data-r="${r}"][data-c="${c}"]`);const v=(r,c)=>+cell(r,c).textContent;
  T.querySelectorAll('td.c').forEach(td=>td.onclick=()=>{T.querySelectorAll('td').forEach(x=>x.classList.remove('hl','hl2','pick'));const r=+td.dataset.r,c=+td.dataset.c;
   td.classList.add('pick');cell(r,5).classList.add('hl');cell(2,c).classList.add('hl');cell(2,5).classList.add('hl2');
   const f=v(r,c),p=x=>(x*100).toFixed(1).replace('.0','')+'%';
   let t=`<b>${f}</b> ${r<2?rn[r]+' students':'students'} ${c<5?'responded <b>'+cn[c]+'</b>':'were surveyed'}.`;
   if(!(r==2&&c==5))t+=`<br>As a proportion of everyone surveyed: $\\frac{${f}}{115}$ ≈ <b>${p(f/115)}</b>`;
   if(r<2&&c<5)t+=`<br>As a proportion of the ${rn[r]} students: $\\frac{${f}}{${v(r,5)}}$ ≈ <b>${p(f/v(r,5))}</b>`;
   O.innerHTML=t;renderMathInElement(O,{delimiters:[{left:'$',right:'$',display:false}],throwOnError:false})})});
// quartiles helper (method in the book: leave the median out of the halves)
const med=a=>{const n=a.length,m=Math.floor(n/2);return n%2?a[m]:(a[m-1]+a[m])/2};
const fivefig=a=>{a=[...a].sort((x,y)=>x-y);const n=a.length,h=Math.floor(n/2);return{a,min:a[0],max:a[n-1],q2:med(a),q1:med(a.slice(0,h)),q3:med(a.slice(n%2?h+1:h))}};
// 9D fences
document.querySelectorAll('.slide.fence').forEach(sl=>{const sv=sl.querySelector('svg.fz'),r=sl.querySelector('input.big'),O=sl.querySelector('.fsum');
  const draw=()=>{const X=+r.value;sl.querySelector('.bv').textContent=X;const d=[2,7,8,10,11,11,13,X];const f=fivefig(d),iqr=f.q3-f.q1,lo=f.q1-1.5*iqr,hi=f.q3+1.5*iqr;
    const mean=d.reduce((s,v)=>s+v,0)/d.length;const A=-5,B=45,px=v=>40+(v-A)/(B-A)*620;let s=`<line x1="20" y1="190" x2="680" y2="190" stroke="#000" stroke-width="2"/>`;
    for(let v=-5;v<=45;v+=5)s+=`<line x1="${px(v)}" y1="184" x2="${px(v)}" y2="196" stroke="#000"/><text x="${px(v)}" y="216" font-size="16" text-anchor="middle">${v}</text>`;
    s+=`<rect x="${px(lo)}" y="40" width="${px(hi)-px(lo)}" height="140" fill="#1f5fbf" fill-opacity=".07"/><line x1="${px(lo)}" y1="30" x2="${px(lo)}" y2="190" stroke="#1f5fbf" stroke-width="3" stroke-dasharray="8 6"/><line x1="${px(hi)}" y1="30" x2="${px(hi)}" y2="190" stroke="#1f5fbf" stroke-width="3" stroke-dasharray="8 6"/>`;
    s+=`<text x="${px(lo)}" y="22" font-size="15" text-anchor="middle" fill="#1f5fbf">lower fence ${lo}</text><text x="${px(hi)}" y="22" font-size="15" text-anchor="middle" fill="#1f5fbf">upper fence ${hi}</text>`;
    const seen={};d.forEach(v=>{seen[v]=(seen[v]||0)+1;const o=v<lo||v>hi;s+=`<circle cx="${px(v)}" cy="${178-seen[v]*20}" r="9" fill="${o?'#d00000':'#555'}"/>`});
    s+=`<line x1="${px(f.q2)}" y1="60" x2="${px(f.q2)}" y2="180" stroke="#000" stroke-width="3"/><line x1="${px(mean)}" y1="60" x2="${px(mean)}" y2="180" stroke="#d00000" stroke-width="3" stroke-dasharray="4 4"/>`;
    sv.innerHTML=s;const ol=d.filter(v=>v<lo||v>hi);
    O.innerHTML=`$Q_1$ = <b>${f.q1}</b> &nbsp; $Q_3$ = <b>${f.q3}</b><br>IQR = <b>${iqr}</b><br>Lower fence = <b>${lo}</b><br>Upper fence = <b>${hi}</b><br>Outlier: <span class="ol">${ol.length?ol.join(', '):'none'}</span><br><span style="border-top:3px solid #000;display:inline-block;width:26px"></span> Median = <b>${f.q2}</b><br><span style="border-top:3px dashed #d00000;display:inline-block;width:26px"></span> Mean = <b>${mean.toFixed(2)}</b>`;
    renderMathInElement(O,{delimiters:[{left:'$',right:'$',display:false}],throwOnError:false})};r.oninput=draw;draw()});
// 9E live box plot
document.querySelectorAll('.slide.boxl').forEach(sl=>{const sv=sl.querySelector('svg.bz'),r=sl.querySelector('input.big'),O=sl.querySelector('.fsum');
  const draw=()=>{const X=+r.value;sl.querySelector('.bv').textContent=X;const d=[0,1,1,1,2,2,2,2,2,3,3,4,X];const f=fivefig(d),iqr=f.q3-f.q1,lo=f.q1-1.5*iqr,hi=f.q3+1.5*iqr;
    const ok=d.filter(v=>v>=lo&&v<=hi),ol=d.filter(v=>v<lo||v>hi);const wl=Math.min(...ok),wh=Math.max(...ok);const px=v=>40+v/16*680;let s='';
    const seen={};d.forEach(v=>{seen[v]=(seen[v]||0)+1;s+=`<circle cx="${px(v)}" cy="${150-seen[v]*22}" r="9" fill="#888"/>`});
    s+=`<line x1="20" y1="300" x2="740" y2="300" stroke="#000" stroke-width="2"/>`;for(let v=0;v<=16;v++)s+=`<line x1="${px(v)}" y1="294" x2="${px(v)}" y2="306" stroke="#000"/><text x="${px(v)}" y="326" font-size="16" text-anchor="middle">${v}</text>`;
    const y=230;s+=`<line x1="${px(wl)}" y1="${y}" x2="${px(f.q1)}" y2="${y}" stroke="#d00000" stroke-width="3"/><rect x="${px(f.q1)}" y="${y-28}" width="${px(f.q3)-px(f.q1)}" height="56" fill="#d00000" fill-opacity=".12" stroke="#d00000" stroke-width="3"/>`;
    s+=`<line x1="${px(f.q2)}" y1="${y-28}" x2="${px(f.q2)}" y2="${y+28}" stroke="#d00000" stroke-width="3"/><line x1="${px(f.q3)}" y1="${y}" x2="${px(wh)}" y2="${y}" stroke="#d00000" stroke-width="3"/>`;
    s+=`<line x1="${px(wl)}" y1="${y-14}" x2="${px(wl)}" y2="${y+14}" stroke="#d00000" stroke-width="3"/><line x1="${px(wh)}" y1="${y-14}" x2="${px(wh)}" y2="${y+14}" stroke="#d00000" stroke-width="3"/>`;
    ol.forEach(v=>s+=`<circle cx="${px(v)}" cy="${y}" r="8" fill="#d00000"/>`);s+=`<line x1="${px(hi)}" y1="${y-45}" x2="${px(hi)}" y2="${y+45}" stroke="#1f5fbf" stroke-width="2" stroke-dasharray="7 5"/><text x="${px(hi)}" y="${y-50}" font-size="14" text-anchor="middle" fill="#1f5fbf">upper fence ${hi}</text>`;
    sv.innerHTML=s;O.innerHTML=`Min = <b>${f.min}</b><br>$Q_1$ = <b>${f.q1}</b><br>Median = <b>${f.q2}</b><br>$Q_3$ = <b>${f.q3}</b><br>Max = <b>${f.max}</b><br>IQR = <b>${iqr}</b>, upper fence = <b>${hi}</b><br>Outlier: <span class="ol">${ol.length?ol.join(', '):'none'}</span>`;
    renderMathInElement(O,{delimiters:[{left:'$',right:'$',display:false}],throwOnError:false})};r.oninput=draw;draw()});
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
    tag='' if len(subs)==5 else f" ({', '.join(subs)} sample)"
    S=[f'<section class="slide title cover"><div class="code">10MAG</div><h1>Univariate Statistics</h1><div class="unit">Year 10 General Mathematics · Unit 1 slides{tag}</div><div class="pp">{BOOK}</div><span class="pg" style="display:none"></span></section>']
    for s in subs:S+=subchapter(s)
    t=open(os.path.join(B.ROOT,'lessons/slides-template.html')).read()
    head=t[:t.index('<div class="stage" id="stage">')].replace('<title>Slide templates · Worked example / You try</title>','<title>10MAG Univariate Statistics · Slides</title>')
    head=head.replace('</style>',B.EXTRA_CSS+NL_CSS+'</style>')
    nav=B.NAV_JS.replace("addEventListener('click',e=>e.clientX>innerWidth/2?fwd():back());","addEventListener('click',e=>{if(e.target.closest('.ix,button,input'))return;e.clientX>innerWidth/2?fwd():back()});")
    nav=nav.replace("addEventListener('keydown',e=>{","addEventListener('keydown',e=>{if(e.target.tagName==='INPUT')return;")
    assert nav!=B.NAV_JS
    nav=nav.replace('</script></body></html>','</script>'+NL_JS+'</body></html>')
    html_=('\n'.join(S))
    for k in ('ex9','yt9'):   # Example 9: wider box-plot column
        html_=re.sub(r'(data-id="C10-9E-%s".*?grid-template-columns:)repeat\(2,minmax\(0,1fr\)\)'%k,r'\1minmax(0,.85fr) minmax(0,1.15fr)',html_,count=1,flags=re.S)
    for k in ('ex3','yt3'):   # Example 3: wider histogram column
        html_=re.sub(r'(data-id="C10-9B-%s".*?grid-template-columns:)repeat\(3,minmax\(0,1fr\)\)'%k,r'\1minmax(0,.95fr) minmax(0,1.45fr) minmax(0,.7fr)',html_,count=1,flags=re.S)
    html_=re.sub(r'<p class="q">(.*?)</p>(<div class="ki">)',r'<div class="q">\1</div>\2',html_,flags=re.S)
    S=[html_]
    out=os.path.join(B.ROOT,'lessons/10MAG Univariate Statistics - Slides.html' if len(subs)==5 else f'lessons/10MAG Univariate Statistics - Slides ({subs[0]}-{subs[-1]} sample).html')
    open(out,'w').write(head+'<div class="stage" id="stage">\n'+'\n'.join(S)+'\n</div>'+nav);print(out,len(S),'slides')
if __name__=='__main__':main(sys.argv[1:] or ['9A','9B','9C','9D','9E'])
