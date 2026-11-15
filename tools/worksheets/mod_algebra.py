"""10MAG Modified, G3 Algebra and Linear Relations: one guided worksheet per lesson (L1-L15, same order as 10MAG).
Year 8 level; Year 9 where the skill is first taught in Year 9 (gradient-intercept form, gradient between two points,
equation of a line, midpoint/length, parallel/perpendicular, simultaneous equations). Everything verbatim + cited.
1I, 1J, 1L have no Freefall sheet: their worksheets carry a Practice box (Cambridge 8/9 exercise questions, Rocco 16 Nov).
Run from the repo root:  python3 tools/worksheets/mod_algebra.py [L1 ...]"""
import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from modified import *

def plane(x0,x1,y0,y1,lines=(),pts=(),grid=True,w=48,ticks=True,shade=None):
    """Cartesian plane in house style. lines: ('m',m,c,label) | ('h',v,label) | ('v',v,label); pts: (x,y,label).
    grid=False draws axes only (labels on the marked points only), like the book's sketches."""
    u=10;W=(x1-x0)*u;H=(y1-y0)*u;X=lambda x:(x-x0)*u;Y=lambda y:(y1-y)*u;o=[]
    if grid:
        for i in range(x0,x1+1):o.append(f'<line x1="{X(i)}" y1="0" x2="{X(i)}" y2="{H}" stroke="#bbb" stroke-width=".4"/>')
        for j in range(y0,y1+1):o.append(f'<line x1="0" y1="{Y(j)}" x2="{W}" y2="{Y(j)}" stroke="#bbb" stroke-width=".4"/>')
    ox,oy=X(0),Y(0)
    o.append(f'<line x1="-4" y1="{oy}" x2="{W+4}" y2="{oy}" stroke="#000" stroke-width=".8"/><line x1="{ox}" y1="{H+4}" x2="{ox}" y2="-4" stroke="#000" stroke-width=".8"/>'
             f'<path d="M{W+6} {oy} l-5 -2.2 v4.4z M{ox} -6 l-2.2 5 h4.4z M-6 {oy} l5 -2.2 v4.4z M{ox} {H+6} l-2.2 -5 h4.4z"/>'
             f'<text x="{W+5}" y="{oy-4}" font-size="8" font-style="italic" font-family="Times New Roman">x</text><text x="{ox+4}" y="-2" font-size="8" font-style="italic" font-family="Times New Roman">y</text>'
             f'<text x="{ox-2}" y="{oy+8}" font-size="7" font-style="italic" font-family="Times New Roman" text-anchor="end">O</text>')
    if grid and ticks:
        for i in range(x0,x1+1):
            if i:o.append(f'<text x="{X(i)}" y="{oy+8}" font-size="6" text-anchor="middle">{i}</text>'.replace('>-','>−'))
        for j in range(y0,y1+1):
            if j:o.append(f'<text x="{ox-2.5}" y="{Y(j)+2}" font-size="6" text-anchor="end">{j}</text>'.replace('>-','>−'))
    clip=f'<clipPath id="c{x0}{x1}{y0}{y1}"><rect x="-2" y="-2" width="{W+4}" height="{H+4}"/></clipPath>'
    for L in lines:
        if L[0]=='m':
            _,m,c,lab=L;a,b=(x0-1,x1+1);seg=(X(a),Y(m*a+c),X(b),Y(m*b+c))
        elif L[0]=='h':_,v,lab=L;seg=(-3,Y(v),W+3,Y(v))
        else:_,v,lab=L;seg=(X(v),H+3,X(v),-3)
        o.append(f'<line x1="{seg[0]:.1f}" y1="{seg[1]:.1f}" x2="{seg[2]:.1f}" y2="{seg[3]:.1f}" stroke="#000" stroke-width="1.1" clip-path="url(#c{x0}{x1}{y0}{y1})"/>')
        if lab:
            lx,ly=lab[1],lab[2];o.append(f'<text x="{X(lx)}" y="{Y(ly)}" font-size="7" font-family="Times New Roman" font-style="italic">{lab[0]}</text>')
    for x,y,lab in pts:
        o.append(f'<circle cx="{X(x)}" cy="{Y(y)}" r="1.6"/>')
        if lab:o.append(f'<text x="{X(x)+3}" y="{Y(y)-3}" font-size="7">{lab}</text>'.replace('-','−'))
    return f'<svg viewBox="-9 -9 {W+18} {H+18}" style="width:{w}mm;display:block;margin:1mm 0">{clip}{"".join(o)}</svg>'
def axes_tick(x0,x1,y0,y1,xt=(),yt=(),lines=(),w=34):
    """axes only, with chosen intercepts labelled (book-style sketch)"""
    s=plane(x0,x1,y0,y1,lines,grid=False,w=w);u=10;X=lambda x:(x-x0)*u;Y=lambda y:(y1-y)*u;add=''
    for t in xt:add+=f'<text x="{X(t)-2}" y="{Y(0)-3}" font-size="7" text-anchor="end">{t}</text>'.replace('>-','>−')
    for t in yt:add+=f'<text x="{X(0)-3}" y="{Y(t)+2.5}" font-size="7" text-anchor="end">{t}</text>'.replace('>-','>−')
    return s.replace('</svg>',add+'</svg>')
