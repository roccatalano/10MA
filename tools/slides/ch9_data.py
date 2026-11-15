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

# ---------------------------------------------------------------- helpers for 9C–9E
def tw(cols,rows,col='#000',bold_last=True,fs=15):
    td=f'border:1.5px solid {col};padding:2px 8px;text-align:center'
    h=''.join(f'<th style="{td};font-size:{fs-2}px;background:#f2f2f2">{x}</th>' for x in ['']+cols)
    b=''.join('<tr>'+''.join(f'<td style="{td}{";text-align:left;font-weight:bold" if k==0 else ""}">{x}</td>' for k,x in enumerate(r))+'</tr>' for r in rows)
    return f'<table style="border-collapse:collapse;color:{col};font-size:{fs}px;margin:4px 0">{"<tr>"+h+"</tr>"}{b}</table>'
def boxplot(a,b,step,lab,five,out=(),label='',W=360,col=RED,box_y=26):
    mn,q1,q2,q3,mx=five;n=round((b-a)/step);L=16;u=(W-2*L)/n;x=lambda v:L+(v-a)/step*u
    o=[f'<line x1="4" y1="64" x2="{W-4}" y2="64" stroke="#000" stroke-width="1.4"/><path d="M{W-2} 64 l-7 -3.5 v7z"/><path d="M2 64 l7 -3.5 v7z"/>']
    for k in range(n+1):
        v=a+k*step;o.append(f'<line x1="{x(v):.1f}" y1="61" x2="{x(v):.1f}" y2="67" stroke="#000"/>')
        if abs(((v-a)/lab)-round((v-a)/lab))<1e-6:o.append(f'<text x="{x(v):.1f}" y="80" font-size="12" text-anchor="middle">{v:g}</text>')
    o.append(f'<line x1="{x(mn)}" y1="{box_y}" x2="{x(q1)}" y2="{box_y}" stroke="{col}" stroke-width="2"/><rect x="{x(q1)}" y="{box_y-14}" width="{x(q3)-x(q1)}" height="28" fill="{col}" fill-opacity=".12" stroke="{col}" stroke-width="2"/>'
             f'<line x1="{x(q2)}" y1="{box_y-14}" x2="{x(q2)}" y2="{box_y+14}" stroke="{col}" stroke-width="2"/><line x1="{x(q3)}" y1="{box_y}" x2="{x(mx)}" y2="{box_y}" stroke="{col}" stroke-width="2"/>'
             f'<line x1="{x(mn)}" y1="{box_y-7}" x2="{x(mn)}" y2="{box_y+7}" stroke="{col}" stroke-width="2"/><line x1="{x(mx)}" y1="{box_y-7}" x2="{x(mx)}" y2="{box_y+7}" stroke="{col}" stroke-width="2"/>')
    for v in out:o.append(f'<circle cx="{x(v)}" cy="{box_y}" r="4.5" fill="{col}"/>')
    if label:o.append(f'<text x="{W/2}" y="96" font-size="12" text-anchor="middle">{label}</text>')
    return f'<svg class="fig" width="{W}" height="{100 if label else 86}" viewBox="0 0 {W} {100 if label else 86}">{"".join(o)}</svg>'
