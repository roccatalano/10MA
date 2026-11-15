import json
PQ=('Progress quiz',45); SA=('Chapter review · Short answer',None); MC=('Chapter review · Multiple choice',None)
def pg(kind,q):
  if kind is PQ:return 45
  if kind is SA:return 90 if q<=9 else 91
  return 92 if q<=9 else 93
items=[]
def add(sub,kind,q,part,stem,tex,tenA=False):
  items.append(dict(sub=sub,kind='mc' if kind is MC else 'sa',src=f"C10 Ch1 {kind[0]} Q{q}{part}",page=pg(kind,q),stem=stem,tex=tex,tenA=tenA))
def mc(opts):return '<div class="mc">'+''.join(f'<span><b>{k}</b> {v}</span>' for k,v in zip('ABCDE',opts))+'</div>'
S='Simplify the following.'
for p,t in zip('abc',['$15a^2b + 2ab - 6ba^2 + 8b$','$-3xy \\times 4x$','$4(m + 5) + 3(3m - 2)$']):add('1A',PQ,1,p,S,t)
S='Simplify the following. You may need to expand the brackets first.'
for p,t in zip('abcdef',['$8xy + 5x - 3xy + x$','$3a \\times 4ab$','$18xy \\div (12y)$','$3(b + 5) + 6$','$-3m(2m - 4) + 4m^2$','$3(2x + 4) - 5(x + 2)$']):add('1A',SA,1,p,S,t)
add('1A',MC,1,'','The simplified form of $3x + 2x \\times 7y - 3xy + 5x$ is:',mc(['$10x + 4y$','$35xy - 6x^2y$','$\\dfrac{35y - 6xy}{7}$','$5xy - 6x^2$','$8x + 11xy$']))
S='Solve the following equations and check your solution by substitution.'
for p,t in zip('abc',['$2x + 8 = 18$','$2(3k - 4) = -17$','$\\dfrac{m + 5}{5} = 7$']):add('1B',PQ,2,p,S,t)
add('1B',PQ,3,'','','<b>a</b>&nbsp; Simplify $\\dfrac{3}{4} + \\dfrac{m}{8}$ &emsp;&emsp; <b>b</b>&nbsp; Hence, solve $\\dfrac{3}{4} + \\dfrac{m}{8} = 2$')
S='Solve these linear equations.'
for p,t in zip('abc',['$3 - 2x = 9$','$3(2x + 1) = 7 - 2(x + 5)$','$\\dfrac{x - 9}{4} = -2$']):add('1B',SA,2,p,S,t)
add('1B',SA,5,'a–b','Marie’s watering can is initially filled with $2$ litres of water. However, the watering can has a small hole in the base and is leaking at a rate of $0.4$ litres per minute.','<b>a</b>&nbsp; Write a rule for the volume of water, $V$ litres, in the can after $t$ minutes.<br><b>b</b>&nbsp; What volume of water remains after $90$ seconds?')
add('1B',MC,2,'','The solution to $-4(2x - 6) = 10x$ is:',mc(['$x = \\dfrac{3}{2}$','$x = 12$','$x = \\dfrac{4}{3}$','$x = -12$','$x = -\\dfrac{4}{3}$']))
add('1B',MC,4,'','$\\dfrac{x + 1}{3} + \\dfrac{2x}{7}$ simplifies to:',mc(['$\\dfrac{3x + 1}{10}$','$\\dfrac{17x + 3}{21}$','$\\dfrac{3x + 1}{21}$','$\\dfrac{13x + 7}{21}$','$\\dfrac{13x + 1}{10}$']),True)
S='Solve the following inequalities and graph their solutions on a number line.'
for p,t in zip('abcd',['$2a + 3 > 9$','$8 - \\dfrac{x}{2} \\leqslant 10$','$5m + 2 > 7m - 6$','$-(a - 3) \\leqslant 5(a + 3)$']):add('1C',PQ,4,p,S,t)
S='Solve the following inequalities.'
for p,t in zip('abcd',['$4x - 3 > 17$','$3x + 2 \\leqslant 4(x - 2)$','$1 - \\dfrac{x}{3} < 2$','$-2x \\geqslant -4(1 - 3x)$']):add('1C',SA,4,p,S,t)
S='Simplify the following algebraic fractions.'
for p,t in zip('ab',['$\\dfrac{a + 4}{8} + \\dfrac{1 - 3a}{12}$','$\\dfrac{3x + 2}{5} - \\dfrac{x - 2}{3}$']):add('1D',PQ,5,p,S,t,True)
S='Solve the following equations.'
for p,t in zip('ab',['$\\dfrac{2y + 1}{2} - \\dfrac{y + 4}{5} = 2$','$\\dfrac{2a - 3}{3} = \\dfrac{4a + 2}{4}$']):add('1D',PQ,6,p,S,t,True)
S='Simplify these algebraic fractions using the lowest common denominator.'
for p,t in zip('abc',['$\\dfrac{2x}{3} + \\dfrac{4}{9}$','$\\dfrac{x}{8} + \\dfrac{x + 2}{4}$','$\\dfrac{x + 2}{3} - \\dfrac{x - 4}{5}$']):add('1D',SA,6,p,S,t,True)
S='Solve the following equations.'
for p,t in zip('abcd',['$\\dfrac{2x + 1}{5} + \\dfrac{x - 3}{10} = 2$','$\\dfrac{4 - x}{6} - \\dfrac{x + 2}{4} = 1$','$\\dfrac{x}{4} - 1 = \\dfrac{3x}{5}$','$\\dfrac{x + 2}{3} = \\dfrac{2x - 1}{4}$']):add('1D',SA,7,p,S,t,True)
S='Decide if the point $(-3, 2)$ is on the line with the given equations.'
for p,t in zip('ab',['$y = x + 2$','$-2x + y = 8$']):add('1E',PQ,7,p,S,t)
add('1E',PQ,8,'a','Sketch the following linear relations. For parts a and b, use the method suggested.','$y = -\\dfrac{3}{2}x + 1$; use the gradient and $y$-intercept.')
add('1E',PQ,8,'b','Sketch the following linear relations. For parts a and b, use the method suggested.','$-2x - 3y = 6$; use the $x$- and $y$-intercepts.')
for p,t in zip('cde',['$y = 3$','$x = -2$','$y = -\\dfrac{3}{4}x$']):add('1E',PQ,8,p,'Sketch the following linear relations.',t)
S='State the gradient and coordinates of the $y$-intercept of the following lines.'
for p,t in zip('ab',['$y = 3x - 2$','$3x + 5y = 15$']):add('1E',PQ,9,p,S,t)
S='Sketch graphs of the following linear relations, labelling the axis intercepts.'
for p,t in zip('abcdefgh',['$y = 3x - 9$','$y = 5 - 2x$','$y = 3$','$x = 5$','$y = 2x$','$y = -5x$','$x + 2y = 8$','$3x + 8y = 24$']):add('1E',SA,8,p,S,t)
add('1E',MC,5,'','If $(-1, 2)$ is a point on the line $ax - 4y + 11 = 0$, the value of $a$ is:',mc(['$-19$','$3$','$-\\dfrac{15}{2}$','$5$','$-1$']))
add('1E',MC,7,'','The gradient and the coordinates of the $y$-intercept, respectively, of the graph of $3x + 8y = 2$ are:',mc(['$-\\dfrac{3}{8}, \\left(0, \\dfrac{1}{4}\\right)$','$3, (0, 2)$','$\\dfrac{2}{3}, \\left(0, \\dfrac{1}{4}\\right)$','$-3, (2, 0)$','$\\dfrac{3}{8}, (2, 0)$']))
add('1F',SA,10,'','For the line that passes through the points $(-2, 8)$ and $(3, 5)$, determine:','<b>a</b>&nbsp; the gradient of the line &emsp;&emsp; <b>b</b>&nbsp; the equation of the line.')
add('1F',MC,8,'','The equation of the line joining the points $(-1, 3)$ and $(1, -1)$ is:',mc(['$2y - x = 1$','$y = 2x - 1$','$y = -2x + 1$','$y - 2x = 1$','$y = \\dfrac{1}{2}x + 1$']))
S='Find the midpoint and the exact length of the line segment joining these points.'
for p,t in zip('abc',['$(2, 5)$ and $(6, 11)$','$(3, -2)$ and $(8, 4)$','$(-1, -4)$ and $(2, -1)$']):add('1G',SA,11,p,S,t)
add('1G',SA,13,'c','Find the value(s) of the pronumeral in each situation below.','The distance between $(c, -1)$ and $(2, 2)$ is $\\sqrt{13}$.')
add('1G',MC,9,'','The midpoint of the line segment joining the points $(a, -6)$ and $(7, b)$ is $(4.5, -1)$. The values of the pronumerals are:',mc(['$a = 2, b = 8$','$a = 3, b = -11$','$a = 9, b = 5$','$a = 2, b = 4$','$a = 2.5, b = 5$']))
S='Determine the equation of the line that is:'
for p,t in zip('abcd',['parallel to the line $y = 3x + 8$ and passes through the point $(2, 4)$','parallel to the line with equation $y = 4$ and passes through the point $(3, -1)$','perpendicular to the line $y = 2x - 4$ and has a $y$-intercept with coordinates $(0, 5)$','perpendicular to the line with equation $x + 3y = 5$ and passes through the point $(2, 5)$.']):add('1H',SA,12,p,S,t)
S='Find the value(s) of the pronumeral in each situation below.'
add('1H',SA,13,'a',S,'The gradient of the line joining the points $(2, -5)$ and $(6, a)$ is $3$.')
add('1H',SA,13,'b',S,'The line $bx + 2y = 7$ is parallel to the line $y = 4x + 3$.')
add('1H',MC,10,'','The line that is perpendicular to the line with equation $y = -3x + 7$ is:',mc(['$y = -3x + 2$','$3x + y = -1$','$y = 3x - 3$','$3y = 4 - x$','$3y - x = 4$']))
add('1H',MC,11,'','The line that is parallel to the line with equation $y = 2x + 3$ and passes through the point $(-3, 2)$ has the equation:',mc(['$2x + y = 5$','$y = 2x + 8$','$y = -\\dfrac{1}{2}x + \\dfrac{1}{2}$','$y = 2x - 4$','$y - 2x = -7$']))
S='Solve the following simultaneous equations, using the substitution method.'
add('1I',SA,14,'a',S,'$\\begin{aligned} y &= 5x + 14 \\\\ y &= 2x + 5 \\end{aligned}$')
add('1I',SA,14,'b',S,'$\\begin{aligned} 3x - 2y &= 18 \\\\ y &= 2x + 5 \\end{aligned}$')
add('1I',MC,12,'','The solution to the simultaneous equations $2x - 3y = -1$ and $y = 2x + 3$ is:',mc(['$x = -2, y = -1$','$x = \\dfrac{5}{2}, y = 8$','$x = 2, y = 7$','$x = -\\dfrac{2}{3}, y = -\\dfrac{1}{9}$','$x = -3, y = 3$']))
S='Solve these simultaneous equations by elimination.'
add('1J',SA,15,'a',S,'$\\begin{aligned} 3x + 2y &= -11 \\\\ 2x - y &= -5 \\end{aligned}$')
add('1J',SA,15,'b',S,'$\\begin{aligned} 2y - 5x &= 4 \\\\ 3y - 2x &= 6 \\end{aligned}$')
add('1K',SA,16,'','At the movies Jodie buys three regular popcorns and five small drinks for her friends at a cost of $\\$24.50$. Her friend Renee buys four regular popcorns and three small drinks for her friends at a cost of $\\$23.50$. Find the individual costs of a regular popcorn and a small drink.','')
add('1K',MC,13,'','A community fundraising concert raises $\\$3540$ from ticket sales to $250$ people. Children’s tickets were sold for $\\$12$ and adult tickets sold for $\\$18$. If $x$ adults and $y$ children attended the concert, the two equations that represent this problem are:',mc(['$\\begin{aligned} x + y &= 250 \\\\ 18x + 12y &= 3540 \\end{aligned}$','$\\begin{aligned} x + y &= 3540 \\\\ 216xy &= 3540 \\end{aligned}$','$\\begin{aligned} x + y &= 250 \\\\ 12x + 18y &= 3540 \\end{aligned}$','$\\begin{aligned} x + y &= 3540 \\\\ 18x + 12y &= 250 \\end{aligned}$','$\\begin{aligned} 3x + 2y &= 3540 \\\\ x + y &= 250 \\end{aligned}$']))
S='Sketch these regions.'
for p,t in zip('ab',['$y \\geqslant 3x - 4$','$2x - 3y > -8$']):add('1L',SA,17,p,S,t)
add('1L',SA,18,'','Shade the intersecting region of the inequalities $x + 2y \\geqslant 4$ and $3x - 2y < 12$ by sketching their regions on the same axes and finding their point of intersection.','')
add('1L',MC,14,'','The point that is <i>not</i> in the region defined by $2x - 3y \\leqslant 5$ is:',mc(['$(0, 0)$','$(1, -1)$','$(-3, 2)$','$(2, -1)$','$\\left(\\dfrac{5}{2}, 3\\right)$']))
for i,x in enumerate(items):x['id']=f"C10-{x['sub']}-"+('PQ' if 'Progress' in x['src'] else 'MC' if 'Multiple' in x['src'] else 'SA')+x['src'].split()[-1][1:].replace('–','')
from collections import Counter;print(len(items),Counter(x['sub'] for x in items))
assert len({x['id'] for x in items})==len(items)
json.dump(items,open('pool.json','w'),ensure_ascii=False,indent=1)
