r"""Write the CFAT blocks for C10 9A–9E (10MAG Univariate Statistics). Run once: python3 tools/cfat/gen_ch9.py
Every question verbatim from the cited page; "adapted" in src = stem reworded / part chosen so it stands alone.
L1 = Cambridge Year 9 Ch 9 review; L2 = Oxford Maths 10 VC (Ch 10 Statistics, Ch 11 Probability).
Only the levels 10MAG needs (L1, L2). Answers worked by teacher and checked."""
import json,os
HERE=os.path.dirname(os.path.abspath(__file__))
R='#d00000'
C9='Cambridge Essential Mathematics 9 (3rd Ed)';O10='Oxford Maths 10 VC (2022)'
LV={"L1":"Level 9 (review)","L2":"Level 10","L3":"Level 10 extension / 10A"}

def table(head,rows,col='#000',fs='10pt',pad='.6mm 2.4mm'):
    td=f'border:1px solid {col};padding:{pad};text-align:center'
    h='<tr>'+''.join(f'<th style="{td};background:#eee;font-size:9pt">{x}</th>' for x in head)+'</tr>' if head else ''
    return f'<table style="border-collapse:collapse;font-size:{fs};color:{col};margin:1.2mm 0">{h}'+''.join('<tr>'+''.join(f'<td style="{td}">{x}</td>' for x in r)+'</tr>' for r in rows)+'</table>'
def stemleaf(rows,key,col='#000'):
    td='padding:.3mm 2.5mm'
    b=''.join(f'<tr><td style="{td};border-right:1.2px solid {col};text-align:right">{s}</td><td style="{td};word-spacing:2mm">{l}</td></tr>' for s,l in rows)
    return (f'<table style="border-collapse:collapse;color:{col};font-size:10.5pt;margin:1mm 0;width:auto"><tr><th style="{td};border-right:1.2px solid {col};border-bottom:1.2px solid {col}">Stem</th>'
            f'<th style="{td};border-bottom:1.2px solid {col};text-align:left">Leaf</th></tr>{b}</table><div style="font-size:9.5pt;color:{col}">{key}</div>')
def axis(a,b,step,lab,W=420,lab0=None,lab1=None):
    n=round((b-a)/step);L=14;u=(W-2*L)/n;x=lambda v:L+(v-a)/step*u
    o=[f'<line x1="2" y1="60" x2="{W-2}" y2="60" stroke="#000" stroke-width="1.2"/><path d="M{W} 60 l-7 -3.5 v7z"/><path d="M0 60 l7 -3.5 v7z"/>']
    for k in range(n+1):
        v=a+k*step;o.append(f'<line x1="{x(v):.1f}" y1="57" x2="{x(v):.1f}" y2="63" stroke="#000"/>')
        if abs((v-(a if lab0 is None else lab0))/lab-round((v-(a if lab0 is None else lab0))/lab))<1e-6 and (lab0 is None or lab0<=v<=lab1):o.append(f'<text x="{x(v):.1f}" y="76" font-size="12" text-anchor="middle">{v:g}</text>')
    return o,x
def boxplot(a,b,step,lab,five,out=(),col=R,W=420,blank=False,lab0=None,lab1=None):
    o,x=axis(a,b,step,lab,W,lab0,lab1);mn,q1,q2,q3,mx=five;y=28
    if not blank:
        o.append(f'<g stroke="{col}" stroke-width="1.8" fill="none"><line x1="{x(mn)}" y1="{y}" x2="{x(q1)}" y2="{y}"/><rect x="{x(q1)}" y="{y-13}" width="{x(q3)-x(q1)}" height="26"/>'
                 f'<line x1="{x(q2)}" y1="{y-13}" x2="{x(q2)}" y2="{y+13}"/><line x1="{x(q3)}" y1="{y}" x2="{x(mx)}" y2="{y}"/><line x1="{x(mn)}" y1="{y-7}" x2="{x(mn)}" y2="{y+7}"/><line x1="{x(mx)}" y1="{y-7}" x2="{x(mx)}" y2="{y+7}"/></g>')
        for v in out:o.append(f'<circle cx="{x(v)}" cy="{y}" r="4" fill="{col}"/>')
    return f'<svg class="fig" width="{W}" height="82" viewBox="0 0 {W} 82">{"".join(o)}</svg>'
