r"""Add the 10MAG Modified level (L0) to the CFAT blocks C10-1A ... 1L (G3 Algebra and Linear Relations).
Run after the 10MAG blocks exist (gen_ch1b.py writes 1E-1L once; 1A-1C were built before it):  python3 tools/cfat/gen_ch1m.py
Year 8 first; Year 9 where the skill is first taught in Year 9. Every question verbatim from the cited page;
"adapted" = stem reworded so one part stands alone (Rocco OK'd 16 Nov). None of these is used on the modified worksheets.
Short weeks (CFAT 3.1.4M, 3.1.5M: fewer than 6 skills) get two L0 questions per skill.
1L skill 2 (intersecting region of two inequalities) has no Year 7-9 source: its L0 item is the 10MAG L1 item (Rocco's
Networks rule: easiest 10MAG item where there is no Year 7-9 source)."""
import os,sys,json
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE);sys.path.insert(0,os.path.join(HERE,'..','slides'));sys.path.insert(0,os.path.join(HERE,'..','worksheets'))
from modified_l0 import apply,C8,C9
from svgs import plane as PL
from ch1_data import region,L
from ch9 import numline
def sa(q,sol,src,vc,m=1,blank=None):
    d=dict(level='L0',type='sa',marks=m,q=q,sol=sol,src=src,vc2=vc)
    if blank:d['blank']=blank
    return d
