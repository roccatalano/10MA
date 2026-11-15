"""10MAG Unit 1 (Univariate Statistics) guided worksheets, C10 9A–9E.
Everything here is verbatim from the books (cited); layout matches the Chapter 1 worksheets.
Run from the repo root:  python3 tools/worksheets/ch9.py   (needs KaTeX at /home/claude/kx: npm i katex@0.16.11)"""
import json,subprocess,os,sys,re
HERE=os.path.dirname(os.path.abspath(__file__));ROOT=os.path.join(HERE,'..','..')
sys.path.insert(0,HERE);import hw,pw_all
hw.H.update(pw_all.P)

# ---------- small house-style drawing helpers ----------
def tbl(head,rows,first_bold=True,w=None):
    """plain bordered table; head = list or None"""
    st='border-collapse:collapse;font-size:10.5pt;margin:1.5mm 0'+(f';width:{w}' if w else '')
    td='border:1px solid #000;padding:1mm 2.2mm;text-align:center'
    h=('<tr>'+''.join(f'<th style="{td};background:#eee;font-size:9.5pt">{x}</th>' for x in head)+'</tr>') if head else ''
    b=''.join('<tr>'+''.join(f'<td style="{td}{";font-weight:bold;text-align:left" if (k==0 and first_bold) else ""}">{x}</td>' for k,x in enumerate(r))+'</tr>' for r in rows)
    return f'<table style="{st}">{h}{b}</table>'
def stemleaf(rows,key):
    td='padding:.6mm 3mm'
    b=''.join(f'<tr><td style="{td};border-right:1.2px solid #000;text-align:right">{s}</td><td style="{td};letter-spacing:2.5mm">{l}</td></tr>' for s,l in rows)
    return (f'<table style="border-collapse:collapse;font-size:11pt;margin:1.5mm 0 0 4mm"><tr><th style="{td};border-right:1.2px solid #000;border-bottom:1.2px solid #000">Stem</th>'
            f'<th style="{td};border-bottom:1.2px solid #000;text-align:left">Leaf</th></tr>{b}</table><div style="font-size:10pt;margin:0 0 1mm 4mm">{key}</div>')
def numline(a,b,step,lab=None,label='',box=None,w=150):
    """number line a..b; box=(min,q1,q2,q3,max) draws a box plot above it"""
    n=int((b-a)/step);u=(w-20)/n;x=lambda v:10+(v-a)/step*u
    o=[f'<line x1="2" y1="40" x2="{w+2}" y2="40" stroke="#000" stroke-width="1"/><path d="M{w+4} 40 l-5 -2.5 v5z"/><path d="M0 40 l5 -2.5 v5z"/>']
    lab=lab or step
    for k in range(n+1):
        v=a+k*step;o.append(f'<line x1="{x(v):.1f}" y1="38" x2="{x(v):.1f}" y2="42" stroke="#000" stroke-width=".8"/>')
        if round((v-a)/lab,6)==int(round((v-a)/lab,6)):o.append(f'<text x="{x(v):.1f}" y="49" font-size="6" text-anchor="middle">{v:g}</text>')
    if label:o.append(f'<text x="{w+8}" y="42" font-size="6">{label}</text>')
    if box:
        mn,q1,q2,q3,mx=box
        o.append(f'<line x1="{x(mn)}" y1="22" x2="{x(q1)}" y2="22" stroke="#000"/><rect x="{x(q1)}" y="14" width="{x(q3)-x(q1)}" height="16" fill="none" stroke="#000"/>'
                 f'<line x1="{x(q2)}" y1="14" x2="{x(q2)}" y2="30" stroke="#000"/><line x1="{x(q3)}" y1="22" x2="{x(mx)}" y2="22" stroke="#000"/>'
                 f'<line x1="{x(mn)}" y1="18" x2="{x(mn)}" y2="26" stroke="#000"/><line x1="{x(mx)}" y1="18" x2="{x(mx)}" y2="26" stroke="#000"/>')
    return f'<svg viewBox="-2 8 {w+42} 46" style="width:{(w+44)*0.62:.0f}mm;max-width:100%;display:block;margin:1mm 0">{"".join(o)}</svg>'
def grid(nx=12,ny=8,mm_=4.2):
    """blank square grid with axes for drawing a histogram"""
    W=nx*10;H=ny*10;o=[]
    for i in range(nx+1):o.append(f'<line x1="{i*10}" y1="0" x2="{i*10}" y2="{H}" stroke="#bbb" stroke-width=".5"/>')
    for j in range(ny+1):o.append(f'<line x1="0" y1="{j*10}" x2="{W}" y2="{j*10}" stroke="#bbb" stroke-width=".5"/>')
    o.append(f'<line x1="0" y1="0" x2="0" y2="{H}" stroke="#000" stroke-width="1.2"/><line x1="0" y1="{H}" x2="{W}" y2="{H}" stroke="#000" stroke-width="1.2"/>')
    return f'<svg viewBox="-2 -2 {W+4} {H+4}" style="width:{nx*mm_:.0f}mm;display:block;margin:1.5mm auto">{"".join(o)}</svg>'