def hist(groups,freqs,total,xlabel,ymax,blank=False,W=360,H=220,col=R):
    n=len(freqs);L,Rm,T,B=40,44,10,40;w=(W-L-Rm)/n;h=H-T-B;y=lambda f:T+h-f/ymax*h
    o=[f'<line x1="{L}" y1="{T+h}" x2="{W-Rm}" y2="{T+h}" stroke="#000" stroke-width="1.3"/><line x1="{L}" y1="{T-4}" x2="{L}" y2="{T+h}" stroke="#000" stroke-width="1.3"/>']
    for k in range(ymax+1):o.append(f'<line x1="{L}" y1="{y(k)}" x2="{W-Rm}" y2="{y(k)}" stroke="#ccc" stroke-width=".6"/>')
    for i in range(n+1):o.append(f'<line x1="{L+i*w}" y1="{T}" x2="{L+i*w}" y2="{T+h}" stroke="#ccc" stroke-width=".6"/>')
    if not blank:
        for k in range(ymax+1):
            o.append(f'<text x="{L-6}" y="{y(k)+4}" font-size="11" text-anchor="end">{k}</text>')
            pc=k/total*100
            if abs(pc-round(pc))<1e-9:o.append(f'<text x="{W-Rm+5}" y="{y(k)+4}" font-size="10">{pc:g}</text>')
        o.append(f'<line x1="{W-Rm}" y1="{T-4}" x2="{W-Rm}" y2="{T+h}" stroke="#000" stroke-width="1.3"/>')
        for i,f in enumerate(freqs):
            if f:o.append(f'<rect x="{L+i*w}" y="{y(f)}" width="{w}" height="{T+h-y(f)}" fill="{col}" fill-opacity=".2" stroke="{col}" stroke-width="1.5"/>')
        for i,g in enumerate(groups):o.append(f'<text x="{L+i*w}" y="{T+h+15}" font-size="11" text-anchor="middle">{g}</text>')
        o.append(f'<text x="{(L+W-Rm)/2}" y="{H-6}" font-size="12" text-anchor="middle">{xlabel}</text><text x="12" y="{T+h/2}" font-size="11" text-anchor="middle" transform="rotate(-90 12 {T+h/2})">Frequency</text>'
                 f'<text x="{W-8}" y="{T+h/2}" font-size="11" text-anchor="middle" transform="rotate(90 {W-8} {T+h/2})">% frequency</text>')
    return f'<svg class="fig" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(o)}</svg>'

def mc(level,q,opts,ans,sol,src,vc2,fill=False):
    d=dict(level=level,type='mc',marks=1,q=q,options=opts,answer=ans,sol=sol,src=src,vc2=vc2)
    if fill:d['fill']=True
    return d
def sa(level,marks,q,sol,src,vc2,blank=None):
    d=dict(level=level,type='sa',marks=marks,q=q,sol=sol,src=src,vc2=vc2)
    if blank:d['blank']=blank
    return d
AD='adapted: stem reworded for a single part'

B={}
# ------------------------------------------------------------------ 9A
B['9A']=[dict(n=1,skill='I can describe types of data.',items=[
  mc('L1','The type of data generated by the survey question ‘How long is your arm length?’ is:',['a random number','categorical ordinal','categorical nominal','numerical discrete','numerical continuous'],'E',
     ['A length can take any value in a range: numerical continuous (E)'],f'{C9}, Ch 9 review, multiple-choice Q7 (p. 713)','VC2M10ST04')]),
 dict(n=2,skill='I can choose a survey sample.',items=[
  mc('L2','If a representative sample of $20$ people is to be taken from a group of $280$ children and $120$ adults, how many adults should be chosen?',['$6$','$10$','$14$','$20$','$60$'],'A',
     [r'$\dfrac{120}{400} \times 20 = 6$ (A)'],f'{O10}, Ch 10 review, multiple-choice Q10 (p. 566)','VC2M10ST04')])]
