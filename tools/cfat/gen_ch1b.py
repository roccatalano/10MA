"""Write CFAT blocks 1E-1L (verbatim questions, cited). Run once; edit the JSON afterwards."""
import json,sys,os
sys.path.insert(0,'../slides')
from svgs import plane as PL
from ch1_data import region,L
C9='Cambridge Essential Mathematics 9 (3rd Ed)';OX='Oxford Maths 10 VC (2022)';JA='Jacaranda Maths Quest 10 + 10A (2022)'
AD='; adapted: stem reworded for a single part'
def mc(lv,q,o,a,sol,src,vc): return dict(level=lv,type='mc',marks=1,q=q,options=o,answer=a,sol=sol,src=src,vc2=vc)
def sa(lv,q,sol,src,vc,m=None): return dict(level=lv,type='sa',marks=m or (2 if lv=='L3' else 1),q=q,sol=sol,src=src,vc2=vc)
P=lambda *a,**k:PL(*a,w=k.pop('w',150),**k)
B={}
B['C10-1E']=[
("I can determine if a point is on a straight line.",[
 mc('L1','The point that is not on the straight line $y = -2x + 3$ is:',['$(1, 1)$','$(0, 3)$','$(2, 0)$','$(-2, 7)$','$(3, -3)$'],'C',['$x = 2$: $y = -4 + 3 = -1 \\neq 0$','(C)'],C9+', Ch 4 review, multiple-choice Q4 (p. 324)','VC2M9A06'),
 sa('L2','Determine if the point $(2, 5)$ is the intersection point of the graphs of $y = 4x - 3$ and $y = -2x + 6$.',['$4(2) - 3 = 5$ ✓','$-2(2) + 6 = 2 \\neq 5$','No, $(2, 5)$ is not on both lines.'],C9+', Ch 4 review, short answer Q13a (p. 322)'+AD,'VC2M10A06'),
 sa('L3','Determine if the point $(2, 5)$ is the intersection point of the graphs of $3x - 2y = -4$ and $2x + y = 9$.',['$3(2) - 2(5) = -4$ ✓','$2(2) + 5 = 9$ ✓','Yes, $(2, 5)$ is the intersection point.'],C9+', Ch 4 review, short answer Q13b (p. 322)'+AD,'VC2M10A06')]),
("I can find the gradient and $y$-intercept from a straight line equation.",[
 mc('L1','The linear graph that <i>does not</i> have a gradient of $3$ is:',['$y = 3x + 7$','$\\dfrac{y}{3} = x + 2$','$2y - 6x = 1$','$y - 3x = 4$','$3x + y = -1$'],'E',['$3x + y = -1 \\Rightarrow y = -3x - 1$, $m = -3$','(E)'],C9+', Ch 4 review, multiple-choice Q5 (p. 324)','VC2M9A06'),
 mc('L2','The gradient of the line $12x + 4y = 8$ is:',['$3$','$-3$','$12$','$-12$','$4$'],'B',['$4y = -12x + 8$, $y = -3x + 2$','$m = -3$ (B)'],OX+', Ch 4 review, multiple-choice Q6 (p. 207)','VC2M10A06'),
 sa('L3','State the value of the gradient and the $y$-intercept of $2y - 3x - 8 = 0$.',['$2y = 3x + 8$','$y = \\dfrac{3}{2}x + 4$','$m = \\dfrac{3}{2}$, $y$-intercept $(0, 4)$'],C9+', Ch 4 review, short answer Q7d (p. 321)'+AD,'VC2M10A06')]),
("I can use the gradient and $y$-intercept to sketch a graph.",[
 sa('L1','Sketch $y = 2x + 3$ using the gradient–intercept method.',['$m = 2$, $y$-intercept $(0, 3)$',P(-3,2,-1,6,[L(2,3),('pt',(0,3),'(0, 3)',8,0),('pt',(1,5),'(1, 5)',8,0)])],C9+', Ch 4 review, short answer Q7a (p. 321)'+AD,'VC2M9A06',2),
 sa('L2','Sketch $x - 2y = 4$ using the gradient–intercept method.',['$y = \\dfrac{1}{2}x - 2$: $m = \\dfrac{1}{2}$, $(0, -2)$',P(-2,6,-4,2,[L(.5,-2),('pt',(0,-2),'(0, −2)',8,10),('pt',(4,0),'(4, 0)',4,-6)])],OX+', Ch 4 review, short answer Q7b (p. 208)'+AD,'VC2M10A06',2),
 sa('L3','Sketch $5y - 10 = 15x$ using the gradient–intercept method.',['$5y = 15x + 10$, $y = 3x + 2$','$m = 3$, $(0, 2)$',P(-2,2,-3,6,[L(3,2),('pt',(0,2),'(0, 2)',-8,-4),('pt',(1,5),'(1, 5)',8,0)])],OX+', Ch 4 review, short answer Q7c (p. 208)'+AD,'VC2M10A06')]),
("I can find the $x$- and $y$-intercepts of a linear graph.",[
 mc('L1','The $x$- and $y$-intercepts of the graph of $2x + 4y = 12$ are respectively at:',['$(4, 0), (0, 2)$','$(3, 0), (0, 2)$','$(6, 0), (0, 3)$','$(2, 0), (0, 12)$','$(8, 0), (0, 6)$'],'C',['$y = 0$: $x = 6$; $x = 0$: $y = 3$','(C)'],C9+', Ch 4 review, multiple-choice Q1 (p. 323)','VC2M9A06'),
 sa('L2','Find the $x$- and $y$-intercepts of $2x - 4y - 12 = 0$ and sketch the graph.',['$x = 0$: $-4y = 12$, $y = -3$','$y = 0$: $2x = 12$, $x = 6$',P(-2,8,-5,2,[L(.5,-3),('pt',(0,-3),'−3',8,6),('pt',(6,0),'6',4,14)])],OX+', Ch 4 review, short answer Q8a (p. 208)'+AD,'VC2M10A06',2),
 sa('L3','Find the $x$- and $y$-intercepts of $7x + 3y + 21 = 0$ and sketch the graph.',['$x = 0$: $3y = -21$, $y = -7$','$y = 0$: $7x = -21$, $x = -3$',P(-5,2,-9,2,[L(-7/3,-7),('pt',(0,-7),'−7',8,6),('pt',(-3,0),'−3',-6,-6)])],OX+', Ch 4 review, short answer Q8c (p. 208)'+AD,'VC2M10A06')]),
("I can sketch a horizontal or vertical line.",[
 sa('L1','Sketch $y = 3$.',[P(-3,3,-2,5,[('line',(0,3),(1,3)),('lab',(.2,3.4),'3','start')])],C9+', Ch 4 review, short answer Q4a (p. 321)'+AD,'VC2M9A06'),
 sa('L2','Sketch $x = -4$.',[P(-6,2,-3,3,[('line',(-4,0),(-4,1)),('lab',(-3.9,-.5),'−4','start')])],C9+', Ch 4 review, short answer Q4c (p. 321)'+AD,'VC2M9A06'),
 sa('L3','Sketch $y = -2$ and $x = 5$ on the same set of axes.',[P(-3,7,-4,3,[('line',(0,-2),(1,-2)),('line',(5,0),(5,1)),('lab',(1,-1.6),'y = −2'),('lab',(5.2,2),'x = 5','start')])],C9+', Ch 4 review, short answer Q4b, Q4d (p. 321); adapted: two parts on one set of axes','VC2M9A06')]),
("I can sketch a line of the form $y = mx$.",[
 sa('L1','Sketch $y = 3x$.',['passes through $(0, 0)$ and $(1, 3)$',P(-2,2,-3,4,[L(3,0),('pt',(1,3),'(1, 3)',8,4)])],C9+', Ch 4 review, short answer Q4e (p. 321)'+AD,'VC2M9A06'),
 sa('L2','Sketch $y = -2x$.',['passes through $(0, 0)$ and $(1, -2)$',P(-2,2,-3,3,[L(-2,0),('pt',(1,-2),'(1, −2)',8,4)])],C9+', Ch 4 review, short answer Q4f (p. 321)'+AD,'VC2M9A06'),
 sa('L3','Sketch $y = 3x$ and $y = -2x$ on the same set of axes, labelling one point other than the origin on each.',['$(1, 3)$ and $(1, -2)$',P(-2,2,-3,4,[L(3,0),L(-2,0),('pt',(1,3),'(1, 3)',8,4),('pt',(1,-2),'(1, −2)',8,4)])],C9+', Ch 4 review, short answer Q4e, Q4f (p. 321); adapted: two parts on one set of axes','VC2M9A06')])]
