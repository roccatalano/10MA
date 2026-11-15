r"""Chapter 1 (C10) slide content, one entry per subchapter. Shared by the 10MAA and 10MAG decks.

Conventions (see build.py):
  parts: (label, question, lines[, fig_html])   question = TeX (no $); '!' prefix = HTML text with $..$
  lines: TeX (no $). '!' prefix = HTML text with $..$ ; '<svg' = a diagram step; '*' prefix = bold answer line.
         If no line is marked '*', the last TeX line is bold.
  Worked examples = the book's SOLUTION lines. You try = teacher working in the same steps (answers checked
  against the book's Now you try answers, pp. 956-969). APK + exit-task working = teacher.
"""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from svgs import numberline as NL, plane as PL
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','worksheets'))
import svg as WS   # worksheet diagrams (APK)

KI_LIKE=r"<b>Like terms</b> have the same pronumeral part and, using addition and subtraction, can be collected to form a single term.<div class='kf'>$3x - 7x + x = -3x$ &emsp; $6a^2b - ba^2 = 5a^2b$</div><div class='kn'>Note that $a^2b = ba^2$</div>"
KI_MULT=r"The symbols for multiplication $(\times)$ and division $(\div)$ are usually not shown.<div class='kf'>$7 \times x \div y = \dfrac{7x}{y}$ &emsp; $-6a^2b \div (ab) = \dfrac{-6a^2b}{ab} = -6a$</div>"
KI_DIST=r"The <b>distributive law</b> is used to expand brackets.<div class='kf'>$a(b + c) = ab + ac$ &emsp; $a(b - c) = ab - ac$</div><div class='kn'>e.g. $2(x + 7) = 2x + 14$, &nbsp;$-x(3 - x) = -3x + x^2$</div>"
KI_HCF=r"<b>Factorisation</b> involves writing expressions as a product of factors. Many expressions can be factorised by taking out the highest common factor (HCF).<div class='kf'>$3x - 12 = 3(x - 4)$</div>"
KI_EVAL=r"Expressions can be <b>evaluated</b> by substituting a value for each pronumeral (variable). Order of operations are followed."
KI_SOLVE=r"We <b>solve</b> linear equations by operating on both sides of the equation until a solution is found: inverse operations (<b>backtracking</b>), collecting like terms, expanding brackets, multiplying by the denominator."
KI_LCD=r"Algebraic fractions can be added or subtracted by first finding the <b>lowest common denominator (LCD)</b> and then combining the numerators."
KI_CIRC=r"An <b>open circle</b> is used for $<$ or $>$ (endpoint not included).<br>A <b>closed circle</b> is used for $\leqslant$ or $\geqslant$ (endpoint included)."
KI_REV=r"Solve like a linear equation, except <b>reverse the inequality sign</b> if you multiply or divide by a negative number, or if the sides are switched.<div class='kn'>e.g. if $-2x < 4$, then $x > -2$; if $2 \geqslant x$, then $x \leqslant 2$.</div>"
KI_LCD2=r"Add and subtract algebraic fractions by first finding the <b>LCD</b>, then combining the numerators. Solving equations can involve <b>multiplying by the LCD</b>.<div class='kn'>Expand numerators carefully: $-2(x + 1) = -2x - 2$</div>"
KI_ONLINE=r"A point is on the line if its coordinates make the equation <b>true</b> (LHS = RHS)."
KI_GI=r"<b>Gradient–intercept form</b> $y = mx + c$: $m$ is the gradient and $(0, c)$ is the $y$-intercept.<div class='kf'>$m = \dfrac{\text{rise}}{\text{run}}$</div>"
KI_INT=r"<b>$y$-intercept:</b> let $x = 0$.<br><b>$x$-intercept:</b> let $y = 0$."
KI_SPEC=r"Horizontal lines $y = c$ &emsp; Vertical lines $x = b$<br>Lines through the origin $y = mx$"
KI_GRAD=r"<div class='kf'>$m = \dfrac{y_2 - y_1}{x_2 - x_1}$</div><div class='kn'>where $(x_1, y_1)$ and $(x_2, y_2)$ are points on the line</div>"
KI_YMC=r"Given the gradient $(m)$ and the $y$-intercept $(0, c)$, use $y = mx + c$ to state the equation of the line.<div class='kf'>$m = \dfrac{y_2 - y_1}{x_2 - x_1}$</div>"
KI_2PT=r"Given two points: find the gradient $(m)$, then substitute a point to find $c$ in $y = mx + c$, or use<div class='kf'>$y - y_1 = m(x - x_1)$</div>"
KI_DIST2=r"<div class='kf'>$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$</div><div class='kn'>(Pythagoras’ theorem)</div>"
KI_MID=r"<div class='kf'>$M = \left(\dfrac{x_1 + x_2}{2}, \dfrac{y_1 + y_2}{2}\right)$</div><div class='kn'>the average of the $x$-coordinates and of the $y$-coordinates</div>"
KI_PP=r"<b>Parallel</b> lines: $m_1 = m_2$<br><b>Perpendicular</b> lines: $m_1 \times m_2 = -1$<div class='kf'>$m_2 = -\dfrac{1}{m_1}$</div>"
KI_PPEQ=r"Find the gradient $(m)$ (same, or negative reciprocal), then substitute the point to find $c$ in $y = mx + c$."
KI_SUB=r"The <b>substitution method</b> is used when one equation has a pronumeral as the subject, e.g. $y = 3x + 2$. Substitute it into the other equation, then solve."
KI_ELIM=r"The <b>elimination method</b> is used when both equations are in the form $ax + by = d$. Add or subtract the equations to eliminate one pronumeral (multiply first if there is no matching pair)."
KI_APP=r"Define a variable for each unknown. Write two equations. Solve simultaneously. Answer the question in words."
KI_REG=r"$\geqslant, \leqslant$: <b>solid</b> line &emsp; $>, <$: <b>broken</b> line<br>Test a point, e.g. $(0, 0)$, to decide which side to shade."
KI_INTR=r"The <b>intersecting region</b> is where both regions overlap. Find and label the <b>point of intersection</b> of the two lines."

# ---------- diagrams ----------
def L(m,c): return ('line',(0,c),(1,m+c))
def LB(m,c): return ('line',(0,c),(1,m+c),'#000')   # question graph (black)
def region(x0,x1,y0,y1,hp):
    """polygon of the box clipped by half-planes a*x+b*y<=c"""
    P=[(x0,y0),(x1,y0),(x1,y1),(x0,y1)]
    for a,b,c in hp:
        Q=[];n=len(P)
        for i in range(n):
            p,q=P[i],P[(i+1)%n];fp=a*p[0]+b*p[1]-c;fq=a*q[0]+b*q[1]-c
            if fp<=0:Q.append(p)
            if fp*fq<0:t=fp/(fp-fq);Q.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
        P=Q
    return ('poly',P)