# ------------------------------------------------------------------ 9B
RALLY='$134 \\;\\; 147 \\;\\; 162 \\;\\; 164 \\;\\; 145 \\;\\; 159 \\;\\; 151 \\;\\; 143 \\;\\; 136 \\;\\; 155 \\;\\; 163 \\;\\; 157 \\;\\; 168$<br>$128 \\;\\; 144 \\;\\; 161 \\;\\; 158 \\;\\; 136 \\;\\; 178 \\;\\; 152 \\;\\; 167 \\;\\; 154 \\;\\; 161 \\;\\; 152 \\;\\; 171$'
FT_BLANK=table(['Class interval','Frequency','Percentage frequency'],[[g,'',''] for g in ['120–','130–','140–','150–','160–','170–180','Total']],fs='9.5pt',pad='.25mm 2.4mm')
CUPS=stemleaf([('4','0 1 3 5 7 9'),('5','2 5 5 7 8'),('6','2 3 3 5 7 7 9 9'),('7','3 5 6 7 8'),('8','2 4 6 7 8'),('9','3 6')],'Key: $4\\,|\\,0 = 40$')
B['9B']=[dict(n=1,skill='I can present data in a histogram.',items=[
  sa('L1',2,'The data below represents the finish times, in minutes, of $25$ competitors in a local car rally.<br>'+RALLY+'<br><b>a</b>&nbsp; Record the data in a frequency table in class intervals of $10$ minutes. Include a percentage frequency column.<br><b>b</b>&nbsp; Construct a frequency histogram.',
     [table(['Class interval','Frequency','% frequency'],[['120–','1','4'],['130–','3','12'],['140–','4','16'],['150–','8','32'],['160–','7','28'],['170–180','2','8'],['<b>Total</b>','<b>25</b>','<b>100</b>']],col=R),
      hist(['120','130','140','150','160','170','180'],[1,3,4,8,7,2],25,'Finish time (minutes)',9)],
     f'{C9}, Ch 9 review, short-answer Q11a–b (p. 712); adapted: parts a and b only','VC2M10ST05',
     blank='<div style="display:flex;gap:5mm;align-items:flex-start">'+FT_BLANK+hist([],[0]*6,25,'',9,blank=True,W=380,H=190)+'</div>')]),
 dict(n=2,skill='I can analyse data in a statistical graph.',items=[
  sa('L2',2,'For the data in the stem-and-leaf plot below showing the number of ice creams sold per day during the month of January, find:<br>'+CUPS+'<div><b>a</b>&nbsp; the range &nbsp;&nbsp;&nbsp;&nbsp; <b>b</b>&nbsp; the median</div>',
     [r'a Range $= 96 - 40 = 56$',r'b $31$ values, so the median is the $16$th value',r'Median $= 67$'],f'{O10}, Ch 10 review, short-answer Q1a–b (p. 566); adapted: parts a and b only','VC2M10ST04')])]
