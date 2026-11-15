r"""Add the 10MAG Modified level (L0 = Year 7-8, Year 9 for box plots) to the CFAT blocks C10-9A...9E.
Run after gen_ch9.py:  python3 tools/cfat/gen_ch9m.py   (gen_ch9.py rewrites the blocks without L0, so always run both, in that order)
Every question verbatim from the cited page; "adapted" in src = stem reworded / parts chosen so it stands alone (Rocco OK'd, 16 Nov).
Questions are NOT the ones used on the modified worksheets (Examples / Now you try)."""
import json,os
HERE=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(HERE,'gen_ch9.py')).read();exec(src[:src.index('B={}')])   # helpers only: table, stemleaf, axis, boxplot, mc, sa, R
C7='Cambridge Essential Mathematics 7 (3rd Ed)';C8='Cambridge Essential Mathematics 8 (3rd Ed)';C9='Cambridge Essential Mathematics 9 (3rd Ed)'
PARTS='adapted: parts chosen'

def colgraph(labels,freqs,xlabel,ymax,step=2,blank=False,W=380,H=200,col=R):
    """frequency (column) graph, one column per class, labels under the columns"""
    n=len(labels);L,Rm,T,B=36,10,8,38;w=(W-L-Rm)/n;h=H-T-B;y=lambda f:T+h-f/ymax*h
    o=[f'<line x1="{L}" y1="{T+h}" x2="{W-Rm}" y2="{T+h}" stroke="#000" stroke-width="1.3"/><line x1="{L}" y1="{T-4}" x2="{L}" y2="{T+h}" stroke="#000" stroke-width="1.3"/>']
    for k in range(ymax+1):o.append(f'<line x1="{L}" y1="{y(k)}" x2="{W-Rm}" y2="{y(k)}" stroke="#ccc" stroke-width=".6"/>')
    for i in range(n+1):o.append(f'<line x1="{L+i*w}" y1="{T}" x2="{L+i*w}" y2="{T+h}" stroke="#ccc" stroke-width=".6"/>')
    if not blank:
        for k in range(0,ymax+1,step):o.append(f'<text x="{L-5}" y="{y(k)+4}" font-size="11" text-anchor="end">{k}</text>')
        for i,f in enumerate(freqs):o.append(f'<rect x="{L+i*w+2}" y="{y(f)}" width="{w-4}" height="{T+h-y(f)}" fill="{col}" fill-opacity=".2" stroke="{col}" stroke-width="1.5"/>')
        for i,g in enumerate(labels):o.append(f'<text x="{L+(i+.5)*w}" y="{T+h+14}" font-size="10" text-anchor="middle">{g}</text>')
        o.append(f'<text x="{(L+W-Rm)/2}" y="{H-6}" font-size="11" text-anchor="middle">{xlabel}</text><text x="11" y="{T+h/2}" font-size="11" text-anchor="middle" transform="rotate(-90 11 {T+h/2})">Frequency</text>')
    return f'<svg class="fig" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(o)}</svg>'
def dotplot(a,b,data,col=R,W=420,blank=False):
    o,x=axis(a,b,1,1,W);cnt={}
    if not blank:
        for v in data:
            cnt[v]=cnt.get(v,0)+1;o.append(f'<circle cx="{x(v):.1f}" cy="{60-cnt[v]*9}" r="3.6" fill="{col}"/>')
    return f'<svg class="fig" width="{W}" height="82" viewBox="0 0 {W} 82">{"".join(o)}</svg>'

L0={}
# ------------------------------------------------------------------ 9A
L0[('9A',1)]=[sa('L0',3,'Classify the following variables as categorical, continuous numerical or discrete numerical data.<br><b>a</b>&nbsp; the number of cars in each household<br><b>b</b>&nbsp; the highest temperature of the ocean each day<br><b>c</b>&nbsp; the favourite brand of chocolate of the teachers at your school',
  ['a discrete numerical','b continuous numerical','c categorical'],f'{C7}, Exercise 8A Q2a, c, d (p. 517); {PARTS}','VC2M7ST01')]