S={}
# ======================================================================== 1A
S['1A']=dict(
 apk_src="Cambridge Essential Mathematics 3rd Ed: Year 7 Ch4 checklist item 11 (p. 278); Year 8 Ch5 checklist items 6, 15 (p. 400); Year 9 Ch2 checklist item 2 (p. 162). Working by teacher.",
 apk=[dict(skill='Year 7 · I can simplify expressions involving multiplication.',q=r'Simplify $4a \times 2b \times 3c$, giving your final answer without multiplication signs.',w=[r'= 24abc']),
      dict(skill='Year 8 · I can simplify expressions by combining like terms.',q=r'Simplify $5ac + 3b - 2ca + 4b - 5b$.',w=[r'= 3ac + 2b']),
      dict(skill='Year 8 · I can factorise expressions by taking out the highest common factor.',q=r'Factorise $12a + 18ab$.',w=[r'= 6a(2 + 3b)']),
      dict(skill='Year 9 · I can substitute values into expressions and evaluate.',q=r'Evaluate $a^2 + 3(ab - c)$ if $a = -2$, $b = 3$ and $c = -8$.',w=[r'= (-2)^2 + 3\big((-2)(3) - (-8)\big)',r'= 4 + 3(2)',r'= 10'])],
 ki_html='TEMPLATE',
 ex=[dict(n=1,page=6,kp='p. 5',instr='Simplify by collecting like terms.',ki=KI_LIKE,
          parts=[('a','7a + 3a',['= 10a']),('b','3a^2b - 2a^2b',['= a^2b']),('c','5xy + 2xy^2 - 2xy + 3y^2x',['= 3xy + 5xy^2'])],
          yt=[('a','4a + 13a',['= 17a']),('b','5ab^2 - 2ab^2',['= 3ab^2']),('c','3xy + 4x^2y - xy + 2yx^2',['= 2xy + 6x^2y'])]),
     dict(n=2,page=6,kp='p. 5',instr='Simplify the following.',ki=KI_MULT,
          parts=[('a',r'2h \times 7l',['= 14hl']),('b',r'-3pr \times 2p',['= -6p^2r']),('c',r'-\dfrac{7xy}{14y}',[r'= -\dfrac{x}{2}'])],
          yt=[('a',r'3a \times 6b',['= 18ab']),('b',r'-2xy \times 5x',['= -10x^2y']),('c',r'-\dfrac{4ab}{8a}',[r'= -\dfrac{b}{2}'])]),
     dict(n=3,page=7,kp='p. 5',instr='Expand the following using the distributive law. Simplify where possible.',ki=KI_DIST,
          parts=[('a','2(x + 4)',['= 2x + 8']),('b','-3x(x - y)',['= -3x^2 + 3xy']),('c','3(x + 2) - 4(2x - 4)',['= 3x + 6 - 8x + 16','= -5x + 22'])],
          yt=[('a','3(x + 2)',['= 3x + 6']),('b','-2x(x - y)',['= -2x^2 + 2xy']),('c','2(x + 3) - 3(2x - 1)',['= 2x + 6 - 6x + 3','= -4x + 9'])]),
     dict(n=4,page=7,kp='p. 5',instr='Factorise:',ki=KI_HCF,
          parts=[('a','3x - 9',['= 3(x - 3)']),('b','2x^2 + 4x',['= 2x(x + 2)'])],
          yt=[('a','2x - 10',['= 2(x - 5)']),('b','3x^2 + 9x',['= 3x(x + 3)'])]),
     dict(n=5,page=8,kp='p. 4',instr=r'Evaluate $a^2 - 2bc$ if $a = -3$, $b = 5$ and $c = -1$.',yinstr=r'Evaluate $b^2 - 3ac$ if $a = 1$, $b = -2$ and $c = -3$.',ki=KI_EVAL,
          parts=[('','',[r'a^2 - 2bc = (-3)^2 - 2(5)(-1)',r'= 9 - (-10)','= 19'])],
          yt=[('','',[r'b^2 - 3ac = (-2)^2 - 3(1)(-3)',r'= 4 - (-9)','= 13'])])],
 exit=[dict(q=r'Simplify $3x \times 2y - 4x^2y + 2xy + 3x^2y$.',w=['= 6xy - 4x^2y + 2xy + 3x^2y','= 8xy - x^2y']),
       dict(q=r'Expand and simplify $-4y(2y + 3)$.',w=['= -8y^2 - 12y']),
       dict(q=r'Factorise $6x^2 - 15x$.',w=['= 3x(2x - 5)']),
       dict(q=r'Given $a = -3$ and $b = 4$, evaluate $ab + a^2$.',w=['= (-3)(4) + (-3)^2','= -12 + 9','= -3'])],
)
# ======================================================================== 1B
S['1B']=dict(
 apk=[dict(q=r'Solve $7 + 4a = 23$ algebraically.',w=['4a = 16','a = 4']),
      dict(q=r'Solve $6x + 4 = 22 - 3x$ algebraically.',w=['9x + 4 = 22','9x = 18','x = 2']),
      dict(q=r'Solve $2(4x + 3) = 7$.',w=['8x + 6 = 7','8x = 1',r'x = \dfrac{1}{8}'])],
 ex=[dict(n=6,page=12,kp='p. 11',instr='Solve the following equations and check your solution using substitution.',ki=KI_SOLVE,
          parts=[('a','4x + 5 = 17',['4x = 12','*x = 3',r'\text{Check: LHS} = 4 \times 3 + 5 = 17,\ \text{RHS} = 17']),
                 ('b','3(2x + 5) = 4x',['6x + 15 = 4x','2x + 15 = 0','2x = -15',r'*x = -\dfrac{15}{2}',r'\text{Check: LHS} = 3\left(2 \times \left(-\dfrac{15}{2}\right) + 5\right) = -30',r'\text{RHS} = 4 \times \left(-\dfrac{15}{2}\right) = -30'])],
          yt=[('a','2x + 7 = 13',['2x = 6','*x = 3',r'\text{Check: LHS} = 2 \times 3 + 7 = 13,\ \text{RHS} = 13']),
              ('b','4(2x + 1) = 2x',['8x + 4 = 2x','6x + 4 = 0','6x = -4',r'*x = -\dfrac{2}{3}',r'\text{Check: LHS} = 4\left(2 \times \left(-\dfrac{2}{3}\right) + 1\right) = -\dfrac{4}{3}',r'\text{RHS} = 2 \times \left(-\dfrac{2}{3}\right) = -\dfrac{4}{3}'])]),
     dict(n=7,page=13,kp='p. 11',instr='Solve the following equations and check your solution using substitution.',ki=KI_SOLVE,
          parts=[('a',r'\dfrac{x + 3}{4} = 2',['x + 3 = 8','*x = 5',r'\text{Check: LHS} = \dfrac{5 + 3}{4} = 2,\ \text{RHS} = 2']),
                 ('b',r'4 - \dfrac{x}{2} = 7',[r'-\dfrac{x}{2} = 3','*x = -6',r'\text{Check: LHS} = 4 - \dfrac{(-6)}{2} = 4 + 3 = 7',r'\text{RHS} = 7']),
                 ('c',r'\dfrac{5 - x}{4} = x - 3',['5 - x = 4(x - 3)','5 - x = 4x - 12','5 = 5x - 12',r'\therefore 5x = 17',r'*x = \dfrac{17}{5}',r'\text{Check: LHS} = \dfrac{5 - \frac{17}{5}}{4} = \dfrac{8}{5} \div 4 = \dfrac{2}{5}',r'\text{RHS} = \dfrac{17}{5} - 3 = \dfrac{2}{5}'])],
          yt=[('a',r'\dfrac{x + 1}{3} = 4',['x + 1 = 12','*x = 11',r'\text{Check: LHS} = \dfrac{11 + 1}{3} = 4,\ \text{RHS} = 4']),
              ('b',r'2 - \dfrac{x}{5} = 6',[r'-\dfrac{x}{5} = 4','*x = -20',r'\text{Check: LHS} = 2 - \dfrac{(-20)}{5} = 2 + 4 = 6',r'\text{RHS} = 6']),
              ('c',r'\dfrac{4 - x}{3} = x + 2',['4 - x = 3(x + 2)','4 - x = 3x + 6','4 = 4x + 6',r'\therefore 4x = -2',r'*x = -\dfrac{1}{2}',r'\text{Check: LHS} = \dfrac{4 - \left(-\frac{1}{2}\right)}{3} = \dfrac{9}{2} \div 3 = \dfrac{3}{2}',r'\text{RHS} = -\dfrac{1}{2} + 2 = \dfrac{3}{2}'])]),
     dict(n=8,page=14,kp='p. 11',instr='Consider these algebraic fractions.',ki=KI_LCD,
          parts=[('a',r'!Simplify $\dfrac{a}{6} + \dfrac{2a}{9}$',[r'= \dfrac{3a}{18} + \dfrac{4a}{18}',r'= \dfrac{7a}{18}']),
                 ('b',r'!Hence, solve $\dfrac{a}{6} + \dfrac{2a}{9} = 2$',[r'\text{From part a, } \dfrac{a}{6} + \dfrac{2a}{9} = \dfrac{7a}{18}',r'\text{Solve } \dfrac{7a}{18} = 2','7a = 36',r'\therefore a = \dfrac{36}{7}'])],
          yt=[('a',r'!Simplify $\dfrac{3a}{8} + \dfrac{a}{6}$',[r'= \dfrac{9a}{24} + \dfrac{4a}{24}',r'= \dfrac{13a}{24}']),
              ('b',r'!Hence, solve $\dfrac{3a}{8} + \dfrac{a}{6} = 2$',[r'\text{From part a, } \dfrac{3a}{8} + \dfrac{a}{6} = \dfrac{13a}{24}',r'\text{Solve } \dfrac{13a}{24} = 2','13a = 48',r'\therefore a = \dfrac{48}{13}'])])],
 exit=[dict(q=r'Solve $4(3x - 5) = 7x$.',w=['12x - 20 = 7x','5x - 20 = 0','5x = 20','x = 4']),
       dict(q=r'Solve $\dfrac{x + 1}{3} = 4$ and $\dfrac{x}{2} - 3 = 7$.',w=['x + 1 = 12','*x = 11',r'\dfrac{x}{2} = 10','*x = 20']),
       dict(q=r'Simplify $\dfrac{x}{4} + \dfrac{2x}{3}$ and hence, solve $\dfrac{x}{4} + \dfrac{2x}{3} = 2$.',w=[r'= \dfrac{3x}{12} + \dfrac{8x}{12} = \dfrac{11x}{12}',r'\dfrac{11x}{12} = 2 \;\Rightarrow\; 11x = 24',r'x = \dfrac{24}{11}'])],
)
# ======================================================================== 1C
S['1C']=dict(
 apk=[dict(q=r'Insert the symbol $<$ (less than) or $>$ (greater than) into the statement $-1 \;\boxed{\phantom{<}}\; -6$ to make it true.',w=['-1 > -6']),
      dict(q=r'Solve $15 - 2x > 1$ algebraically.',w=['-2x > -14',r'x < 7 \quad (\text{reverse: } \div\, -2)']),
      dict(q=r'Show $x$ is less than or equal to 3 $(x \leqslant 3)$ on a number line.',w=[NL(0,5,right=(3,True),w=280)])],
 ex=[dict(n=9,page=19,kp='p. 18',instr='Write as an inequality.',ki=KI_CIRC,
          parts=[('a','!'+NL(0,4,labels=[1,2,3],left=(2,False),w=230),['x > 2']),('b','!'+NL(-4,1,labels=[-3,-2,-1,0],left=(-3,True),right=(0,False),w=260),[r'-3 \leqslant x < 0'])],
          yt=[('a','!'+NL(-1,3,labels=[0,1,2],right=(2,False),w=230),['x < 2']),('b','!'+NL(-5,0,labels=[-4,-3,-2,-1],left=(-4,False),right=(-1,True),w=260),[r'-4 < x \leqslant -1'])]),
     dict(n=10,page=20,kp='pp. 18–19',instr='Solve the following inequalities and graph their solutions on a number line.',ki=KI_REV,
          parts=[('a','3x + 4 > 13',['3x > 9',r'\therefore x > 3',NL(0,6,labels=[1,2,3,4,5],left=(3,False),w=250)]),
                 ('b',r'4 - \dfrac{x}{3} \leqslant 6',[r'-\dfrac{x}{3} \leqslant 2',r'\therefore x \geqslant -6',NL(-8,-2,labels=[-7,-6,-5,-4,-3],left=(-6,True),w=250)]),
                 ('c','3x + 2 > 6x - 4',['2 > 3x - 4','6 > 3x','2 > x',r'\therefore x < 2',NL(-2,4,labels=[-1,0,1,2,3],right=(2,False),w=250)])],
          yt=[('a','2x + 5 > 11',['2x > 6',r'\therefore x > 3',NL(1,5,labels=[2,3,4],left=(3,False),w=250)]),
              ('b',r'2 - \dfrac{x}{3} \leqslant 4',[r'-\dfrac{x}{3} \leqslant 2',r'\therefore x \geqslant -6',NL(-8,-4,labels=[-7,-6,-5],left=(-6,True),w=250)]),
              ('c','4x + 1 > 7x - 2',['1 > 3x - 2','3 > 3x','1 > x',r'\therefore x < 1',NL(-1,3,labels=[0,1,2],right=(1,False),w=250)])])],
 exit=[dict(q='Write as an inequality.<br>'+NL(-3,2,labels=[-2,-1,0,1],left=(-1,True),w=260),w=[r'x \geqslant -1']),
       dict(q=r'Solve $4 - \dfrac{x}{3} > 8$ and represent the solution on a number line.',w=[r'-\dfrac{x}{3} > 4',r'*x < -12',NL(-15,-10,labels=[-14,-13,-12,-11],right=(-12,False),w=260)])],
)
# ======================================================================== 1D
S['1D']=dict(
 apk=[dict(q=r'Find the value of $\dfrac{3}{4} + \dfrac{5}{6}$.',w=[r'= \dfrac{9}{12} + \dfrac{10}{12}',r'= \dfrac{19}{12} = 1\dfrac{7}{12}']),
      dict(q=r'Simplify $\dfrac{4a}{3} + \dfrac{2a}{5}$ and $\dfrac{a}{6} - \dfrac{b}{9}$.',w=[r'\dfrac{20a}{15} + \dfrac{6a}{15} = \dfrac{26a}{15}',r'\dfrac{3a}{18} - \dfrac{2b}{18} = \dfrac{3a - 2b}{18}']),
      dict(q=r'Solve $\dfrac{4x - 2}{3} = 6$.',w=['4x - 2 = 18','4x = 20','x = 5'])],
 ex=[dict(n=11,page=25,kp='p. 24',instr='Simplify the following algebraic expressions.',ki=KI_LCD2,
          parts=[('a',r'\dfrac{x + 3}{2} + \dfrac{x - 2}{5}',[r'= \dfrac{5(x + 3)}{10} + \dfrac{2(x - 2)}{10}',r'= \dfrac{5(x + 3) + 2(x - 2)}{10}',r'= \dfrac{5x + 15 + 2x - 4}{10}',r'= \dfrac{7x + 11}{10}']),
                 ('b',r'\dfrac{2x - 1}{3} - \dfrac{x - 1}{4}',[r'= \dfrac{4(2x - 1)}{12} - \dfrac{3(x - 1)}{12}',r'= \dfrac{4(2x - 1) - 3(x - 1)}{12}',r'= \dfrac{8x - 4 - 3x + 3}{12}',r'= \dfrac{5x - 1}{12}'])],
          yt=[('a',r'\dfrac{x + 1}{3} + \dfrac{x - 2}{2}',[r'= \dfrac{2(x + 1)}{6} + \dfrac{3(x - 2)}{6}',r'= \dfrac{2(x + 1) + 3(x - 2)}{6}',r'= \dfrac{2x + 2 + 3x - 6}{6}',r'= \dfrac{5x - 4}{6}']),
              ('b',r'\dfrac{3x - 2}{2} - \dfrac{x - 2}{5}',[r'= \dfrac{5(3x - 2)}{10} - \dfrac{2(x - 2)}{10}',r'= \dfrac{5(3x - 2) - 2(x - 2)}{10}',r'= \dfrac{15x - 10 - 2x + 4}{10}',r'= \dfrac{13x - 6}{10}'])]),
     dict(n=12,page=26,kp='p. 24',instr='Solve the following equations. You can check your answer using substitution.',ki=KI_LCD2,
          parts=[('a',r'\dfrac{4x - 2}{3} = \dfrac{3x - 1}{2}',[r'\dfrac{6(4x - 2)}{3} = \dfrac{6(3x - 1)}{2}','2(4x - 2) = 3(3x - 1)','8x - 4 = 9x - 3','-4 = x - 3','-1 = x',r'\therefore x = -1']),
                 ('b',r'\dfrac{x + 2}{3} - \dfrac{2x - 1}{2} = 4',[r'\dfrac{2(x + 2)}{6} - \dfrac{3(2x - 1)}{6} = 4',r'\dfrac{2x + 4 - 6x + 3}{6} = 4',r'\dfrac{-4x + 7}{6} = 4','-4x + 7 = 24','-4x = 17',r'x = -\dfrac{17}{4}'])],
          yt=[('a',r'\dfrac{2x - 1}{3} = \dfrac{x - 3}{4}',[r'\dfrac{12(2x - 1)}{3} = \dfrac{12(x - 3)}{4}','4(2x - 1) = 3(x - 3)','8x - 4 = 3x - 9','5x - 4 = -9','5x = -5',r'\therefore x = -1']),
              ('b',r'\dfrac{x + 1}{2} - \dfrac{2x - 1}{3} = 2',[r'\dfrac{3(x + 1)}{6} - \dfrac{2(2x - 1)}{6} = 2',r'\dfrac{3x + 3 - 4x + 2}{6} = 2',r'\dfrac{-x + 5}{6} = 2','-x + 5 = 12','-x = 7','x = -7'])])],
 exit=[dict(q=r'Simplify $\dfrac{x + 2}{5} - \dfrac{x + 4}{7}$.',w=[r'= \dfrac{7(x + 2) - 5(x + 4)}{35}',r'= \dfrac{7x + 14 - 5x - 20}{35}',r'= \dfrac{2x - 6}{35}']),
       dict(q=r'Solve $\dfrac{x + 1}{3} + \dfrac{x - 2}{5} = 2$ and $\dfrac{1 - 2x}{3} = \dfrac{x + 1}{2}$.',w=[r'\dfrac{5(x + 1) + 3(x - 2)}{15} = 2 \Rightarrow 8x - 1 = 30',r'*x = \dfrac{31}{8}',r'2(1 - 2x) = 3(x + 1) \Rightarrow 2 - 4x = 3x + 3',r'*x = -\dfrac{1}{7}'])],
)
# ======================================================================== 1E
P=lambda *a,**k:PL(*a,**k)
S['1E']=dict(
 apk=[dict(q=r'For the rule $\textit{output}(y) = \textit{input}(x) + 1$, construct a table of values using $\textit{input}$ values of $0, 1, 2$ and $3$. Use the table of coordinates to plot a graph.',
           w=[r'!<table class="tv"><tr><td>$x$</td><td>0</td><td>1</td><td>2</td><td>3</td></tr><tr><td>$y$</td><td>1</td><td>2</td><td>3</td><td>4</td></tr></table>',
              P(-1,4,-1,5,[('line',(0,1),(3,4)),('pt',(0,1),'(0, 1)',-8,-4),('pt',(1,2),''),('pt',(2,3),''),('pt',(3,4),'(3, 4)',8,8)],w=130,ticks=True)]),
      dict(q=r'Find the $x$-intercept and $y$-intercept for the graph of $y = -2x + 1$.',w=[r'x = 0: y = 1 \;\Rightarrow\; (0, 1)',r'y = 0: 0 = -2x + 1',r'x = \dfrac{1}{2} \;\Rightarrow\; \left(\dfrac{1}{2}, 0\right)']),
      dict(q=r'Rearrange $2x + 3y = 8$ to the form $y = mx + c$.',w=['3y = -2x + 8',r'y = -\dfrac{2}{3}x + \dfrac{8}{3}'])],
 ex=[dict(n=13,page=31,kp='p. 29',instr=r'Decide if the point $(-2, 7)$ is on the line with the given equations.',yinstr=r'Decide if the point $(-1, 4)$ is on the line with the given equations.',ki=KI_ONLINE,
          parts=[('a','y = -3x + 1',['= -3(-2) + 1','= 7',r'\therefore (-2, 7) \text{ is on the line.}']),
                 ('b','2x + 2y = 1',['2x + 2y = 2(-2) + 2(7)','= -4 + 14',r'= 10 \neq 1',r'\therefore (-2, 7) \text{ is not on the line.}'])],
          yt=[('a','y = -2x + 2',['= -2(-1) + 2','= 4',r'\therefore (-1, 4) \text{ is on the line.}']),
              ('b','3x + 3y = 2',['3x + 3y = 3(-1) + 3(4)','= -3 + 12',r'= 9 \neq 2',r'\therefore (-1, 4) \text{ is not on the line.}'])]),
     dict(n=14,page=32,kp='pp. 29–30',instr=r'Find the gradient and $y$-intercept for these linear relations and sketch each graph.',ki=KI_GI,
          parts=[('a','y = 2x - 1',[r'\text{Gradient} = 2',r'y\text{-intercept has coordinates } (0, -1)',P(-2,2.5,-2.5,2.5,[L(2,-1),('dash',[(0,-1),(1,-1),(1,1)]),('pt',(1,1),'(1, 1)',8,0),('pt',(0,-1),'(0, −1)',8,10)],w=200)]),
                 ('b','2x + 3y = 3',['3y = -2x + 3',r'y = -\dfrac{2}{3}x + 1',r'\text{Gradient} = -\dfrac{2}{3}',r'y\text{-intercept has coordinates } (0, 1)',P(-2,4.5,-2,2.5,[L(-2/3,1),('dash',[(0,1),(3,1),(3,-1)]),('pt',(0,1),'(0, 1)',-6,-8),('pt',(3,-1),'(3, −1)',-6,14)],w=220)])],
          yt=[('a','y = 3x - 1',[r'\text{Gradient} = 3',r'y\text{-intercept has coordinates } (0, -1)',P(-2,2.5,-2.5,3,[L(3,-1),('dash',[(0,-1),(1,-1),(1,2)]),('pt',(1,2),'(1, 2)',8,0),('pt',(0,-1),'(0, −1)',8,10)],w=200)]),
              ('b','3x + 4y = 4',['4y = -3x + 4',r'y = -\dfrac{3}{4}x + 1',r'\text{Gradient} = -\dfrac{3}{4}',r'y\text{-intercept has coordinates } (0, 1)',P(-2,5.5,-3,2.5,[L(-3/4,1),('dash',[(0,1),(4,1),(4,-2)]),('pt',(0,1),'(0, 1)',-6,-8),('pt',(4,-2),'(4, −2)',-6,14)],w=230)])]),
     dict(n=15,page=33,kp='p. 30',instr=r'Sketch the following by finding the $x$- and $y$-intercepts.',ki=KI_INT,
          parts=[('a','y = 2x - 8',[r'y\text{-intercept } (x = 0)\text{:}','y = 2(0) - 8','y = -8',r'\text{The } y\text{-intercept is at } (0, -8).',r'x\text{-intercept } (y = 0)\text{:}','0 = 2x - 8','8 = 2x','x = 4',r'\text{The } x\text{-intercept is at } (4, 0).',P(-2,6,-10,3,[L(2,-8),('pt',(0,-8),'−8',-8,4),('pt',(4,0),'4',6,14)],w=160,h=200)]),
                 ('b','-3x - 2y = 6',[r'y\text{-intercept } (x = 0)\text{:}','-3(0) - 2y = 6','-2y = 6','y = -3',r'\text{The } y\text{-intercept is at } (0, -3).',r'x\text{-intercept } (y = 0)\text{:}','-3x - 2(0) = 6','-3x = 6','x = -2',r'\text{The } x\text{-intercept is at } (-2, 0).',P(-4,2,-5,2,[L(-1.5,-3),('pt',(0,-3),'−3',8,4),('pt',(-2,0),'−2',-6,-6)],w=170)])],
          yt=[('a','y = 2x - 4',[r'y\text{-intercept } (x = 0)\text{:}','y = 2(0) - 4','y = -4',r'\text{The } y\text{-intercept is at } (0, -4).',r'x\text{-intercept } (y = 0)\text{:}','0 = 2x - 4','4 = 2x','x = 2',r'\text{The } x\text{-intercept is at } (2, 0).',P(-2,4,-6,3,[L(2,-4),('pt',(0,-4),'−4',-8,4),('pt',(2,0),'2',6,14)],w=160,h=200)]),
              ('b','-2x - 5y = 10',[r'y\text{-intercept } (x = 0)\text{:}','-2(0) - 5y = 10','-5y = 10','y = -2',r'\text{The } y\text{-intercept is at } (0, -2).',r'x\text{-intercept } (y = 0)\text{:}','-2x - 5(0) = 10','-2x = 10','x = -5',r'\text{The } x\text{-intercept is at } (-5, 0).',P(-7,2,-4,2,[L(-0.4,-2),('pt',(0,-2),'−2',8,6),('pt',(-5,0),'−5',-6,-6)],w=200)])]),
     dict(n=16,page=34,kp='p. 30',instr='Sketch these special lines.',ki=KI_SPEC,
          parts=[('a','y = 2',[P(-3,3,-2,3.5,[('line',(0,2),(1,2)),('lab',(0.15,2.3),'2','start'),('lab',(1.3,2.3),'y = 2','start')],w=200)]),
                 ('b','x = -3',[P(-5,2,-3,3,[('line',(-3,0),(-3,1)),('lab',(-2.9,-0.45),'−3','start'),('lab',(-2.8,-2.4),'x = −3','start')],w=200)]),
                 ('c',r'y = -\dfrac{1}{2}x',[P(-3,4,-3,2.5,[L(-0.5,0),('dash',[(0,0),(2,0),(2,-1)]),('pt',(2,-1),'(2, −1)',6,12)],w=200)])],
          yt=[('a','y = -1',[P(-3,3,-3,2.5,[('line',(0,-1),(1,-1)),('lab',(0.15,-1.6),'−1','start'),('lab',(1.3,-0.6),'y = −1','start')],w=200)]),
              ('b','x = 2',[P(-2,4,-3,3,[('line',(2,0),(2,1)),('lab',(2.1,-0.45),'2','start'),('lab',(2.2,-2.4),'x = 2','start')],w=200)]),
              ('c',r'y = -\dfrac{1}{3}x',[P(-3,5,-3,2.5,[L(-1/3,0),('dash',[(0,0),(3,0),(3,-1)]),('pt',(3,-1),'(3, −1)',6,12)],w=200)])])],
 exit=[dict(q=r'Decide if the point $(3, -1)$ is on the line $3x + 2y = 7$.',w=['3x + 2y = 3(3) + 2(-1)','= 9 - 2 = 7',r'\therefore (3, -1) \text{ is on the line.}']),
       dict(q=r'State the gradient and $y$-intercept of $3y - 2x = 6$.',w=['3y = 2x + 6',r'y = \dfrac{2}{3}x + 2',r'\text{Gradient} = \dfrac{2}{3},\ y\text{-intercept } (0, 2)']),
       dict(q=r'Find the gradient and $y$-intercept of $y = -2x + 7$ and sketch its graph.',w=[r'*\text{Gradient} = -2,\ y\text{-intercept } (0, 7)',P(-1,4,-1,8,[L(-2,7),('pt',(0,7),'(0, 7)',8,0),('pt',(1,5),'(1, 5)',8,0)],w=120)]),
       dict(q=r'Find the $x$- and $y$-intercepts and sketch the graph of $3x + y = 9$.',w=[r'x = 0: y = 9 \;\Rightarrow\; (0, 9)',r'*y = 0: 3x = 9,\ x = 3 \;\Rightarrow\; (3, 0)',P(-1,4.5,-2,10,[L(-3,9),('pt',(0,9),'9',8,4),('pt',(3,0),'3',6,14)],w=110)]),
       dict(q=r'Sketch $y = 3$ and $x = -2$.',w=[P(-4,3,-2,4.5,[('line',(0,3),(1,3)),('line',(-2,0),(-2,1)),('lab',(0.6,3.35),'y = 3'),('lab',(-1.9,-1.4),'x = −2')],w=180)]),
       dict(q=r'Sketch $y = 2x$ labelling the axis intercept and one other point.',w=[P(-2,3,-2,3.5,[L(2,0),('pt',(1,2),'(1, 2)',8,6)],w=150)])],
)
# ======================================================================== 1F
g18=P(-2,5,-2,14,[LB(3,1),('lab',(-0.3,1.4),'1','end','#000'),('pt',(4,13),'(4, 13)',8,4,'#000')],w=150,h=210)
g18y=P(-3,5,-5,9,[LB(2,1),('lab',(-0.3,1.4),'1','end','#000'),('pt',(3,7),'(3, 7)',8,4,'#000')],w=150,h=210)
g19=P(-1,9,-2,13,[LB(-4/3,15),('pt',(3,11),'(3, 11)',8,-2,'#000'),('pt',(6,7),'(6, 7)',8,-2,'#000')],w=190,h=200)
g19y=P(-1,11,-2,14,[LB(-5/4,12),('pt',(4,7),'(4, 7)',8,-2,'#000'),('pt',(8,2),'(8, 2)',8,-2,'#000')],w=190,h=200)
S['1F']=dict(
 apk=[dict(q='!Find the gradient of this line.<br>'+WS.f1F(),w=[r'm = \dfrac{\text{rise}}{\text{run}} = \dfrac{3}{2}']),
      dict(q=r'Find the gradient of the line joining the points $(-1, 3)$ and $(4, 9)$.',w=[r'm = \dfrac{9 - 3}{4 - (-1)}',r'= \dfrac{6}{5}']),
      dict(q=r'Find the equation of the line which has a gradient of $2$ and passes through the point $(-2, 5)$.',w=['y = 2x + c','5 = 2(-2) + c','c = 9','y = 2x + 9'])],
 ex=[dict(n=17,page=39,kp='p. 38',instr=r'Find the gradient of the line joining the pair of points $(-3, 8)$ and $(5, -2)$.',yinstr=r'Find the gradient of the line joining the pair of points $(-2, 6)$ and $(3, -1)$.',ki=KI_GRAD,
          parts=[('','',[r'm = \dfrac{y_2 - y_1}{x_2 - x_1}',r'= \dfrac{-2 - 8}{5 - (-3)}',r'= -\dfrac{10}{8}',r'= -\dfrac{5}{4}'])],
          yt=[('','',[r'm = \dfrac{y_2 - y_1}{x_2 - x_1}',r'= \dfrac{-1 - 6}{3 - (-2)}',r'= -\dfrac{7}{5}'])]),
     dict(n=18,page=40,kp='p. 38',instr=r'Find the equation of the straight line with the given $y$-intercept.',ki=KI_YMC,
          parts=[('','',[r'\text{The equation of a straight line is of the form } y = mx + c.',r'm = \dfrac{y_2 - y_1}{x_2 - x_1}',r'= \dfrac{13 - 1}{4 - 0}',r'= \dfrac{12}{4}','= 3',r'\text{and } c = 1',r'\therefore y = 3x + 1'],g18)],
          yt=[('','',[r'\text{The equation of a straight line is of the form } y = mx + c.',r'm = \dfrac{y_2 - y_1}{x_2 - x_1}',r'= \dfrac{7 - 1}{3 - 0}',r'= \dfrac{6}{3}','= 2',r'\text{and } c = 1',r'\therefore y = 2x + 1'],g18y)]),
     dict(n=19,page=41,kp='p. 38',instr='Find the equation of the straight line with the given two points.',ki=KI_2PT,
          parts=[('Method 1','',['y = mx + c',r'm = \dfrac{y_2 - y_1}{x_2 - x_1}',r'= \dfrac{7 - 11}{6 - 3}',r'= -\dfrac{4}{3}',r'y = -\dfrac{4}{3}x + c',r'7 = -\dfrac{4}{3} \times (6) + c','7 = -8 + c','15 = c',r'\therefore y = -\dfrac{4}{3}x + 15']),
                 ('Method 2','',[r'y - y_1 = m(x - x_1)',r'y - 11 = -\dfrac{4}{3}(x - 3)',r'y = -\dfrac{4}{3}x + 4 + 11',r'= -\dfrac{4}{3}x + 15'],g19)],
          yt=[('Method 1','',['y = mx + c',r'm = \dfrac{y_2 - y_1}{x_2 - x_1}',r'= \dfrac{2 - 7}{8 - 4}',r'= -\dfrac{5}{4}',r'y = -\dfrac{5}{4}x + c',r'2 = -\dfrac{5}{4} \times (8) + c','2 = -10 + c','12 = c',r'\therefore y = -\dfrac{5}{4}x + 12']),
              ('Method 2','',[r'y - y_1 = m(x - x_1)',r'y - 7 = -\dfrac{5}{4}(x - 4)',r'y = -\dfrac{5}{4}x + 5 + 7',r'= -\dfrac{5}{4}x + 12'],g19y)])],
 exit=[dict(q=r'Determine the gradient of the line joining the points $(-2, 4)$ and $(3, 1)$.',w=[r'm = \dfrac{1 - 4}{3 - (-2)}',r'= -\dfrac{3}{5}']),
       dict(q='!Find the equation of the straight line shown.<br>'+P(-5,9,-5,9,[LB(2,2),('lab',(-0.3,2.3),'2','end','#000'),('pt',(3,8),'(3, 8)',8,4,'#000')],w=110,h=110),w=[r'm = \dfrac{8 - 2}{3 - 0} = 2,\ c = 2','y = 2x + 2']),
       dict(q=r'Find the equation of the straight line joining the points $(-2, -2)$ and $(2, 3)$.',w=[r'm = \dfrac{3 - (-2)}{2 - (-2)} = \dfrac{5}{4}',r'3 = \dfrac{5}{4}(2) + c \Rightarrow c = \dfrac{1}{2}',r'y = \dfrac{5}{4}x + \dfrac{1}{2}'])],
)
# ======================================================================== 1G
S['1G']=dict(
 apk=[dict(q=r'Draw a set of axes from $-4$ to $4$ on both axes, and plot the points $(-3, 2)$ and $(-2, -4)$.',w=[P(-4,4,-4,4,[('pt',(-3,2),'(−3, 2)',8,-8),('pt',(-2,-4),'(−2, −4)',8,-2)],w=150,ticks=True)]),
      dict(q=r'Decide if $6, 8, 10$ is a Pythagorean triple.',w=[r'6^2 + 8^2 = 36 + 64 = 100 = 10^2',r'\text{Yes, it is a Pythagorean triple.}']),
      dict(q='!Find the value of the pronumeral correct to one decimal place.<br>'+WS.f1G(),w=[r'x^2 + 5^2 = 10^2','x^2 = 75',r'x = \sqrt{75} \approx 8.7'])],
 ex=[dict(n=20,page=47,kp='p. 46',instr='Find the exact distance between each pair of points.',ki=KI_DIST2,
          parts=[('a',r'(0, 2) \text{ and } (1, 7)',[r'd = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}',r'= \sqrt{(1 - 0)^2 + (7 - 2)^2}',r'= \sqrt{1^2 + 5^2}',r'= \sqrt{26} \text{ units}']),
                 ('b',r'(-3, 8) \text{ and } (4, -1)',[r'd = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}',r'= \sqrt{(4 - (-3))^2 + (-1 - 8)^2}',r'= \sqrt{7^2 + (-9)^2}',r'= \sqrt{49 + 81}',r'= \sqrt{130} \text{ units}'])],
          yt=[('a',r'(0, 3) \text{ and } (1, 5)',[r'd = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}',r'= \sqrt{(1 - 0)^2 + (5 - 3)^2}',r'= \sqrt{1^2 + 2^2}',r'= \sqrt{5} \text{ units}']),
              ('b',r'(-2, 7) \text{ and } (3, -1)',[r'd = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}',r'= \sqrt{(3 - (-2))^2 + (-1 - 7)^2}',r'= \sqrt{5^2 + (-8)^2}',r'= \sqrt{25 + 64}',r'= \sqrt{89} \text{ units}'])]),
     dict(n=21,page=48,kp='p. 46',instr=r'Find the midpoint of the line segment joining $(-3, -5)$ and $(2, 7)$.',yinstr=r'Find the midpoint of the line segment joining $(-2, -6)$ and $(3, -2)$.',ki=KI_MID,
          parts=[('','',[r'M = \left(\dfrac{x_1 + x_2}{2}, \dfrac{y_1 + y_2}{2}\right)',r'= \left(\dfrac{-3 + 2}{2}, \dfrac{-5 + 7}{2}\right)',r'= \left(-\dfrac{1}{2}, 1\right)'])],
          yt=[('','',[r'M = \left(\dfrac{x_1 + x_2}{2}, \dfrac{y_1 + y_2}{2}\right)',r'= \left(\dfrac{-2 + 3}{2}, \dfrac{-6 + (-2)}{2}\right)',r'= \left(\dfrac{1}{2}, -4\right)'])]),
     dict(n=22,page=48,kp='p. 46',instr=r'Find the values of $a$ if the distance between $(2, a)$ and $(4, 9)$ is $\sqrt{5}$.',yinstr=r'Find the values of $a$ if the distance between $(1, a)$ and $(3, 7)$ is $\sqrt{13}$.',ki=KI_DIST2,
          parts=[('','',[r'd = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}',r'\sqrt{5} = \sqrt{(4 - 2)^2 + (9 - a)^2}',r'\sqrt{5} = \sqrt{2^2 + (9 - a)^2}','5 = 4 + (9 - a)^2','1 = (9 - a)^2',r'\pm 1 = 9 - a',r'\text{So } 9 - a = 1 \text{ or } 9 - a = -1.',r'\therefore a = 8 \text{ or } a = 10'])],
          yt=[('','',[r'd = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}',r'\sqrt{13} = \sqrt{(3 - 1)^2 + (7 - a)^2}',r'\sqrt{13} = \sqrt{2^2 + (7 - a)^2}','13 = 4 + (7 - a)^2','9 = (7 - a)^2',r'\pm 3 = 7 - a',r'\text{So } 7 - a = 3 \text{ or } 7 - a = -3.',r'\therefore a = 4 \text{ or } a = 10'])])],
 exit=[dict(q=r'Find the exact distance between the points $(2, 4)$ and $(5, 2)$.',w=[r'd = \sqrt{(5 - 2)^2 + (2 - 4)^2}',r'= \sqrt{9 + 4}',r'= \sqrt{13} \text{ units}']),
       dict(q=r'Find the midpoint of the line segment joining $(-1, 5)$ and $(5, 2)$.',w=[r'M = \left(\dfrac{-1 + 5}{2}, \dfrac{5 + 2}{2}\right)',r'= \left(2, \dfrac{7}{2}\right)']),
       dict(q=r'Find the values of $a$ if the distance between $(3, a)$ and $(6, 10)$ is $\sqrt{34}$.',w=[r'34 = (6 - 3)^2 + (10 - a)^2','25 = (10 - a)^2',r'10 - a = \pm 5',r'a = 5 \text{ or } a = 15'])],
)
# ======================================================================== 1H
S['1H']=dict(
 apk=[dict(q='!State whether the two lines cut by this transversal are parallel.<br>'+WS.f1H_t(),w=[r'122^\circ + 58^\circ = 180^\circ',r'\text{co-interior angles are supplementary,}',r'\text{so the lines are parallel.}']),
      dict(q='!For the graphs shown, state whether the gradient is positive, negative, zero or undefined and find the gradient.<br>'+WS.f1H_g(),w=[r'\text{a negative},\ m = -\dfrac{4}{2} = -2',r'\text{b zero},\ m = 0']),
      dict(q=r'Rearrange $2x + 3y = 8$ to the form $y = mx + c$.',w=['3y = -2x + 8',r'y = -\dfrac{2}{3}x + \dfrac{8}{3}'])],
 ex=[dict(n=23,page=53,kp='p. 51',instr='Decide if the graph of each pair of rules will be parallel, perpendicular or neither.',ki=KI_PP,
          parts=[('a',r'!$y = -3x - 8$ and $y = \dfrac{1}{3}x + 1$',[r'y = -3x - 8,\ m = -3 \quad [1]',r'y = \dfrac{1}{3}x + 1,\ m = \dfrac{1}{3} \quad [2]',r'-3 \times \dfrac{1}{3} = -1',r'\text{So the lines are perpendicular.}']),
                 ('b',r'!$y = \dfrac{1}{2}x + 2$ and $2y - x = 5$',[r'y = \dfrac{1}{2}x + 2,\ m = \dfrac{1}{2} \quad [1]','2y - x = 5','2y = x + 5',r'y = \dfrac{1}{2}x + \dfrac{5}{2},\ m = \dfrac{1}{2} \quad [2]',r'\text{So the lines are parallel.}']),
                 ('c',r'!$3x + 2y = -5$ and $x - y = 2$',['3x + 2y = -5','2y = -3x - 5',r'y = -\dfrac{3}{2}x - \dfrac{5}{2},\ m = -\dfrac{3}{2} \quad [1]','x - y = 2','-y = -x + 2',r'y = x - 2,\ m = 1 \quad [2]',r'-\dfrac{3}{2} \times 1 \neq -1',r'*\text{So the lines are neither}',r'*\text{parallel nor perpendicular.}'])],
          yt=[('a',r'!$y = -4x - 1$ and $y = \dfrac{1}{4}x + 3$',[r'y = -4x - 1,\ m = -4 \quad [1]',r'y = \dfrac{1}{4}x + 3,\ m = \dfrac{1}{4} \quad [2]',r'-4 \times \dfrac{1}{4} = -1',r'\text{So the lines are perpendicular.}']),
              ('b',r'!$y = \dfrac{1}{2}x + 1$ and $2y + x = 7$',[r'y = \dfrac{1}{2}x + 1,\ m = \dfrac{1}{2} \quad [1]','2y + x = 7','2y = -x + 7',r'y = -\dfrac{1}{2}x + \dfrac{7}{2},\ m = -\dfrac{1}{2} \quad [2]',r'\dfrac{1}{2} \times \left(-\dfrac{1}{2}\right) \neq -1',r'*\text{So the lines are neither}',r'*\text{parallel nor perpendicular.}']),
              ('c',r'!$5x - 3y = -10$ and $5x = 3y + 2$',['5x - 3y = -10','-3y = -5x - 10',r'y = \dfrac{5}{3}x + \dfrac{10}{3},\ m = \dfrac{5}{3} \quad [1]','5x = 3y + 2','-3y = -5x + 2',r'y = \dfrac{5}{3}x - \dfrac{2}{3},\ m = \dfrac{5}{3} \quad [2]',r'\text{So the lines are parallel.}'])]),
     dict(n=24,page=54,kp='p. 51',instr='Find the equation of the line that is:',ki=KI_PPEQ,
          parts=[('a',r'!parallel to $y = -2x - 7$ and passes through $(1, 9)$',['y = mx + c','m = -2','y = -2x + c',r'\text{Substitute } (1, 9)\text{:}','9 = -2(1) + c','11 = c',r'\therefore y = -2x + 11']),
                 ('b',r'!perpendicular to $y = \dfrac{3}{4}x - 1$ and passes through $(3, -2)$',['y = mx + c',r'm = \dfrac{-1}{\left(\frac{3}{4}\right)} = -\dfrac{4}{3}',r'y = -\dfrac{4}{3}x + c',r'\text{Substitute } (3, -2)\text{:}',r'-2 = -\dfrac{4}{3}(3) + c','-2 = -4 + c','c = 2',r'\therefore y = -\dfrac{4}{3}x + 2'])],
          yt=[('a',r'!parallel to $y = -3x - 5$ and passes through $(1, 5)$',['y = mx + c','m = -3','y = -3x + c',r'\text{Substitute } (1, 5)\text{:}','5 = -3(1) + c','8 = c',r'\therefore y = -3x + 8']),
              ('b',r'!perpendicular to $y = \dfrac{2}{3}x - 3$ and passes through $(2, -1)$',['y = mx + c',r'm = \dfrac{-1}{\left(\frac{2}{3}\right)} = -\dfrac{3}{2}',r'y = -\dfrac{3}{2}x + c',r'\text{Substitute } (2, -1)\text{:}',r'-1 = -\dfrac{3}{2}(2) + c','-1 = -3 + c','c = 2',r'\therefore y = -\dfrac{3}{2}x + 2'])])],
 exit=[dict(q=r'Decide if the graph of the lines $y = 2x + 5$ and $2y + x = 3$ will be parallel, perpendicular or neither.',w=[r'm_1 = 2;\ \ 2y = -x + 3,\ m_2 = -\dfrac{1}{2}',r'2 \times \left(-\dfrac{1}{2}\right) = -1',r'\text{perpendicular}']),
       dict(q=r'Find the equation of the line that is parallel to $y = 3x - 4$ and passes through $(2, 4)$.',w=['m = 3',r'4 = 3(2) + c,\ c = -2','y = 3x - 2']),
       dict(q=r'Find the equation of a line that is perpendicular to $y = -2x + 5$ and passes through $(0, 8)$.',w=[r'm = \dfrac{-1}{-2} = \dfrac{1}{2},\ c = 8',r'y = \dfrac{1}{2}x + 8'])],
)
# ======================================================================== 1I
S['1I']=dict(
 apk=[dict(q=r'Decide if the $(1, 3)$ and $(-2, -4)$ lie on the graph of $y = 3x$.',w=[r'(1, 3)\text{: } 3(1) = 3 \;\checkmark',r'(-2, -4)\text{: } 3(-2) = -6 \neq -4',r'\text{Only } (1, 3) \text{ lies on the graph.}']),
      dict(q=r'Determine if the point $(2, -1)$ is at the intersection of the lines with equations $y = -2x + 3$ and $2x - 3y = 7$.',w=[r'-2(2) + 3 = -1 \;\checkmark',r'2(2) - 3(-1) = 7 \;\checkmark',r'\text{Yes, it is the intersection point.}']),
      dict(q=r'Solve $6x + 5 = 3x - 13$.',w=['3x + 5 = -13','3x = -18','x = -6'])],
 ex=[dict(n=25,page=59,kp='p. 57',instr='Solve these pairs of simultaneous equations using the method of substitution.',ki=KI_SUB,
          parts=[('a',r'!$2x + y = -7$ and $y = x + 2$',[r'2x + y = -7 \quad [1]',r'y = x + 2 \quad [2]',r'\text{Substitute equation [2] into equation [1].}','2x + (x + 2) = -7','3x + 2 = -7','3x = -9','x = -3',r'\text{Substitute } x = -3 \text{ into equation [2].}','y = (-3) + 2','= -1',r'\text{Solution is } x = -3,\ y = -1.']),
                 ('b',r'!$2x - 3y = -8$ and $y = x + 3$',[r'2x - 3y = -8 \quad [1]',r'y = x + 3 \quad [2]',r'\text{Substitute equation [2] into equation [1].}','2x - 3(x + 3) = -8','2x - 3x - 9 = -8','-x - 9 = -8','-x = 1','x = -1',r'\text{Substitute } x = -1 \text{ into equation [2].}','y = (-1) + 3','= 2',r'\text{Solution is } x = -1,\ y = 2.'])],
          yt=[('a',r'!$3x + y = 4$ and $y = x - 4$',[r'3x + y = 4 \quad [1]',r'y = x - 4 \quad [2]',r'\text{Substitute equation [2] into equation [1].}','3x + (x - 4) = 4','4x - 4 = 4','4x = 8','x = 2',r'\text{Substitute } x = 2 \text{ into equation [2].}','y = (2) - 4','= -2',r'\text{Solution is } x = 2,\ y = -2.']),
              ('b',r'!$x - 2y = -7$ and $y = x + 4$',[r'x - 2y = -7 \quad [1]',r'y = x + 4 \quad [2]',r'\text{Substitute equation [2] into equation [1].}','x - 2(x + 4) = -7','x - 2x - 8 = -7','-x - 8 = -7','-x = 1','x = -1',r'\text{Substitute } x = -1 \text{ into equation [2].}','y = (-1) + 4','= 3',r'\text{Solution is } x = -1,\ y = 3.'])]),
     dict(n=26,page=60,kp='p. 57',instr=r'Solve the pair of simultaneous equations: $y = -3x + 2$ and $y = 7x - 8$.',yinstr=r'Solve the pair of simultaneous equations: $y = -4x + 7$ and $y = 5x - 11$.',ki=KI_SUB,
          parts=[('','',[r'y = -3x + 2 \quad [1]',r'y = 7x - 8 \quad [2]',r'\text{Substitute equation [2] into equation [1].}','7x - 8 = -3x + 2','10x = 10','x = 1',r'\text{Substitute } x = 1 \text{ into equation [1].}','y = -3(1) + 2','= -1',r'\text{Solution is } x = 1,\ y = -1.'])],
          yt=[('','',[r'y = -4x + 7 \quad [1]',r'y = 5x - 11 \quad [2]',r'\text{Substitute equation [2] into equation [1].}','5x - 11 = -4x + 7','9x = 18','x = 2',r'\text{Substitute } x = 2 \text{ into equation [1].}','y = -4(2) + 7','= -1',r'\text{Solution is } x = 2,\ y = -1.'])])],
 exit=[dict(q=r'Solve the pair of simultaneous equations $x - 2y = 4$ and $y = x - 3$ using the method of substitution.',w=['x - 2(x - 3) = 4','x - 2x + 6 = 4',r'-x = -2,\ x = 2','y = 2 - 3 = -1',r'x = 2,\ y = -1'])],
)
# ======================================================================== 1J
S['1J']=dict(
 apk=[dict(q=r'State the result of adding $4$ to both sides of the equation $7q - 4 = 10$.',w=['7q = 14']),
      dict(q=r'Simplify $5ac + 3b - 2ca + 4b - 5b$.',w=['= 3ac + 2b']),
      dict(q=r'Solve the following pair of simultaneous equations using substitution:<br>$\begin{aligned} x + 2y &= 4 \\ y &= 2x - 3 \end{aligned}$',w=['x + 2(2x - 3) = 4','5x - 6 = 4','x = 2','y = 2(2) - 3 = 1',r'x = 2,\ y = 1'])],
 ex=[dict(n=27,page=67,kp='p. 66',instr=r'Solve the following pair of simultaneous equations using the elimination method.<br>$x + y = 6$ and $3x - y = 10$',yinstr=r'Solve the following pair of simultaneous equations using the elimination method.<br>$x + y = 4$ and $5x - y = 14$',ki=KI_ELIM,
          parts=[('','',[r'x + y = 6 \quad [1]',r'3x - y = 10 \quad [2]',r'[1] + [2]\text{: } 4x = 16','x = 4',r'\text{Substitute } x = 4 \text{ into equation [1].}','(4) + y = 6',r'\therefore y = 2',r'\text{Solution is } x = 4,\ y = 2.'])],
          yt=[('','',[r'x + y = 4 \quad [1]',r'5x - y = 14 \quad [2]',r'[1] + [2]\text{: } 6x = 18','x = 3',r'\text{Substitute } x = 3 \text{ into equation [1].}','(3) + y = 4',r'\therefore y = 1',r'\text{Solution is } x = 3,\ y = 1.'])]),
     dict(n=28,page=67,kp='p. 66',instr='Solve the following pairs of simultaneous equations using the elimination method.',ki=KI_ELIM,
          parts=[('a',r'!$y - 3x = 1$ and $2y + 5x = 13$',[r'y - 3x = 1 \quad [1]',r'2y + 5x = 13 \quad [2]',r'[1] \times 2\text{: } 2y - 6x = 2 \quad [3]',r'[2] - [3]\text{: } 11x = 11','x = 1',r'\text{Substitute } x = 1 \text{ into equation [1].}','y - 3(1) = 1',r'\therefore y = 4',r'\text{Solution is } x = 1,\ y = 4.']),
                 ('b',r'!$3x + 2y = 6$ and $5x + 3y = 11$',[r'3x + 2y = 6 \quad [1]',r'5x + 3y = 11 \quad [2]',r'[1] \times 3\text{: } 9x + 6y = 18 \quad [3]',r'[2] \times 2\text{: } 10x + 6y = 22 \quad [4]',r'[4] - [3]\text{: } x = 4',r'\text{Substitute } x = 4 \text{ into equation [1].}','3(4) + 2y = 6','2y = -6',r'\therefore y = -3',r'\text{Solution is } x = 4,\ y = -3.'])],
          yt=[('a',r'!$y - 2x = 1$ and $4y + 3x = 15$',[r'y - 2x = 1 \quad [1]',r'4y + 3x = 15 \quad [2]',r'[1] \times 4\text{: } 4y - 8x = 4 \quad [3]',r'[2] - [3]\text{: } 11x = 11','x = 1',r'\text{Substitute } x = 1 \text{ into equation [1].}','y - 2(1) = 1',r'\therefore y = 3',r'\text{Solution is } x = 1,\ y = 3.']),
              ('b',r'!$5x + 2y = 11$ and $3x + 5y = -1$',[r'5x + 2y = 11 \quad [1]',r'3x + 5y = -1 \quad [2]',r'[1] \times 5\text{: } 25x + 10y = 55 \quad [3]',r'[2] \times 2\text{: } 6x + 10y = -2 \quad [4]',r'[3] - [4]\text{: } 19x = 57','x = 3',r'\text{Substitute } x = 3 \text{ into equation [1].}','5(3) + 2y = 11','2y = -4',r'\therefore y = -2',r'\text{Solution is } x = 3,\ y = -2.'])])],
 exit=[dict(q=r'Solve the simultaneous equations $x - 2y = 10$ and $x + y = 4$ using elimination.',w=[r'[2] - [1]\text{: } 3y = -6','y = -2',r'x + (-2) = 4,\ x = 6',r'x = 6,\ y = -2']),
       dict(q=r'Solve the pair of simultaneous equations $2x + 3y = 5$ and $3x - 4y = -18$ using the elimination method.',w=[r'[1] \times 3\text{: } 6x + 9y = 15 \quad [3]',r'[2] \times 2\text{: } 6x - 8y = -36 \quad [4]',r'[3] - [4]\text{: } 17y = 51,\ y = 3',r'2x + 9 = 5,\ x = -2',r'x = -2,\ y = 3'])],
)
# ======================================================================== 1K
S['1K']=dict(
 apk=[dict(q=r'Write an equation for “the sum of $x$ and $5$ is $22$.”',w=['x + 5 = 22']),
      dict(q=r'The weight of $6$ identical books is $1.2\text{ kg}$. Set up and solve an equation to find the weight of one book.',w=['6w = 1.2','w = 0.2',r'\text{One book weighs } 0.2\text{ kg.}']),
      dict(q=r'Ava and Elise have $27$ soft toys between them. Ava has $5$ more than Elise. Use an equation to find how many soft toys they each have.',w=['e + (e + 5) = 27',r'2e + 5 = 27,\ e = 11',r'\text{Elise has 11, Ava has 16.}'])],
 ex=[dict(n=29,page=71,kp='p. 70',instr='The sum of the ages of two children is 17 and the difference in their ages is 5. If Kara is the older sister of Ben, determine their ages.',
          yinstr='The sum of the ages of two children is 20 and the difference in their ages is 8. If Tim is the older brother of Tina, determine their ages.',ki=KI_APP,
          parts=[('','',[r'\text{Let } k \text{ be Kara’s age and } b \text{ be Ben’s age.}',r'k + b = 17 \quad [1]',r'k - b = 5 \quad [2]',r'[1] + [2]\text{: } 2k = 22',r'\therefore k = 11',r'\text{Substitute } k = 11 \text{ into equation [1].}','(11) + b = 17','b = 6',r'\therefore \text{Kara is 11 years old and Ben is 6 years old.}'])],
          yt=[('','',[r'\text{Let } t \text{ be Tim’s age and } n \text{ be Tina’s age.}',r't + n = 20 \quad [1]',r't - n = 8 \quad [2]',r'[1] + [2]\text{: } 2t = 28',r'\therefore t = 14',r'\text{Substitute } t = 14 \text{ into equation [1].}','(14) + n = 20','n = 6',r'\therefore \text{Tim is 14 years old and Tina is 6 years old.}'])]),
     dict(n=30,page=72,kp='p. 70',instr=r'John buys 3 daffodils and 5 petunias from the nursery and pays \$25. Julia buys 4 daffodils and 3 petunias for \$26. Determine the cost of each type of flower.',
          yinstr=r'Georgie buys 2 coffees and 3 muffins for \$17 and Rick buys 4 coffees and 2 muffins for \$22 from the same shop. Determine the cost of each coffee and muffin.',ki=KI_APP,
          parts=[('','',[r'\text{Let \$}d \text{ be the cost of a daffodil and \$}p \text{ be the cost of a petunia.}',r'3d + 5p = 25 \quad [1]',r'4d + 3p = 26 \quad [2]',r'[1] \times 4\text{: } 12d + 20p = 100 \quad [3]',r'[2] \times 3\text{: } 12d + 9p = 78 \quad [4]',r'[3] - [4]\text{: } 11p = 22',r'\therefore p = 2',r'\text{Substitute } p = 2 \text{ into equation [1].}','3d + 5(2) = 25','3d + 10 = 25','3d = 15',r'\therefore d = 5',r'\text{A petunia costs \$2 and a daffodil costs \$5.}'])],
          yt=[('','',[r'\text{Let \$}c \text{ be the cost of a coffee and \$}m \text{ be the cost of a muffin.}',r'2c + 3m = 17 \quad [1]',r'4c + 2m = 22 \quad [2]',r'[1] \times 2\text{: } 4c + 6m = 34 \quad [3]',r'[2] \times 1\text{: } 4c + 2m = 22 \quad [4]',r'[3] - [4]\text{: } 4m = 12',r'\therefore m = 3',r'\text{Substitute } m = 3 \text{ into equation [1].}','2c + 3(3) = 17','2c + 9 = 17','2c = 8',r'\therefore c = 4',r'\text{A coffee costs \$4 and a muffin costs \$3.}'])])],
 exit=[dict(q=r'A teacher buys 5 of the same chocolate bars and 2 of the same ice-creams for \$18 while another teacher buys 4 of the same chocolate bars and 5 of the same ice-creams for \$28. Determine the individual costs of these chocolate bars and ice-creams.',
            w=[r'5c + 2i = 18 \ [1],\ \ 4c + 5i = 28 \ [2]',r'[1] \times 5 - [2] \times 2\text{: } 17c = 34,\ c = 2',r'5(2) + 2i = 18,\ i = 4',r'\text{Bars cost \$2, ice-creams cost \$4.}'])],
)
# ======================================================================== 1L
def shade_hp(a,b,c): return (a,b,c)
X0,X1,Y0,Y1=-4,5,-6,6
g31a=P(-4,5,-6,6,[region(-4,5,-6,6,[(1.5,-1,3)]),('line',(0,-3),(2,0),None,True),('pt',(0,-3),'(0, −3)',8,6),('pt',(2,0),'(2, 0)',8,14),('lab',(-3.6,4.5),'Region required','start','#000')],w=170,h=190)
g31b=P(-4,5,-6,6,[region(-4,5,-6,6,[(2,1,4)]),('line',(0,4),(2,0)),('pt',(0,4),'(0, 4)',8,-2),('pt',(2,0),'(2, 0)',8,14),('lab',(-3.6,-5),'Region required','start','#000')],w=170,h=190)
g31ay=P(-4,5,-7,6,[region(-4,5,-7,6,[(2.5,-1,5)]),('line',(0,-5),(2,0),None,True),('pt',(0,-5),'(0, −5)',8,6),('pt',(2,0),'(2, 0)',8,14),('lab',(-3.6,4.5),'Region required','start','#000')],w=170,h=190)
g31by=P(-4,5,-6,8,[region(-4,5,-6,8,[(3,1,6)]),('line',(0,6),(2,0)),('pt',(0,6),'(0, 6)',8,-2),('pt',(2,0),'(2, 0)',8,14),('lab',(-3.6,-5),'Region required','start','#000')],w=170,h=200)
g32=P(-3,6,-2,13,[region(-3,6,-2,13,[(4,1,12),(3,-2,-2)]),('line',(0,12),(3,0)),('line',(0,1),(-2/3,0),None,True),('pt',(2,4),'(2, 4)',8,10),('pt',(0,12),'12',8,4),('pt',(3,0),'3',6,14),('lab',(0.3,0.6),'1','start'),('lab',(-0.6,-1),'−2/3','end'),('lab',(-2.8,11),'Region required','start','#000')],w=200,h=240)
g32y=P(-5,4,-2,8,[region(-5,4,-2,8,[(3,1,6),(2,-3,-7)]),('line',(0,6),(2,0)),('line',(0,7/3),(-3.5,0),None,True),('pt',(1,3),'(1, 3)',8,10),('pt',(0,6),'6',8,4),('pt',(2,0),'2',6,14),('lab',(-4.7,7),'Region required','start','#000')],w=200,h=220)
S['1L']=dict(
 apk=[dict(q=r'Sketch the region $y < 4$.',w=[P(-3,3,-2,6,[region(-3,3,-2,6,[(0,1,4)]),('line',(0,4),(1,4),None,True),('lab',(0.2,4.4),'4','start')],w=150)]),
      dict(q=r'Show $x$ is less than or equal to 3 $(x \leqslant 3)$ on a number line.',w=[NL(0,5,right=(3,True),w=260)]),
      dict(q=r'Sketch the graphs of $y = -2x + 4$ and $3x - 4y = 12$ showing $x$- and $y$-intercepts.',w=[r'y = -2x + 4\text{: } (0, 4),\ (2, 0)',r'3x - 4y = 12\text{: } (0, -3),\ (4, 0)',P(-2,6,-5,6,[L(-2,4),L(0.75,-3),('pt',(0,4),'4',8,0),('pt',(2,0),'2',-10,14),('pt',(0,-3),'−3',8,8),('pt',(4,0),'4',4,14)],w=160)])],
 ex=[dict(n=31,page=76,kp='p. 74',instr='Sketch the region for the following linear inequalities.',yinstr='Sketch the half planes for the following linear inequalities.',ki=KI_REG,
          parts=[('a','y > 1.5x - 3',['y = 1.5x - 3',r'y\text{-intercept } (x = 0)\text{: } y = -3',r'\therefore (0, -3)',r'x\text{-intercept } (y = 0)\text{: } 0 = 1.5x - 3',r'1.5x = 3,\ x = 2',r'\therefore (2, 0)',g31a]),
                 ('b',r'y + 2x \leqslant 4',['y + 2x = 4',r'y\text{-intercept } (x = 0)\text{: } y = 4',r'\therefore (0, 4)',r'x\text{-intercept } (y = 0)\text{: } 2x = 4,\ x = 2',r'\therefore (2, 0)',r'\text{Shading: Test } (0, 0).',r'0 + 2(0) \leqslant 4',r'0 \leqslant 4 \text{ (True)}',r'\therefore (0, 0) \text{ is included.}',g31b])],
          yt=[('a','y > 2.5x - 5',['y = 2.5x - 5',r'y\text{-intercept } (x = 0)\text{: } y = -5',r'\therefore (0, -5)',r'x\text{-intercept } (y = 0)\text{: } 0 = 2.5x - 5',r'2.5x = 5,\ x = 2',r'\therefore (2, 0)',g31ay]),
              ('b',r'y + 3x \leqslant 6',['y + 3x = 6',r'y\text{-intercept } (x = 0)\text{: } y = 6',r'\therefore (0, 6)',r'x\text{-intercept } (y = 0)\text{: } 3x = 6,\ x = 2',r'\therefore (2, 0)',r'\text{Shading: Test } (0, 0).',r'0 + 3(0) \leqslant 6',r'0 \leqslant 6 \text{ (True)}',r'\therefore (0, 0) \text{ is included.}',g31by])]),
     dict(n=32,page=77,kp='pp. 74–75',instr=r'Sketch both the inequalities $4x + y \leqslant 12$ and $3x - 2y < -2$ on the same set of axes, show the region of intersection and find the point of intersection of the two lines.',
          yinstr=r'Sketch both the inequalities $3x + y \leqslant 6$ and $2x - 3y < -7$ on the same set of axes, show the region of intersection and find the point of intersection of the two lines.',ki=KI_INTR,
          parts=[('','',['4x + y = 12',r'y\text{-int: } y = 12,\ (0, 12);\ \ x\text{-int: } 4x = 12,\ x = 3,\ (3, 0)',r'\text{Test } (0, 0)\text{: } 4(0) + 0 \leqslant 12,\ 0 \leqslant 12 \text{ (True)}','3x - 2y = -2',r'y\text{-int: } -2y = -2,\ y = 1,\ (0, 1);\ \ x\text{-int: } 3x = -2,\ x = -\dfrac{2}{3}',r'\text{Test } (0, 0)\text{: } 0 < -2 \text{ (False)}',g32,r'4x + y = 12 \quad [1]',r'3x - 2y = -2 \quad [2]',r'[1] \times 2\text{: } 8x + 2y = 24 \quad [3]',r'[2] + [3]\text{: } 11x = 22,\ x = 2',r'4(2) + y = 12,\ y = 4',r'\therefore \text{The point of intersection is } (2, 4).'])],
          yt=[('','',['3x + y = 6',r'y\text{-int: } y = 6,\ (0, 6);\ \ x\text{-int: } 3x = 6,\ x = 2,\ (2, 0)',r'\text{Test } (0, 0)\text{: } 3(0) + 0 \leqslant 6,\ 0 \leqslant 6 \text{ (True)}','2x - 3y = -7',r'y\text{-int: } -3y = -7,\ y = \dfrac{7}{3};\ \ x\text{-int: } 2x = -7,\ x = -\dfrac{7}{2}',r'\text{Test } (0, 0)\text{: } 0 < -7 \text{ (False)}',g32y,r'3x + y = 6 \quad [1]',r'2x - 3y = -7 \quad [2]',r'[1] \times 3\text{: } 9x + 3y = 18 \quad [3]',r'[2] + [3]\text{: } 11x = 11,\ x = 1',r'3(1) + y = 6,\ y = 3',r'\therefore \text{The point of intersection is } (1, 3).'])])],
 exit=[dict(q=r'Sketch the region $y > 2x - 5$.',w=[r'(0, -5),\ (2.5, 0),\ \text{broken line}',r'\text{Test } (0, 0)\text{: } 0 > -5 \text{ (True)}',P(-3,5,-6,4,[region(-3,5,-6,4,[(2,-1,5)]),('line',(0,-5),(2.5,0),None,True),('pt',(0,-5),'−5',8,6),('pt',(2.5,0),'2.5',6,14)],w=130)]),
       dict(q=r'Sketch both the inequalities $2x + y \geqslant -2$ and $2x - 3y < 6$ on the same set of axes, showing the point of intersection of the two lines and the intersecting region.',
            w=[r'2x + y = -2\text{: } (0, -2),\ (-1, 0),\ \text{solid}',r'2x - 3y = 6\text{: } (0, -2),\ (3, 0),\ \text{broken}',r'\text{intersection } (0, -2)',P(-3,5,-5,4,[region(-3,5,-5,4,[(-2,-1,2),(2,-3,6)]),('line',(0,-2),(-1,0)),('line',(0,-2),(3,0),None,True),('pt',(0,-2),'(0, −2)',8,10)],w=140)])],
)
