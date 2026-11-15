import pymupdf as fitz,re,json
doc=fitz.open('/mnt/user-data/uploads/10MA Course Planner/02 Sources/2023-cambridge-units-1-2.pdf')
ents=[];cur=None
for pn in range(790,doc.page_count):
  t=doc[pn].get_text()
  if pn>790 and 'Glossary' not in t[:200]: break
  for b in doc[pn].get_text('dict')['blocks']:
    for l in b.get('lines',[]):
      if cur: cur['def' if not cur.get('open') else 'term']+=' '
      for s in l['spans']:
        txt=s['text']
        if 'Bold' in s['font'] and re.search(r'\[p\.\s*\d+\]',txt) or ('Bold' in s['font'] and txt.strip() and len(txt.strip())>1 and not re.fullmatch(r'[A-Z]',txt.strip())):
          if cur and cur.get('open'): cur['term']+=txt; 
          else: cur={'term':txt,'def':'','open':True}; ents.append(cur)
        else:
          if cur: cur['open']=False; cur['def']+=txt
out=[]
for e in ents:
  m=re.search(r'^(.*?)\s*\[p\.\s*(\d+)\]',e['term']+' '+e['def'])
  if not m: continue
  term=re.sub(r'\s+',' ',m.group(1)).strip(); rest=(e['term']+' '+e['def'])[m.end():]
  out.append({'term':term,'printed_page':int(m.group(2)),'definition':re.sub(r'\s+',' ',rest).replace('ﬁ','fi').replace('ﬀ','ff').strip()[:400]})
json.dump(out,open('g11_glossary.json','w'),indent=0,ensure_ascii=False)
print(len(out)); [print(x) for x in out[:6]]