B['C10-1F']=[
("I can find the gradient of a line joining two points.",[
 mc('L1','The gradient of the line joining the points $(1, -2)$ and $(5, 6)$ is:',['$2$','$1$','$3$','$-1$','$\\dfrac{1}{3}$'],'A',['$m = \\dfrac{6 - (-2)}{5 - 1} = \\dfrac{8}{4} = 2$ (A)'],C9+', Ch 4 review, multiple-choice Q3 (p. 323)','VC2M9A06'),
 mc('L2','The gradient of the line passing through the points $(1, 8)$ and $(-3, -6)$ is:',['$1$','$-1$','$\\dfrac{2}{7}$','$\\dfrac{7}{2}$','$-\\dfrac{7}{2}$'],'D',['$m = \\dfrac{-6 - 8}{-3 - 1} = \\dfrac{-14}{-4} = \\dfrac{7}{2}$ (D)'],OX+', Ch 4 review, multiple-choice Q8 (p. 207)','VC2M10A06'),
 sa('L3','Find the missing coordinate, $n$, if the line joining $(-1, 3)$ and $(2, n)$ has gradient $2$.',['$\\dfrac{n - 3}{2 - (-1)} = 2$','$n - 3 = 6$','$n = 9$'],C9+', Ch 4 review, short answer Q11a (p. 322)'+AD,'VC2M10A06')]),
("I can find the equation of a line using a point and the $y$-intercept.",[
 sa('L1','Give the equation of the straight line that has gradient $3$ and passes through the point $(0, 2)$.',['$m = 3$, $c = 2$','$y = 3x + 2$'],C9+', Ch 4 review, short answer Q8a (p. 321)'+AD,'VC2M9A06'),
 mc('L2','A straight line has a gradient of $-2$ and passes through the point $(0, 5)$. Its equation is:',['$2y = -2x + 10$','$y = -2x + 5$','$y = 5x - 2$','$y - 2x = 5$','$y = -2(x - 5)$'],'B',['$m = -2$, $c = 5$','$y = -2x + 5$ (B)'],C9+', Ch 4 review, multiple-choice Q6 (p. 324)','VC2M9A06'),
 mc('L3','The equation for the linear graph with a gradient of $\\dfrac{3}{4}$ and a $y$-intercept of $\\dfrac{5}{8}$ is:',['$8x - 6y + 5 = 0$','$8y = 6x - 5$','$6x - 8y + 5 = 0$','$6y = 8x + 5$','$6x - 5y + 8 = 0$'],'C',['$y = \\dfrac{3}{4}x + \\dfrac{5}{8}$, $\\times 8$: $8y = 6x + 5$','$6x - 8y + 5 = 0$ (C)'],OX+', Ch 4 review, multiple-choice Q7 (p. 207)','VC2M10A06')]),
("I can find the equation of a line given two points.",[
 sa('L1','Give the equation of the straight line that has gradient $\\dfrac{4}{3}$ and passes through the point $(6, 3)$.',['$3 = \\dfrac{4}{3}(6) + c$','$3 = 8 + c$, $c = -5$','$y = \\dfrac{4}{3}x - 5$'],C9+', Ch 4 review, short answer Q8c (p. 321)'+AD,'VC2M9A06'),
 sa('L2','Find the equation of the line that passes through the points $(1, 3)$ and $(2, 4)$. Write your answer in the form $y = mx + c$.',['$m = \\dfrac{4 - 3}{2 - 1} = 1$','$3 = 1 + c$, $c = 2$','$y = x + 2$'],OX+', Ch 4 review, short answer Q11a (p. 208)'+AD,'VC2M10A06'),
 sa('L3','Find the equation of the line that passes through the points $(-1, 5)$ and $(3, -7)$. Write your answer in the form $y = mx + c$.',['$m = \\dfrac{-7 - 5}{3 - (-1)} = -3$','$5 = -3(-1) + c$, $c = 2$','$y = -3x + 2$'],OX+', Ch 4 review, short answer Q11b (p. 208)'+AD,'VC2M10A06')])]
