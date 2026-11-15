r"""Chapter 9 (C10) slide content: 9A, 9B (sample for the new 'New learning' slides).
Same conventions as ch1_data.py. Worked examples = the book's SOLUTION; You try = teacher working in the same
steps, answers checked against the book's Now you try answers (p. 1070). APK + exit-task working = teacher.
'learn' = list of New learning slides (HTML) inserted after Key ideas: animated / interactive, built only from the
book's Key ideas, Building understanding and Lesson starter content (cited on each slide)."""
RED='#d00000'
def hist(groups,freqs,total,xlabel,pct=True,W=360,H=210,col='#d00000',ymax=None):
    """histogram with frequency (left) and percentage frequency (right) axes; groups = boundary labels"""
    n=len(freqs);ymax=ymax or max(freqs)+1;L,R,T,B=40,40 if pct else 10,12,36;w=(W-L-R)/n;h=H-T-B;y=lambda f:T+h-f/ymax*h
    o=[f'<line x1="{L}" y1="{T+h}" x2="{W-R}" y2="{T+h}" stroke="#000" stroke-width="1.5"/><line x1="{L}" y1="{T-4}" x2="{L}" y2="{T+h}" stroke="#000" stroke-width="1.5"/>']
    if pct:o.append(f'<line x1="{W-R}" y1="{T-4}" x2="{W-R}" y2="{T+h}" stroke="#000" stroke-width="1.5"/>')
    for k in range(ymax+1):
        o.append(f'<line x1="{L-4}" y1="{y(k)}" x2="{L}" y2="{y(k)}" stroke="#000"/><text x="{L-7}" y="{y(k)+4}" font-size="12" text-anchor="end">{k}</text>')
        if pct:
            v=k/total*100;o.append(f'<line x1="{W-R}" y1="{y(k)}" x2="{W-R+4}" y2="{y(k)}" stroke="#000"/><text x="{W-R+7}" y="{y(k)+4}" font-size="11">{v:g}</text>' if (v*100)%100==0 or total in (20,10) else '')
    for i,f in enumerate(freqs):
        if f:o.append(f'<rect x="{L+i*w}" y="{y(f)}" width="{w}" height="{h-(y(f)-T)}" fill="{col}" fill-opacity=".25" stroke="{col}" stroke-width="1.6"/>')
    for i,g in enumerate(groups):o.append(f'<text x="{L+i*w}" y="{T+h+16}" font-size="12" text-anchor="middle">{g}</text>')
    o.append(f'<text x="{(L+W-R)/2}" y="{H-3}" font-size="13" text-anchor="middle">{xlabel}</text>')
    o.append(f'<text x="12" y="{T+h/2}" font-size="12" text-anchor="middle" transform="rotate(-90 12 {T+h/2})">Frequency</text>')
    if pct:o.append(f'<text x="{W-6}" y="{T+h/2}" font-size="12" text-anchor="middle" transform="rotate(90 {W-6} {T+h/2})">% frequency</text>')
    return f'<svg class="fig" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(o)}</svg>'
def colgraph(cats,freqs,xlabel,W=300,H=190,col=RED):
    n=len(cats);ymax=max(freqs)+1;L,T,B=34,10,36;w=(W-L-10)/n;h=H-T-B;y=lambda f:T+h-f/ymax*h
    o=[f'<line x1="{L}" y1="{T+h}" x2="{W-10}" y2="{T+h}" stroke="#000" stroke-width="1.5"/><line x1="{L}" y1="{T-4}" x2="{L}" y2="{T+h}" stroke="#000" stroke-width="1.5"/>']
    for k in range(ymax+1):o.append(f'<line x1="{L-4}" y1="{y(k)}" x2="{L}" y2="{y(k)}" stroke="#000"/><text x="{L-7}" y="{y(k)+4}" font-size="12" text-anchor="end">{k}</text>')
    for i,(c,f) in enumerate(zip(cats,freqs)):
        o.append(f'<rect x="{L+i*w+w*.2}" y="{y(f)}" width="{w*.6}" height="{T+h-y(f)}" fill="{col}" fill-opacity=".25" stroke="{col}" stroke-width="1.6"/><text x="{L+i*w+w/2}" y="{T+h+15}" font-size="12" text-anchor="middle">{c}</text>')
    o.append(f'<text x="{(L+W)/2}" y="{H-3}" font-size="13" text-anchor="middle">{xlabel}</text><text x="11" y="{T+h/2}" font-size="12" text-anchor="middle" transform="rotate(-90 11 {T+h/2})">Frequency</text>')
    return f'<svg class="fig" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(o)}</svg>'
