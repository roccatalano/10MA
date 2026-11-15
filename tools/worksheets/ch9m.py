"""10MAG Modified, G1 Univariate Statistics: one guided worksheet per lesson (L1-L6), at Year 7-8 level (Year 9 for box plots).
Same lesson order as 10MAG (courses/lessons.json). Everything verbatim from Cambridge Essential Mathematics 7 / 8 / 9 (3rd Ed), cited.
Layout = the 10MAG worksheets (ws.css), simplified: Learning intentions, Key ideas, Example | You try pairs, Skills checklist (I can... only).
Practice = the Freefall sheets for the lesson, which go in the modified unit workbook (G: only, licensed).
Run from the repo root:  python3 tools/worksheets/ch9m.py   (needs KaTeX at /home/claude/kx: npm i katex@0.16.11)"""
import json,os,sys
HERE=os.path.dirname(os.path.abspath(__file__));ROOT=os.path.join(HERE,'..','..')
sys.path.insert(0,HERE)
from ch9 import tbl,stemleaf,numline,grid,tw_blank,SHEETS,PAGINATE,katex
BK={7:'Cambridge Essential Mathematics for the Victorian Curriculum 7 3rd Ed',8:'Cambridge Essential Mathematics for the Victorian Curriculum 8 3rd Ed',9:'Cambridge Essential Mathematics for the Victorian Curriculum 9 3rd Ed'}
CL=lambda y,ns:[x['text'] for x in json.load(open(os.path.join(ROOT,f'tools/data/checklist{y}.json'))) if x['n'] in ns and x['chapter']==(9 if y==9 else 8)]
ft=lambda head,rows:tbl(head,rows,first_bold=False)
def venn(): # blank two-circle Venn diagram in a rectangle
    return '<svg viewBox="0 0 200 110" style="width:55mm;display:block;margin:1mm 0"><rect x="2" y="2" width="196" height="106" fill="none" stroke="#000"/><circle cx="80" cy="55" r="38" fill="none" stroke="#000"/><circle cx="122" cy="55" r="38" fill="none" stroke="#000"/></svg>'
def bplot(a,b,step,lab,five,label):
    return numline(a,b,step,lab,'',box=five,w=170)+f'<div style="font-size:9.5pt;margin:-1mm 0 1mm 30mm">{label}</div>'

