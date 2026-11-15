import json
it=json.load(open('sd_gm.json'))
it={k:v for k,v in it.items() if not ((k.startswith('GM-U1-AoS4-kk') and int(k.split('kk')[1])>6) or (k.startswith('GM-U2-AoS4-kk') and int(k.split('kk')[1])>8))}
for v in it.values(): v['text']=v['text'].replace('[rule]','[formula not in the text extract — see Study Design]')
json.dump(it,open('sd_gm.json','w'),indent=0,ensure_ascii=False)
A1='GM-U1-AoS1-';A2='GM-U1-AoS2-';A4='GM-U1-AoS4-';B1='GM-U2-AoS1-';B2='GM-U2-AoS2-'
M={
'1A':[A2+'kk6'],'1B':[A2+'c8',A2+'kk6'],'1C':[A2+'c8'],'1D':[A2+'kk6'],'1E':[A2+'kk6'],'1F':[A2+'c10',A2+'kk6'],
'2A':[A1+'c1',A1+'c2',A1+'kk1'],'2B':[A1+'c2'],'2C':[A1+'c3',A1+'kk2'],'2D':[A1+'c3',A1+'c6',A1+'kk2'],
'2E':[A1+'c4',A1+'kk4'],'2F':[A1+'c4',A1+'kk4'],'2G':[A1+'c6'],'2H':[A1+'c5',A1+'kk3'],'2I':[A1+'c7'],
'3A':[A2+'c1',A2+'c2',A2+'kk1'],'3B':[A2+'c3',A2+'kk1',A2+'kk2'],'3C':[A2+'c1',A2+'c7',A2+'kk3'],'3D':[A2+'c3',A2+'kk2'],
'3E':[A2+'c4',A2+'kk4'],'3F':[A2+'c1',A2+'c7',A2+'kk3'],'3G':[A2+'c5',A2+'kk2'],'3H':[A2+'c6',A2+'kk5'],'3I':[A2+'c6',A2+'c7',A2+'kk5'],
'4A':[A4+'c1',A4+'c2',A4+'kk1',A4+'kk2'],'4B':[A4+'c3',A4+'kk3'],'4C':[A4+'c3',A4+'kk3'],'4D':[A4+'c3',A4+'kk3'],
'4E':[A4+'c5',A4+'kk4'],'4F':[A4+'c4',A4+'kk5'],'4G':[A4+'c6',A4+'kk6'],'4H':[A4+'c6',A4+'kk6'],'4I':[A4+'c4'],
'7A':[B1+'c1',B1+'c2',B1+'kk1'],'7B':[B1+'c2',B1+'c3',B1+'kk2',B1+'kk3'],'7C':[B1+'c2',B1+'kk2'],'7D':[B1+'c4',B1+'kk4'],'7E':[B1+'c4',B1+'c5',B1+'kk4'],
'8A':[B2+'c1',B2+'kk1'],'8B':[B2+'c1',B2+'kk1'],'8C':[B2+'c2',B2+'kk1'],'8D':[B2+'c3',B2+'kk1'],'8E':[B2+'c3',B2+'kk1'],'8F':[B2+'c3',B2+'kk1'],
'8G':[B2+'c4',B2+'kk2'],'8H':[B2+'c5',B2+'kk3']}
P='../10MA/library/G11.json'; d=json.load(open(P))
for ch in d['chapters']:
  for c in ch['subchapters']:
    if c['sub'] in M and c.get('status')=='indexed':
      c.pop('vc2',None); c.pop('vc2_note',None)
      c['study_design']=[dict(it[k]) for k in M[c['sub']]]
      c['study_design_note']='VCE Mathematics Study Design 2023–2027 (2023MathematicsSD.docx), General Mathematics Units 1 & 2: topic content dot points (c) and Outcome 1 key knowledge (kk). Mapped by Claude.'
  if any(c.get('study_design') for c in ch['subchapters']):
    ch['study_design_topic']=sorted({x['topic'] for c in ch['subchapters'] for x in c.get('study_design',[])})
    ch.pop('vc2_codes',None)
d['book']['curriculum']='VCE Mathematics Study Design 2023–2027 — General Mathematics Units 1 & 2 (not VC2)'
json.dump(d,open(P,'w'),indent=1,ensure_ascii=False)
print(sum(1 for ch in d['chapters'] for c in ch['subchapters'] if c.get('study_design')))
