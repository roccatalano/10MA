import json,re,items
cards=[c for c in json.load(open('cards2.json')) if c['chapter']==1]
vc2=json.load(open('vc2_all.json'))
ck10=[x for x in json.load(open('checklist10.json')) if x['chapter']==1]
ck={y:json.load(open(f'checklist{y}.json')) for y in (7,8,9)}
P=items.pages('c10.txt')
def is10A(code): return bool(re.match(r'VC2M10A[A-Z]+\d\d$',code))
def code(c): return {'code':c,'text':vc2.get(c,''),'tenA':is10A(c),'level':'10A' if is10A(c) else ('9' if c.startswith('VC2M9') else '10')}
VC={'1A':['VC2M9A02','VC2M10A01','VC2M10A05'],'1B':['VC2M10A07','VC2M10A12','VC2M10A03'],'1C':['VC2M10A08'],
'1D':['VC2M10A03','VC2M10A12','VC2M10AA03'],'1E':['VC2M9A03'],'1F':['VC2M9A03','VC2M9A04'],'1G':['VC2M9A04'],
'1H':['VC2M10A10'],'1I':['VC2M10A09'],'1J':['VC2M10A09'],'1K':['VC2M10A09','VC2M10A07'],'1L':['VC2M10A08']}
APK={'1A':[(7,83),(8,96),(8,105),(9,47)],'1B':[(7,172),(8,134),(9,55)],'1C':[(7,109),(8,141),(9,59)],
'1D':[(7,57),(8,100),(9,54)],'1E':[(7,46),(8,172),(9,91)],'1F':[(8,175),(9,89),(9,94)],'1G':[(7,120),(8,86),(9,68)],
'1H':[(7,130),(9,88),(9,91)],'1I':[(8,164),(9,100),(9,56)],'1J':[(7,169),(8,96),(9,64)],'1K':[(7,167),(8,139),(9,58)],
'1L':[(8,170),(9,59),(9,85)]}
LIVOCAB={'1D':['algebraic fraction','lowest common denominator'],'1F':['gradient','y-intercept'],'1K':['simultaneous equations']}
VID={
'1A':[('Class Mathematics: Review of Algebra (5 videos)','https://classmathematics.com.au/resources/sa/year-10/maths-10a/linear-relations/review-of-algebra')],
'1B':[('Class Mathematics: Solving Linear Equations (3 videos)','https://classmathematics.com.au/resources/wa/year-10/maths-10a/linear-relations/solving-linear-equations')],
'1C':[('Class Mathematics: Linear Inequalities','https://classmathematics.com.au/resources/wa/year-10/maths-10/linear-relations/linear-inequalities'),('Khan Academy: Plotting an inequality on a number line','https://www.youtube.com/watch?v=dTwZ5N126gw')],
'1D':[('Class Mathematics: Adding and Subtracting Algebraic Fractions','https://classmathematics.com.au/resources/wa/year-10/maths-10/linear-relations/adding-and-subtracting-algebraic-fractions')],
'1E':[('Class Mathematics: Graphing Straight Lines','https://classmathematics.com.au/resources/wa/year-10/maths-10/linear-relations/graphing-straight-lines')],
'1F':[('Class Mathematics: Finding an Equation of a Line','https://classmathematics.com.au/resources/wa/year-10/maths-10/linear-relations/finding-an-equation-of-a-line')],
'1G':[('Khan Academy: Midpoint formula','https://www.youtube.com/watch?v=Ez_-RwV9WVo'),('Mathispower4u: Distance between two points','https://youtu.be/Vj7twkiUgf0')],
'1H':[('Khan Academy: Equations of parallel and perpendicular lines','https://www.youtube.com/watch?v=9hryH94KFJA')],
'1I':[('Class Mathematics: Simultaneous Equations Using Substitution','https://classmathematics.com.au/resources/sa/year-10/maths-10a/linear-relations/simultaneous-equations-using-substitution')],
'1J':[('Class Mathematics: Simultaneous Equations Using Elimination','https://classmathematics.com.au/resources/sa/year-10/maths-10/linear-relations/simultaneous-equations-using-elimination'),('Khan Academy: Systems with elimination practice','https://www.youtube.com/watch?v=u5dPUHjagSI')],
'1K':[('Khan Academy: Setting up systems of linear equations','https://www.youtube.com/watch?v=pL4PXSXH-R8')],
'1L':[]}
# Do Now pools
pq=[(1,'1A'),(2,'1B'),(3,'1B'),(4,'1C'),(5,'1D'),(6,'1D'),(7,'1E'),(8,'1E'),(9,'1E'),(10,'1F')]
mc=[(1,'1A'),(2,'1B'),(3,'1C'),(4,'1D'),(5,'1E'),(6,'1E'),(7,'1E'),(8,'1F'),(9,'1G'),(10,'1H'),(11,'1H'),(12,'1I'),(13,'1K'),(14,'1L'),(15,'1L')]
pool={}
for q,s in pq: pool.setdefault(s,[]).append({'src':'C10 Ch1 Progress quiz','q':q,'printed_page':45,'pdf_page':66})
for q,s in mc: pool.setdefault(s,[]).append({'src':'C10 Ch1 Review · Multiple choice','q':q,'printed_page':92 if q<=9 else 93,'pdf_page':113 if q<=9 else 114})
pool.setdefault('1J',[]).append({'src':'C10 Ch1 Review · Short answer','q':15,'printed_page':91,'pdf_page':112,'note':'no progress-quiz/MC item for 1J'})
y9=[x for x in json.load(open('pq9.json')) if x['pdf_page']<800 and x['sub'] and x['sub'][0] in '24']
y9pool={'2':[x for x in y9 if x['sub'][0]=='2'],'4':[x for x in y9 if x['sub'][0]=='4']}
used=set()
def take(lst):
  for it in lst:
    k=(it['src'],it['q'])
    if k not in used: used.add(k); return it