NL=lambda a,b:numline(a,b,1,1,'',w=95)
EQ=lambda a,b:f'$\\begin{{aligned}}{a}\\\\{b}\\end{{aligned}}$'
Y8='Year 8';Y9='Year 9'
P=lambda q,h,src:(q,h,src)
C8='Cambridge 8';C9='Cambridge 9'

W={
'L1':dict(sub='1A',title='Review of algebra',src=[(8,'5B','pp. 342–344'),(8,'5C','pp. 347–348'),(8,'5G','pp. 366–368'),(8,'5H','pp. 372–374')],
 li=['To be able to substitute values to evaluate algebraic expressions','To be able to combine like terms to simplify expressions','To be able to expand brackets using the distributive law','To be able to factorise expressions'],
 ki=['To <b>evaluate</b> an expression or to <b>substitute</b> values means to replace each pronumeral in an expression with a number to obtain a final value.',
     '<b>Like terms</b> contain exactly the same pronumerals with the same powers; the pronumerals do not need to be in the same order; for example, $4ab$ and $7ba$ are like terms.',
     'Like terms can be combined when they are added or subtracted to simplify an expression; for example, $3xy + 5xy = 8xy$.',
     'The <b>distributive law</b> is used to rewrite an expression without brackets. For example: $4(2x + 5) = 8x + 20$ and $3(5 - 2y) = 15 - 6y$',
     'To <b>factorise</b> an expression, first take the HCF of the terms outside the brackets and divide each term by it, leaving the result in brackets.'],
 ex=[dict(n='Year 8 Example 3',t='Substituting values',q='Substitute $x = 3$ and $y = 6$ to evaluate the following expressions.',parts=['$5x$','$5x^2 + 2y + x$'],
          yq='Substitute $x = 4$ and $y = 5$ to evaluate the following expressions.',yparts=['$6x$','$x^2 + 2y - 3x$'],h=[8,16]),
     dict(n='Year 8 Example 6',t='Simplifying by combining like terms',q='Simplify the following by combining like terms.',parts=['$7t + 2t - 3t$','$4x + 3y + 2x + 7y$','$7ac + 3b - 2ca + 4b - 5b$'],
          yq='Simplify the following by combining like terms.',yparts=['$8x - 3x + 2x$','$4a + 3b + 2b + 9a$','$6pq + 8p - 2qp + 5q - 2p$'],h=[7,12,14]),
     dict(n='Year 8 Example 12',t='Expanding using the distributive law',q='Expand the following using the distributive law.',parts=['$3(2x + 5)$','$4x(2 - y)$','$-8(7 + 2y)$'],
          yq='Expand the following using the distributive law.',yparts=['$5(3x + 4)$','$7a(4 - b)$','$-2(8 + 5b)$'],h=[9,9,9]),
     dict(n='Year 8 Example 15',t='Factorising expressions',q='Factorise the following expressions.',parts=['$6x + 15$','$12a + 18ab$','$21x - 14y$'],
          yq='Factorise the following expressions.',yparts=['$12x + 30$','$15a + 25ab$','$18x - 15y$'],h=[9,9,9])],
 sc=CL(8,[3,6,12,15],5)),
'L2':dict(sub='1B',title='Solving linear equations',src=[(8,'7C','pp. 491–493'),(8,'7D','pp. 496–498'),(8,'7E','pp. 501–503')],
 li=['To be able to solve equations involving pronumerals on both sides','To be able to solve equations by expanding brackets','To be able to solve equations involving algebraic fractions'],
 ki=['If both sides of an equation have the same term added or subtracted, the new equation will be equivalent to the original equation.',
     'If pronumerals are on both sides of an equation, add or subtract terms so that the pronumeral appears only one side.',
     'Equations involving brackets can be solved by first expanding brackets and collecting like terms.',
     'To solve an equation with a fraction on one side, multiply both sides by the denominator.'],
 ex=[dict(n='Year 8 Example 7',t='Solving equations with pronumerals on both sides',q='Solve the following equations and check your solutions using substitution.',parts=['$7t + 4 = 5t + 10$','$6x + 4 = 22 - 3x$','$2u = 7u - 20$'],
          yq='Solve the following equations and check your solutions using substitution.',yparts=['$7m + 2 = 4m + 14$','$5x + 2 = 23 - 2x$','$4p = 9p - 30$'],h=[18,18,16]),
     dict(n='Year 8 Example 8',t='Solving equations with brackets',q='Solve the following equations by first expanding any brackets.',parts=['$3(p + 4) = 18$','$4(2x - 5) + 3x = 57$'],
          yq='Solve the following equations by first expanding any brackets.',yparts=['$5(k + 3) = 30$','$2(3x - 4) + 2x = 40$'],h=[18,22],src_note='parts a and c'),
     dict(n='Year 8 Example 6',t='Solving equations with fractions',q='Solve the following equations algebraically.',parts=['$\\dfrac{4x}{3} = 8$','$\\dfrac{4y + 15}{9} = 3$','$4 + \\dfrac{5x}{2} = 29$'],
          yq='Solve the following equations algebraically.',yparts=['$\\dfrac{5k}{2} = 20$','$\\dfrac{3y + 6}{2} = 9$','$2 + \\dfrac{5x}{3} = 12$'],h=[16,18,18],src_note='parts a–c')],
 sc=CL(8,[6,7,5],7)),
'L3':dict(sub='1C',title='Linear inequalities',src=[(8,'7I','pp. 523–525'),(8,'7J','pp. 528–530')],
 li=['To be able to represent inequalities on a number line using open or closed circles and/or arrows','To be able to describe real-life situations using inequalities','To understand that the sign of an inequality is reversed if both sides are multiplied or divided by a negative number','To be able to solve inequalities algebraically'],
 ki=['An <b>inequality</b> is a statement of the form: LHS $>$ RHS (greater than), LHS $\\geqslant$ RHS (greater than or equal), LHS $<$ RHS (less than), LHS $\\leqslant$ RHS (less than or equal).',
     'Inequalities can be reversed: $3 < x$ and $x > 3$ are equivalent.',
     'Inequalities can be represented on a number line, using closed circles at the end points if the value is included, or open circles if it is excluded.',
     'Given an inequality, an equivalent inequality can be obtained by: adding or subtracting an expression from both sides; multiplying or dividing both sides by any positive number; multiplying or dividing both sides by a negative number and reversing the inequality symbol.'],
 ex=[dict(n='Year 8 Example 15',t='Representing inequalities on a number line',q='Represent the following inequalities on a number line.',parts=['$x \\geqslant 4$'+NL(0,8),'$x < 6$'+NL(0,8),'$1 < x \\leqslant 5$'+NL(0,8)],
          yq='Represent the following inequalities on a number line.',yparts=['$x \\geqslant 5$'+NL(0,10),'$x < 9$'+NL(4,12),'$3 \\leqslant x < 6$'+NL(0,8)],h=[1,1,1]),
     dict(n='Year 8 Example 16',t='Using inequalities to describe real-life situations',q='Describe the following situations as an inequality, using $x$ to stand for the unknown quantity.',parts=['Fred is shorter than $160\\,\\text{cm}$.','John is at least as old as Maria, who is $10$.','Rose’s test score is between $40$ and $50$ inclusive.'],
          yq='Describe the following situations as an inequality, using $x$ to stand for the unknown quantity.',yparts=['Michelle is taller than $170\\,\\text{cm}$.','Peter’s salary is at least &#36;100&#8201;000 per annum.','The average rating for this café is between $3$ and $4$ exclusive.'],h=[7,7,7]),
     dict(n='Year 8 Example 17',t='Solving inequalities',q='Solve the following inequalities.',parts=['$5x + 2 < 47$','$\\dfrac{3 + 4x}{9} \\geqslant 3$','$15 - 2x > 1$'],
          yq='Solve the following inequalities.',yparts=['$3x + 6 < 21$','$\\dfrac{4 + 2x}{3} \\leqslant 2$','$20 - 3x < 8$'],h=[14,18,16])],
 sc=CL(8,[13,14,15],7)),
'L4':dict(sub='1E',title='Graphing straight lines',src=[(8,'9B','pp. 644–646'),(8,'9F','pp. 681–684')],
 li=['To understand that a point lies on the graph of an equation if substituting the values for $x$ and $y$ makes the equation true','To understand that the $x$-intercept is the point on the graph where the $y$-coordinate is zero','To understand that the $y$-intercept is the point on the graph where the $x$-coordinate is zero','To be able to sketch linear graphs by first finding the axes intercepts'],
 ki=['A <b>linear relationship</b> will result in a straight line graph.',
     'Special lines: <b>Horizontal</b>: All points will have the same $y$-value, for example, $y = 4$. <b>Vertical</b>: All points will have the same $x$-value, for example, $x = -2$.',
     'The <b>$y$-intercept</b> is the point on a graph where $x = 0$.',
     'The <b>$x$-intercept</b> is the point on a graph where $y = 0$. Find the $x$-intercept by substituting $y = 0$ into the rule. Solve using algebraic steps.'],
 ex=[dict(n='Year 8 Example 3',t='Checking if a point lies on a line',q='Decide if the points $(1, 3)$ and $(-2, -4)$ lie on the graph of $y = 3x$.',parts=[],
          yq='Decide if the points $(4, 12)$ and $(-2, -8)$ lie on the graph of $y = 4x$.',yparts=[],h=22),
     dict(n='Year 8 Example 11',t='Finding the $x$- and $y$-intercepts',q='For the graphs of these rules, find the $x$- and $y$-intercepts.',parts=['$y = 3x - 6$','$y = -2x + 1$'],
          yq='For the graphs of these rules, find the $x$- and $y$-intercepts.',yparts=['$y = 2x - 10$','$y = -5x + 2$'],h=[24,24]),
     dict(n='Year 8 Example 12',t='Sketching with intercepts',q='Find the $x$- and $y$-intercepts and then sketch the graph of the rule $y = 2x - 8$.',parts=[],
          yq='Find the $x$- and $y$-intercepts and then sketch the graph of the rule $y = 3x + 6$.',yparts=[],h=55)],
 sc=CL(8,[4,12,13],9)),
'L5':dict(sub='1F',part=1,title='Gradient',src=[(9,'4F','pp. 277–280'),(9,'4D','pp. 264–268')],
 li=['To know the gradient–intercept form of a straight line graph','To be able to determine the gradient and $y$-intercept from the rule of a linear graph','To be able to use the $y$-intercept and gradient to sketch a straight line graph','To be able to find the gradient of a line using a graph or two given points'],
 ki=['Gradient $(m) = \\dfrac{\\text{rise}}{\\text{run}}$',
     'The gradient–intercept form of a straight line equation: $y = mx + c$, where $m$ = gradient and $y$-intercept $= (0, c)$.',
     'If the $y$-intercept is $(0, 0)$, the equation becomes $y = mx$ and these graphs will therefore pass through the origin.',
     'To sketch a graph using the gradient–intercept method, locate the $y$-intercept and use the gradient to find a second point. For example, if $m = \\frac{2}{5}$, move $5$ across (right) and $2$ up.'],
 ex=[dict(n='Year 9 Example 10',t='Stating the gradient and $y$-intercept',q='State the gradient and the $y$-intercept coordinates for the graphs of the following.',parts=['$y = 2x + 1$','$y = -3x$'],
          yq='State the gradient and the $y$-intercept coordinates for the graphs of the following.',yparts=['$y = 5x - 2$','$y = 6x$'],h=[9,9]),
     dict(n='Year 9 Example 12',t='Sketching linear graphs using the gradient and $y$-intercept',q='Find the value of the gradient and $y$-intercept for the following and sketch their graphs.',parts=['$y = 2x - 1$'+plane(-4,4,-4,4,w=36)],
          yq='Find the value of the gradient and $y$-intercept for the following and sketch their graphs.',yparts=['$y = 3x - 2$'+plane(-4,4,-4,4,w=36)],h=[4],src_note='part a'),
     dict(n='Year 9 Example 8',t='Finding the gradient between two points',q='Find the gradient $(m)$ of the line joining the given points.',parts=['$A(3, 4)$ and $B(5, 6)$','$A(-3, 6)$ and $B(1, -3)$'],
          yq='Find the gradient $(m)$ of the line joining the given points.',yparts=['$A(2, 6)$ and $B(3, 8)$','$A(-5, 1)$ and $B(2, -3)$'],h=[18,18])],
 sc=CL(9,[12,8],4)),
'L6':dict(sub='1F',part=2,title='Finding the equation of a line',src=[(9,'4G','pp. 285–287')],
 li=['To know that all straight line equations can be written in the form $y = mx + c$','To know how to use the $y$-intercept and gradient to form a straight line equation','To be able to find the equation of a line given two points'],
 ki=['To find the equation of a line in gradient–intercept form $y = mx + c$, you need to find: the value of the gradient $(m)$ using $m = \\dfrac{\\text{rise}}{\\text{run}}$; the value of the constant $(c)$, by observing the $y$-intercept or by substituting another point.'],
 ex=[dict(n='Year 9 Example 13',t='Finding the equation of a line given the $y$-intercept and another point',q='Determine the equation of the straight line shown here.'+axes_tick(-4,3,-5,2,xt=[-2],yt=[-4],lines=[('m',-2,-4,None)]),parts=[],
          yq='Determine the equation of the straight line shown here.'+axes_tick(-2,4,-2,5,xt=[2],yt=[4],lines=[('m',-2,4,None)]),yparts=[],h=26),
     dict(n='Year 9 Example 14',t='Finding the equation of a line given the gradient and a point',q='Find the equation of the line which has a gradient $m$ of $\\frac{1}{3}$ and passes through the point $(9, 2)$.',parts=[],
          yq='Find the equation of the line which has a gradient $m$ of $\\frac{2}{3}$ and passes through the point $(-3, 4)$.',yparts=[],h=34)],
 sc=CL(9,[13,14],4)),
'L7':dict(sub='1G',title='Length and midpoint of a line segment',src=[(9,'4H','pp. 290–292')],
 li=['To understand that a line segment has a midpoint and a length','To know how to find the midpoint of a line segment between two points','To understand how Pythagoras’ theorem can be used to find the distance between two points','To be able to find the length of a line segment'],
 ki=['The <b>midpoint</b> $(M)$ of a line segment is the halfway point between the two endpoints.',
     'The $x$-coordinate of the midpoint is the average (mean) of the $x$-coordinates of the two endpoints. The $y$-coordinate of the midpoint is the average (mean) of the $y$-coordinates of the two endpoints.',
     '$M = \\left(\\dfrac{x_1 + x_2}{2}, \\dfrac{y_1 + y_2}{2}\\right)$'],
 ex=[dict(n='Year 9 Example 15',t='Finding a midpoint of a line segment',q='Find the midpoint $M(x, y)$ of the line segment joining these pairs of points.',parts=['$(1, 0)$ and $(4, 4)$','$(-3, -2)$ and $(5, 3)$'],
          yq='Find the midpoint $M(x, y)$ of the line segment joining these pairs of points.',yparts=['$(0, 2)$ and $(4, 5)$','$(-4, 1)$ and $(2, -4)$'],h=[20,20]),
     dict(n='Year 9 Example 16',t='Finding the length of a line segment',q='Find the length of the segment joining $(-2, 2)$ and $(4, -1)$, correct to two decimal places.',parts=[],
          yq='Find the length of the segment joining $(-1, 5)$ and $(3, -2)$, correct to two decimal places.',yparts=[],h=50)],
 sc=CL(9,[15,16],4)),
'L8':dict(sub='1H',part=1,title='Parallel lines',src=[(9,'4I','pp. 295–296'),(9,'4F','pp. 278–279')],
 li=['To understand what is meant by lines being parallel or perpendicular','To know the relationship between the gradients of lines that are either parallel or perpendicular','To be able to rearrange linear equations'],
 ki=['If two lines are <b>parallel</b> then they have the same gradient.',
     'If two <b>perpendicular</b> lines (at right angles) have gradients $m_1$ and $m_2$ then: $m_1 \\times m_2 = -1$ or $m_2 = -\\dfrac{1}{m_1}$. The negative reciprocal of $m_1$ gives $m_2$.',
     'The gradient–intercept form of a straight line equation: $y = mx + c$, where $m$ = gradient and $y$-intercept $= (0, c)$.'],
 ex=[dict(n='Year 9 Example 11',t='Rearranging linear equations',q='Rearrange these linear equations into the form shown in the brackets.',parts=['$4x + 2y = 10 \\quad (y = mx + c)$','$y = 4x - 7 \\quad (ax + by = d)$'],
          yq='Rearrange these linear equations into the form shown in the brackets.',yparts=['$10x + 2y = 20 \\quad (y = mx + c)$','$y = -2x + 3 \\quad (ax + by = d)$'],h=[24,18]),
     dict(n='Year 9 Example 17',t='Finding the equation of a parallel line',q='Find the equation of a line which is parallel to $y = 3x - 1$ and passes through $(0, 4)$.',parts=[],
          yq='Find the equation of a line which is parallel to $y = 4x + 3$ and passes through $(0, -2)$.',yparts=[],h=30)],
 sc=CL(9,[10,17],4)),
'L9':dict(sub='1H',part=2,title='Perpendicular lines',src=[(9,'4I','pp. 295–297')],
 li=['To know the relationship between the gradients of lines that are either parallel or perpendicular','To be able to find the gradient of a perpendicular line','To be able to find the equation of a line given a point and a line to which it is parallel or perpendicular'],
 ki=['If two lines are parallel then they have the same gradient.',
     'If two perpendicular lines (at right angles) have gradients $m_1$ and $m_2$ then: $m_1 \\times m_2 = -1$ or $m_2 = -\\dfrac{1}{m_1}$',
     'The negative reciprocal of $m_1$ gives $m_2$. For example: If $m_1 = 4$ then $m_2 = -\\frac{1}{4}$.'],
 ex=[dict(n='Year 9 Example 18',t='Finding the equation of a perpendicular line',q='Find the equation of a line which is perpendicular to the line $y = 2x - 3$ and passes through $(0, -1)$.',parts=[],
          yq='Find the equation of a line which is perpendicular to the line $y = -3x + 1$ and passes through $(0, 4)$.',yparts=[],h=36)],
 sc=CL(9,[18],4)),
'L10':dict(sub='1I',part=1,title='Simultaneous equations: the graphical method',src=[(9,'4K','pp. 306–309')],practice_only=True,
 li=['To know that the point of intersection of two lines is the solution of the simultaneous equations','To know how to use the linear rules to check if a point is at the intersection of the two lines','To be able to use the graphs of two straight lines to read off the coordinates of the point of intersection'],
 ki=['When we consider two or more equations at the same time, they are called <b>simultaneous equations</b>.',
     'To determine the point of intersection of two lines, we can use an accurate graph and determine its coordinates $(x, y)$.',
     'The two graphs intersect at one point only and there is one solution $(x, y)$. The point of intersection is simultaneously on both lines and is the solution to the simultaneous equations.',
     'The two lines are parallel and there is no intersection.'],
 ex=[dict(n='Year 9 Example 20',t='Checking an intersection point',q='Decide if the given point is at the intersection of the two lines with the given equations.',parts=['$y = 2x + 3$ and $y = -x$ with point $(-1, 1)$','$y = -2x$ and $3x + 2y = 4$ with point $(2, -4)$'],
          yq='Decide if the given point is at the intersection of the two lines with the given equations.',yparts=['$y = 3x - 5$ and $y = -2x$ with point $(1, -2)$','$y = -4x$ and $3x - y = 2$ with point $(2, -8)$'],h=[22,22]),
     dict(n='Year 9 Example 21',t='Solving simultaneous equations graphically',q='Solve the simultaneous equations $y = 2x - 2$ and $x + y = 4$ graphically.'+plane(-2,5,-3,5,w=36),parts=[],
          yq='Solve the simultaneous equations $y = -x + 1$ and $2x + y = 3$ graphically.'+plane(-2,5,-3,5,w=36),yparts=[],h=4)],
 practice=[P('Decide if the given point is at the intersection of the two lines with the given equations.<br>$y = 3x - 4$ and $y = 2x - 2$ with point $(2, 2)$',14,f'{C9}, Exercise 4K Q1a (p. 310); adapted: stem reworded for a single part'),
           P('Decide if the given point is at the intersection of the two lines with the given equations.<br>$y = -x + 3$ and $y = -x$ with point $(2, 1)$',14,f'{C9}, Exercise 4K Q1b (p. 310); adapted: stem reworded for a single part'),
           P('Decide if the given point is at the intersection of the two lines with the given equations.<br>$y = -4x + 1$ and $y = -x - 1$ with point $(1, -3)$',14,f'{C9}, Exercise 4K Q1c (p. 310); adapted: stem reworded for a single part'),
           P('Solve these pairs of simultaneous equations graphically by finding the coordinates of the intersection point.<br>'+EQ('y = x + 2','y = 3x - 2')+plane(-2,5,-3,6,w=36),2,f'{C9}, Exercise 4K Q2h (p. 310); adapted: one part only')],
 sc=CL(9,[20,21],4)),
'L11':dict(sub='1I',part=2,title='Simultaneous equations using substitution',src=[(9,'2I','pp. 138–140')],practice_only=True,
 li=['To understand that for two different linear equations with two unknowns there is at most one solution','To know when the method of substitution can be used to solve simultaneous linear equations','To be able to use the substitution technique to solve simultaneous linear equations'],
 ki=['An algebraic method called <b>substitution</b> can be used to solve simultaneous equations. It is used when at least one of the equations has a single variable as the subject. For example, $y$ is the subject in the equation $y = x + 1$.',
     'To solve simultaneous equations using substitution: <b>1</b> Substitute one equation into the other, using brackets. <b>2</b> Solve for the remaining variable. <b>3</b> Substitute to find the value of the second variable.'],
 ex=[dict(n='Year 9 Example 21',t='Solving simultaneous equations using substitution',q='Solve each of the following pairs of simultaneous equations by using substitution.',parts=[EQ('x + y = 10','y = 4x'),EQ('3x + 2y = 19','y = 2x - 8')],
          yq='Solve each of the following pairs of simultaneous equations by using substitution.',yparts=[EQ('x + y = 8','y = 3x'),EQ('5x + 3y = 7','y = x + 5')],h=[32,38],src_note='parts a and b')],
 practice=[P('Solve each of the following pairs of simultaneous equations by using substitution.<br>'+EQ('x + y = 3','y = 2x'),24,f'{C9}, Exercise 2I Q1a (p. 141); adapted: one part only'),
           P('Solve each of the following pairs of simultaneous equations by using substitution.<br>'+EQ('x + y = 12','y = x + 6'),26,f'{C9}, Exercise 2I Q2a (p. 141); adapted: one part only'),
           P('Solve each of the following pairs of simultaneous equations by using substitution.<br>'+EQ('2x + y = 1','y = x + 4'),26,f'{C9}, Exercise 2I Q2b (p. 141); adapted: one part only'),
           P('Solve each of the following pairs of simultaneous equations by using substitution.<br>'+EQ('3x + 2y = 8','y = 4x - 7'),28,f'{C9}, Exercise 2I Q2d (p. 141); adapted: one part only')],
 sc=CL(9,[19],2)),
'L12':dict(sub='1J',title='Simultaneous equations using elimination',src=[(9,'2J','pp. 145–148')],practice_only=True,
 li=['To know that two equations can at times be added or subtracted to eliminate one of the variables','To understand that a matching pair is required to eliminate a variable from two equations','To know when to use addition and when to use subtraction to eliminate a variable','To be able to use elimination to solve simultaneous linear equations'],
 ki=['<b>Elimination</b> involves the addition or subtraction of two equations to remove one variable.',
     'Add equations to eliminate terms of opposite sign. Subtract equations to eliminate terms of the same sign.',
     'If terms cannot be eliminated just by using addition or subtraction, first multiply one or both equations to form a matching pair.'],
 ex=[dict(n='Year 9 Example 22',t='Solving simultaneous equations using elimination',q='Solve the following pairs of simultaneous equations by using elimination.',parts=[EQ('x - 2y = 1','-x + 5y = 2'),EQ('3x - 2y = 5','5x - 2y = 11')],
          yq='Solve the following pairs of simultaneous equations by using elimination.',yparts=[EQ('-x + y = 1','x - 2y = -3'),EQ('4x - 3y = -16','3x - 3y = -15')],h=[34,34]),
     dict(n='Year 9 Example 23',t='Solving simultaneous equations by creating a matching pair',q='Solve the following pairs of simultaneous equations by using elimination.',parts=[EQ('5x + 2y = -7','x + 7y = 25')],
          yq='Solve the following pairs of simultaneous equations by using elimination.',yparts=[EQ('7x + 2y = 12','x - 3y = 5')],h=[42],src_note='part a')],
 practice=[P('Solve these simultaneous equations by first adding the equations.<br>'+EQ('3x - y = 2','2x + y = 3'),24,f'{C9}, Exercise 2J Q1a (p. 149); adapted: one part only'),
           P('Solve these simultaneous equations by first adding the equations.<br>'+EQ('2x - 3y = -2','-5x + 3y = -4'),24,f'{C9}, Exercise 2J Q1b (p. 149); adapted: one part only'),
           P('Solve these simultaneous equations by first subtracting the equations.<br>'+EQ('3x + y = 10','x + y = 6'),24,f'{C9}, Exercise 2J Q2a (p. 149); adapted: one part only'),
           P('Solve these simultaneous equations by first subtracting the equations.<br>'+EQ('5x - y = -2','3x - y = 4'),24,f'{C9}, Exercise 2J Q2d (p. 149); adapted: one part only'),
           P('Solve the following pairs of simultaneous linear equations by using elimination.<br>'+EQ('4x + y = -8','3x - 2y = -17'),30,f'{C9}, Exercise 2J Q3a (p. 149); adapted: one part only'),
           P('Solve the following pairs of simultaneous linear equations by using elimination.<br>'+EQ('2x - y = 3','5x + 2y = 12'),30,f'{C9}, Exercise 2J Q3b (p. 149); adapted: one part only')],
 sc=CL(9,[20],2)),
'L13':dict(sub='1K',title='Applications of simultaneous equations',src=[(9,'2K','pp. 151–153')],
 li=['To know that if there are two variables in a problem, two equations will be required to find the solution','To be able to form a pair of equations from a word problem','To be able to identify which technique is best to apply to solve the simultaneous equations','To understand to check the solution by substituting into the original equations'],
 ki=['To solve worded problems with simultaneous equations complete these steps.<br>• Define two variables by writing down what they represent.<br>• Write a pair of simultaneous equations from the given information using your two variables.<br>• Solve the equations simultaneously using substitution or elimination.<br>• Check the solution by substituting into the original equations.<br>• Express the answer in words.'],
 ex=[dict(n='Year 9 Example 24',t='Setting up and solving simultaneous linear equations',q='The length of a rectangle is $5\\,\\text{cm}$ longer than its width. If the perimeter is $84\\,\\text{cm}$, find the dimensions of the rectangle.',parts=[],
          yq='The length of a rectangle is $6\\,\\text{cm}$ longer than its width. If the perimeter is $52\\,\\text{cm}$, find the dimensions of the rectangle.',yparts=[],h=48),
     dict(n='Year 9 Example 25',t='Solving further word problems with simultaneous equations',q='Andrea bought two containers of ice-cream and three bottles of maple syrup for a total of &#36;22. At the same shop, Bettina bought one container of the same ice-cream and two bottles of the same maple syrup for &#36;13. How much does each container of ice-cream and each bottle of maple syrup cost?',parts=[],
          yq='Wally bought three identical hats and four identical scarfs for &#36;70. From the same store on another day he bought five hats and two scarfs for &#36;64.40. How much does each hat and each scarf cost?',yparts=[],h=52)],
 sc=CL(9,[21],2)),
'L14':dict(sub='1L',part=1,title='Regions on the Cartesian plane',src=[(8,'9E','pp. 667–671')],practice_only=True,
 li=['To be able to sketch horizontal and vertical lines given their equation','To be able to graph inequalities using horizontal and vertical lines as regions in the plane'],
 ki=['A horizontal line (parallel to the $x$-axis) has a rule in the form $y = c$, where $c$ is any number.',
     'A vertical line (parallel to the $y$-axis) has a rule in the form $x = k$, where $k$ is any number.',
     'A <b>region</b> in the plane is described using an inequality. All the points that satisfy the inequality form the shaded region.',
     'A dashed line is used to show that the points on the line are not included in the region. A dashed line is used when the $<$ or $>$ symbols are given.',
     'A full line is used to show that the points on the line are included in the region. A full line is used when the $\\leqslant$ or $\\geqslant$ symbols are given.'],
 ex=[dict(n='Year 8 Example 8',t='Finding rules for horizontal and vertical lines',q='Write the rule for these horizontal and vertical lines.',parts=[axes_tick(-3,3,-4,2,lines=[('h',-3,None)]).replace('</svg>','<text x="32" y="58" font-size="7">(0, −3)</text></svg>'),axes_tick(-2,8,-3,3,lines=[('v',7,None)]).replace('</svg>','<text x="72" y="38" font-size="7">(7, 0)</text></svg>')],
          yq='Write the rule for these horizontal and vertical lines.',yparts=[axes_tick(-3,3,-2,3,lines=[('h',2,None)]).replace('</svg>','<text x="32" y="8" font-size="7">(0, 2)</text></svg>'),axes_tick(-5,2,-3,3,lines=[('v',-4,None)]).replace('</svg>','<text x="12" y="28" font-size="7">(−4, 0)</text></svg>')],h=[7,7]),
     dict(n='Year 8 Example 9',t='Sketching regions in the plane',q='Sketch the following regions.',parts=['$y \\geqslant -2$'+plane(-4,4,-4,4,w=34),'$x < 5$'+plane(-2,6,-4,4,w=34)],
          yq='Sketch the following regions.',yparts=['$y < 1$'+plane(-4,4,-4,4,w=34),'$x \\geqslant -4$'+plane(-6,2,-4,4,w=34)],h=[1,1])],
 practice=[P('Sketch horizontal or vertical graphs for these rules.<br>$y = -1$'+plane(-4,4,-4,4,w=34),1,f'{C8}, Exercise 9E Q2b (p. 674); adapted: one part only'),
           P('Sketch horizontal or vertical graphs for these rules.<br>$x = 4$'+plane(-4,5,-4,4,w=34),1,f'{C8}, Exercise 9E Q2f (p. 674); adapted: one part only'),
           P('Sketch the following regions.<br>$y \\geqslant 1$'+plane(-4,4,-4,4,w=34),1,f'{C8}, Exercise 9E Q3a (p. 674); adapted: one part only'),
           P('Sketch the following regions.<br>$y < 3$'+plane(-4,4,-4,4,w=34),1,f'{C8}, Exercise 9E Q3c (p. 674); adapted: one part only'),
           P('Sketch the following regions.<br>$x < 2$'+plane(-4,4,-4,4,w=34),1,f'{C8}, Exercise 9E Q3e (p. 674); adapted: one part only'),
           P('Sketch the following regions.<br>$x > -1$'+plane(-4,4,-4,4,w=34),1,f'{C8}, Exercise 9E Q3h (p. 674); adapted: one part only')],
 sc=CL(8,[9,10],9)),
'L15':dict(sub='1L',part=2,title='Using graphs to solve inequalities',src=[(8,'9E','pp. 667–673')],practice_only=True,
 li=['To understand that graphs can be used to solve inequalities','To be able to solve simple inequalities using graphs'],
 ki=['Graphs can be used to solve inequalities. To solve $2x + 1 \\leqslant 5$ for example: Consider the graph of $y = 2x + 1$ and the region $y \\leqslant 5$.',
     'The solution to $2x + 1 \\leqslant 5$ will be all the $x$ values of the points that are on the line $y = 2x + 1$ and also in the region $y \\leqslant 5$. The solution is therefore $x \\leqslant 2$.',
     'Alternatively, the solution to $2x + 1 > 5$ will be $x > 2$ where the line $y = 5$ would be drawn as a dashed line.'],
 ex=[dict(n='Year 8 Example 10',t='Solving inequalities using graphs',q='Solve the following inequalities using the given graphs.',parts=['$3x - 1 \\leqslant 2$'+plane(-4,4,-4,4,[('m',3,-1,('y = 3x − 1',-3.8,-3.6))],w=36),'$-x + 1 > 3$'+plane(-4,4,-4,4,[('m',-1,1,('y = −x + 1',1.2,-3.6))],w=36)],
          yq='Solve the following inequalities using the given graphs.',yparts=['$2x - 3 \\geqslant 1$'+plane(-4,4,-4,4,[('m',2,-3,('y = 2x − 3',0.3,-3.6))],w=36),'$-x - 2 < 2$'+plane(-4,4,-4,4,[('m',-1,-2,('y = −x − 2',0.5,-3.6))],w=36)],h=[6,6])],
 practice=[P('Solve the following inequalities using the given graphs.<br>$2x + 1 \\leqslant 5$'+plane(-6,6,-6,6,[('m',2,1,('y = 2x + 1',2.6,-5))],w=36),6,f'{C8}, Exercise 9E Q6a (p. 675); adapted: one part only'),
           P('Solve the following inequalities using the given graphs.<br>$x + 2 \\leqslant 3$'+plane(-6,6,-6,6,[('m',1,2,('y = x + 2',1.5,-5))],w=36),6,f'{C8}, Exercise 9E Q6b (p. 675); adapted: one part only'),
           P('Solve the following inequalities using the given graphs.<br>$-x + 2 \\geqslant 1$'+plane(-6,6,-6,6,[('m',-1,2,('y = −x + 2',2.2,-5))],w=36),6,f'{C8}, Exercise 9E Q7a (p. 676); adapted: one part only')],
 sc=['I can use graphs to solve a linear inequality.']),
}
if __name__=='__main__':main(W,sys.argv[1:])
