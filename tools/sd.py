import re,json
L=open('sd.txt').read().splitlines()
s=next(i for i,l in enumerate(L) if l.strip()=='Unit 1: General Mathematics')
e=next(i for i,l in enumerate(L) if l.strip()=='Unit 1: Mathematical Methods' and i>s)
B=L[s:e]
items={};unit=None;aos=None;topic=None;mode=None;cur=None;ckc={}
for l in B:
  t=l.strip()
  m=re.match(r'Unit (\d): General Mathematics',t)
  if m: unit=int(m.group(1)); mode=None; continue
  m=re.match(r'Area of Study (\d)$',t)
  if m: aos=int(m.group(1)); continue
  if t=='This topic includes:': mode='c'; continue
  if t=='Key knowledge': mode='kk'; continue
  if t in ('Key skills','Mathematical investigation') or t.startswith('Outcome 2'): mode=None; cur=None; continue
  if t.startswith('Outcome'): continue
  if mode and t.startswith('-'):
    k=(unit,aos,mode); ckc[k]=ckc.get(k,0)+1
    cur=f"GM-U{unit}-AoS{aos}-{mode}{ckc[k]}"
    items[cur]={'id':cur,'unit':unit,'aos':aos,'kind':'content' if mode=='c' else 'key knowledge','text':re.sub(r'\s+',' ',t[1:]).strip()}
  elif mode and cur and t and not t.startswith('Area of Study') and l.startswith('    '):
    items[cur]['text']+=' '+re.sub(r'\s+',' ',t)
  elif mode and not t.startswith('-') and t and cur is None: pass
  if mode and t and not t.startswith('-') and not l.startswith('    '): 
    if mode=='c' and cur and t!='This topic includes:': pass
# topic names
TOP={(1,1):'Investigating and comparing data distributions',(1,2):'Arithmetic and geometric sequences, first-order linear recurrence relations and financial mathematics',(1,3):'Linear functions, graphs, equations and models',(1,4):'Matrices',(2,1):'Investigating relationships between two numerical variables',(2,2):'Graphs and networks',(2,3):'Variation',(2,4):'Space, measurement and applications of trigonometry'}
AOS={1:'Data analysis, probability and statistics',2:'Algebra, number and structure'}
for v in items.values():
  v['topic']=TOP[(v['unit'],v['aos'])]
  v['text']=v['text'].replace('[]','[rule]')
json.dump(items,open('sd_gm.json','w'),indent=0,ensure_ascii=False)
for k,v in items.items(): print(k,v['text'][:110])