def y9take(ch):
  for x in y9pool[ch]:
    k=('C9 Ch%s Progress quiz'%ch,x['q'])
    if k not in used:
      used.add(k); return {'src':'C9 Ch%s Progress quiz'%ch,'q':x['q'],'sub':'C9-'+x['sub'],'pdf_page':x['pdf_page'],'printed_page':None}
subs=[c['sub'] for c in cards]
for i,c in enumerate(cards):
  s=c['sub']
  c['vc2']=[code(x) for x in VC[s]]
  c['success_criteria']=[{'n':x['n'],'text':x['text']} for x in ck10 if x['sub']==s]
  c['exit_tasks']=[{'n':x['n'],'skill':x['text'],'question_locator':x['eg'],'src':'C10 Ch1 Chapter checklist','printed_page':x['pdf_page']-21,'pdf_page':x['pdf_page']} for x in ck10 if x['sub']==s]
  kt=[t.replace('ﬁ ','fi').replace('ﬁ','fi') for t in c.pop('key_terms',[]) if not re.match(r'(Lesson starter|iii)',t) and t.lower()!=c['title'].lower()]
  c['key_vocab']=kt+[t for t in LIVOCAB.get(s,[]) if t not in kt]
  c['key_vocab_note']='bold terms from Key ideas' + (' + terms from the learning intentions' if s in LIVOCAB else '')
  c['videos']=[{'title':t,'url':u} for t,u in VID[s]]
  apk=[]
  for y,idx in APK[s]:
    x=ck[y][idx]; apk.append({'book':f'C{y}','sub':f"C{y}-{x['sub']}",'n':x['n'],'skill':x['text'],'question_locator':x['eg'],'src':f'Cambridge Year {y} Ch{x["chapter"]} checklist','pdf_page':x['pdf_page']})
  c['apk']=apk
  ch9='2' if s in '1A1B1C1D' else '4'
  dn=[]
  if i>=1:
    it=take(pool.get(subs[i-1],[])); 
    if it: dn.append(dict(it,slot='Last lesson',sub='C10-'+subs[i-1]))
  for j in range(i-2,-1,-1):
    it=take(pool.get(subs[j],[]))
    if it: dn.append(dict(it,slot='Earlier this chapter',sub='C10-'+subs[j])); break
  while len(dn)<3:
    it=y9take(ch9); dn.append(dict(it,slot='Previous year (Y9 Ch%s)'%ch9))
  c['do_now']=dn
  c['status']='indexed'
ch={'id':'C10-Ch1','book':'C10','chapter':1,'title':'Algebra, equations and linear relationships',
'pdf_page':22,'vc2_codes':[code(x) for x in sorted({k for c in cards for k in VC[c['sub']]}|set(cards[0]['vc2_chapter_codes']))],
'chapter_resources':[{'name':'Progress quiz','printed_page':45},{'name':'Applications and problem-solving','printed_page':64},{'name':'Modelling','printed_page':82},{'name':'Technology and computational thinking','printed_page':83},{'name':'Investigation','printed_page':85},{'name':'Problems and challenges','printed_page':86},{'name':'Chapter summary','printed_page':87},{'name':'Chapter checklist with success criteria','printed_page':88},{'name':'Chapter review','printed_page':90}],
'subchapters':cards}
for c in cards:
  for k in ['vc2_chapter_codes','chapter_title','chapter']: c.pop(k,None)
json.dump({'book':{'id':'C10','title':'Essential Mathematics for the Victorian Curriculum 10 & 10A (3rd ed, 2024)','pdf_offset':21},'chapters':[ch]},open('/home/claude/10ma/library/C10.json','w'),indent=1,ensure_ascii=False)
for c in cards: print(c['sub'],len(c['success_criteria']),[d['slot'][:5]+':'+d['sub']+'#'+str(d['q']) for d in c['do_now']])