P=lambda *a,**k:PL(*a,w=k.pop('w',150),**k)
AD='; adapted: stem reworded for a single part'
NL=lambda a,b:numline(a,b,1,1,'',w=110)
R='#d00000'
L0={}
# ---- CFAT 3.1.1M: 1A-1C
L0[('1A',1)]=[sa('Simplify the following by combining like terms.<br>$10a + 5b + 3a + 4b$',['$= 13a + 9b$'],f'{C8}, Exercise 5C Q5d (p. 349)'+AD,'VC2M9A02')]
L0[('1A',2)]=[sa('Simplify the following by expanding and then collecting like terms.<br>$4(2a + 8) + 7a$',['$= 8a + 32 + 7a$','$= 15a + 32$'],f'{C8}, Exercise 5G Q4c (p. 369)'+AD,'VC2M9A02')]
L0[('1A',3)]=[sa('Factorise the following by first finding the highest common factor.<br>$8v + 40$',['HCF $= 8$','$= 8(v + 5)$'],f'{C8}, Exercise 5H Q3b (p. 374); adapted: stem shortened for a single part','VC2M10A01')]
L0[('1A',4)]=[sa('Substitute $a = 2$ and $b = 5$ into $3a + 2b$.',['$= 3(2) + 2(5)$','$= 6 + 10 = 16$'],f'{C8}, Exercise 5B Q4e (p. 344)'+AD,'VC2M9A02')]
L0[('1B',1)]=[sa('Solve the following equation. Check your solution using substitution.<br>$7s + 7 = 3s + 19$',['$4s + 7 = 19$','$4s = 12$','$s = 3$ (check: $28 = 28$)'],f'{C8}, Exercise 7D Q2a (p. 499)'+AD,'VC2M9A03')]
L0[('1B',2)]=[sa('Solve the following equation algebraically.<br>$\\dfrac{2l}{5} = 8$',['$2l = 40$','$l = 20$'],f'{C8}, Exercise 7C Q2a (p. 493)'+AD,'VC2M9A03')]
L0[('1B',3)]=[sa('Simplify the following sum.<br>$\\dfrac{a}{2} + \\dfrac{a}{3}$',['$= \\dfrac{3a}{6} + \\dfrac{2a}{6}$','$= \\dfrac{5a}{6}$'],f'{C8}, Exercise 5E Q4e (p. 358)'+AD+' (Year 8 adds algebraic fractions but does not solve equations with them)','VC2M10A03')]
L0[('1C',1)]=[sa('Represent the following inequality on a number line.<br>$-2 < x \\leqslant 6$',['Open circle at $-2$, closed circle at $6$, line between'],f'{C8}, Exercise 7I Q4c (p. 525)'+AD,'VC2M9A03',blank=NL(-3,7))]
L0[('1C',2)]=[sa('Solve the following inequality and graph the solution on a number line.<br>$4l + 9 \\geqslant 21$',['$4l \\geqslant 12$','$l \\geqslant 3$ (closed circle at $3$, arrow right)'],f'{C8}, Exercise 7J Q2b (p. 530); adapted: stem reworded for a single part, ‘graph the solution on a number line’ added','VC2M9A03',blank=NL(0,7))]
# ---- CFAT 3.1.2M: 1E-1F
L0[('1E',1)]=[sa('For the rule $y = 3x - 1$, decide if the given points lie on the graph.<br><b>i</b>&nbsp; $(1, 1)$ &nbsp;&nbsp; <b>ii</b>&nbsp; $(2, 5)$',['i $3(1) - 1 = 2 \\ne 1$: no','ii $3(2) - 1 = 5$: yes'],f'{C8}, Exercise 9B Q4b (p. 647)'+AD,'VC2M9A06')]
L0[('1E',2)]=[sa('State the gradient and $y$-intercept coordinates for the graph of $y = 3x + 4$.',['$m = 3$, $y$-intercept $(0, 4)$'],f'{C9}, Exercise 4F Q1a (p. 280)'+AD,'VC2M9A06')]
L0[('1E',3)]=[sa('Find the gradient and $y$-intercept for $y = x - 2$ and sketch its graph.',['$m = 1$, $y$-intercept $(0, -2)$',P(-3,4,-4,3,[L(1,-2),('pt',(0,-2),'(0, −2)',8,10),('pt',(2,0),'(2, 0)',4,-6)])],f'{C9}, Exercise 4F Q3a (p. 280)'+AD,'VC2M9A06',2)]
L0[('1E',4)]=[sa('For the graph of the rule $y = 4x - 12$, find the $x$- and $y$-intercepts.',['$y = 0$: $4x = 12$, $x = 3$: $(3, 0)$','$x = 0$: $y = -12$: $(0, -12)$'],f'{C8}, Exercise 9F Q2e (p. 684)'+AD,'VC2M9A06')]
L0[('1E',5)]=[sa('Sketch the graph of the horizontal line $y = 4$.',[P(-3,3,-1,5,[('line',(0,4),(1,4)),('lab',(1.2,4.4),'y = 4','start')])],f'{C9}, Exercise 4C Q1c (p. 261)'+AD,'VC2M9A06')]
L0[('1E',6)]=[sa('Sketch the graph of the linear relation $y = 2x$, which passes through the origin.',[P(-3,3,-4,5,[L(2,0),('pt',(1,2),'(1, 2)',8,0)])],f'{C9}, Exercise 4C Q2a (p. 261)'+AD,'VC2M9A06')]
L0[('1F',1)]=[sa('Find the gradient of the line joining $A(2, 3)$ and $B(3, 5)$.',['$m = \\dfrac{5 - 3}{3 - 2} = 2$'],f'{C9}, Exercise 4D Q2a (p. 270)'+AD,'VC2M9A06')]
L0[('1F',2)]=[sa('Find the equation of the line for which the gradient is $m = 3$ and one point is $(1, 8)$.',['$8 = 3(1) + c$, $c = 5$','$y = 3x + 5$'],f'{C9}, Exercise 4G Q2a (p. 288)'+AD+' (Year 9 uses a point, not the y-intercept)','VC2M9A06')]
L0[('1F',3)]=[sa('For the line connecting $(2, 6)$ and $(4, 10)$:<br><b>i</b>&nbsp; find the gradient &nbsp;&nbsp; <b>ii</b>&nbsp; find the equation.',['i $m = \\dfrac{10 - 6}{4 - 2} = 2$','ii $6 = 2(2) + c$, $c = 2$: $y = 2x + 2$'],f'{C9}, Exercise 4G Q4a (p. 288)'+AD,'VC2M9A06',2)]
# ---- CFAT 3.1.3M: 1G-1H
L0[('1G',1)]=[sa('Find the length of the segment joining $(1, 2)$ and $(3, 4)$ correct to two decimal places.',['$d = \\sqrt{2^2 + 2^2} = \\sqrt{8}$','$\\approx 2.83$'],f'{C9}, Exercise 4H Q2b (p. 293)'+AD,'VC2M10A06')]
L0[('1G',2)]=[sa('Find the midpoint $M(x, y)$ of the line segment joining $(3, 0)$ and $(5, 2)$.',['$M = \\left(\\dfrac{3 + 5}{2}, \\dfrac{0 + 2}{2}\\right) = (4, 1)$'],f'{C9}, Exercise 4H Q1c (p. 293)'+AD,'VC2M10A06')]
L0[('1G',3)]=[sa('$M$ is the midpoint of points $A$ and $B$. $A$ is $(4, 2)$ and $M$ is $(6, 1)$. Find the coordinates of $B$.',['$\\dfrac{4 + x}{2} = 6$, $x = 8$; $\\dfrac{2 + y}{2} = 1$, $y = 0$','$B(8, 0)$'],f'{C9}, Exercise 4H Q3 row 1 (p. 293); adapted: table row written as a sentence (Year 9 finds coordinates from a midpoint, not a distance)','VC2M10A06')]
L0[('1H',1)]=[sa('Using $m_2 = -\\dfrac{1}{m_1}$, find the gradient of a line perpendicular to the line with gradient $m_1 = \\dfrac{2}{3}$.',['$m_2 = -\\dfrac{3}{2}$'],f'{C9}, Exercise 4I Q7a i (p. 298)'+AD,'VC2M10A06')]
L0[('1H',2)]=[sa('Find the equation of the line that is parallel to $y = 4x + 2$ and passes through $(0, 8)$.',['$m = 4$, $c = 8$','$y = 4x + 8$'],f'{C9}, Exercise 4I Q1a (p. 297)'+AD,'VC2M10A06')]
L0[('1H',3)]=[sa('Find the equation of the line that is perpendicular to $y = 3x - 2$ and passes through $(0, 3)$.',['$m = -\\dfrac{1}{3}$, $c = 3$','$y = -\\dfrac{1}{3}x + 3$'],f'{C9}, Exercise 2I'.replace('2I','4I')+' Q2a (p. 297)'+AD,'VC2M10A06')]
# ---- CFAT 3.1.4M: 1I-1J (short week: two per skill)
EQ=lambda a,b:f'$\\begin{{aligned}}{a}\\\\{b}\\end{{aligned}}$'
L0[('1I',1)]=[sa('Solve the following pair of simultaneous equations by using substitution.<br>'+EQ('5x + y = 5','y = 1 - x'),['$5x + (1 - x) = 5$','$4x = 4$, $x = 1$','$y = 1 - 1 = 0$'],f'{C9}, Exercise 2I Q2c (p. 141)'+AD,'VC2M10A04',2),
             sa('Solve the following pair of simultaneous equations by using substitution.<br>'+EQ('3x - y = 7','y = x + 5'),['$3x - (x + 5) = 7$','$2x = 12$, $x = 6$','$y = 6 + 5 = 11$'],f'{C9}, Exercise 2I Q3a (p. 141)'+AD,'VC2M10A04',2)]