B['C10-1G']=[
("I can find the distance between two points.",[
 mc('L1','The length of the line segment joining the points $A(1, 2)$ and $B(4, 6)$ is:',['$5$','$\\dfrac{4}{3}$','$7$','$\\sqrt{5}$','$\\sqrt{2}$'],'A',['$d = \\sqrt{3^2 + 4^2} = 5$ (A)'],C9+', Ch 4 review, multiple-choice Q8 (p. 324)','VC2M10A06'),
 sa('L2','For the line segment joining $(2, 4)$ and $(6, 8)$, find the length (to two decimal places where applicable).',['$d = \\sqrt{(6 - 2)^2 + (8 - 4)^2}$','$= \\sqrt{32} \\approx 5.66$'],C9+', Ch 4 review, short answer Q10a ii (p. 322)'+AD,'VC2M10A06'),
 sa('L3','For the line segment joining $(-5, 7)$ and $(-1, -2)$, find the length (to two decimal places where applicable).',['$d = \\sqrt{(-1 - (-5))^2 + (-2 - 7)^2}$','$= \\sqrt{16 + 81} = \\sqrt{97} \\approx 9.85$'],C9+', Ch 4 review, short answer Q10d ii (p. 322)'+AD,'VC2M10A06')]),
("I can find the midpoint of a line segment joining two points.",[
 sa('L1','For the line segment joining $(2, 4)$ and $(6, 8)$, find the midpoint.',['$M = \\left(\\dfrac{2 + 6}{2}, \\dfrac{4 + 8}{2}\\right)$','$= (4, 6)$'],C9+', Ch 4 review, short answer Q10a i (p. 322)'+AD,'VC2M10A06'),
 sa('L2','For the line segment joining $(-2, 1)$ and $(2, 7)$, find the midpoint.',['$M = \\left(\\dfrac{-2 + 2}{2}, \\dfrac{1 + 7}{2}\\right)$','$= (0, 4)$'],C9+', Ch 4 review, short answer Q10c i (p. 322)'+AD,'VC2M10A06'),
 sa('L3','Find the missing coordinate, $n$, if the midpoint of the line segment joining $(n, 1)$ and $(1, -3)$ is $(3.5, -1)$.',['$\\dfrac{n + 1}{2} = 3.5$','$n + 1 = 7$','$n = 6$'],C9+', Ch 4 review, short answer Q11c (p. 322)'+AD,'VC2M10A06')]),
("I can use a given distance to find coordinates.",[
 sa('L1','Find the missing coordinate, $n$, if the line segment joining $(-2, 2)$ and $(4, n)$ has length $10$, $n > 0$.',['$10^2 = 6^2 + (n - 2)^2$','$(n - 2)^2 = 64$, $n - 2 = \\pm 8$','$n = 10$ (as $n > 0$)'],C9+', Ch 4 review, short answer Q11b (p. 322)'+AD,'VC2M10A06',2),
 sa('L2','The following three points are plotted on a Cartesian plane: $A(-2, 3)$, $B(1, 12)$ and $C(7, 10)$. Show that line segments drawn between these points form a right-angled triangle with the points $A$, $B$ and $C$ as vertices.',['$AB^2 = 3^2 + 9^2 = 90$, $BC^2 = 6^2 + 2^2 = 40$','$AC^2 = 9^2 + 7^2 = 130$','$90 + 40 = 130$, so right-angled at $B$'],OX+', Exercise 4E Q20a (p. 196)','VC2M10A06',2),
 sa('L3','Prove that quadrilateral $KLMN$, with vertices at $K(0, 0)$, $L(2, 4)$, $M(6, 2)$ and $N(4, -2)$, is a square. Then find its perimeter correct to one decimal place.',['$KL = LM = MN = NK = \\sqrt{20}$','diagonals $KM = LN = \\sqrt{40}$, so a square','perimeter $= 4\\sqrt{20} \\approx 17.9$'],OX+', Exercise 4E Q22 (p. 196)','VC2M10A06')])]