LIK=['Strongly agree','Agree','Neutral','Disagree','Strongly disagree','Total']
T5=tw(LIK,[['$40$ and over','2','7','10','5','0','24'],['Under $40$','0','1','6','12','7','26'],['Total','2','8','16','17','7','50']],fs=14)
T5y=tw(LIK,[['Public','1','2','4','2','1','10'],['Private','0','2','6','1','1','10'],['Total','1','4','10','3','2','20']],fs=14)
# ======================================================================== 9C
KI_TW=r"A <b>two-way table</b> compares two related categorical variables. The entries are totalled both vertically and horizontally.<div class='kf'>% $= \dfrac{\text{frequency}}{\text{total}} \times 100$</div>"
S['9C']=dict(
 apk=[dict(q=r'Write the proportion <span class="nomath">$</span>40 out of <span class="nomath">$</span>200 as a fraction, a decimal and a percentage.',w=[r'\dfrac{40}{200} = \dfrac{1}{5}','= 0.2',r'= 20\%']),
      dict(q=r'Of $50$ people it was found that $20$ people liked both coffee and tea, $15$ liked coffee but not tea and $10$ people liked tea but not coffee. Draw a two-way table of this situation.',
           w=['!'+tw(['Tea','Not tea','Total'],[['Coffee','20','15','35'],['Not coffee','10','5','15'],['Total','30','20','50']],col=RED),'*!<span class="tx">Neither: $50 - 20 - 15 - 10 = 5$</span>']),
      dict(q=r'On a particular day at a car service station, $20$ cars are serviced: $12$ cars need a wheel alignment, $10$ cars need their brake fluid replaced and $4$ require both. Illustrate the situation using a two-way table. Use the table to find how many cars require neither, and the probability that a randomly selected car needs only a wheel alignment.',
           w=['!'+tw(['Brake fluid','No brake fluid','Total'],[['Wheel alignment','4','8','12'],['No wheel alignment','6','2','8'],['Total','10','10','20']],col=RED),'*!<span class="tx">Neither: $2$ cars &nbsp; Only wheel alignment: $\\dfrac{8}{20} = \\dfrac{2}{5}$</span>'])],
 ex=[dict(n=5,page=783,kp='p. 781',instr='This two-way table summarises data collected from a survey using a 5-point Likert scale. The survey asked $50$ people if they are over or under the age of $40$ and to what degree they agree with the idea to reduce the driving blood alcohol limit from $0.05$ to $0.04$.'+T5,
          yinstr='This two-way table summarises data collected from a survey using a 5-point Likert scale. The survey asked $20$ teachers if they thought there was enough time in the day to prepare for classes. Some teachers were from public schools and some were from private schools.'+T5y,ki=KI_TW,
          parts=[('a','!State how many of the people surveyed: <b>i</b> were $40$ years of age or over <b>ii</b> strongly agree with the idea <b>iii</b> were $40$ years of age or over and responded Agree to the question <b>iv</b> were under $40$ and responded Disagree to the question.',[r'\text{i } 24',r'\text{ii } 2',r'\text{iii } 7',r'*\text{iv } 12']),
                 ('b','!What percentage of the people surveyed: <b>i</b> were under $40$ years of age? <b>ii</b> were neutral to the idea? <b>iii</b> were under $40$ years of age and responded Strongly Disagree with the idea? <b>iv</b> were $40$ years of age or over and responded Neutral to the idea?',[r'\text{i } 52\%',r'\text{ii } 32\%',r'\text{iii } 14\%',r'*\text{iv } 20\%']),
                 ('c','!Would you say that this data supports the notion that younger people would prefer a lower driving blood alcohol limit? Give a reason.',['*!<span class="tx">No. A greater proportion of the people under 40 disagree with the idea.</span>'])],
          yt=[('a','!State how many of the teachers surveyed: <b>i</b> were from public schools <b>ii</b> responded Agree to the question <b>iii</b> were from public schools and responded Agree to the question <b>iv</b> were from private schools and responded Disagree to the question.',[r'\text{i } 10',r'\text{ii } 4',r'\text{iii } 2',r'*\text{iv } 1']),
              ('b','!What percentage of the teachers surveyed: <b>i</b> were from private schools? <b>ii</b> were neutral to the question? <b>iii</b> were from private schools and responded Neutral to the question? <b>iv</b> were from public schools and responded Disagree to the question?',[r'\text{i } \tfrac{10}{20} \times 100 = 50\%',r'\text{ii } \tfrac{10}{20} \times 100 = 50\%',r'\text{iii } \tfrac{6}{20} \times 100 = 30\%',r'*\text{iv } \tfrac{2}{20} \times 100 = 10\%']),
              ('c','!Would you say that this data supports the notion that teachers from public schools feel that there is enough time in the day to prepare for classes compared to private school teachers? Give a reason.',['*!<span class="tx">No. There is not a significant difference in the way teachers from the different types of schools responded to the question.</span>'])]),
     dict(n=6,page=784,kp='p. 781',instr='A number of people were surveyed to see if they owned a beach house. They were also asked as to whether they were over $60$ years of age. $15$ of the $25$ people $60$ years of age and over said that they owned a beach house and $6$ of the $15$ people under $60$ years of age said that they owned a beach house.',
          yinstr='A number of city and country dogs were checked to see if they were of pure or mixed breed. $18$ of the $30$ country dogs were of pure breed and $13$ of the $20$ city dogs were of mixed breed.',ki=KI_TW,
          parts=[('a','!Represent this information in a two-way table.',['!'+tw(['Beach house','No beach house','Total'],[['$60$ and over','15','10','25'],['Under $60$','6','9','15'],['Total','21','19','40']],col=RED)]),
                 ('b','!What fraction of the people surveyed: <b>i</b> were under $60$ years of age? <b>ii</b> were under $60$ years of age and owned a beach house?',[r'\text{i } \dfrac{15}{40} = \dfrac{3}{8}',r'*\text{ii } \dfrac{6}{40} = \dfrac{3}{20}']),
                 ('c','!Would you say that this data supports the notion that older people are more likely to own a beach house? Give a reason.',['*!<span class="tx">Yes. A much larger proportion of the people over 60 years of age own a beach house.</span>'])],
          yt=[('a','!Represent this information in a two-way table.',['!'+tw(['Pure','Mixed','Total'],[['Country','18','12','30'],['City','7','13','20'],['Total','25','25','50']],col=RED)]),
              ('b','!What fraction of the dogs surveyed: <b>i</b> were from the city? <b>ii</b> were from the city and of pure breed?',[r'\text{i } \dfrac{20}{50} = \dfrac{2}{5}',r'*\text{ii } \dfrac{7}{50}']),
              ('c','!Would you say that this data supports the notion that country dogs are more likely to be of mixed breed? Give a reason.',['*!<span class="tx">No. The proportion of mixed breed dogs is higher for the city.</span>'])])],
 exit=[dict(q=r'This two-way table summarises data from a survey of $40$ people using a 5-point Likert scale. The survey asked if they live in Australia or live overseas and are visiting and to what degree they thought Australians were friendly.'+tw(LIK,[['Aus','2','4','6','3','3','18'],['Overseas','8','8','2','3','1','22'],['Total','10','12','8','6','4','40']],fs=12)+r'<b>i</b> State how many people surveyed were from Australia and responded Agree. <b>ii</b> Do you think that the data supports the notion that overseas visitors think Australians are more friendly? Give a reason.',
            w=[r'\text{i } 4','*!<span class="tx">ii Yes. $\\tfrac{16}{22} \\approx 73\\%$ of overseas visitors agree or strongly agree, compared with $\\tfrac{6}{18} \\approx 33\\%$ of Australians.</span>']),
       dict(q=r'A number of people were surveyed to see if they had a mortgage. They were also asked whether they were under or over $50$ years of age. $11$ of the $15$ people under $50$ had a mortgage and $5$ of the $10$ people $50$ or over had a mortgage. Represent the information in a two-way table and find what fraction of people surveyed were $50$ or over and had a mortgage.',
            w=['!'+tw(['Mortgage','No mortgage','Total'],[['Under $50$','11','4','15'],['$50$ or over','5','5','10'],['Total','16','9','25']],col=RED),r'*\dfrac{5}{25} = \dfrac{1}{5}'])],
 learn=['tw_read','tw_build'],
)
# ======================================================================== 9D
KI_5=r"<b>Five-figure summary</b>: min, $Q_1$, median $(Q_2)$, $Q_3$, max.<div class='kf'>$\text{IQR} = Q_3 - Q_1$</div><div class='kn'>Leave the median out of the halves when there is an odd number of values.</div>"
KI_OUT=r"A data point is an <b>outlier</b> when it is below the lower fence or above the upper fence.<div class='kf'>$Q_1 - 1.5 \times \text{IQR}$ &emsp; $Q_3 + 1.5 \times \text{IQR}$</div>"
S['9D']=dict(
 apk=[dict(q=r'Find the median of $15, 31, 12, 47, 21, 65, 12, 29$.',w=['12, 12, 15, 21, 29, 31, 47, 65',r'\text{Median} = \dfrac{21 + 29}{2}','= 25']),
      dict(q=r'Find the IQR of $1, 15, 8, 2, 13, 10, 4, 14$.',w=['1, 2, 4, 8, 10, 13, 14, 15',r'Q_1 = \dfrac{2 + 4}{2} = 3,\ Q_3 = \dfrac{13 + 14}{2} = 13.5',r'\text{IQR} = 13.5 - 3 = 10.5']),
      dict(q=r'List the data below in order from smallest to largest and find the median $(Q_2)$, the lower quartile $(Q_1)$, the upper quartile $(Q_3)$ and the interquartile range (IQR). Interpret the IQR.<br>$12 \;\; 21 \;\; 18 \;\; 8 \;\; 4 \;\; 16 \;\; 24 \;\; 11 \;\; 27 \;\; 10$',
           w=['4, 8, 10, 11, 12, 16, 18, 21, 24, 27',r'Q_2 = \dfrac{12 + 16}{2} = 14,\ Q_1 = 10,\ Q_3 = 21',r'\text{IQR} = 21 - 10 = 11','*!<span class="tx">The middle 50% of the data are spread over 11.</span>'])],
 ex=[dict(n=7,page=791,kp='p. 790',instr='Determine the range and IQR for these data sets by finding the five-figure summary.',ki=KI_5,
          parts=[('a','2, 2, 4, 5, 6, 8, 10, 13, 16, 20',[r'\text{Range} = 20 - 2 = 18',r'Q_2 = 7,\ \text{so } Q_1 = 4 \text{ and } Q_3 = 13',r'\text{IQR} = 13 - 4','= 9']),
                 ('b','1.6, 1.7, 1.9, 2.0, 2.1, 2.4, 2.4, 2.7, 2.9',[r'\text{Range} = 2.9 - 1.6 = 1.3',r'Q_1 = \dfrac{1.7 + 1.9}{2} = 1.8',r'Q_3 = \dfrac{2.4 + 2.7}{2} = 2.55',r'\text{IQR} = 2.55 - 1.8','= 0.75'])],
          yt=[('a','3, 5, 5, 6, 7, 9, 10, 12',[r'\text{Range} = 12 - 3 = 9',r'Q_2 = 6.5,\ \text{so } Q_1 = 5 \text{ and } Q_3 = 9.5',r'\text{IQR} = 9.5 - 5','= 4.5']),
              ('b','3.8, 3.9, 4.0, 4.2, 4.5, 4.5, 4.7',[r'\text{Range} = 4.7 - 3.8 = 0.9',r'Q_1 = 3.9',r'Q_3 = 4.5',r'\text{IQR} = 4.5 - 3.9','= 0.6'])]),
     dict(n=8,page=792,kp='p. 790',instr='The following data set represents the number of flying geese spotted on each day of a $13$-day tour of England. &nbsp;$5, 1, 2, 6, 3, 3, 18, 4, 4, 1, 7, 2, 4$',
          yinstr='The following data set represents the number of people on $11$ buses in a local area. &nbsp;$36, 24, 15, 23, 26, 0, 19, 24, 26, 33, 19$',ki=KI_OUT,
          parts=[('a','!For the data, find: <b>i</b> the min and max <b>ii</b> the median <b>iii</b> the upper and lower quartiles <b>iv</b> the IQR <b>v</b> any outliers by determining the lower and upper fences.',
                  [r'\text{i Min} = 1,\ \text{max} = 18',r'\text{ii } 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 6, 7, 18 \;\therefore\ \text{Median} = 4',r'\text{iii Lower quartile} = \dfrac{2 + 2}{2} = 2,\ \text{Upper quartile} = \dfrac{5 + 6}{2} = 5.5',r'\text{iv IQR} = 5.5 - 2 = 3.5',r'\text{v Lower fence} = 2 - 1.5 \times 3.5 = -3.25',r'\text{Upper fence} = 5.5 + 1.5 \times 3.5 = 10.75',r'*\therefore \text{The outlier is } 18.']),
                 ('b','!Can you give a possible reason for why the outlier occurred?',['*!<span class="tx">Perhaps a flock of geese was spotted that day.</span>'])],
          yt=[('a','!For the data, find: <b>i</b> the min and max <b>ii</b> the median <b>iii</b> the upper and lower quartiles <b>iv</b> the IQR <b>v</b> any outliers by determining the lower and upper fences.',
               [r'\text{i Min} = 0,\ \text{max} = 36',r'\text{ii } 0, 15, 19, 19, 23, 24, 24, 26, 26, 33, 36 \;\therefore\ \text{Median} = 24',r'\text{iii Lower quartile} = 19,\ \text{Upper quartile} = 26',r'\text{iv IQR} = 26 - 19 = 7',r'\text{v Lower fence} = 19 - 1.5 \times 7 = 8.5',r'\text{Upper fence} = 26 + 1.5 \times 7 = 36.5',r'*\therefore \text{The outlier is } 0.']),
              ('b','!Can you give a possible reason for why the outlier occurred?',['*!<span class="tx">Perhaps the bus was not taking passengers.</span>'])])],
 exit=[dict(q=r'For the data set below find the minimum, maximum, median, upper and lower quartiles and the range and IQR.<br>$7, 10, 12, 12, 14, 18, 22, 25, 26, 30$',
            w=[r'\text{Min} = 7,\ \text{max} = 30',r'\text{Median} = \dfrac{14 + 18}{2} = 16',r'Q_1 = 12,\ Q_3 = 25',r'\text{Range} = 30 - 7 = 23',r'*\text{IQR} = 25 - 12 = 13']),
       dict(q=r'The following data represent the number of aces by a tennis player in $11$ grand slam matches for the year:<br>$15, 12, 22, 2, 10, 18, 16, 14, 15, 20, 16$<br>For the data find the upper and lower quartiles and use these to help determine if there are any outliers.',
            w=['2, 10, 12, 14, 15, 15, 16, 16, 18, 20, 22',r'Q_1 = 12,\ Q_3 = 18,\ \text{IQR} = 6',r'12 - 1.5 \times 6 = 3,\ \ 18 + 1.5 \times 6 = 27',r'*\therefore \text{The outlier is } 2.'])],
 learn=['five','fence'],
)
# ======================================================================== 9E
KI_BOX=r"A <b>box plot</b> shows min, $Q_1$, $Q_2$, $Q_3$, max. An outlier is marked with a dot $(\bullet)$; the whiskers stretch to the lowest and highest values that are not outliers.<div class='kf'>outlier: $< Q_1 - 1.5 \times \text{IQR}$ or $> Q_3 + 1.5 \times \text{IQR}$</div>"
S['9E']=dict(
 apk=[dict(q=r'Find the IQR of $1, 15, 8, 2, 13, 10, 4, 14$.',w=['1, 2, 4, 8, 10, 13, 14, 15',r'Q_1 = 3,\ Q_3 = 13.5',r'\text{IQR} = 10.5']),
      dict(q=r'This box plot summarises the test results $(\%)$ of a class of students.'+boxplot(40,100,5,10,(45,60,70,90,95),label='Score (%)',W=330,col='#000')+r'<b>i</b> Find the range and interquartile range of the results. <b>ii</b> Twenty-five per cent of results were above what number? <b>iii</b> If there were $24$ students in the class, how many scored above $70\%$?',
           w=[r'\text{i Range} = 95 - 45 = 50,\ \text{IQR} = 90 - 60 = 30',r'\text{ii } 90',r'*\text{iii } \tfrac{1}{2} \times 24 = 12']),
      dict(q=r'For the data shown below, find the minimum and maximum values, the median and lower and upper quartiles and draw a box plot to represent the data.<br>$18 \;\; 15 \;\; 13 \;\; 14 \;\; 21 \;\; 25 \;\; 17 \;\; 11 \;\; 15 \;\; 16 \;\; 18 \;\; 20 \;\; 24 \;\; 19$',
           w=['11, 13, 14, 15, 15, 16, 17, 18, 18, 19, 20, 21, 24, 25',r'\text{Min} = 11,\ \text{max} = 25,\ \text{median} = 17.5,\ Q_1 = 15,\ Q_3 = 20',boxplot(10,26,1,2,(11,15,17.5,20,25),W=320)])],
 ex=[dict(n=9,page=797,kp='p. 796',instr='Consider the given data set: &nbsp;$5, 9, 4, 3, 5, 6, 6, 5, 7, 12, 2, 3, 5$',yinstr='Consider the given data set: &nbsp;$12, 8, 19, 13, 22, 15, 1, 17, 24, 19$',ki=KI_BOX,
          parts=[('a','!Determine whether any outliers exist by first finding $Q_1$ and $Q_3$.',['2, 3, 3, 4, 5, 5, 5, 5, 6, 6, 7, 9, 12',r'Q_1 = \dfrac{3 + 4}{2} = 3.5,\ Q_3 = \dfrac{6 + 7}{2} = 6.5',r'\therefore \text{IQR} = 6.5 - 3.5 = 3',r'Q_1 - 1.5 \times \text{IQR} = 3.5 - 1.5 \times 3 = -1',r'Q_3 + 1.5 \times \text{IQR} = 6.5 + 1.5 \times 3 = 11',r'*\therefore 12 \text{ is an outlier.}']),
                 ('b','!Draw a box plot to summarise the data, marking outliers if they exist.',[boxplot(0,13,1,1,(2,3.5,5,6.5,9),out=(12,),W=560)])],
          yt=[('a','!Determine whether any outliers exist by first finding $Q_1$ and $Q_3$.',['1, 8, 12, 13, 15, 17, 19, 19, 22, 24',r'Q_1 = 12,\ Q_3 = 19',r'\therefore \text{IQR} = 19 - 12 = 7',r'Q_1 - 1.5 \times \text{IQR} = 12 - 1.5 \times 7 = 1.5',r'Q_3 + 1.5 \times \text{IQR} = 19 + 1.5 \times 7 = 29.5',r'*\therefore 1 \text{ is an outlier.}']),
              ('b','!Draw a box plot to summarise the data, marking outliers if they exist.',[boxplot(0,26,2,2,(8,12,16,19,24),out=(1,),W=560)])])],
 exit=[dict(q=r'For the data set $5, 8, 2, 1, 6, 3, 3, 1, 4, 18, 2, 8, 5$, draw a box plot to summarise the data, marking outliers if they exist.',
            w=['1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 8, 8, 18',r'Q_1 = 2,\ Q_2 = 4,\ Q_3 = 7,\ \text{IQR} = 5',r'2 - 1.5 \times 5 = -5.5,\ \ 7 + 1.5 \times 5 = 14.5\ \therefore\ 18 \text{ is an outlier}',boxplot(0,20,1,2,(1,2,4,7,8),out=(18,),W=600)])],
 learn=['box','boxlive'],
)