L0[('1J',1)]=[sa('Solve these simultaneous equations by first adding the equations.<br>'+EQ('4x + 3y = 5','-4x - 5y = -3'),['Add: $-2y = 2$, $y = -1$','$4x - 3 = 5$, $x = 2$'],f'{C9}, Exercise 2J Q1c (p. 149)'+AD,'VC2M10A04',2),
             sa('Solve these simultaneous equations by first subtracting the equations.<br>'+EQ('2x + 7y = 9','2x + 5y = 11'),['Subtract: $2y = -2$, $y = -1$','$2x - 7 = 9$, $x = 8$'],f'{C9}, Exercise 2J Q2b (p. 149)'+AD,'VC2M10A04',2)]
L0[('1J',2)]=[sa('Solve the following pair of simultaneous linear equations by using elimination.<br>'+EQ('-x + 4y = 2','3x - 8y = -2'),['$2 \\times [1]$: $-2x + 8y = 4$','Add: $x = 2$','$-2 + 4y = 2$, $y = 1$'],f'{C9}, Exercise 2J Q3c (p. 149)'+AD,'VC2M10A04',2),
             sa('Solve the following pair of simultaneous linear equations by using elimination.<br>'+EQ('3x + 2y = 0','4x + y = -5'),['$2 \\times [2]$: $8x + 2y = -10$','Subtract: $5x = -10$, $x = -2$','$-8 + y = -5$, $y = 3$'],f'{C9}, Exercise 2J Q3d (p. 149)'+AD,'VC2M10A04',2)]
# ---- CFAT 3.1.5M: 1K-1L (short week)
L0[('1K',1)]=[sa('Mila plants $820$ hectares of potatoes and corn. To maximise his profit he plants $140$ hectares more of potatoes than of corn. How many hectares of each does he plant?',['$p + c = 820$, $p = c + 140$','$2c + 140 = 820$, $c = 340$','$p = 480$: $480$ ha potatoes, $340$ ha corn'],f'{C9}, Exercise 2K Q2 (p. 153)','VC2M10A04',2),
             sa('Mal bought three bottles of milk and four bags of chips for a total of \\$17. At the same shop, Barbara bought one bottle of milk and five bags of chips for \\$13. Find how much each bottle of milk and each bag of chips cost.',['$3m + 4c = 17$, $m + 5c = 13$','$m = 13 - 5c$: $39 - 15c + 4c = 17$, $c = 2$','$m = 3$: milk \\$3, chips \\$2'],f'{C9}, Exercise 2K Q3 (p. 154); adapted: steps a–d left out','VC2M10A04',2)]
L0[('1L',1)]=[sa('Sketch the following region.<br>$y > -2$',['Dashed line $y = -2$, shade above',P(-3,3,-4,3,[region(-3,3,-4,3,[(0,-1,2)]),('line',(0,-2),(1,-2),R,True),('lab',(1.6,-1.6),'y = −2','start')])],f'{C8}, Exercise 9E Q3b (p. 674)'+AD,'VC2M10A08'),
             sa('Sketch the following region.<br>$x \\leqslant -4$',['Solid line $x = -4$, shade to the left',P(-6,2,-3,3,[region(-6,2,-3,3,[(1,0,-4)]),('line',(-4,0),(-4,1)),('lab',(-3.8,2.3),'x = −4','start')])],f'{C8}, Exercise 9E Q3f (p. 674)'+AD,'VC2M10A08')]
b=json.load(open(os.path.join(HERE,'C10-1L.json')))
L0[('1L',2)]=[dict(next(i for i in b['skills'][1]['items'] if i['level']=='L1'),level='L0')]
L0[('1L',2)][0]['src']+='; same as the 10MAG L1 item (no Year 7–9 source)'
apply(L0,['1A','1B','1C','1E','1F','1G','1H','1I','1J','1K','1L'],'10MAG Modified (Year 8; Year 9 where first taught in Year 9)')