L0[('9A',2)]=[sa('L0',1,'A survey is conducted to determine how many siblings children have. Which of the following methods of conducting the survey is more likely to lead to bias?<br>Method 1: Choosing $20$ children at random from a school.<br>Method 2: Asking $20$ children waiting outside a primary school at the end of a day.',
  ['Method 2: children waiting outside a primary school at the end of the day are more likely to be picking up a younger brother or sister, so they are more likely to have siblings.'],
  f'{C8}, Exercise 8F Q4c (p. 585); adapted: stem from Q4 kept, graph and parts a–b left out','VC2M8ST01')]
# ------------------------------------------------------------------ 9B
FT=table(['Number','Frequency'],[['0−5','5'],['6−10','12'],['11−15','14'],['16−20','11'],['21−25','5'],['26−30','8'],['31−35','2'],['36−40','1']],fs='9.5pt',pad='.2mm 2.4mm')
L0[('9B',1)]=[sa('L0',2,'Represent the following frequency table as a frequency graph.<div style="display:flex;gap:5mm;align-items:flex-start">'+FT+'</div>',
  [colgraph(['0−5','6−10','11−15','16−20','21−25','26−30','31−35','36−40'],[5,12,14,11,5,8,2,1],'Number',14)],
  f'{C8}, Exercise 8C Q4 (p. 565)','VC2M8ST02',blank=colgraph(['']*8,[0]*8,'',14,blank=True,W=470,H=200))]
L0[('9B',2)]=[sa('L0',3,'The ages of boys in an after-school athletics squad are shown in the table below.'+table(['Age','Frequency'],[['10','3'],['11','8'],['12','12'],['13','4'],['14','3']],fs='9.5pt',pad='.2mm 2.4mm')
  +'<b>a</b>&nbsp; State the total number of boys in the squad.<br><b>b</b>&nbsp; Calculate the mean age of the squad, correct to two decimal places.<br><b>c</b>&nbsp; What is the median age of the boys in the squad?',
  [r'a $3 + 8 + 12 + 4 + 3 = 30$ boys',r'b $\dfrac{10 \times 3 + 11 \times 8 + 12 \times 12 + 13 \times 4 + 14 \times 3}{30} = \dfrac{356}{30} = 11.87$ years',r'c The $15$th and $16$th ages are both $12$, so the median is $12$ years.'],
  f'{C8}, Chapter 8 review, short-answer Q4a, c, d (p. 633); {PARTS}','VC2M8ST02')]
# ------------------------------------------------------------------ 9C
L0[('9C',1)]=[sa('L0',4,'The two-way table below shows the results of a poll conducted of a group of boys and girls who own mobile phones to see who pays their own bills.'
  +table(['','Boys','Girls','Total'],[['<b>Pay own bill</b>','4','7','11'],['<b>Do not pay own bill</b>','8','7','15'],['<b>Total</b>','12','14','26']],fs='10pt')
  +'<b>a</b>&nbsp; How many people participated in this poll?<br><b>b</b>&nbsp; How many boys were surveyed?<br><b>c</b>&nbsp; How many of the people surveyed pay their own bill?<br><b>d</b>&nbsp; Find the probability that a randomly selected person is a boy and pays his own bill.',
  [r'a $26$',r'b $12$',r'c $11$',r'd $\dfrac{4}{26} = \dfrac{2}{13}$'],f'{C8}, Exercise 8J Q4a–c, d i (p. 616); {PARTS}','VC2M8P02')]
L0[('9C',2)]=[sa('L0',2,'In a group of $40$ dogs, $25$ had a name tag and a collar, $7$ had only a name tag and $4$ had only a collar.<br><b>a</b>&nbsp; How many dogs had neither a name tag nor a collar?<br><b>b</b>&nbsp; Represent the survey findings in a two-way table.',
  [r'a $40 - 25 - 7 - 4 = 4$',table(['','Collar','No collar','Total'],[['<b>Name tag</b>','25','7','32'],['<b>No name tag</b>','4','4','8'],['<b>Total</b>','29','11','40']],col=R)],
  f'{C8}, Exercise 8J Q2a, f (p. 615); {PARTS}','VC2M8P02',
  blank=table(['','Collar','No collar','Total'],[['<b>Name tag</b>','','',''],['<b>No name tag</b>','','',''],['<b>Total</b>','','','']],fs='11pt'))]