B['C10-1H']=[
("I can decide if lines are parallel, perpendicular or neither.",[
 mc('L1','The gradient of a line perpendicular to $y = 4x - 7$ would be:',['$\\dfrac{1}{4}$','$4$','$-4$','$-\\dfrac{1}{4}$','$-7$'],'D',['$m_2 = -\\dfrac{1}{4}$ (D)'],C9+', Ch 4 review, multiple-choice Q9 (p. 324)','VC2M10A06'),
 mc('L2','A line parallel to the line $3x + 2y = 6$ would have a gradient of:',['$\\dfrac{2}{3}$','$-3$','$-\\dfrac{3}{2}$','$\\dfrac{3}{2}$','$-\\dfrac{2}{3}$'],'C',['$y = -\\dfrac{3}{2}x + 3$; parallel: same gradient (C)'],OX+', Ch 4 review, multiple-choice Q10 (p. 207)','VC2M10A06'),
 sa('L3','Four points are plotted on a Cartesian plane: $A(-2, 1)$, $B(5, 4)$, $C(-6, -4)$ and $D(8, 2)$. Is line segment $AB$ parallel to line segment $CD$?',['$m_{AB} = \\dfrac{4 - 1}{5 - (-2)} = \\dfrac{3}{7}$','$m_{CD} = \\dfrac{2 - (-4)}{8 - (-6)} = \\dfrac{6}{14} = \\dfrac{3}{7}$','Yes, equal gradients so $AB \\parallel CD$'],OX+', Exercise 4E Q19a (p. 196)'+AD,'VC2M10A06')]),
("I can find the equation of a parallel line.",[
 sa('L1','Determine the linear equation that is parallel to the line $y = 2x - 1$ and passes through the point $(0, 4)$.',['$m = 2$, $c = 4$','$y = 2x + 4$'],C9+', Ch 4 review, short answer Q12a (p. 322)'+AD,'VC2M10A06'),
 sa('L2','Write an equation for a line that is parallel to the graph of $y = -4x + 5$; with $y$-intercept of $-3$.',['$m = -4$, $c = -3$','$y = -4x - 3$'],OX+', Ch 4 review, short answer Q12a (p. 208)'+AD,'VC2M10A06'),
 sa('L3','Write an equation for a line that is parallel to the graph of $y = 3x + 2$ and passes through $(-3, -2)$.',['$m = 3$','$-2 = 3(-3) + c$, $c = 7$','$y = 3x + 7$'],OX+', Ch 4 review, short answer Q13b (p. 208)'+AD,'VC2M10A06')]),
("I can find the equation of a perpendicular line.",[
 sa('L1','Determine the linear equation that is perpendicular to the line $y = 2x + 3$ and passes through the point $(0, -1)$.',['$m = -\\dfrac{1}{2}$, $c = -1$','$y = -\\dfrac{1}{2}x - 1$'],C9+', Ch 4 review, short answer Q12c (p. 322)'+AD,'VC2M10A06'),
 sa('L2','Write an equation for a line that is perpendicular to the graph of $y = 2x - 7$; with $y$-intercept of $-4$.',['$m = -\\dfrac{1}{2}$, $c = -4$','$y = -\\dfrac{1}{2}x - 4$'],OX+', Ch 4 review, short answer Q12b (p. 208)'+AD,'VC2M10A06'),
 sa('L3','Write an equation for a line that is perpendicular to the graph of $y = 3x + 2$ and passes through $(3, 2)$.',['$m = -\\dfrac{1}{3}$','$2 = -\\dfrac{1}{3}(3) + c$, $c = 3$','$y = -\\dfrac{1}{3}x + 3$'],OX+', Ch 4 review, short answer Q13a (p. 208)'+AD,'VC2M10A06')])]