def blank_ft(rows,extra='Percentage frequency'):
    return tbl(['Class interval','Frequency']+([extra] if extra else []),[[r,'&nbsp;']+(['&nbsp;'] if extra else []) for r in rows]+[['Total','&nbsp;']+(['&nbsp;'] if extra else [])])
def twoway(cols,rows):
    return tbl(['']+cols,rows)
LIK=['Strongly agree','Agree','Neutral','Disagree','Strongly disagree','Total']
def tw_blank(cols,rows):
    return twoway(cols,[[r]+['&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;']*len(cols) for r in rows])

C10='Cambridge Essential Mathematics for the Victorian Curriculum 10 &amp; 10A 3rd Ed'
# ---------- content (verbatim) ----------
W={
'9A':dict(title='Collecting representative data',pages='766–771',expg='769–771',
 defs=['<b>Surveys</b> are used to collect statistical data. Survey questions should use simple language and should not be ambiguous, and should not be worded so that they deliberately try to provoke a certain kind of response.',
  'If the question contains an option to be chosen from a list, the number of options should be an odd number, so that there is a ‘neutral’ choice.',
  'A <b>population</b> is a group of people, animals or objects with something in common, e.g. all the students in your school.',
  'A <b>sample</b> is a group that has been chosen from a population. Sometimes information from a sample is used to describe the whole population, so it is important to choose the sample carefully.',
  '<b>Statistical data</b> can be divided into subgroups (see the table below).'],
 formulas=[('Types of data','<table style="border-collapse:collapse;width:100%"><tr><th colspan="2" style="border:1px solid #000;padding:1mm 2mm;text-align:center;font-size:10pt;background:#eee">Categorical</th><th colspan="2" style="border:1px solid #000;padding:1mm 2mm;text-align:center;font-size:10pt;background:#eee">Numerical</th></tr><tr><td style="border:1px solid #000;padding:1mm 2mm;text-align:center;font-size:10pt;width:25%"><b>Nominal</b><br>Categories have no order; e.g. colours: red, blue, yellow</td><td style="border:1px solid #000;padding:1mm 2mm;text-align:center;font-size:10pt;width:25%"><b>Ordinal</b><br>Categories can be ordered; e.g. low, medium, high</td><td style="border:1px solid #000;padding:1mm 2mm;text-align:center;font-size:10pt;width:25%"><b>Discrete</b><br>Data can take on only a limited number of values; e.g. number of children in a family</td><td style="border:1px solid #000;padding:1mm 2mm;text-align:center;font-size:10pt;width:25%"><b>Continuous</b><br>Data can take on any value in a given range; e.g. time taken to complete a race</td></tr></table>')],
 apk=[('Decide whether a primary or secondary source is suitable for an economist collecting data on the average income of Australian households, and suggest a method for its collection.',26,'Year 7 Ch8 checklist item 2 (p. 585)'),
  ('In conducting a survey to determine how many children adults generally have, explain why randomly selecting people outside a childcare centre is likely to lead to bias.',22,'Year 8 Ch8 checklist item 10 (p. 632)'),
  ('One hundred people at the airport are surveyed about how often they travel.<br>This data is used to make conclusions about that city and how often people travel.<br>Do you think this survey will contain bias? If so, explain why.',22,'Year 9 Ch9 checklist item 12 (p. 709)')],
 ex=[dict(n=1,t='Describing types of data',q='What type of data would the following survey questions generate?',parts=['How many televisions do you have in your home?','To what type of music do you most like to listen?'],
          yq='What type of data would the following survey questions generate?',yparts=['How tall are the students in Year 10?','What is your level of satisfaction (low, medium and high) with a meal at a restaurant?'],h=18),
     dict(n=2,t='Choosing a survey sample',q='A survey is carried out on the internet to determine Australia’s favourite musical performer. Why will this sample not necessarily be representative of Australia’s views?',parts=[],
          yq='A survey is carried out in a library to determine typical study habits of Year 12 students. Why will this sample not necessarily be representative of all Year 12 students?',yparts=[],h=34)],
 sc=[(1,'I can describe types of data.','What type of data would the survey question ‘How many pairs of shoes do you own?’ generate?',18),
     (2,'I can choose a survey sample.','A survey is carried out by calling people listed in the phone book to determine their voting preferences for a state election. Why will this sample not necessarily be representative of the state’s views?',24)]),
'9B':dict(title='Review of data displays',pages='772–780',expg='777–780',
 defs=['Categorical data (nominal or ordinal) and numerical data (discrete or continuous) can be displayed using different types of graphs.',
  'Graphs for a single set of categorical or discrete data: <b>dot plot</b>, <b>stem-and-leaf plot</b>, <b>column graph</b>.',
  '<b>Histograms</b> can be used for grouped discrete or continuous numerical data. The interval 10– includes all numbers from $10$ (including $10$) to fewer than $20$.',
  'The <b>mode</b> of a data set is the data value that occurs most frequently.',
  'Data can be <b>symmetrical</b> or <b>skewed</b>. Symmetrical: the mean and median will be equal. <b>Positively skewed</b> (tail to the right): the median will be less than the mean. <b>Negatively skewed</b> (tail to the left): the median will be greater than the mean.'],
 formulas=[('Mean','$\\bar{x} = \\dfrac{\\text{sum of all data values}}{\\text{number of data values}}$'),('Median','the middle value when data are placed in order'),
   ('Percentage frequency','$\\dfrac{\\text{frequency}}{\\text{total}} \\times 100$ &nbsp;&nbsp; e.g. frequency $8$ out of $20$: $\\dfrac{8}{20} \\times 100 = 40\\%$')],
 apk=[('Represent this set of data as a stem-and-leaf plot: $23, 10, 36, 25, 31, 34, 34, 27, 36, 37, 16, 33$.',24,'Year 7 Ch8 checklist item 12 (p. 586)'),
  ('Represent the table below as a frequency graph and as a dot plot.'+tbl(['Number of siblings','Frequency'],[['0','3'],['1','4'],['2','2'],['3','1']],first_bold=False),40,'Year 8 Ch8 checklist item 4 (p. 631)'),
  ('For the data below showing the ice-cream sales each hour of operation over a week, set up and complete a grouped frequency table using class intervals 0–4, 5–9, etc.'+
   tbl(None,[['15','22','1','0','20','3','10','2','23','3','11','14','19','3'],['16','14','24','7','1','15','5','7','2','29','28','3','2','13'],['26','20','22','25','6','7','12','6','13','7','7','20','11','11']],first_bold=False)+
   'From the table, construct a frequency histogram and state for how many hours there were sales of $15$ or more ice-creams.',70,'Year 9 Ch9 checklist item 17 (p. 709)')],
 ex=[dict(n=3,t='Presenting and analysing data in frequency histograms',q='Twenty people were surveyed to find out how many times they use the internet in a week. The raw data are listed.<br>$21, 19, 5, 10, 15, 18, 31, 40, 32, 25$<br>$11, 28, 31, 29, 16, 2, 13, 33, 14, 24$',
          parts=['Organise the data into a frequency table using class intervals of $10$. Include a percentage frequency column.'+blank_ft(['0–','10–','20–','30–','40–50']),
                 'Construct a histogram for the data, showing both the frequency and percentage frequency on the one graph.'+grid(14,10,5.6),
                 'Describe the data in the histogram as symmetrical, positively skewed or negatively skewed.'],
          yq='Sixteen people were surveyed to find out how many phone texts they send in one day. The raw data are as follows.<br>$10, 7, 2, 5, 22, 14, 7, 9, 11, 29, 32, 18, 5, 24, 12, 14$',
          yparts=['Organise the data into a frequency table using class intervals of $10$. Include a percentage frequency column.'+blank_ft(['0–','10–','20–','30–40']),
                  'Construct a histogram for the data, showing both the frequency and percentage frequency on the one graph.'+grid(14,10,5.6),
                  'Describe the data in the histogram as symmetrical, positively skewed or negatively skewed.'],h=[4,4,12],split=True),
     dict(n=4,t='Working with stem and leaf plots',q='Twelve test marks for Rolle in a semester are given as percentages in the raw data below:<br>$66 \\;\\; 74 \\;\\; 81 \\;\\; 68 \\;\\; 94 \\;\\; 88 \\;\\; 74 \\;\\; 85 \\;\\; 90 \\;\\; 72 \\;\\; 79 \\;\\; 86$',
          parts=['Construct a stem-and-leaf plot for the data.','Use your stem-and-leaf plot to find:<br><b>i</b>&nbsp; the mode<br><b>ii</b>&nbsp; the median<br><b>iii</b>&nbsp; the mean.'],
          yq='Payments from Lucy’s last twelve babysitting jobs are given below.<br>&#36;36 &nbsp; &#36;48 &nbsp; &#36;44 &nbsp; &#36;62 &nbsp; &#36;56 &nbsp; &#36;58 &nbsp; &#36;52 &nbsp; &#36;39 &nbsp; &#36;56 &nbsp; &#36;38 &nbsp; &#36;60 &nbsp; &#36;45',
          yparts=['Construct a stem-and-leaf plot for the data.','Use your stem-and-leaf plot to find:<br><b>i</b>&nbsp; the mode<br><b>ii</b>&nbsp; the median<br><b>iii</b>&nbsp; the mean.'],h=[34,40])],
 sc=[(3,'I can present data in a histogram.','Fifteen people were surveyed to find out how many hours they spend on the internet in a week. The data are:<br>$7, 12, 14, 20, 2, 26, 8, 11, 17, 12, 21, 5, 6, 18, 14$<br>Construct a histogram for the data using class intervals of $5$, showing both the frequency and percentage frequency on the one graph. Is the data symmetrical, positively skewed or negatively skewed?'+grid(12,8,3.6),10),
     (4,'I can analyse data in a statistical graph.','For the stem-and-leaf plot shown below, find the mean correct to one decimal place, the median and the mode.'+stemleaf([('0','2 5 7'),('1','1 1 4 6'),('2','0 3 9'),('3','2 5')],'$2 \\,|\\, 3$ means $23$'),30)]),
'9C':dict(title='Two-way tables',sc1=True,pages='781–788',expg='785–788',
 defs=['A <b>two-way table</b> is a way of displaying data to help compare two related categorical variables.',
  'The options for one variable form the rows and the options for the other variable form the columns.',
  'The entries in the table, often given as frequencies or proportions, are totalled both vertically and horizontally.',
  'A <b>Likert scale</b> is a list of ordered options which can be responded to as part of a survey question.',
  'A 5-point scale is often used as it provides a neutral option and the ability for respondents to offer a degree of opinion: Strongly agree, Agree, Neutral, Disagree, Strongly disagree.'],
 formulas=[('Percentage of those surveyed','$\\dfrac{\\text{frequency}}{\\text{total surveyed}} \\times 100$ &nbsp;&nbsp; e.g. $\\dfrac{26}{50} \\times 100 = 52\\%$'),('Fraction of those surveyed','$\\dfrac{\\text{frequency}}{\\text{total surveyed}}$, then simplify &nbsp;&nbsp; e.g. $\\dfrac{15}{40} = \\dfrac{3}{8}$')],
 apk=[('Write the proportion &#36;40 out of &#36;200 as a fraction, a decimal and a percentage.',20,'Year 7 Ch5 checklist item 19 (p. 342)'),
  ('Of $50$ people it was found that $20$ people liked both coffee and tea, $15$ liked coffee but not tea and $10$ people liked tea but not coffee. Draw a two-way table of this situation.',34,'Year 8 Ch8 checklist item 15 (p. 632)'),
  ('On a particular day at a car service station, $20$ cars are serviced: $12$ cars need a wheel alignment, $10$ cars need their brake fluid replaced and $4$ require both.<br>Illustrate the situation using a two-way table. Use the table to find how many cars require neither, and the probability that a randomly selected car needs only a wheel alignment.',40,'Year 9 Ch9 checklist item 3 (p. 708)')],
 ex=[dict(n=5,t='Interpreting a two-way table',q='This two-way table summarises data collected from a survey using a 5-point Likert scale. The survey asked $50$ people if they are over or under the age of $40$ and to what degree they agree with the idea to reduce the driving blood alcohol limit from $0.05$ to $0.04$.'+
          twoway(LIK,[['$40$ and over','2','7','10','5','0','24'],['Under $40$','0','1','6','12','7','26'],['Total','2','8','16','17','7','50']]),
          parts=['State how many of the people surveyed:<br><b>i</b>&nbsp; were $40$ years of age or over<br><b>ii</b>&nbsp; strongly agree with the idea<br><b>iii</b>&nbsp; were $40$ years of age or over and responded Agree to the question<br><b>iv</b>&nbsp; were under $40$ and responded Disagree to the question.',
                 'What percentage of the people surveyed:<br><b>i</b>&nbsp; were under $40$ years of age?<br><b>ii</b>&nbsp; were neutral to the idea?<br><b>iii</b>&nbsp; were under $40$ years of age and responded Strongly Disagree with the idea?<br><b>iv</b>&nbsp; were $40$ years of age or over and responded Neutral to the idea?',
                 'Would you say that this data supports the notion that younger people would prefer a lower driving blood alcohol limit? Give a reason.'],
          yq='This two-way table summarises data collected from a survey using a 5-point Likert scale. The survey asked $20$ teachers if they thought there was enough time in the day to prepare for classes. Some teachers were from public schools and some were from private schools.'+
          twoway(LIK,[['Public','1','2','4','2','1','10'],['Private','0','2','6','1','1','10'],['Total','1','4','10','3','2','20']]),
          yparts=['State how many of the teachers surveyed:<br><b>i</b>&nbsp; were from public schools<br><b>ii</b>&nbsp; responded Agree to the question<br><b>iii</b>&nbsp; were from public schools and responded Agree to the question<br><b>iv</b>&nbsp; were from private schools and responded Disagree to the question.',
                  'What percentage of the teachers surveyed:<br><b>i</b>&nbsp; were from private schools?<br><b>ii</b>&nbsp; were neutral to the question?<br><b>iii</b>&nbsp; were from private schools and responded Neutral to the question?<br><b>iv</b>&nbsp; were from public schools and responded Disagree to the question?',
                  'Would you say that this data supports the notion that teachers from public schools feel that there is enough time in the day to prepare for classes compared to private school teachers? Give a reason.'],h=[34,38,24],split=True),
     dict(n=6,t='Constructing a two-way table',q='A number of people were surveyed to see if they owned a beach house. They were also asked as to whether they were over $60$ years of age. $15$ of the $25$ people $60$ years of age and over said that they owned a beach house and $6$ of the $15$ people under $60$ years of age said that they owned a beach house.',
          parts=['Represent this information in a two-way table.'+tw_blank(['Beach house','No beach house','Total'],['$60$ and over','Under $60$','Total']),'What fraction of the people surveyed:<br><b>i</b>&nbsp; were under $60$ years of age?<br><b>ii</b>&nbsp; were under $60$ years of age and owned a beach house?','Would you say that this data supports the notion that older people are more likely to own a beach house? Give a reason.'],
          yq='A number of city and country dogs were checked to see if they were of pure or mixed breed. $18$ of the $30$ country dogs were of pure breed and $13$ of the $20$ city dogs were of mixed breed.',
          yparts=['Represent this information in a two-way table.'+tw_blank(['Pure breed','Mixed breed','Total'],['Country','City','Total']),'What fraction of the dogs surveyed:<br><b>i</b>&nbsp; were from the city?<br><b>ii</b>&nbsp; were from the city and of pure breed?','Would you say that this data supports the notion that country dogs are more likely to be of mixed breed? Give a reason.'],h=[4,18,18])],
 sc=[(5,'I can interpret a two-way table.','This two-way table summarises data from a survey of $40$ people using a 5-point Likert scale. The survey asked if they live in Australia or live overseas and are visiting and to what degree they thought Australians were friendly.'+
      twoway(LIK,[['Aus','2','4','6','3','3','18'],['Overseas','8','8','2','3','1','22'],['Total','10','12','8','6','4','40']])+'<b>i</b>&nbsp; State how many people surveyed were from Australia and responded Agree.<br><b>ii</b>&nbsp; Do you think that the data supports the notion that overseas visitors think Australians are more friendly? Give a reason.',22),
     (6,'I can construct a two-way table.','A number of people were surveyed to see if they had a mortgage. They were also asked whether they were under or over $50$ years of age. $11$ of the $15$ people under $50$ had a mortgage and $5$ of the $10$ people $50$ or over had a mortgage. Represent the information in a two-way table and find what fraction of people surveyed were $50$ or over and had a mortgage.',42)]),
'9D':dict(title='Summary statistics',pages='789–794',expg='793–794',
 defs=['<b>Five-figure summary</b>: minimum value (min); lower quartile $(Q_1)$, the number above $25\\%$ of the ordered data; median $(Q_2)$, the middle value above $50\\%$ of the ordered data; upper quartile $(Q_3)$, the number above $75\\%$ of the ordered data; maximum value (max).',
  '<b>Outliers</b> are data elements outside the vicinity of the rest of the data. A data point is an outlier when it is below the lower fence (i.e. lower limit) or above the upper fence (i.e. upper limit).',
  'An outlier does not significantly affect the median of a data set.',
  'An outlier does significantly affect the mean of a data set.'],
 formulas=[('Range','$\\text{Range} = \\text{max value} - \\text{min value}$'),('Interquartile range (IQR)','$\\text{IQR} = \\text{upper quartile} - \\text{lower quartile} = Q_3 - Q_1$'),
   ('Fences','$\\text{Lower fence} = Q_1 - 1.5 \\times \\text{IQR}$ &nbsp;&nbsp; $\\text{Upper fence} = Q_3 + 1.5 \\times \\text{IQR}$'),
   ('Odd number of values','$1 \\;\\; 2 \\;\\; 2 \\;\\; 3 \\;\\; 5 \\;\\; 6 \\;\\; 6 \\;\\; 7 \\;\\; 9$ &nbsp;&nbsp; $Q_1 = 2$, $Q_2 = 5$, $Q_3 = 6.5$, $\\text{IQR} = 4.5$'),
   ('Even number of values','$2 \\;\\; 3 \\;\\; 3 \\;\\; 4 \\;\\; 7 \\;\\; 8 \\;\\; 8 \\;\\; 9 \\;\\; 9 \\;\\; 9$ &nbsp;&nbsp; $Q_1 = 3$, $Q_2 = 7.5$, $Q_3 = 9$, $\\text{IQR} = 6$')],
 apk=[('Find the median of $15, 31, 12, 47, 21, 65, 12, 29$.',20,'Year 7 Ch8 checklist item 5 (p. 585)'),
  ('Find the IQR of $1, 15, 8, 2, 13, 10, 4, 14$.',24,'Year 8 Ch8 checklist item 8 (p. 631)'),
  ('List the data below in order from smallest to largest and find the median $(Q_2)$, the lower quartile $(Q_1)$, the upper quartile $(Q_3)$ and the interquartile range (IQR). Interpret the IQR.<br>$12 \\;\\; 21 \\;\\; 18 \\;\\; 8 \\;\\; 4 \\;\\; 16 \\;\\; 24 \\;\\; 11 \\;\\; 27 \\;\\; 10$',30,'Year 9 Ch9 checklist item 20 (p. 710)')],
 ex=[dict(n=7,t='Finding the range and IQR',q='Determine the range and IQR for these data sets by finding the five-figure summary.',parts=['$2, 2, 4, 5, 6, 8, 10, 13, 16, 20$','$1.6, 1.7, 1.9, 2.0, 2.1, 2.4, 2.4, 2.7, 2.9$'],
          yq='Determine the range and IQR for these data sets by finding the five-figure summary.',yparts=['$3, 5, 5, 6, 7, 9, 10, 12$','$3.8, 3.9, 4.0, 4.2, 4.5, 4.5, 4.7$'],h=42),
     dict(n=8,t='Finding the five-figure summary and outliers',q='The following data set represents the number of flying geese spotted on each day of a $13$-day tour of England.<br>$5, 1, 2, 6, 3, 3, 18, 4, 4, 1, 7, 2, 4$',
          parts=['For the data, find:<br><b>i</b>&nbsp; the minimum and maximum number of geese spotted<br><b>ii</b>&nbsp; the median<br><b>iii</b>&nbsp; the upper and lower quartiles<br><b>iv</b>&nbsp; the IQR<br><b>v</b>&nbsp; any outliers by determining the lower and upper fences.','Can you give a possible reason for why the outlier occurred?'],
          yq='The following data set represents the number of people on $11$ buses in a local area.<br>$36, 24, 15, 23, 26, 0, 19, 24, 26, 33, 19$',
          yparts=['For the data, find:<br><b>i</b>&nbsp; the minimum and maximum number of people on the buses.<br><b>ii</b>&nbsp; the median<br><b>iii</b>&nbsp; the upper and lower quartiles<br><b>iv</b>&nbsp; the IQR<br><b>v</b>&nbsp; any outliers by determining the lower and upper fences.','Can you give a possible reason for why the outlier occurred?'],h=[70,16])],
 sc=[(7,'I can find the five-figure summary and interquartile range.','For the data set below find the minimum, maximum, median, upper and lower quartiles and the range and IQR.<br>$7, 10, 12, 12, 14, 18, 22, 25, 26, 30$',40),
     (8,'I can find any outliers in a data set.','The following data represent the number of aces by a tennis player in $11$ grand slam matches for the year:<br>$15, 12, 22, 2, 10, 18, 16, 14, 15, 20, 16$<br>For the data find the upper and lower quartiles and use these to help determine if there are any outliers.',40)]),
'9E':dict(title='Box plots',pages='795–801',expg='799–801',
 defs=['A <b>box plot</b> (also called a box-and-whisker plot) can be used to summarise a data set. It divides the data set into four groups that are approximately equal in size $(25\\%)$.',
  'An <b>outlier</b> is marked with a dot $(\\bullet)$. An outlier is greater than $Q_3 + 1.5 \\times \\text{IQR}$ or less than $Q_1 - 1.5 \\times \\text{IQR}$.',
  'The <b>whiskers</b> stretch to the lowest and highest data values that are not outliers.',
  '<b>Parallel box plots</b> are two or more box plots drawn on the same scale. They are used to compare data sets within the same context.'],
 formulas=[('Five-figure summary','min, $Q_1$, $Q_2$ (median), $Q_3$, max'),('IQR','$\\text{IQR} = Q_3 - Q_1$'),('Outliers','below $Q_1 - 1.5 \\times \\text{IQR}$ or above $Q_3 + 1.5 \\times \\text{IQR}$')],
 apk=[('Find the IQR of $1, 15, 8, 2, 13, 10, 4, 14$.',24,'Year 8 Ch8 checklist item 8 (p. 631)'),
  ('This box plot summarises the test results $(\\%)$ of a class of students.'+numline(40,100,5,10,'Score (%)',box=(45,60,70,90,95),w=170)+
   '<b>i</b>&nbsp; Find the range and interquartile range of the results.<br><b>ii</b>&nbsp; Twenty-five per cent of results were above what number?<br><b>iii</b>&nbsp; If there were $24$ students in the class, how many scored above $70\\%$?',24,'Year 9 Ch9 checklist item 21 (p. 710)'),
  ('For the data shown below, find the minimum and maximum values, the median and lower and upper quartiles and draw a box plot to represent the data.<br>$18 \\;\\; 15 \\;\\; 13 \\;\\; 14 \\;\\; 21 \\;\\; 25 \\;\\; 17 \\;\\; 11 \\;\\; 15 \\;\\; 16 \\;\\; 18 \\;\\; 20 \\;\\; 24 \\;\\; 19$',40,'Year 9 Ch9 checklist item 22 (p. 710)')],
 ex=[dict(n=9,t='Constructing a box plot',q='Consider the given data set:<br>$5, 9, 4, 3, 5, 6, 6, 5, 7, 12, 2, 3, 5$',
          parts=['Determine whether any outliers exist by first finding $Q_1$ and $Q_3$.','Draw a box plot to summarise the data, marking outliers if they exist.'+numline(0,13,1,2,'',w=110)],
          yq='Consider the given data set:<br>$12, 8, 19, 13, 22, 15, 1, 17, 24, 19$',
          yparts=['Determine whether any outliers exist by first finding $Q_1$ and $Q_3$.','Draw a box plot to summarise the data, marking outliers if they exist.'+numline(0,26,2,4,'',w=110)],h=[60,22])],
 sc=[(9,'I can construct a box plot.','For the data set $5, 8, 2, 1, 6, 3, 3, 1, 4, 18, 2, 8, 5$, draw a box plot to summarise the data, marking outliers if they exist.'+numline(0,20,1,2,'',w=150),40)]),
}
YEAR_SRC='Cambridge Essential Mathematics for the Victorian Curriculum 3rd Ed'

