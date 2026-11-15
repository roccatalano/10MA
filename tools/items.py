import re,json,sys
def pages(fn): return open(fn).read().split('\f')
LAB=re.compile(r'^\s*(\d{1,2}[A-N](?:[/,–-]\s*\d{0,2}[A-N])*)\s*$')
def clean(s): return re.sub(r'\s+',' ',s.replace('​','')).strip()
def checklist(P):
  out=[];k=0
  while k<len(P):
    if 'Chapter checklist with success criteria' in P[k] and 'I can' in P[k]:
      j=k;buf=[]
      while j<len(P) and ('I can' in P[j]) and (j==k or 'Short-answer questions' not in P[j].split('I can')[0]):
        buf.append((j+1,P[j]));j+=1
        if 'Short-answer questions' in P[j-1]: break
      cur=None
      for pg,p in buf:
        L=p.splitlines()
        for i,l in enumerate(L):
          m=re.match(r'^\s*(\d{1,2})\.\s+(I can .*)$',l)
          if m:
            cur=dict(n=int(m.group(1)),text=clean(re.split(r'\s{4,}',m.group(2))[0]),sub=None,eg='',pdf_page=pg);out.append(cur);continue
          if cur and cur['sub'] is None:
            m=LAB.match(l)
            if m: cur['sub']=m.group(1).replace(' ',''); continue
          if cur and 'e.g.' in l and not cur['eg']: cur['eg']=clean(l.split('e.g.',1)[1])
      k=j
    else: k+=1
  # chapter = from sub
  for x in out: x['chapter']=int(re.match(r'\d+',x['sub'] or '0').group()) if x['sub'] else None
  return out
def labelled_qs(P,start,stopwords):
  """questions with margin subchapter labels from page start until stop"""
  out=[];k=start-1;cur=None
  while k<len(P):
    p=P[k]
    for l in p.splitlines():
      m=re.match(r'^\s{0,30}(\d{1,2})\s{1,4}(\S.*)$',l)
      if m and (not out or 0<int(m.group(1))-out[-1]['q']<=2 or int(m.group(1))==1):
        cur=dict(q=int(m.group(1)),stem=clean(re.split(r'\s{4,}',m.group(2))[0])[:90],sub=None,pdf_page=k+1);out.append(cur);continue
      mm=LAB.match(l)
      if cur and cur['sub'] is None and mm: cur['sub']=mm.group(1).replace(' ','')
    k+=1
    if any(w in P[k][:600] for w in stopwords) if k<len(P) else True: break
  return out