B['C10-1I']=[
("I can solve simultaneous equations using substitution.",[
 mc('L1','The pair of linear equations $y = x + 3$ and $y = -2x + 6$ intersect at which of these points?',['$(-3, 0)$','$(3, 6)$','$(1, 8)$','$(1, 4)$','$(0, 6)$'],'D',['$x + 3 = -2x + 6$, $x = 1$, $y = 4$ (D)'],OX+', Ch 4 review, multiple-choice Q12 (p. 207)','VC2M10A04'),
 sa('L2','Use the substitution method to solve $3x + 4y = -1$ and $y = x - 2$.',['$3x + 4(x - 2) = -1$','$7x - 8 = -1$, $x = 1$','$y = 1 - 2 = -1$','$x = 1$, $y = -1$'],OX+', Ch 4 review, short answer Q15a (p. 208)'+AD,'VC2M10A04',2),
 sa('L3','Use the substitution method to solve $7x - y = 4$ and $y = 4x + 2$.',['$7x - (4x + 2) = 4$','$3x - 2 = 4$, $x = 2$','$y = 4(2) + 2 = 10$','$x = 2$, $y = 10$'],OX+', Ch 4 review, short answer Q15c (p. 208)'+AD,'VC2M10A04')])]
B['C10-1J']=[
("I can solve simultaneous equations by adding or subtracting them.",[
 sa('L1','Solve $x + y = 15$ and $x - y = 7$ using the elimination method.',['add: $2x = 22$, $x = 11$','$11 + y = 15$, $y = 4$'],C9+', Ch 2 review, short answer Q14d (p. 165)'+AD,'VC2M10A04'),
 mc('L2','Consider the two equations: $2x - y + 3 = 0$ ① and $4x - y + 5 = 0$ ②. If equation ② is subtracted from equation ①, the resulting equation will be:',['$-2x - 2 = 0$','$-2x - 8 = 0$','$2x + 2 = 0$','$2x + 8 = 0$','$2x - 2 = 0$'],'A',['① − ②: $-2x - 2 = 0$ (A)'],OX+', Ch 4 review, multiple-choice Q15 (p. 207)','VC2M10A04'),
 sa('L3','Use the elimination method to solve $x + 5y = 13$ and $x + 2y = 4$.',['subtract: $3y = 9$, $y = 3$','$x + 6 = 4$, $x = -2$','$x = -2$, $y = 3$'],OX+', Ch 4 review, short answer Q16b (p. 208)'+AD,'VC2M10A04')]),
("I can use the elimination method to solve simultaneous equations.",[
 sa('L1','Solve $3x + 2y = -19$ and $4x - y = -7$ using the elimination method.',['$\\times 2$: $8x - 2y = -14$','add: $11x = -33$, $x = -3$','$4(-3) - y = -7$, $y = -5$'],C9+', Ch 2 review, short answer Q14e (p. 165)'+AD,'VC2M10A04',2),
 sa('L2','Use the elimination method to solve $2x - y = 7$ and $3x + 5y = 4$.',['$\\times 5$: $10x - 5y = 35$','add: $13x = 39$, $x = 3$','$6 - y = 7$, $y = -1$'],OX+', Ch 4 review, short answer Q16c (p. 208)'+AD,'VC2M10A04',2),
 sa('L3','Solve $3x - 5y = 7$ and $5x + 2y = 22$ using the elimination method.',['$\\times 2$: $6x - 10y = 14$; $\\times 5$: $25x + 10y = 110$','add: $31x = 124$, $x = 4$','$12 - 5y = 7$, $y = 1$'],C9+', Ch 2 review, short answer Q14f (p. 165)'+AD,'VC2M10A04')])]