# ------------------------------------------------------------------ 9C
TW2=table(['','A','not A','Total'],[['<b>B</b>','','5','9'],['<b>not B</b>','8','$y$',''],['<b>Total</b>','$x$','','25']])
B['9C']=[dict(n=1,skill='I can interpret a two-way table.',items=[
  mc('L1','The values of $x$ and $y$ in the two-way table are:'+TW2,['$x = 12$, $y = 8$','$x = 12$, $y = 11$','$x = 16$, $y = 4$','$x = 10$, $y = 1$','$x = 14$, $y = 6$'],'A',
     [r'B and A: $9 - 5 = 4$, so $x = 4 + 8 = 12$',r'not B total $= 25 - 9 = 16$, so $y = 16 - 8 = 8$ (A)'],f'{C9}, Ch 9 review, multiple-choice Q2 (p. 713)','VC2M10ST05')]),
 dict(n=2,skill='I can construct a two-way table.',items=[
  sa('L2',2,'In a room there are $60$ children, each of whom is either left-handed or right-handed. There are $30$ right-handed boys, and $11$ left-handed children. There are $25$ girls among the $60$ children. Complete a two-way table to find how many left-handed girls are in the room.',
     [table(['','Left-handed','Right-handed','Total'],[['<b>Boys</b>','5','30','35'],['<b>Girls</b>','6','19','25'],['<b>Total</b>','11','49','60']],col=R),r'There are $6$ left-handed girls.'],
     f'{O10}, Exercise 11C Q18 (p. 590)','VC2M10ST05',
     blank=table(['','Left-handed','Right-handed','Total'],[['<b>Boys</b>','','',''],['<b>Girls</b>','','',''],['<b>Total</b>','','','']],fs='11pt'))])]
# ------------------------------------------------------------------ 9D
B['9D']=[dict(n=1,skill='I can find the five-figure summary and interquartile range.',items=[
  mc('L1','Consider the set of ordered data below.<br>$1.1 \\;\\; 2.3 \\;\\; 2.4 \\;\\; 2.8 \\;\\; 3.1 \\;\\; 3.4 \\;\\; 3.6$<br>$3.8 \\;\\; 3.8 \\;\\; 4.1 \\;\\; 4.5 \\;\\; 4.7 \\;\\; 4.9$<br>The interquartile range is:',['$2–5$','$1.7$','$3.8$','$1.3$','$2.1$'],'B',
     [r'$13$ values: median $= 3.6$',r'$Q_1 = \dfrac{2.4 + 2.8}{2} = 2.6$, $Q_3 = \dfrac{4.1 + 4.5}{2} = 4.3$',r'IQR $= 4.3 - 2.6 = 1.7$ (B)'],f'{C9}, Ch 9 review, multiple-choice Q9 (p. 714)','VC2M10ST04'),
  sa('L2',2,'Find the five-number summary for this ordered data set.<br>$7, 9, 11, 12, 13, 13, 18, 19, 35, 42, 45, 46, 61, 62, 78$',
     [r'$15$ values: median is the $8$th value $= 19$',r'$Q_1 = 12$ (middle of the lower $7$), $Q_3 = 46$ (middle of the upper $7$)',r'Min $= 7$, $Q_1 = 12$, median $= 19$, $Q_3 = 46$, max $= 78$'],f'{O10}, Exercise 10A Q2b (p. 504); {AD}','VC2M10ST04'),
  mc('L2','A data set has $14$ values. Which of the following is correct?',['The median and both upper and lower quartiles are values in the set.','The median is a value in the set, but the upper and lower quartiles are not.','The upper and lower quartiles are values in the set, but the median is not.','None of the median, upper or lower quartiles are values in the set.','The median and the upper quartile are values in the set, but the lower quartile is not.'],'C',
     [r'Median = average of the $7$th and $8$th values (not a value in the set)',r'Each half has $7$ values, so $Q_1$ and $Q_3$ are the $4$th value of each half (C)'],f'{O10}, Ch 10 review, multiple-choice Q1 (p. 565)','VC2M10ST04',fill=True)]),
 dict(n=2,skill='I can find any outliers in a data set.',items=[
  sa('L1',1,'The data below represents the data collected over a month of $30$ consecutive days of the delay time (in minutes) of the flight departures of the same evening flight for airline A.<br>'
     +table(None,[['2','11','6','14','18','1','7','4','12','14','9','2','13','4','19'],['13','17','3','52','24','19','12','14','0','7','13','18','1','23','8']])+'Does the data for airline A appear to have any outliers (numbers not near the majority of data elements)?',
     [r'Yes: $52$ is an outlier (the other values are all between $0$ and $24$).'],f'{C9}, Ch 9 review, extended-response Q2a (p. 715); {AD}','VC2M10ST04'),
  sa('L2',2,'Consider this data set: $2, 6, 3, 8, 9, 10, 14, 19, 4, 8, 22, 11, 13, 17, 4, 19, 7, 7, 10$.<br>Find the lower quartile, median and upper quartile, calculate the values of the lower and upper fences, and determine whether there are any outliers in this data set.',
     [r'$2, 3, 4, 4, 6, 7, 7, 8, 8, 9, 10, 10, 11, 13, 14, 17, 19, 19, 22$',r'Median $= 9$, $Q_1 = 6$, $Q_3 = 14$, IQR $= 8$',r'Lower fence $= 6 - 1.5 \times 8 = -6$, upper fence $= 14 + 1.5 \times 8 = 26$',r'No outliers.'],
     f'{O10}, Exercise 10B Q2b–d (p. 509); adapted: parts b–d combined','VC2M10ST04')])]
