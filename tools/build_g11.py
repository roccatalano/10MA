import json,sys,re
sys.path.insert(0,'.')
from maps_apk_g11 import APK; from maps_vid_g11 import VID
d=json.load(open('g11_stage1.json')); gl=json.load(open('g11_glossary.json'))
ck={y:json.load(open(f'checklist{y}.json')) for y in (7,8,9,10)}
V=json.load(open('edrolo_vcaa_mapped.json'))
units=json.load(open('../10MA/courses/units.json'))['units']
target={i['id'] for u in units for i in u['items'] if i['id'].startswith('G11-')}
E2G={'1A':['2E'],'1B':['2E','3A'],'1C':['3A'],'1D':['2F'],'1E':['2F'],'1F':['2G'],
'2A':['12A','12B'],'2B':['12B'],'2C':['12C'],'2D':['12D'],'2E':['12E'],'2F':['12F'],'2G':['12F'],'2H':['12G'],'2I':['12H'],
'3A':['6A'],'3B':['6A','1B'],'3C':['6B'],'3D':['6C'],'3E':['3C'],'3F':['6D'],'3G':['6E'],'3H':['3D'],'3I':['6E','3D'],
'4A':['4A'],'4B':['4B'],'4C':['4C'],'4D':['4C','4D'],'4E':['4G'],'4F':['4F'],'4G':[],'4H':[],'4I':['4E'],
'7A':['13A'],'7B':['13B'],'7C':['13C'],'7D':['13D'],'7E':['13E'],
'8A':['5A'],'8B':['5A','4F'],'8C':['5B'],'8D':['5C'],'8E':['5C'],'8F':['5C'],'8G':['5D'],'8H':['5E']}
def find(y,key):
  sub,n=key.split('.'); r=[x for x in ck[y] if x['sub']==sub and x['n']==int(n)]
  assert len(r)==1,(y,key,len(r)); return r[0]
for ch in d['chapters']:
  for c in ch['subchapters']:
    if c['id'] not in target: continue
    s=c['sub']
    if not c['learning_intentions']: c['learning_intentions_note']='book has no learning intentions box for this subchapter'
    g=[x for x in gl if c['printed_page']<=x['printed_page']<=c['printed_end']]
    c['key_vocab']=[x['term'] for x in g]
    c['key_definitions']=[{'term':x['term'],'definition':x['definition'],'printed_page':x['printed_page']} for x in g]
    c['key_vocab_note']='G11 glossary terms whose page reference falls in this subchapter'
    c['videos']=[{'title':t,'url':u} for t,u in VID[s]]
    c['apk']=[]
    for y,key in APK[s]:
      x=find(y,key); c['apk'].append({'book':f'C{y}','sub':f"C{y}-{x['sub']}",'n':x['n'],'skill':x['text'],'question_locator':x['eg'],'src':f'Cambridge Year {y} Ch{x["chapter"]} checklist','pdf_page':x['pdf_page']})
    c['edrolo_lessons']=['E11-'+e for e in E2G[s]]
    c['do_now_pool']=[{'src':f"E11-{q['edrolo']} Q{q['q']}",'vcaa':q['tag'],'section':{'multiple':'Questions from multiple lessons','vcaa':'VCAA question','lesson':'Lesson questions'}[q['section']],'pdf_page':q['pdf_page'],'question_locator':q['text_locator'][:160],'also_in':q['also_in'],'mapped_by':q['map']} for q in V if q['g11']==s]
    c['do_now']=[]; c['do_now_note']='use do_now_pool (Edrolo VCAA questions on this subchapter) for the lesson AFTER this one; slots wait for lesson groupings'
    c['vc2']=[]; c['vc2_note']='VCE unit (no VC2 codes)'
    c['status']='indexed'
d['book']['sources']={'E11':'2020-edrolo-units-1-2.pdf (Edrolo VCE General Maths Units 1&2, 2nd ed 2020; old study design)'}
json.dump(d,open('../10MA/library/G11.json','w'),indent=1,ensure_ascii=False)
for ch in d['chapters']:
  for c in ch['subchapters']:
    if c['id'] in target: print(c['sub'],'LI',len(c['learning_intentions']),'SC',len(c['success_criteria']),'voc',len(c['key_vocab']),'vid',len(c['videos']),'pool',len(c['do_now_pool']),'ed',c['edrolo_lessons'])