B['C10-1K']=[
("I can set up and solve simultaneous equations.",[
 sa('L1','The sum of the ages of Billy and his sister is 32. If Billy is 8 years older than his sister, what are their ages?',['$b + s = 32$, $b - s = 8$','$2b = 40$, $b = 20$, $s = 12$','Billy is 20, his sister is 12.'],C9+', Ch 2 review, short answer Q15 (p. 165)','VC2M10A04',2),
 sa('L2','The perimeter around the top of a rectangular billiard table is 810 cm. The length is twice the width. Use $l$ and $w$ to write two linear equations, then solve them to find the dimensions of the top of the billiard table.',['$2l + 2w = 810$, $l = 2w$','$6w = 810$, $w = 135$','$l = 270$ cm, $w = 135$ cm'],OX+', Exercise 4F Q14a–c (p. 204); adapted: three parts combined','VC2M10A04',2),
 sa('L3','Sophie has decided to make hand-painted cards. She invests \\$60 in a set of paintbrushes and enough paint to make 40 cards. The cost of each plain white card is \\$2 and she plans to sell the painted cards for \\$6 each. The cost is $a = 2n + 60$ and the money received is $a = 6n$. What are the coordinates of the point of intersection of the two graphs? What does this tell you?',['$6n = 2n + 60$, $4n = 60$, $n = 15$','$a = 90$: $(15, 90)$','Selling 15 cards recovers the \\$90 spent (break even).'],OX+', Exercise 4F Q13d (p. 204); adapted: parts a, b given in the stem','VC2M10A04')])]