def page(sub,d,R):
    L=json.load(open(os.path.join(ROOT,'library/C10.json')))
    card=next(s for c in L['chapters'] for s in c['subchapters'] if s['id']=='C10-'+sub)
    o=[f'<div class="title"><div class="code">{sub}</div><h1>{d["title"]}</h1><div class="pg">Cambridge pp. {d["pages"]}</div></div>']
    o.append('<div class="box "><div class="hd">Learning intentions<span></span></div><div class="bd"><ul>'+''.join(f'<li>{x}</li>' for x in card['learning_intentions'])+'</ul></div></div>')
    o.append('<div class="box "><div class="hd">Key definitions<span></span></div><div class="bd"><ul class="ki">'+''.join(f'<li>{R(x)}</li>' for x in d['defs'])+'</ul></div></div>')
    if d.get('formulas'):
        o.append('<div class="box split"><div class="hd">Key formulas<span></span></div><div class="bd"><table class="kf"><tbody>'+''.join(f'<tr><td>{a}</td><td>{R(b)}</td></tr>' for a,b in d['formulas'])+'</tbody></table></div></div>')
    q=''.join(f'<div class="apq"><b>{n}.</b><div><p class="q">{R(t)}</p><div style="min-height:{h}mm"></div></div></div>' for n,(t,h,_) in enumerate(d['apk'],1))
    o.append(f'<div class="box "><div class="hd">Activating prior knowledge<span></span></div><div class="bd">{q}<p class="src">{YEAR_SRC}: '+'; '.join(c for *_,c in d['apk'])+'</p></div></div>')
    for e in d['ex']:
        hs=e['h'] if isinstance(e['h'],list) else [e['h']]*max(1,len(e['parts']))
        def col(q,parts):
            s=f'<p class="q">{R(q)}</p>'
            if not parts:return s+f'<div style="height:{hs[0]}mm"></div>'
            sp=lambda k,p:hs[k] if ('<svg' in p or '<table' in p) else max(hs[k],12)   # working space BELOW the question text
            return s+''.join(f'<div class="ytp"><b>{"abcdef"[k]}</b><div><div>{R(p)}</div><div style="height:{sp(k,p)}mm"></div></div></div>' for k,p in enumerate(parts))
        fs='11.0pt' if len(e['t'])<36 else '9.5pt'
        if e.get('split'):   # long parts: Example on top, You try below (each full width)
            o.append(f'<div class="box"><div class="hd">Example {e["n"]} · {e["t"]}<span></span></div><div class="bd">{col(e["q"],e["parts"])}</div></div>')
            o.append(f'<div class="box"><div class="hd">You try {e["n"]}<span></span></div><div class="bd">{col(e["yq"],e["yparts"])}</div></div>')
        else:
            o.append(f'<div class="pair"><div class="hd" style="font-size:{fs}">Example {e["n"]} · {e["t"]}</div><div class="hd" style="font-size:{fs}">You try {e["n"]}</div>'
                     f'<div class="bd">{col(e["q"],e["parts"])}</div><div class="bd">{col(e["yq"],e["yparts"])}</div></div>')
    sc=''.join(f'<div class="sc"><div class="tick"></div><div><b>{n}. {s}</b><br>e.g. {R(t)}<div style="height:{h}mm"></div></div></div>' for n,s,t,h in d['sc'])
    cls='scg' if len(d['sc'])>1 and not d.get('sc1') else ''
    o.append(f'<div class="box split"><div class="hd">Skills checklist<span>Tick when you can do it</span></div><div class="bd"><div class="{cls}">{sc}</div><p class="src">{C10}, Ch 9 Chapter checklist (pp. 853–854)</p></div></div>')
    o.append(hw.box(sub,f'pp. {d["expg"]}'))
    return ''.join(o)

