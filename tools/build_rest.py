import json,re,sys
sys.path.insert(0,'.')
from maps_vc import VC; from maps_apk import APK; from maps_vid import VID; from maps_vocab import DROP,FIX,LIVOCAB
LIB='../10MA/library/C10.json'
d=json.load(open(LIB)); vc2=json.load(open('vc2_all.json')); voc=json.load(open('vocab.json'))
ck10=json.load(open('checklist10.json')); ck={y:json.load(open(f'checklist{y}.json')) for y in (7,8,9)}
P=open('c10.txt').read().split('\f')
units=json.load(open('../10MA/courses/units.json'))['units']
target={i['id'] for u in units for i in u['items'] if i['id'].startswith('C10-') and not i['id'].startswith('C10-1')}
def is10A(c): return bool(re.match(r'VC2M10A[A-Z]+\d\d$',c))
def code(c): return {'code':c,'text':vc2[c],'tenA':is10A(c),'level':'10A' if is10A(c) else ('9' if c.startswith('VC2M9') else '10')}
def find(y,key):
  sub,n=key.split('.'); r=[x for x in ck[y] if x['sub']==sub and x['n']==int(n)]
  assert len(r)==1,(y,key,len(r)); return r[0]
done=[]
for ch in d['chapters']:
  for c in ch['subchapters']:
    if c['id'] not in target: continue
    s=c['sub']
    c['vc2']=[code(x) for x in VC[s]]
    items=[x for x in ck10 if x['sub']==s or ('/' in x['sub'] and s in [x['sub'].split('/')[0]]+[x['sub'][0]+t for t in x['sub'].split('/')[1:]])]
    c['success_criteria']=[{'n':x['n'],'text':x['text']} for x in items]
    c['exit_tasks']=[{'n':x['n'],'skill':x['text'],'question_locator':x['eg'],'src':f'C10 Ch{ch["chapter"]} Chapter checklist','printed_page':x['pdf_page']-21,'pdf_page':x['pdf_page']} for x in items]
    kv=[FIX.get(t,t) for t in voc.get(s,[]) if t not in DROP and t.lower()!=c['title'].lower()]
    kv=list(dict.fromkeys(kv)); add=[t for t in LIVOCAB.get(s,[]) if t.lower() not in [k.lower() for k in kv]]
    c['key_vocab']=kv+add
    c['key_vocab_note']='bold terms from Key ideas'+(' + terms from the learning intentions' if add else '')
    c['videos']=[{'title':t,'url':u} for t,u in VID[s]]
    c['apk']=[]
    for y,key in APK[s]:
      x=find(y,key); c['apk'].append({'book':f'C{y}','sub':f"C{y}-{x['sub']}",'n':x['n'],'skill':x['text'],'question_locator':x['eg'],'src':f'Cambridge Year {y} Ch{x["chapter"]} checklist','pdf_page':x['pdf_page']})
    # Example -> Now you try
    T='\n'.join(P[c['pdf_page']-1:c['pdf_end']])
    for e in c['examples']:
      m=re.search(r'Example %d\b'%e['n'],T)
      seg=T[m.end():] if m else ''
      nx=re.search(r'Example %d\b'%(e['n']+1),seg)
      e['now_you_try']=bool(re.search(r'Now you try',seg[:nx.start()] if nx else seg))
    c['do_now']=[]; c['do_now_note']='waiting for lesson groupings'
    c['status']='indexed'
    done.append(s)
json.dump(d,open(LIB,'w'),indent=1,ensure_ascii=False)
print(len(done),done)
for ch in d['chapters']:
  for c in ch['subchapters']:
    if c['sub'] in done:
      flags=[k for k in ('success_criteria','key_vocab','videos') if not c[k]]+[f"ex{e['n']}-noNYT" for e in c['examples'] if not e['now_you_try']]
      if flags: print(c['sub'],flags)
# chapter-level VC2 lists (codes printed at chapter opener + any assigned to its subchapters)
cc=json.load(open('chcodes.json'))
for ch in d['chapters']:
  if ch['id'] in cc and any(c['id'] in target for c in ch['subchapters']):
    ch['vc2_codes']=[code(x) for x in sorted(set(cc[ch['id']])|{k for c in ch['subchapters'] if c['sub'] in VC for k in VC[c['sub']]})]
json.dump(d,open(LIB,'w'),indent=1,ensure_ascii=False)