B['C10-1L']=[
("I can sketch a region on the Cartesian plane.",[
 sa('L1','Sketch the inequality $y > 2$ on a Cartesian plane.',['broken line $y = 2$, shade above',P(-3,3,-2,5,[region(-3,3,-2,5,[(0,-1,-2)]),('line',(0,2),(1,2),None,True),('lab',(.2,2.4),'2','start')])],OX+', Exercise 4C Q24a iii (p. 179)'+AD,'VC2M10A08'),
 sa('L2','Sketch the inequality $y < 2x + 5$ on a Cartesian plane.',['broken line through $(0, 5)$ and $(-2.5, 0)$','test $(0, 0)$: $0 < 5$ true',P(-4,3,-3,7,[region(-4,3,-3,7,[(-2,1,5)]),('line',(0,5),(-2.5,0),None,True),('pt',(0,5),'5',8,4),('pt',(-2.5,0),'−2.5',-6,-6)])],OX+', Exercise 4C Q24b iii (p. 179)'+AD,'VC2M10A08',2),
 sa('L3','Sketch the inequality $2x + 3y > 18$ on a Cartesian plane.',['broken line through $(0, 6)$ and $(9, 0)$','test $(0, 0)$: $0 > 18$ false, shade the other side',P(-2,11,-2,9,[region(-2,11,-2,9,[(-2,-3,-18)]),('line',(0,6),(9,0),None,True),('pt',(0,6),'6',-10,-4),('pt',(9,0),'9',4,14)])],OX+', Exercise 4C Q24b v (p. 179)'+AD,'VC2M10A08')]),
("I can find the intersecting region of two inequalities.",[
 sa('L1','Sketch the following pair of inequalities: $y < 4$ and $y \\leqslant -x$.',['$y = 4$ broken; $y = -x$ solid; meet at $(-4, 4)$',P(-6,4,-4,6,[region(-6,4,-4,6,[(0,1,4),(1,1,0)]),('line',(0,4),(1,4),None,True),('line',(0,0),(1,-1)),('pt',(-4,4),'(−4, 4)',6,-6)])],JA+', Exercise 4.9 Q3a (p. 275)'+AD,'VC2M10A08',2),
 sa('L2','Sketch the following pair of inequalities: $3x + 4y < 24$ and $y > 2x - 5$.',['$3x + 4y = 24$: $(0, 6)$, $(8, 0)$, broken','$y = 2x - 5$: $(0, -5)$, $(2.5, 0)$, broken','intersection: $3x + 8x - 20 = 24$, $(4, 3)$',P(-2,9,-6,8,[region(-2,9,-6,8,[(3,4,24),(2,-1,5)]),('line',(0,6),(8,0),None,True),('line',(0,-5),(2.5,0),None,True),('pt',(4,3),'(4, 3)',8,4)])],JA+', Exercise 4.9 Q5a (p. 275)'+AD,'VC2M10A08',2),
 sa('L3','Graph the following system of inequalities: $y \\geqslant -3$, $x + 2 \\geqslant 0$, $2y + 5x \\leqslant 7$. Calculate the coordinates of the vertices of the required region.',['vertices: $(-2, -3)$, $(2.6, -3)$, $(-2, 8.5)$',P(-4,5,-5,10,[region(-4,5,-5,10,[(0,-1,3),(-1,0,2),(5,2,7)]),('line',(0,-3),(1,-3)),('line',(-2,0),(-2,1)),('line',(0,3.5),(1.4,0)),('pt',(-2,-3),'(−2, −3)',-6,14),('pt',(2.6,-3),'(2.6, −3)',6,14),('pt',(-2,8.5),'(−2, 8.5)',8,0)])],JA+', Exercise 4.9 Q8a, b (p. 276)','VC2M10A08',3)])]
for card,sk in B.items():
    json.dump({'card':card,'levels':{'L1':'Level 9 (review)','L2':'Level 10','L3':'Level 10 extension / 10A'},
      'skills':[{'n':i+1,'skill':s,'items':its} for i,(s,its) in enumerate(sk)]},open(card+'.json','w'),ensure_ascii=False,indent=1)
print(len(B),'blocks')
