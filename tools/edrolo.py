import re,json
P=open('e11.txt').read().split('\f')
TAG=re.compile(r'^\s*((?:VCAA\s+)?(?:\d{4}\w*\s+VCAA|VCAA\s+\d{4}\w*)\b.*?)\s*$')
qs=[];lesson=None;section='lesson';cur=None
for k,p in enumerate(P):
  for l in p.splitlines():
    m=re.match(r'^\s*LESSON\s+(\d{1,2}[A-Z])\s*$',l)
    if m: lesson=m.group(1); section='lesson'; continue
    if 'Questions from multiple lessons' in l: section='multiple'; continue
    if re.match(r'^\s*VCAA question\s*$',l): section='vcaa'; continue
    m=re.match(r'^\s*Q(\d{1,2})\.\s+(.*)$',l)
    if m and lesson:
      cur=dict(edrolo=lesson,q=int(m.group(1)),pdf_page=k+1,section=section,stem=re.sub(r'\s{2,}',' ',m.group(2)).strip(),body=[],tag=None); qs.append(cur); continue
    if cur and cur['tag'] is None:
      t=TAG.match(l)
      if t and 'key knowledge' not in l and 'Used with permission' not in l: cur['tag']=re.sub(r'\s+',' ',t.group(1)); continue
      if len(cur['body'])<30: cur['body'].append(re.sub(r'\s{2,}',' ',l).strip())
V=[q for q in qs if q['tag']]
for q in V:
  txt=(q['stem']+' '+' '.join(q['body']))
  q['text_locator']=re.sub(r'Difficulty:|Year 1[0-2]|\d marks?',' ',txt)
  q['text_locator']=re.sub(r'\s+',' ',q['text_locator']).strip()[:700]; del q['body']
json.dump(V,open('edrolo_vcaa.json','w'),indent=0,ensure_ascii=False)
from collections import Counter
print(len(qs),len(V),Counter(q['section'] for q in V))
print(Counter(re.sub(r'.*?(Module \d+: [^Q]+|Data analysis|Recursion and financial modelling|Matrices|Networks and decision mathematics|Core|Graphs and relations)\b.*',r'\1',q['tag']) for q in V).most_common(25))