def dotplot(cats,freqs,xlabel,W=260,H=130,col=RED):
    n=len(cats);L=20;w=(W-2*L)/n;base=H-34
    o=[f'<line x1="{L-6}" y1="{base}" x2="{W-L+6}" y2="{base}" stroke="#000" stroke-width="1.5"/>']
    for i,(c,f) in enumerate(zip(cats,freqs)):
        x=L+i*w+w/2;o.append(f'<text x="{x}" y="{base+16}" font-size="12" text-anchor="middle">{c}</text>')
        for k in range(f):o.append(f'<circle cx="{x}" cy="{base-9-k*15}" r="5.5" fill="{col}"/>')
    o.append(f'<text x="{W/2}" y="{H-3}" font-size="13" text-anchor="middle">{xlabel}</text>')
    return f'<svg class="fig" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(o)}</svg>'
def stemleaf(rows,key,col=RED):
    td='padding:1px 12px'
    b=''.join(f'<tr><td style="{td};border-right:2px solid {col};text-align:right">{s}</td><td style="{td};word-spacing:10px">{l}</td></tr>' for s,l in rows)
    return (f'!<table style="border-collapse:collapse;color:{col};font-size:.9em"><tr><th style="{td};border-right:2px solid {col};border-bottom:2px solid {col}">Stem</th>'
            f'<th style="{td};border-bottom:2px solid {col};text-align:left">Leaf</th></tr>{b}</table><div style="font-size:.75em;color:{col}">{key}</div>')
def ftable(rows,col=RED):
    td=f'border:1.5px solid {col};padding:1px 10px;text-align:center'
    h=''.join(f'<th style="{td};font-size:.75em">{x}</th>' for x in ('Class interval','Frequency','% frequency'))
    return '!<table style="border-collapse:collapse;color:%s;font-size:.85em"><tr>%s</tr>%s</table>'%(col,h,''.join('<tr>'+''.join(f'<td style="{td}">{x}</td>' for x in r)+'</tr>' for r in rows))

