import json,re
P=open('g11.txt').read().split('\f')
d=json.load(open('../10MA/library/G11.json'))
CH=(1,2,3,4,7,8)
def clean(s): return re.sub(r'\s+',' ',s.replace('ﬁ','fi').replace('ﬂ','fl').replace('ﬀ','ff')).strip()
# skills checklists
ck=[]
for k,p in enumerate(P):
  if 'Skills checklist' in p or (ck and ck[-1]['pdf_page']>=k and False): pass
starts=[k for k,p in enumerate(P) if re.search(r'^\s*Skills checklist\s*$',p,re.M)]
for s in starts:
  cur=None
  for k in range(s,s+5):
    p=P[k]
    if k>s and re.search(r'Multiple-choice questions|Short-answer questions|Written-response',p.split('I can')[0] if 'I can' in p else p): 
      body=p.split('Multiple-choice')[0]
    else: body=p
    stop=False
    for l in body.splitlines():
      if re.search(r'^\s*(Multiple-choice questions|Short-answer questions|Written-response questions)',l): stop=True;break
      m=re.match(r'^\s*(\d{1,2}[A-Z])\s+(\d{1,2})\s+(.{0,40}?I can .*)$',l)
      if m: cur=dict(sub=m.group(1),n=int(m.group(2)),text=clean(m.group(3)),eg='',pdf_page=k+1); ck.append(cur); continue
      if cur and not cur['eg'] and 'e.g.' in l: cur['eg']=clean(l.split('e.g.',1)[1]); continue
      if cur and cur['eg'] and len(cur['eg'])<200 and l.strip() and not re.search(r'ISBN|Photocopying|Review\s*$|Chapter \d',l):
        if re.match(r'^\s{10,}\S',l): cur['eg']+=' '+clean(l)
      elif cur and not cur['eg'] and l.strip() and re.match(r'^\s{14,}[a-z(]',l): cur['text']+=' '+clean(l)
    if stop: break
for x in ck: x['chapter']=int(re.match(r'\d+',x['sub']).group())
json.dump(ck,open('checklist_g11.json','w'),indent=0,ensure_ascii=False)
from collections import Counter
print(sorted(Counter(x['chapter'] for x in ck).items()))
# per-subchapter
for ch in d['chapters']:
  if ch['chapter'] not in CH: continue
  for c in ch['subchapters']:
    T='\n'.join(P[c['pdf_page']-1:c['pdf_end']]); L=T.splitlines()
    lis=[];on=False
    for l in L:
      if re.match(r'^\s*Learning intentions',l): on=True; continue
      if on:
        st=l.strip()
        if lis and not st: break
        if st.startswith(''): lis.append(clean(st[1:]))
        elif lis and st and re.match(r'^\s{18,}',l) and not st[0].isupper(): lis[-1]+=' '+clean(st)
        elif lis or (not st and lis): break
    c['learning_intentions']=lis
    ex={}
    LB=re.split(r'\n\s*Exercise\s+'+c['sub']+r'\b',T)[0].splitlines()
    for j,l in enumerate(LB):
      m=re.match(r'^\s*Example (\d+)\s{2,}(\S.*?)\s*$',l)
      if m and int(m.group(1)) not in ex and not re.match(r'\d',m.group(2)):
        ex[int(m.group(1))]=clean(m.group(2))
    nyt=set(int(x) for x in re.findall(r'Now try this (\d+)',T))
    c['examples']=[{'n':n,'title':t,'now_you_try':n in nyt} for n,t in sorted(ex.items())]
    ex_=re.search(r'Exercise\s+'+c['sub'],T)
    secs=[]
    if ex_:
      E=T[ex_.end():]
      for name in ('Building understanding','Developing understanding','Testing understanding'):
        m=re.search(name+r'(.*?)(?=Building understanding|Developing understanding|Testing understanding|\Z)',E,re.S)
        if m:
          qn=[int(x) for x in re.findall(r'^\s*(?:Example \d+\s+)?(\d{1,2})\s{2,}\S',m.group(1),re.M)]
          qn=[q for i,q in enumerate(qn) if i==0 or q>qn[i-1]]
          secs.append({'section':name.lower().replace(' ','_'),'q':f'{qn[0]}–{qn[-1]}' if len(qn)>1 else (str(qn[0]) if qn else '')})
    c['exercise']=secs
    c['success_criteria']=[{'n':x['n'],'text':x['text']} for x in ck if x['sub']==c['sub']]
    c['exit_tasks']=[{'n':x['n'],'skill':x['text'],'question_locator':x['eg'],'src':f'G11 Ch{ch["chapter"]} Skills checklist','printed_page':x['pdf_page']-13,'pdf_page':x['pdf_page']} for x in ck if x['sub']==c['sub']]
json.dump(d,open('g11_stage1.json','w'),indent=1,ensure_ascii=False)
for ch in d['chapters']:
  if ch['chapter'] in CH:
    for c in ch['subchapters']: print(c['sub'],len(c['learning_intentions']),len(c['examples']),sum(e['now_you_try'] for e in c['examples']),len(c['success_criteria']),[s['section'][:3]+s['q'] for s in c['exercise']])