# ------------------------------------------------------------------ 9D (short week: two L0 questions per skill)
L0[('9D',1)]=[sa('L0',1,'Find the range of $9, 3, 9, 3, 10, 5, 0, 2$.',[r'Range $= 10 - 0 = 10$'],f'{C8}, Exercise 8E Q2a (p. 578); adapted: stem reworded for a single part','VC2M8ST02'),
  sa('L0',2,'Find the IQR of the following set. Remember to sort first.<br>$6, 11, 3, 15, 18, 14, 13, 2, 16, 7, 7$',
  [r'$2, 3, 6, 7, 7, \underline{11}, 13, 14, 15, 16, 18$ (remove the middle value)',r'Lower quartile $= 6$, upper quartile $= 15$',r'IQR $= 15 - 6 = 9$'],f'{C8}, Exercise 8E Q5c (p. 578); adapted: stem reworded for a single part','VC2M8ST02')]
ACES=[0]+[1]*3+[2]*4+[3]*2+[4]*6+[5]+[10]
L0[('9D',2)]=[sa('L0',2,'Consider the frequency table showing the number of aces served by a tennis player.'+table(['Aces','Frequency'],[['0','1'],['1','3'],['2','4'],['3','2'],['4','6'],['5','1'],['10','1']],fs='9.5pt',pad='.2mm 2.4mm')
  +'<b>a</b>&nbsp; Construct a dot plot for the frequency table.<br><b>b</b>&nbsp; Use your dot plot to identify any outliers.',
  [dotplot(0,10,ACES),r'b $10$ aces is an outlier: it is separated from the main cluster ($0$ to $5$).'],
  f'{C8}, Exercise 8C Q2a, c (p. 564); {PARTS}','VC2M8ST02',blank=dotplot(0,10,[],blank=True))]
# ------------------------------------------------------------------ 9E (Year 9 9L Box plots: the box plot is first met in Year 9)
L0[('9E',1)]=[sa('L0',4,'This box plot summarises the number of rabbits spotted per day in a paddock over a $100$-day period.'+boxplot(-5,65,5,10,(0,10,25,35,60),col='#000',lab0=0,lab1=60).replace('class="fig"','class="qf"')
  +'<b>a</b>&nbsp; State the minimum and maximum number of rabbits spotted.<br><b>b</b>&nbsp; Find the range of the number of rabbits spotted.<br><b>c</b>&nbsp; State the median number of rabbits spotted.<br><b>d</b>&nbsp; Find the interquartile range.',
  [r'a Minimum $= 0$, maximum $= 60$',r'b Range $= 60 - 0 = 60$',r'c Median $= 25$',r'd IQR $= 35 - 10 = 25$'],f'{C9}, Exercise 9L Q2a–d (p. 699); {PARTS}','VC2M9ST02'),
  sa('L0',3,'Consider the set of data below.<br>$2 \\;\\; 2 \\;\\; 3 \\;\\; 3 \\;\\; 4 \\;\\; 6 \\;\\; 7 \\;\\; 7 \\;\\; 7 \\;\\; 8 \\;\\; 8 \\;\\; 8 \\;\\; 8 \\;\\; 9 \\;\\; 11 \\;\\; 11 \\;\\; 13 \\;\\; 13 \\;\\; 13$<br>Find the minimum value, the maximum value, the median $(Q_2)$, the lower quartile $(Q_1)$ and the upper quartile $(Q_3)$, and draw a box plot to represent the data.',
  [r'$19$ values: min $= 2$, max $= 13$, $Q_2 = 8$ (the $10$th value)',r'$Q_1 = 4$ (middle of the lower $9$), $Q_3 = 11$ (middle of the upper $9$)',boxplot(0,14,1,2,(2,4,8,11,13))],
  f'{C9}, Exercise 9L Q3a (p. 700); adapted: parts i–vi combined into one stem','VC2M9ST02',blank=boxplot(0,14,1,2,(0,0,0,0,0),blank=True))]

for sub in ['9A','9B','9C','9D','9E']:
    p=os.path.join(HERE,f'C10-{sub}.json');b=json.load(open(p))
    b['levels']['L0']='10MAG Modified (Year 7–8; Year 9 for box plots)'
    for s in b['skills']:
        s['items']=[x for x in s['items'] if x['level']!='L0']+L0.get((sub,s['n']),[])
    json.dump(b,open(p,'w'),indent=1,ensure_ascii=False);print('L0 added',sub,sum(1 for s in b['skills'] for x in s['items'] if x['level']=='L0'))