W={
'L1':dict(sub='9A',title='Collecting and classifying data',src=[(7,'8A','pp. 514–516')],
 li=['To know the meaning of the terms primary source, secondary source, census, sample and observation','To be able to classify variables as numerical (discrete or continuous) or categorical',
     'To understand that different methods are suitable for collecting different types of data, based on the size and nature of the data'],
 ki=['In statistics, a <b>variable</b> is something measurable or observable that is expected to change over time or between individual observations. It can be numerical or categorical.',
     '<b>Discrete numerical</b> – data that can only be particular numerical values, e.g. the number of TV sets in a house (could be $0, 1, 2, 3$ but not values in between such as $1.3125$).',
     '<b>Continuous numerical</b> – data that can take any value in a range. Variables such as heights, weights and temperatures are all continuous.',
     '<b>Categorical</b> – data that are not numerical such as colours, gender, brands of cars are all examples of categorical data.',
     'Data from a <b>primary source</b> are firsthand information collected from the original source by the person or organisation needing the data. Data from a <b>secondary source</b> have been collected, published and possibly summarised by someone else before we use it.',
     'When an entire population is surveyed, it is called a <b>census</b>. When a subset of the population is surveyed, it is called a <b>sample</b>. Samples should be randomly selected and large enough to represent the views of the overall population.'],
 ex=[dict(n='Year 7 Example 1',t='Classifying variables',q='Classify the following variables as categorical, discrete numerical or continuous numerical.',parts=['the Australian state or territory in which a baby is born','the length of a newborn baby'],
          yq='Classify the following variables as categorical, discrete numerical or continuous numerical.',yparts=['the number of children a person has','the brand of shoes someone wears'],h=12),
     dict(n='Year 7 Example 2',t='Collecting data from primary and secondary sources',q='Decide whether a primary source or a secondary source is suitable for collection of data on each of the following and suggest a method for its collection.',
          parts=['a coffee shop wants to know the average number of customers it has each day','a detergent manufacturer wants to know the favourite washing powder or liquid for households in Australia'],
          yq='Decide whether a primary source or secondary source is suitable for collection of data on each of the following and suggest a method for its collection.',yparts=['the maximum temperature each year in Australia for the past 100 years','the number of pets owned by everyone in a class at school'],h=22)],
 sc=CL(7,[1,2])),
'L2':dict(sub='9B',title='Frequency tables, graphs and stem-and-leaf plots',src=[(8,'8B','pp. 554–556'),(8,'8C','pp. 560–564'),(7,'8E','pp. 542–544')],
 li=['To be able to construct a tally and frequency table from a set of data','To be able to construct a graph from a frequency table','To be able to interpret a stem-and-leaf plot'],
 ki=['<b>Frequency tables</b> show how common a certain value is in a frequency column. A tallying column is also often used as data is gathered.',
     'Frequency tables can be represented using a <b>frequency graph</b>, which has a vertical axis ($y$-axis) used to represent the frequency of each item.',
     'Sometimes the values are grouped (e.g. $0–9$, $10–19$, $20–29$) before the graph is drawn.',
     'A <b>stem-and-leaf plot</b> is a way to display numerical data. Each number is usually split into a stem (the first digit or digits) and a leaf (the last digit).',
     'A key is usually connected to each stem-and-leaf plot to show the value of the stem and leaf. For example: $4\\,|\\,8$ means $48$.'],
 ex=[dict(n='Year 8 Example 4',t='Constructing tables from data',q='Put the following data into a frequency table:<br>$1, 4, 1, 4, 1, 2, 3, 4, 6, 1, 5, 1, 2, 1$.'+tbl(['Number','1','2','3','4','5','6'],[['Tally']+['&nbsp;&nbsp;&nbsp;&nbsp;']*6,['Frequency']+['']*6]),parts=[],
          yq='Put the following data into a frequency table:<br>$1, 2, 4, 2, 1, 2, 2, 4, 5, 2, 4, 1, 5, 3, 2$.'+tbl(['Number','1','2','3','4','5'],[['Tally']+['&nbsp;&nbsp;&nbsp;&nbsp;']*5,['Frequency']+['']*5]),yparts=[],h=4),
     dict(n='Year 8 Example 6',t='Constructing frequency graphs from frequency tables',split=True,q='Represent the frequency tables below as frequency graphs.',
          parts=[ft(['Number of siblings','Frequency'],[['0','15'],['1','20'],['2','13'],['3','2']])+grid(10,7,5),ft(['Number of words in story','Frequency'],[['0−99','2'],['100−199','10'],['200−299','12'],['300−399','8'],['400−500','3']])+grid(12,7,5)],
          yq='Represent the frequency tables below as frequency graphs.',
          yparts=[ft(['Number of pets','Frequency'],[['0','4'],['1','3'],['2','9'],['3','2']])+grid(10,7,5),ft(['Age of customer (years)','Frequency'],[['0−9','4'],['10−19','12'],['20−29','25'],['30−39','18'],['40−50','7']])+grid(12,7,5)],h=[2,2]),
     dict(n='Year 7 Example 9',t='Interpreting a stem-and-leaf plot',split=True,q='Average daily temperatures are shown for some different countries.'+stemleaf([('1','3 6 6'),('2','0 0 1 2 5 5 6 8 9'),('3','0 2')],'$2\\,|\\,5$ means $25$°C'),
          parts=['Write out the temperatures as a list.','How many countries’ temperatures are represented?','What are the minimum and maximum temperatures?','What is the range of temperatures recorded?','What is the median temperature recorded?'],
          yq='The age of a number of people is shown in a stem-and-leaf plot.'+stemleaf([('1','8'),('2','1 1 4'),('3','0 2 8 9'),('4','3')],'$3\\,|\\,2$ means $32$ years old'),
          yparts=['Write out the ages as a list.','How many people’s ages are represented?','What are the youngest and oldest people’s ages?','Give the range of ages.','What is the median age?'],h=[12,8,8,8,10])],
 sc=CL(8,[3])+['I can construct a graph from a frequency table.']+CL(7,[12])),
'L3':dict(sub='9C',title='Venn diagrams and two-way tables',src=[(8,'8J','pp. 611–615')],
 li=['To understand that two-way tables and Venn diagrams can be used to show the number of possible outcomes when two different events are considered','To be able to construct a Venn diagram from a worded situation','To be able to construct a two-way table from a worded situation'],
 ki=['A <b>two-way table</b> shows the number of outcomes or people in different categories, with the final row and column being the total of the other entries in that row or column. For example:'
     +tbl(['','Like Maths','Do not like Maths','Total'],[['Like English','28','33','61'],['Do not like English','5','34','39'],['Total','33','67','100']]),
     'A two-way table can be used to find probabilities. For example: $\\text{Pr(like Maths)} = \\dfrac{33}{100}$',
     'A <b>Venn diagram</b> is a pictorial representation of a two-way table without the total row and column.'],
 ex=[dict(n='Year 8 Example 16',t='Constructing Venn diagrams and two-way tables',q='A survey is conducted of $50$ people, asking who likes coffee and who likes tea. It was found that $20$ people liked both, $15$ people liked coffee but not tea, and $10$ people liked tea but not coffee.',
          parts=['How many people liked neither tea nor coffee?','Represent the survey findings in a Venn diagram.'+venn(),'How many people surveyed like tea?','How many people like coffee or tea or both (inclusive ‘or’)?','How many people like either coffee or tea but not both (exclusive ‘or’)?','Represent the survey findings in a two-way table.'+tw_blank(['Like coffee','Dislike coffee','Total'],['Like tea','Dislike tea','Total'])],
          yq='A survey is conducted of $30$ people, asking who likes coffee and who likes tea. It was found that $7$ people liked both, $12$ people liked coffee but not tea, and $8$ people liked tea but not coffee.',
          yparts=['How many people liked neither tea nor coffee?','Represent the survey findings in a Venn diagram.'+venn(),'How many people surveyed like tea?','How many people like coffee or tea or both (inclusive ‘or’)?','How many people like coffee or tea but not both (exclusive ‘or’)?','Represent the survey findings in a two-way table.'+tw_blank(['Like coffee','Dislike coffee','Total'],['Like tea','Dislike tea','Total'])],h=[8,2,8,8,8,2]),
     dict(n='Year 8 Example 17',t='Using two-way tables to calculate probabilities',q='Consider the two-way table below showing the eating and sleeping preferences of different animals at the zoo.'+tbl(['','Eats meat','No meat','Total'],[['Sleeps during day','20','12','32'],['Only sleeps at night','40','28','68'],['Total','60','40','100']]),
          parts=['For a randomly selected animal, find:<br><b>i</b>&nbsp; Pr(sleeps only at night)<br><b>ii</b>&nbsp; Pr(eats meat or sleeps during day or both).','If an animal is selected at random and it eats meat, what is the probability that it sleeps during the day?','What is the probability that an animal that sleeps during the day does not eat meat?'],
          yq='The two-way table below shows how many vegetarian and non-vegetarians are at a party of men and women.'+tbl(['','Men','Women','Total'],[['Vegetarian','5','10','15'],['Not a vegetarian','20','25','45'],['Total','25','35','60']]),
          yparts=['For a randomly selected person at the party, find:<br><b>i</b>&nbsp; Pr(vegetarian) &nbsp;&nbsp; <b>ii</b>&nbsp; Pr(a vegetarian or a man or both).','If a man is selected at random, what is the probability that he is not a vegetarian?','If a vegetarian is selected at random, what is the probability that they are a woman?'],h=[18,12,12])],
 sc=CL(8,[14,15,16])),
'L4':dict(sub='9D',title='Range, mean, median and mode',src=[(7,'8B','pp. 520–523')],
 li=['To understand that numerical data can be summarised as a single number by finding its range, mean, median or mode','To be able to find the range of a set of numerical data','To be able to find the mean, median and mode of a set of numerical data'],
 ki=['The <b>range</b> of a set of data is given by: Range $=$ highest number $-$ lowest number.',
     '<b>Mean</b>, <b>median</b> and <b>mode</b> are three different measures that can be used to summarise a set of data. The word average is used to refer to the mean.',
     'The mean of a set of data is given by: Mean $=$ (sum of all the values) $\\div$ (total number of values)',
     'The median is the middle value when the values are sorted from lowest to highest. If there are two middle values, then add them together and divide by $2$.',
     'The mode is the most common value. It is the value that occurs most frequently. There can be more than one mode.'],
 ex=[dict(n='Year 7 Example 3',t='Finding the range, mean and mode',q='Consider the ages (in years) of seven people who are surveyed in a shop:<br>$15, 31, 12, 47, 21, 65, 12$.',parts=['Find the range of values.','Find the mean of this set of data.','Find the mode of this set of data.'],
          yq='Consider the test scores of $5$ people: $25, 19, 32, 25, 29$.',yparts=['Find the range of values.','Find the mean test score.','Find the mode test score.'],h=[14,20,10]),
     dict(n='Year 7 Example 4',t='Finding the median',q='Find the median of the following:',parts=['$7, 2, 8, 10, 9, 7, 13$','$12, 9, 15, 1, 23, 7$'],
          yq='Find the median of the following.',yparts=['$7, 2, 9, 3, 5, 1, 8$','$10, 2, 5, 7, 3, 3, 1, 8$'],h=22)],
 sc=CL(7,[3,4,5,6])),
'L5':dict(sub='9E',part=1,title='Measures of spread: range and IQR',src=[(8,'8E','pp. 575–577')],
 li=['To understand that range and interquartile range (IQR) are two measures of spread for numerical data','To be able to calculate the range of a set of numerical data','To be able to calculate the IQR of a set of numerical data'],
 ki=['The range and interquartile range are summary statistics known as <b>measures of spread</b>.','The range of a set of data is given by: Range $=$ highest number $-$ lowest number',
     'The <b>interquartile range</b> (or IQR) is found by the following procedure. Sort the data into ascending order. If there is an odd number of values, remove the middle one. Split the data into two equal-sized groups. The median of the lower half is called the <b>lower quartile</b>. The median of the upper half is called the <b>upper quartile</b>.',
     'IQR $=$ upper quartile $-$ lower quartile','Outliers affect the range but not the IQR.'],
 ex=[dict(n='Year 8 Example 9',t='Finding the range',q='Find the range of the following sets of data.',parts=['$1, 5, 2, 3, 8, 12, 4$','$-6, -20, 7, 12, -24, 19$'],yq='Find the range of the following sets of data.',yparts=['$2, 5, 12, 3, 10, 17$','$-3, 1, -6, 12, 8, -11$'],h=16),
     dict(n='Year 8 Example 10',t='Finding the interquartile range',q='Find the interquartile range (IQR) of the following sets of data.',parts=['$1, 15, 8, 2, 13, 10, 4, 14$','$2, 7, 11, 8, 3, 8, 10, 4, 9, 6, 8$'],
          yq='Find the interquartile range of the following sets of data.',yparts=['$7, 12, 3, 17, 5, 13, 1, 12$','$6, 10, 11, 9, 14, 13, 4$'],h=40)],
 sc=CL(8,[7,8])),
'L6':dict(sub='9E',part=2,title='Box plots',src=[(9,'9L','pp. 695–698')],
 li=['To understand how a box plot is used to display key values of a data set','To be able to read summary statistics from a box plot and interpret quartiles','To be able to construct a box plot for a data set'],
 ki=['A <b>box plot</b> (also called a box-and-whisker plot) is a graph which shows: maximum and minimum values; median $(Q_2)$; lower and upper quartiles $(Q_1$ and $Q_3)$.','A quarter $(25\\%)$ of the data is spread across each of the four sections of the graph.'],
 ex=[dict(n='Year 9 Example 20',t='Interpreting a box plot',split=True,q='This box plot summarises the price of all the books in a book shop.'+bplot(0,55,5,5,(5,15,20,35,50),'Price (&#36;)'),
          parts=['State the minimum and maximum book prices.','Find the range of the book prices.','State the median book price.','Find the interquartile range.','Fifty per cent of the books are priced below what amount?','Twenty-five per cent of the books are priced above what amount?','If there were $1000$ books in the store, how many would be priced below &#36;15?'],
          yq='This box plot summarises the number of air-conditioning units sold at an electrical store each day in summer.'+bplot(0,30,5,5,(0,10,15,25,30),'Number of sales'),
          yparts=['State the minimum and maximum number of units sold in a day.','Find the range of the number of sales.','State the median number of sales.','Find the interquartile range.','Fifty per cent of days had sales below what number?','Twenty-five per cent of days had sales above what number?','If there were $80$ days of sales, on how many days were there fewer than $10$ sales?'],h=[8,8,6,8,6,6,10]),
     dict(n='Year 9 Example 21',t='Constructing a box plot',split=True,q='The following set of data represents the $11$ scores resulting from throwing two dice and adding their scores.<br>$7 \\;\\; 10 \\;\\; 7 \\;\\; 12 \\;\\; 8 \\;\\; 9 \\;\\; 6 \\;\\; 6 \\;\\; 5 \\;\\; 4 \\;\\; 8$',
          parts=['Find:<br><b>i</b>&nbsp; the minimum value &nbsp; <b>ii</b>&nbsp; the maximum value &nbsp; <b>iii</b>&nbsp; the median<br><b>iv</b>&nbsp; the lower quartile &nbsp; <b>v</b>&nbsp; the upper quartile.','Draw a box plot to represent the data.'+numline(2,14,1,1,'',w=150)],
          yq='The following set of data represents the hours worked by a shift worker in their last $15$ shifts.<br>$6 \\;\\; 8 \\;\\; 4 \\;\\; 2 \\;\\; 6 \\;\\; 6 \\;\\; 7 \\;\\; 3 \\;\\; 5 \\;\\; 5 \\;\\; 6 \\;\\; 8 \\;\\; 7 \\;\\; 3 \\;\\; 5$',
          yparts=['Find:<br><b>i</b>&nbsp; the minimum value &nbsp; <b>ii</b>&nbsp; the maximum value &nbsp; <b>iii</b>&nbsp; the median<br><b>iv</b>&nbsp; the lower quartile &nbsp; <b>v</b>&nbsp; the upper quartile.','Draw a box plot to represent the data.'+numline(0,10,1,1,'',w=150)],h=[26,4])],
 sc=CL(9,[21,22])),
}
def fname(k):
    d=W[k];return f'C10-{d["sub"]} modified worksheet'+(f' (part {d["part"]})' if d.get('part') else '')