# A4 sheets on screen and in print (same as the CFATs): content is dealt into 210x297mm sheets
SHEETS='''@page{size:A4;margin:0}
html,body{background:#8a8a8a!important;width:auto!important;min-height:0!important;margin:0!important;padding:0!important;box-shadow:none!important}
#flow{width:186mm;background:#fff}
.sheet{width:210mm;height:297mm;padding:11mm 12mm 12mm;background:#fff;margin:8mm auto;box-shadow:0 2px 14px rgba(0,0,0,.45);position:relative;overflow:hidden}
.sheet .pno{position:absolute;bottom:5mm;left:0;right:0;text-align:center;font-size:8.5pt;color:#444}
@media print{html,body{background:#fff!important}.sheet{margin:0;box-shadow:none;break-after:page}}'''
PAGINATE='''<script>(function(){const f=document.getElementById('flow');const items=[...f.children];const mm=v=>v*96/25.4;const H=mm(297-11-12-6);
let sh,used=0;const add=()=>{sh=document.createElement('div');sh.className='sheet';document.body.appendChild(sh);used=0};add();
items.forEach(el=>{const cs=getComputedStyle(el);const h=el.getBoundingClientRect().height+parseFloat(cs.marginTop)+parseFloat(cs.marginBottom);
 if(used>0&&used+h>H)add();sh.appendChild(el);used+=h});f.remove();
const all=[...document.querySelectorAll('.sheet')];all.forEach((x,k)=>{const p=document.createElement('div');p.className='pno';p.textContent='Page '+(k+1)+' of '+all.length;x.appendChild(p)});document.body.dataset.ready=1})()</script>'''
def katex(strings):
    return json.loads(subprocess.run(['node',os.path.join(HERE,'kt.js')],input=json.dumps(strings),capture_output=True,text=True,check=True).stdout)

def main(subs):
    css=open(os.path.join(HERE,'ws.css')).read()
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b=p.chromium.launch();pg=b.new_page()
        for sub in subs:
            d=W[sub];texts=[]
            page(sub,d,lambda s:texts.append(s) or s)           # pass 1: collect strings with maths
            out=dict(zip(texts,katex(texts)))
            body=page(sub,d,lambda s:out[s])
            html=f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>C10-{sub} worksheet</title><style>{css}{SHEETS}.box>.hd{{white-space:normal}}.scg{{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}}.sc{{break-inside:avoid}}.box>.hd span{{white-space:nowrap;margin-left:3mm}}</style></head><body><div id="flow">{body}</div>{PAGINATE}</body></html>'
            f=os.path.join(ROOT,'lessons',f'C10-{sub} worksheet.html');open(f,'w').write(html)
            pg.goto('file://'+os.path.abspath(f));pg.wait_for_timeout(400)
            pg.wait_for_selector('body[data-ready]');pg.pdf(path=f[:-5]+'.pdf',format='A4',print_background=True,prefer_css_page_size=True,margin={'top':'0','bottom':'0','left':'0','right':'0'})
            print(f)
        b.close()
if __name__=='__main__':main(sys.argv[1:] or list(W))