S={}
# ======================================================================== 9A
KI_TYPES=r"<b>Categorical</b>: nominal (no order) or ordinal (can be ordered).<br><b>Numerical</b>: discrete (limited number of values) or continuous (any value in a given range)."
KI_SAMPLE=r"A <b>sample</b> is a group chosen from a <b>population</b>. Information from a sample is used to describe the whole population, so it is important to choose the sample carefully."
S['9A']=dict(
 apk=[dict(q=r'Decide whether a primary or secondary source is suitable for an economist collecting data on the average income of Australian households, and suggest a method for its collection.',
           w=['!<span class="tx">Secondary source (data already collected by someone else).</span>','!<span class="tx">Method: e.g. use the Australian Bureau of Statistics census data on household income.</span>']),
      dict(q=r'In conducting a survey to determine how many children adults generally have, explain why randomly selecting people outside a childcare centre is likely to lead to bias.',
           w=['!<span class="tx">People outside a childcare centre are very likely to have young children.</span>','*!<span class="tx">Adults with no children (or grown-up children) are left out, so the sample over-represents parents.</span>']),
      dict(q=r'One hundred people at the airport are surveyed about how often they travel.<br>This data is used to make conclusions about that city and how often people travel.<br>Do you think this survey will contain bias? If so, explain why.',
           w=['*!<span class="tx">Yes.</span>','!<span class="tx">People at an airport are travelling, so they are likely to travel more often than a typical person in the city.</span>'])],
 ex=[dict(n=1,page=768,kp='p. 767',instr='What type of data would the following survey questions generate?',ki=KI_TYPES,
          parts=[('a','!How many televisions do you have in your home?',['*!<span class="tx">Numerical and discrete</span>']),('b','!To what type of music do you most like to listen?',['*!<span class="tx">Categorical and nominal</span>'])],
          yt=[('a','!How tall are the students in Year 10?',['!<span class="tx">The answer is a measurement that can take any value in a range.</span>','*!<span class="tx">Numerical and continuous</span>']),
              ('b','!What is your level of satisfaction (low, medium and high) with a meal at a restaurant?',['!<span class="tx">The answer is a category, and the categories can be ordered.</span>','*!<span class="tx">Categorical and ordinal</span>'])]),
     dict(n=2,page=769,kp='p. 767',instr='A survey is carried out on the internet to determine Australia’s favourite musical performer. Why will this sample not necessarily be representative of Australia’s views?',
          yinstr='A survey is carried out in a library to determine typical study habits of Year 12 students. Why will this sample not necessarily be representative of all Year 12 students?',ki=KI_SAMPLE,
          parts=[('','',['*!<span class="tx">An internet survey is restricted to people with a computer and internet access, ruling out some sections of the community from participating in the survey.</span>'])],
          yt=[('','',['!<span class="tx">A library survey only reaches students who study in the library.</span>','*!<span class="tx">Students who study in the library may not reflect a typical group of Year 12 students.</span>'])])],
 exit=[dict(q=r'What type of data would the survey question ‘How many pairs of shoes do you own?’ generate?',w=['!<span class="tx">The answer is a whole number with a limited number of values.</span>','*!<span class="tx">Numerical and discrete</span>']),
       dict(q=r'A survey is carried out by calling people listed in the phone book to determine their voting preferences for a state election. Why will this sample not necessarily be representative of the state’s views?',
            w=['*!<span class="tx">Only people with a phone number listed in the phone book can be included.</span>','!<span class="tx">People with only a mobile, or an unlisted number, are left out, so some sections of the community are missed.</span>'])],
 learn=['types','sample'],
)
# ======================================================================== 9B
KI_HIST=r"Histograms are used for grouped numerical data. The interval $10–$ includes all numbers from $10$ (including $10$) to fewer than $20$.<div class='kf'>% frequency $= \dfrac{\text{frequency}}{\text{total}} \times 100$</div>"
KI_CENTRE=r"<b>mean</b> $\bar{x} = \dfrac{\text{sum of all data values}}{\text{number of data values}}$<br><b>median</b>: the middle value when data are placed in order<br><b>mode</b>: the value that occurs most frequently"
ICE='<table class="tv" style="margin:4px 0;font-size:14px;color:#000">'+''.join('<tr>'+''.join(f'<td style="border-color:#000;padding:0 5px">{x}</td>' for x in r.split())+'</tr>' for r in ['15 22 1 0 20 3 10 2 23 3 11 14 19 3','16 14 24 7 1 15 5 7 2 29 28 3 2 13','26 20 22 25 6 7 12 6 13 7 7 20 11 11'])+'</table>'
G10=['0','10','20','30','40','50']
S['9B']=dict(
 apk=[dict(q=r'Represent this set of data as a stem-and-leaf plot: $23, 10, 36, 25, 31, 34, 34, 27, 36, 37, 16, 33$.',
           w=[stemleaf([('1','0 6'),('2','3 5 7'),('3','1 3 4 4 6 6 7')],'2 | 3 means 23')]),
      dict(q=r'Represent the table at right as a frequency graph and as a dot plot.<table class="tv" style="margin-top:6px;font-size:17px;color:#000"><tr><td style="border-color:#000">Number of siblings</td><td style="border-color:#000">0</td><td style="border-color:#000">1</td><td style="border-color:#000">2</td><td style="border-color:#000">3</td></tr><tr><td style="border-color:#000">Frequency</td><td style="border-color:#000">3</td><td style="border-color:#000">4</td><td style="border-color:#000">2</td><td style="border-color:#000">1</td></tr></table>',
           w=[colgraph(['0','1','2','3'],[3,4,2,1],'Number of siblings',W=250,H=160),dotplot(['0','1','2','3'],[3,4,2,1],'Number of siblings',W=220,H=110)]),
      dict(q=r'For the data below showing the ice-cream sales each hour of operation over a week, set up and complete a grouped frequency table using class intervals 0–4, 5–9, etc.'+ICE+r'From the table, construct a frequency histogram and state for how many hours there were sales of $15$ or more ice-creams.',
           w=['!<span class="tx">0–4: 10 &nbsp; 5–9: 8 &nbsp; 10–14: 9 &nbsp; 15–19: 4 &nbsp; 20–24: 7 &nbsp; 25–29: 4</span>',hist(['0','5','10','15','20','25','30'],[10,8,9,4,7,4],42,'Ice-creams sold per hour',pct=False,W=300,H=170,ymax=10),'*!$4 + 7 + 4 = 15$ hours'])],
 ex=[dict(n=3,page=774,kp='p. 773',instr='Twenty people were surveyed to find out how many times they use the internet in a week. The raw data are listed.<br>$21, 19, 5, 10, 15, 18, 31, 40, 32, 25$<br>$11, 28, 31, 29, 16, 2, 13, 33, 14, 24$',
          yinstr='Sixteen people were surveyed to find out how many phone texts they send in one day. The raw data are as follows.<br>$10, 7, 2, 5, 22, 14, 7, 9, 11, 29, 32, 18, 5, 24, 12, 14$',ki=KI_HIST,
          parts=[('a','!Organise the data into a frequency table using class intervals of $10$. Include a percentage frequency column.',[ftable([['0–','2','10'],['10–','8','40'],['20–','5','25'],['30–','4','20'],['40–50','1','5'],['<b>Total</b>','<b>20</b>','<b>100</b>']])]),
                 ('b','!Construct a histogram for the data, showing both the frequency and percentage frequency on the one graph.',[hist(G10,[2,8,5,4,1],20,'Number of times the internet is accessed',W=440,H=270,ymax=10)]),
                 ('c','!Describe the data in the histogram as symmetrical, positively skewed or negatively skewed.',['*!<span class="tx">Positively skewed</span>','!<span class="tx">The tail of the data is to the right.</span>'])],
          yt=[('a','!Organise the data into a frequency table using class intervals of $10$. Include a percentage frequency column.',[ftable([['0–','6','37.5'],['10–','6','37.5'],['20–','3','18.75'],['30–40','1','6.25'],['<b>Total</b>','<b>16</b>','<b>100</b>']])]),
              ('b','!Construct a histogram for the data, showing both the frequency and percentage frequency on the one graph.',[hist(['0','10','20','30','40'],[6,6,3,1],16,'Number of phone texts',W=440,H=270,ymax=8)]),
              ('c','!Describe the data in the histogram as symmetrical, positively skewed or negatively skewed.',['*!<span class="tx">Positively skewed</span>','!<span class="tx">The tail of the data is to the right.</span>'])]),
     dict(n=4,page=776,kp='p. 773',instr='Twelve test marks for Rolle in a semester are given as percentages in the raw data below: &nbsp;$66 \\;\\; 74 \\;\\; 81 \\;\\; 68 \\;\\; 94 \\;\\; 88 \\;\\; 74 \\;\\; 85 \\;\\; 90 \\;\\; 72 \\;\\; 79 \\;\\; 86$',
          yinstr='Payments from Lucy’s last twelve babysitting jobs are given below. &nbsp;<span class="nomath">$</span>36 <span class="nomath">$</span>48 <span class="nomath">$</span>44 <span class="nomath">$</span>62 <span class="nomath">$</span>56 <span class="nomath">$</span>58 <span class="nomath">$</span>52 <span class="nomath">$</span>39 <span class="nomath">$</span>56 <span class="nomath">$</span>38 <span class="nomath">$</span>60 <span class="nomath">$</span>45',ki=KI_CENTRE,
          parts=[('a','!Construct a stem-and-leaf plot for the data.',[stemleaf([('6','6 8'),('7','2 4 4 9'),('8','1 5 6 8'),('9','0 4')],'8 | 4 means 84%')]),
                 ('b','!Use your stem-and-leaf plot to find: <b>i</b> the mode <b>ii</b> the median <b>iii</b> the mean.',[r'\text{i Mode is } 74\%',r'\text{ii Median} = \dfrac{79 + 81}{2} = 80\%',r'\text{iii Mean} = \dfrac{66 + 68 + \dots + 94}{12}',r'*= 79.75\%'])],
          yt=[('a','!Construct a stem-and-leaf plot for the data.',[stemleaf([('3','6 8 9'),('4','4 5 8'),('5','2 6 6 8'),('6','0 2')],'5 | 2 means <span class="nomath">$</span>52')]),
              ('b','!Use your stem-and-leaf plot to find: <b>i</b> the mode <b>ii</b> the median <b>iii</b> the mean.',[r'\text{i Mode is } \$56',r'\text{ii Median} = \dfrac{48 + 52}{2} = \$50',r'\text{iii Mean} = \dfrac{36 + 38 + \dots + 62}{12}',r'*= \$49.50'])])],
 exit=[dict(q=r'Fifteen people were surveyed to find out how many hours they spend on the internet in a week. The data are: $7, 12, 14, 20, 2, 26, 8, 11, 17, 12, 21, 5, 6, 18, 14$. Construct a histogram for the data using class intervals of $5$, showing both the frequency and percentage frequency on the one graph. Is the data symmetrical, positively skewed or negatively skewed?',
            w=[hist(['0','5','10','15','20','25','30'],[1,4,5,2,2,1],15,'Hours on the internet',W=300,H=175,ymax=6),'*!<span class="tx">Positively skewed (tail to the right)</span>']),
       dict(q=r'For the stem-and-leaf plot shown below, find the mean correct to one decimal place, the median and the mode.'+stemleaf([('0','2 5 7'),('1','1 1 4 6'),('2','0 3 9'),('3','2 5')],'2 | 3 means 23',col='#000')[1:],
            w=[r'\text{Mean} = \dfrac{205}{12} \approx 17.1',r'\text{Median} = \dfrac{14 + 16}{2} = 15',r'*\text{Mode} = 11'])],
 learn=['hist','shape','stem'],
)