# ------------------------------------------------------------------ 9E
B['9E']=[dict(n=1,skill='I can construct a box plot.',items=[
  sa('L1',2,'Scott scores the following runs in each of his innings across the course of a cricket season:<br>$20 \\;\\; 5 \\;\\; 34 \\;\\; 42 \\;\\; 10 \\;\\; 3 \\;\\; 29 \\;\\; 55 \\;\\; 25 \\;\\; 37 \\;\\; 51 \\;\\; 12 \\;\\; 34 \\;\\; 22$<br>Construct a box plot to represent the data by first finding the quartiles.',
     [r'$3, 5, 10, 12, 20, 22, 25, 29, 34, 34, 37, 42, 51, 55$',r'Median $= \dfrac{25 + 29}{2} = 27$, $Q_1 = 12$, $Q_3 = 37$, IQR $= 25$; fences $-25.5$ and $74.5$: no outliers',boxplot(0,60,5,10,(3,12,27,37,55))],
     f'{C9}, Ch 9 review, short-answer Q12b (p. 713); {AD}','VC2M10ST05',blank=boxplot(0,60,5,10,(0,0,0,0,0),blank=True)),
  sa('L2',2,'Draw a box plot to represent this data set.<br>$4, 7, 1, 8, 3, 7, 6, 6, 9, 3, 5, 1, 6, 9, 7, 5, 3$',
     [r'$1, 1, 3, 3, 3, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 9, 9$',r'Median $= 6$, $Q_1 = 3$, $Q_3 = 7$, IQR $= 4$; fences $-3$ and $13$: no outliers',boxplot(0,10,1,1,(1,3,6,7,9))],
     f'{O10}, Exercise 10B Q3c (p. 509); {AD}','VC2M10ST05',blank=boxplot(0,10,1,1,(0,0,0,0,0),blank=True)),
  mc('L1','Choose the incorrect statement about the box plot below.'+boxplot(20,64,2,6,(24,36,42,51,60),col='#000',lab0=24,lab1=60).replace('class="fig"','class="qf"').replace(' x="',' x="',1),
     ['The range is $36$.','Fifty per cent of values are between $36$ and $51$.','The median is $42$.','Twenty-five per cent of values are below $36$.','The interquartile range is $20$.'],'E',
     [r'IQR $= 51 - 36 = 15$, not $20$ (E)'],f'{C9}, Ch 9 review, multiple-choice Q10 (p. 714)','VC2M10ST05',fill=True)])]

for sub,skills in B.items():
    json.dump(dict(card='C10-'+sub,levels=LV,skills=skills),open(os.path.join(HERE,f'C10-{sub}.json'),'w'),indent=1,ensure_ascii=False)
    print('wrote',sub,sum(len(s['items']) for s in skills),'items')
