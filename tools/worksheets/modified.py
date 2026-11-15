"""10MAG Modified worksheets: shared page layout + render. One content file per unit (mod_<unit>.py) holds W = {lesson: dict(...)}.
Each lesson dict: sub, part (opt), title, src [(year, subchapter, pages)], li, ki, ex [Example/You try pairs], sc (I-can list).
Run a unit:  python3 tools/worksheets/mod_<unit>.py [L1 L2 ...]   (needs KaTeX at /home/claude/kx: npm i katex@0.16.11)"""
import json,os,sys
HERE=os.path.dirname(os.path.abspath(__file__));ROOT=os.path.join(HERE,'..','..')
sys.path.insert(0,HERE)
from ch9 import tbl,stemleaf,numline,grid,tw_blank,SHEETS,PAGINATE,katex
BK={7:'Cambridge Essential Mathematics for the Victorian Curriculum 7 3rd Ed',8:'Cambridge Essential Mathematics for the Victorian Curriculum 8 3rd Ed',9:'Cambridge Essential Mathematics for the Victorian Curriculum 9 3rd Ed'}
def CL(y,ns,chapter):
    """'I can' items n in ns from the Year y chapter checklist"""
    return [x['text'] for x in json.load(open(os.path.join(ROOT,f'tools/data/checklist{y}.json'))) if x['n'] in ns and x['chapter']==chapter]
ft=lambda head,rows:tbl(head,rows,first_bold=False)
def fname(W,k):
    d=W[k];return f'C10-{d["sub"]} modified worksheet'+(f' (part {d["part"]})' if d.get('part') else '')
def page(k,d,R):
    srcs='; '.join(f'{BK[y]}, {s} {t}' for y,s,t in d['src'])
    o=[f'<div class="title"><div class="code">{d["sub"]}M</div><h1>{d["title"]}</h1><div class="pg">10MAG Modified · Lesson {k[1:]}</div></div>']
    o.append('<div class="box "><div class="hd">Learning intentions<span></span></div><div class="bd"><ul>'+''.join(f'<li>{x}</li>' for x in d['li'])+'</ul></div></div>')
    o.append('<div class="box "><div class="hd">Key ideas<span></span></div><div class="bd"><ul class="ki">'+''.join(f'<li>{R(x)}</li>' for x in d['ki'])+'</ul></div></div>')
    for e in d['ex']:
        if e.get('src_note'):e=dict(e,n=e['n']+f' <small>(adapted: {e["src_note"]})</small>')
        hs=e['h'] if isinstance(e['h'],list) else [e['h']]*max(1,len(e['parts']))
        def col(q,parts):
            s=f'<p class="q">{R(q)}</p>'
            if not parts:return s+f'<div style="height:{hs[0]}mm"></div>'
            return s+''.join(f'<div class="ytp"><b>{"abcdefg"[i]}</b><div><div>{R(p)}</div><div style="height:{hs[i]}mm"></div></div></div>' for i,p in enumerate(parts))
        if e.get('split'):
            o.append(f'<div class="box"><div class="hd">{e["n"]} · {e["t"]}<span></span></div><div class="bd">{col(e["q"],e["parts"])}</div></div>')
            o.append(f'<div class="box"><div class="hd">You try<span></span></div><div class="bd">{col(e["yq"],e["yparts"])}</div></div>')
        else:
            fs='11.0pt' if len(e['t'])<30 else '9.5pt'
            o.append(f'<div class="pair"><div class="hd" style="font-size:{fs}">{e["n"]} · {e["t"]}</div><div class="hd" style="font-size:{fs}">You try</div>'
                     f'<div class="bd">{col(e["q"],e["parts"])}</div><div class="bd">{col(e["yq"],e["yparts"])}</div></div>')
    if d.get('practice'):   # lessons with no Freefall sheet: Cambridge exercise questions, verbatim + cited (Rocco, 16 Nov)
        pq=''.join(f'<div class="ytp" style="break-inside:avoid"><b>{i+1}</b><div><div>{R(q)}</div><div style="height:{h}mm"></div><p class="src" style="margin:0">{src}</p></div></div>' for i,(q,h,src) in enumerate(d['practice']))
        o.append(f'<div class="box"><div class="hd">Practice<span>No Freefall sheet for this lesson</span></div><div class="bd">{pq}</div></div>')
    sc=''.join(f'<div class="sc"><div class="tick"></div><div><b>{t}</b></div></div>' for t in d['sc'])
    o.append(f'<div class="box split"><div class="hd">Skills checklist<span>Tick when you can do it</span></div><div class="bd">{sc}'+
             (f'<p class="src">Practice: the Practice questions above.</p>' if d.get('practice') and d.get('practice_only') else f'<p class="src">Practice: your Freefall sheets for this lesson (in your modified unit workbook).</p>')+f'<p class="src">{srcs}</p></div></div>')
    return ''.join(o)
def main(W,keys=None):
    keys=keys or list(W)
    css=open(os.path.join(HERE,'ws.css')).read()
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b=p.chromium.launch();pg=b.new_page()
        for k in keys:
            d=W[k];texts=[];page(k,d,lambda s:texts.append(s) or s);out=dict(zip(texts,katex(texts)));body=page(k,d,lambda s:out[s])
            html=f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>{fname(W,k)}</title><style>{css}{SHEETS}.box>.hd{{white-space:normal}}.sc{{break-inside:avoid}}.box>.hd span{{white-space:nowrap;margin-left:3mm}}</style></head><body><div id="flow">{body}</div>{PAGINATE}</body></html>'
            f=os.path.join(ROOT,'lessons',fname(W,k)+'.html');open(f,'w').write(html)
            pg.goto('file://'+os.path.abspath(f));pg.wait_for_selector('body[data-ready]');pg.wait_for_timeout(300)
            pg.pdf(path=f[:-5]+'.pdf',format='A4',print_background=True,prefer_css_page_size=True,margin={'top':'0','bottom':'0','left':'0','right':'0'});print(f)
        b.close()
