import pymupdf as fitz,json,re,sys
doc=fitz.open('/mnt/user-data/uploads/10MA Course Planner/02 Sources/2024 - Essential Mathematics for the Victorian Curriculum 10 & 10A Third Edition.pdf')
d=json.load(open('../10MA/library/C10.json'))
out={}
for ch in d['chapters'][1:10]:
  for c in ch['subchapters']:
    on=False;terms=[];cur=''
    for pn in range(c['pdf_page'],c['pdf_end']+1):
      for b in doc[pn-1].get_text('dict')['blocks']:
        for l in b.get('lines',[]):
          for s in l['spans']:
            t=s['text']
            if 'Helvetica' in s['font'] and 'Bold' in s['font']:
              if re.search(r'KEY IDEAS',t): on=True; continue
              if re.search(r'BUILDING UNDERSTANDING|Example \d',t) and on: on=None
            if on is None: break
            if on and 'Times' in s['font'] and 'Bold' in s['font']:
              cur+=t
            else:
              if cur.strip(): terms.append(cur)
              cur=''
          if on is None: break
        if on is None: break
      if on is None: break
    seen=[]
    for t in terms:
      t=re.sub(r'\s+',' ',t.replace('ﬁ','fi').replace('fi ','fi').replace('ﬂ','fl')).strip(' .,:;()')
      if len(t)>2 and not re.fullmatch(r'[\d\W]+',t) and t.lower() not in [x.lower() for x in seen] and len(t)<45: seen.append(t)
    out[c['sub']]=seen
json.dump(out,open('vocab.json','w'),indent=0,ensure_ascii=False)
for k,v in out.items(): print(k,v)