def page(k,d,R):
    srcs='; '.join(f'{BK[y]}, {s} {t}' for y,s,t in d['src'])
    o=[f'<div class="title"><div class="code">{d["sub"]}M</div><h1>{d["title"]}</h1><div class="pg">10MAG Modified · Lesson {k[1:]}</div></div>']
    o.append('<div class="box "><div class="hd">Learning intentions<span></span></div><div class="bd"><ul>'+''.join(f'<li>{x}</li>' for x in d['li'])+'</ul></div></div>')
    o.append('<div class="box "><div class="hd">Key ideas<span></span></div><div class="bd"><ul class="ki">'+''.join(f'<li>{R(x)}</li>' for x in d['ki'])+'</ul></div></div>')
    for e in d['ex']:
        hs=e['h'] if isinstance(e['h'],list) else [e['h']]*max(1,len(e['parts']))
        def col(q,parts):
            s=f'<p class="q">{R(q)}</p>'
            if not parts:return s+f'<div style="height:{hs[0]}mm"></div>'
            return s+''.join(f'<div class="ytp"><b>{"abcdefg"[i]}</b><div><div>{R(p)}</div><div style="height:{hs[i]}mm"></div></div></div>' for i,p in enumerate(parts))
        if e.get('split'):
            o.append(f'<div class="box"><div class="hd">{e["n"]} · {e["t"]}<span></span></div><div class="bd">{col(e["q"],e["parts"])}</div></div>')
            o.append(f'<div class="box"><div class="hd">You try<span></span></div><div class="bd">{col(e["yq"],e["yparts"])}</div></div>')
        else:
            fs='11.0pt' if len(e['t'])<30 else '9.5pt'
            o.append(f'<div class="pair"><div class="hd" style="font-size:{fs}">{e["n"]} · {e["t"]}</div><div class="hd" style="font-size:{fs}">You try</div>'
                     f'<div class="bd">{col(e["q"],e["parts"])}</div><div class="bd">{col(e["yq"],e["yparts"])}</div></div>')
    sc=''.join(f'<div class="sc"><div class="tick"></div><div><b>{t}</b></div></div>' for t in d['sc'])
    o.append(f'<div class="box split"><div class="hd">Skills checklist<span>Tick when you can do it</span></div><div class="bd">{sc}'
             f'<p class="src">Practice: your Freefall sheets for this lesson (in your modified unit workbook).</p><p class="src">{srcs}</p></div></div>')
    return ''.join(o)
def main(keys):
    css=open(os.path.join(HERE,'ws.css')).read()
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b=p.chromium.launch();pg=b.new_page()
        for k in keys:
            d=W[k];texts=[];page(k,d,lambda s:texts.append(s) or s);out=dict(zip(texts,katex(texts)));body=page(k,d,lambda s:out[s])
            html=f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>{fname(k)}</title><style>{css}{SHEETS}.box>.hd{{white-space:normal}}.sc{{break-inside:avoid}}.box>.hd span{{white-space:nowrap;margin-left:3mm}}</style></head><body><div id="flow">{body}</div>{PAGINATE}</body></html>'
            f=os.path.join(ROOT,'lessons',fname(k)+'.html');open(f,'w').write(html)
            pg.goto('file://'+os.path.abspath(f));pg.wait_for_selector('body[data-ready]');pg.wait_for_timeout(300)
            pg.pdf(path=f[:-5]+'.pdf',format='A4',print_background=True,prefer_css_page_size=True,margin={'top':'0','bottom':'0','left':'0','right':'0'});print(f)
        b.close()
if __name__=='__main__':main(sys.argv[1:] or list(W))
