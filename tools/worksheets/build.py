import json,subprocess,re,glob,sys
sys.path.insert(0,'.');import svg
c=json.load(open('/home/claude/apk/crops.json'))
# verbatim e.g. questions (checked against the crops / book pages); D = diagram, H = answer-space height
Q={
'1A_C7_11':('Simplify $4a \\times 2b \\times 3c$, giving your final answer without multiplication signs.',None,22),
'1A_C8_6':('Simplify $5ac + 3b - 2ca + 4b - 5b$.',None,22),
'1A_C8_15':('Factorise $12a + 18ab$.',None,18),
'1A_C9_2':('Evaluate $a^2 + 3(ab - c)$ if $a = -2$, $b = 3$ and $c = -8$.',None,24),
'1B_C7_8':('Solve $7 + 4a = 23$ algebraically.',None,24),
'1B_C8_6':('Solve $6x + 4 = 22 - 3x$ algebraically.',None,26),
'1B_C9_10':('Solve $2(4x + 3) = 7$.',None,26),
'1C_C7_2':('Insert the symbol $<$ (less than) or $>$ (greater than) into the statement $-1 \;\\boxed{\\phantom{<}}\; -6$ to make it true.',None,10),
'1C_C8_15':('Solve $15 - 2x > 1$ algebraically.',None,24),
'1C_C9_14':('Show $x$ is less than or equal to 3 $(x \\leqslant 3)$ on a number line.',None,22),
'1D_C7_11':('Find the value of $\\dfrac{3}{4} + \\dfrac{5}{6}$.',None,24),
'1D_C8_10':('Simplify $\\dfrac{4a}{3} + \\dfrac{2a}{5}$ and $\\dfrac{a}{6} - \\dfrac{b}{9}$.',None,28),
'1D_C9_9':('Solve $\\dfrac{4x - 2}{3} = 6$.',None,26),
'1E_C7_22':('For the rule $\\textit{output}(y) = \\textit{input}(x) + 1$, construct a table of values using $\\textit{input}$ values of $0, 1, 2$ and $3$. Use the table of coordinates to plot a graph.',None,55),
'1E_C8_12':('Find the $x$-intercept and $y$-intercept for the graph of $y = -2x + 1$.',None,28),
'1E_C9_10':('Rearrange $2x + 3y = 8$ to the form $y = mx + c$.',None,22),
'1F_C8_15':('Find the gradient of this line.','f1F',8),
'1F_C9_8':('Find the gradient of the line joining the points $(-1, 3)$ and $(4, 9)$.',None,22),
'1F_C9_14':('Find the equation of the line which has a gradient of $2$ and passes through the point $(-2, 5)$.',None,26),
'1G_C7_13':('Draw a set of axes from $-4$ to $4$ on both axes, and plot the points $(-3, 2)$ and $(-2, -4)$.',None,55),
'1G_C8_24':('Decide if $6, 8, 10$ is a Pythagorean triple.',None,20),
'1G_C9_2':('Find the value of the pronumeral correct to one decimal place.','f1G',14),
'1H_C7_10':('State whether the two lines cut by this transversal are parallel.','f1H_t',10),
'1H_C9_7':('For the graphs shown, state whether the gradient is positive, negative, zero or undefined and find the gradient.','f1H_g',14),
'1H_C9_10':('Rearrange $2x + 3y = 8$ to the form $y = mx + c$.',None,22),
'1I_C8_4':('Decide if the $(1, 3)$ and $(-2, -4)$ lie on the graph of $y = 3x$.',None,24),
'1I_C9_20':('Determine if the point $(2, -1)$ is at the intersection of the lines with equations $y = -2x + 3$ and $2x - 3y = 7$.',None,28),
'1I_C9_11':('Solve $6x + 5 = 3x - 13$.',None,24),
'1J_C7_5':('State the result of adding $4$ to both sides of the equation $7q - 4 = 10$.',None,16),
'1J_C8_6':('Simplify $5ac + 3b - 2ca + 4b - 5b$.',None,20),
'1J_C9_19':('Solve the following pair of simultaneous equations using substitution:<br><span style="display:inline-block;margin:1.5mm 0 0 6mm">$\\begin{aligned} x + 2y &= 4 \\\\ y &= 2x - 3 \\end{aligned}$</span>',None,30),
'1K_C7_3':('Write an equation for “the sum of $x$ and $5$ is $22$.”',None,14),
'1K_C8_11':('The weight of $6$ identical books is $1.2\\text{ kg}$. Set up and solve an equation to find the weight of one book.',None,26),
'1K_C9_13':('Ava and Elise have $27$ soft toys between them. Ava has $5$ more than Elise. Use an equation to find how many soft toys they each have.',None,30),
'1L_C8_10':('Sketch the region $y < 4$.',None,48),
'1L_C9_14':('Show $x$ is less than or equal to 3 $(x \\leqslant 3)$ on a number line.',None,22),
'1L_C9_4':('Sketch the graphs of $y = -2x + 4$ and $3x - 4y = 12$ showing $x$- and $y$-intercepts.',None,60),
}
keys=[k[:-4] for k in c];assert set(keys)==set(Q),set(keys)^set(Q)
R=json.loads(subprocess.run(['node','kt.js'],input=json.dumps([Q[k][0] for k in keys]),capture_output=True,text=True,check=True).stdout)
HTML=dict(zip(keys,R))
A4='''<style>@media screen{html{background:#8a8a8a}body{width:210mm;min-height:297mm;margin:8mm auto;padding:11mm 12mm 12mm;background:#fff;box-shadow:0 2px 14px rgba(0,0,0,.45)}}</style>'''
pp={'C7':{298:278,665:645,418:398,244:224,156:136,522:502},'C8':{420:400,559:539,746:726,747:727,348:328,745:725},'C9':{181:162,182:163,339:320,338:319,257:238}}
src="/mnt/user-data/uploads/Lesson Handouts/HTML/"
for f in sorted(glob.glob(src+'*.html')):
  sub=f.split('/')[-1][:2];s=open(f).read()
  i=s.index('<div class="box "><div class="hd">Activating prior knowledge');j=s.index('<div class="pair">',i)
  mine=[k for k in keys if c[k+'.png']['card']==sub];q=''
  for n,k in enumerate(mine,1):
    t,d,h=Q[k];fig=getattr(svg,d)() if d else ''
    q+=f'<div class="apq"><b>{n}.</b><div><p class="q">{HTML[k]}</p>{fig}<div style="min-height:{h}mm"></div></div></div>'
  cites='; '.join(f'Year {c[k+".png"]["book"][1]} Ch{"9" if c[k+".png"]["sub"].endswith("None") else c[k+".png"]["sub"].split("-")[1][:-1]} checklist item {c[k+".png"]["n"]} (p. {pp[c[k+".png"]["book"]][c[k+".png"]["page"]]})' for k in mine)
  box=f'<div class="box "><div class="hd">Activating prior knowledge<span></span></div><div class="bd">{q}<p class="src">Cambridge Essential Mathematics for the Victorian Curriculum 3rd Ed: {cites}</p></div></div>'
  t=s[:i]+box+s[j:];t=t.replace('</head>',A4+'</head>',1)
  open(f'/home/claude/apk2/C10-{sub} worksheet.html','w').write(t)
print('built',len(glob.glob('C10-*.html')))
