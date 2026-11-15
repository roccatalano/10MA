import re,json
P=open('c10.txt').read().split('\f')
cards=json.load(open('cards0.json'))
STOP=re.compile(r'^\s*(Progress quiz|Applications and problem-solving|Modelling|Technology and computational thinking|Investigation|Problems and challenges|Chapter summary|Semester review)\b',re.M)
SEC=re.compile(r'^\s*(BUILDING UNDERSTANDING|FLUENCY|PROBLEM.SOLVING|REASONING|ENRICHMENT:?)(.*)$')
# chapter VC2 codes
chcodes={}
for ch in range(1,11):
  for k,p in enumerate(P):
    pass
for i,c in enumerate(cards):
  s=c['pdf_page']-1; e=cards[i+1]['pdf_page']-1 if i+1<len(cards) else s+12
  text=[]
  for k in range(s,e):
    pg=P[k]
    if k>s:
      top='\n'.join(pg.splitlines()[:8]); m=STOP.search(top)
      if m: break
    text.append(pg)
  c['pdf_end']=s+len(text); c['printed_end']=c['printed_page']+len(text)-1
  T='\n'.join(text); L=T.splitlines()
  # LIs
  lis=[];on=False
  for l in L:
    if 'LEARNING INTENTIONS' in l: on=True; continue
    if on:
      st=l.strip()
      if st.startswith('•'): lis.append(st[1:].strip())
      elif st and lis and not re.match(r'^[A-Z]{4,}',st) and len(lis)<9 and not st.startswith('Example'): 
        if l.startswith(' '*14) and len(st)<130: lis[-1]+=' '+st
        else: break
      elif lis: break
  c['learning_intentions']=[re.sub(r'\s+',' ',x) for x in lis]
  # examples
  ex={}
  for j,l in enumerate(L):
    m=re.match(r'^\s{8,}Example (\d+)\s+([A-Z].*?)\s*$',l)
    if m and int(m.group(1)) not in ex:
      t=re.split(r'\s{3,}',m.group(2))[0]
      nx=next((x for x in L[j+1:j+3] if x.strip()),'')
      ind=len(l)-len(l.lstrip())
      mm=re.match(r'^\s{%d,}([a-z(].*?)\s*$'%(ind+5),nx)
      if mm and not re.search(r'[=+]',mm.group(1)[:3]): t+=' '+re.split(r'\s{3,}',mm.group(1))[0]
      ex[int(m.group(1))]=re.sub(r'\s+',' ',t).strip()
  c['examples']=[{'n':n,'title':t} for n,t in sorted(ex.items())]
  # sections
  secs=[];cur=None
  for l in L:
    m=SEC.match(l)
    if m:
      name=m.group(1).replace('–','-').replace('−','-').rstrip(':')
      name={'PROBLEM-SOLVING':'problem_solving'}.get(name,name.lower().replace(' ','_'))
      rest=m.group(2); title=None
      if name=='enrichment':
        mm=re.match(r'\s*(.*?)\s{3,}(.*)$',rest); title=mm.group(1) if mm else rest.strip(); rest=mm.group(2) if mm else ''
      paths=[x.strip() for x in re.split(r'\s{3,}',rest.strip()) if x.strip()]
      cur={'section':name,'questions':[],'pathways':paths}; 
      if title: cur['title']=title
      secs.append(cur); continue
    if cur:
      m=re.match(r'^\s{0,26}(?:Example \d+[a-z,\s]*\s+)?(\d{1,2})\s{1,4}(?=\S)',l)
      if m:
        n=int(m.group(1)); q=cur['questions']
        if (not q and n>=1) or (q and 0<n-q[-1]<=3): q.append(n)
  for x in secs:
    q=x.pop('questions'); x['q']=f"{q[0]}–{q[-1]}" if len(q)>1 else (str(q[0]) if q else '')
    if len(x['pathways'])!=3: x['pathways_raw']=x.pop('pathways')
  c['exercise']=secs
json.dump(cards,open('cards1.json','w'),indent=1,ensure_ascii=False)
