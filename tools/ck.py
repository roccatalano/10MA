import items,json,re
from collections import Counter
for y in (7,8,9,10):
  P=items.pages(f'c{y}.txt'); ck=[x for x in items.checklist(P) if x['pdf_page']>30]
  for i,x in enumerate(ck):
    if not x['sub']:
      p=next((ck[j]['sub'] for j in range(i-1,-1,-1) if ck[j]['sub']),None)
      n=next((ck[j]['sub'] for j in range(i+1,len(ck)) if ck[j]['sub']),None)
      x['sub']=p if p==n or not n else (p if p and p[:-1]==n[:-1] and ord(n[-1])-ord(p[-1])<=1 else n); x['sub_inferred']=True
    x['chapter']=int(re.match(r'\d+',x['sub']).group())
  json.dump(ck,open(f'checklist{y}.json','w'),indent=0,ensure_ascii=False)
  print(y,len(ck),sorted(Counter(x['chapter'] for x in ck).items()))
# known mislabels (label line lost on page break)
for y,fix in ((8,{(4,27):'3K',(4,28):'3K',(4,29):'3K'}),(9,{(9,15):'8J',(9,16):'8J',(9,17):'8J'}),(10,{(8,19):'8J'})):
  ck=json.load(open(f'checklist{y}.json'))
  for x in ck:
    k=(x['chapter'],x['n'])
    if k in fix and (y==10 or ('algebraic' in x['text'] if y==9 else 'unitary' in x['text'])):
      x['sub']=fix[k]; x['chapter']=int(re.match(r'\d+',x['sub']).group()); x['sub_inferred']=True
  json.dump(ck,open(f'checklist{y}.json','w'),indent=0,ensure_ascii=False)
