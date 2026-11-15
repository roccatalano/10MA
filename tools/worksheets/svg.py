# house-style diagrams (match existing worksheet .figc SVGs)
def grid(x0,x1,y0,y1,u=10):
  W=(x1-x0)*u;H=(y1-y0)*u;o=[]
  for i in range(x0,x1+1):X=(i-x0)*u;o.append(f'<line x1="{X}" y1="0" x2="{X}" y2="{H}" stroke="#bbb" stroke-width="0.3"/>')
  for j in range(y0,y1+1):Y=(y1-j)*u;o.append(f'<line x1="0" y1="{Y}" x2="{W}" y2="{Y}" stroke="#bbb" stroke-width="0.3"/>')
  return ''.join(o),W,H
def axes(ox,oy,W,H,pad=4):
  return (f'<line x1="{-pad+1}" y1="{oy}" x2="{W+pad-1}" y2="{oy}" stroke="#000" stroke-width="0.5"/><line x1="{ox}" y1="{H+pad-1}" x2="{ox}" y2="{-pad+1}" stroke="#000" stroke-width="0.5"/>'
   f'<path d="M{W+pad} {oy} l-3 -1.4 v2.8z M{ox} {-pad} l-1.4 3 h2.8z M{-pad} {oy} l3 -1.4 v2.8z M{ox} {H+pad} l-1.4 -3 h2.8z"/>'
   f'<text x="{W+pad-1}" y="{oy-2.5}" font-size="5.5" font-style="italic" font-family="Times New Roman">x</text><text x="{ox+2}" y="{-pad+2}" font-size="5.5" font-style="italic" font-family="Times New Roman">y</text>'
   f'<text x="{ox-2.5}" y="{oy+5.5}" font-size="5" font-style="italic" font-family="Times New Roman" text-anchor="end">O</text>')
def wrap(inner,vb,w):
  return f'<svg class="figc" width="{w}mm" viewBox="{vb}" font-family="Arial" style="display:block;margin:1mm 0 0 4mm">{inner}</svg>'
def f1F():  # C8 Ch9 #15: line through O and (2,3) on a grid
  u=10;x0,x1,y0,y1=-3,3,-3,4;g,W,H=grid(x0,x1,y0,y1,u);ox,oy=-x0*u,y1*u;P=lambda x,y:(ox+x*u,oy-y*u)
  a=P(-2.4,-3.6);b=P(2.6,3.9);p=P(2,3)
  lab=''.join(f'<text x="{P(i,0)[0]}" y="{oy+5.5}" font-size="4.6" text-anchor="middle">{i}</text>' for i in (1,2))+''.join(f'<text x="{ox-1.5}" y="{P(0,j)[1]+1.2}" font-size="4.6" text-anchor="end">{j}</text>' for j in (1,2,3))
  ln=f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#000" stroke-width="0.8"/><circle cx="{p[0]}" cy="{p[1]}" r="1.1"/><text x="{p[0]+2}" y="{p[1]+1}" font-size="5" font-family="Times New Roman">(2, 3)</text>'
  return wrap(g+axes(ox,oy,W,H)+lab+ln,f"-7 -7 {W+24} {H+14}",50)
def f1G():  # C9 Ch3 #2: right triangle, top 5, hypotenuse 10, vertical x
  A,B,C=(0,0),(30,0),(30,52)
  s=f'<polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]}" fill="none" stroke="#000" stroke-width="0.8"/><path d="M{B[0]-4} 0 v4 h4" fill="none" stroke="#000" stroke-width="0.5"/>'
  s+=f'<text x="15" y="-2.5" font-size="6" text-anchor="middle" font-family="Times New Roman">5</text><text x="10" y="30" font-size="6" text-anchor="end" font-family="Times New Roman">10</text><text x="33" y="28" font-size="6" font-style="italic" font-family="Times New Roman">x</text>'
  return wrap(s,"-14 -10 56 68",38)
def f1H_t():  # C7 Ch7 #10: two lines cut by a transversal, 122° and 58°
  import math
  T=lambda x:(x, 34-0.18*x)   # transversal
  s=f'<line x1="-2" y1="{T(-2)[1]}" x2="102" y2="{T(102)[1]}" stroke="#000" stroke-width="0.8"/>'
  L1=(28,T(28)[1]);L2=(70,T(70)[1]);d=(14,-30)
  for P in (L1,L2):s+=f'<line x1="{P[0]-d[0]*0.75}" y1="{P[1]-d[1]*0.75}" x2="{P[0]+d[0]*1.0}" y2="{P[1]+d[1]*1.0}" stroke="#000" stroke-width="0.8"/>'
  # angle arcs: 122° below-left at L1 (between transversal-left and line-down), 58° above-left at L2 (between transversal-left and line-up)
  def arc(P,a1,a2,r=6):
    p1=(P[0]+r*math.cos(math.radians(a1)),P[1]-r*math.sin(math.radians(a1)));p2=(P[0]+r*math.cos(math.radians(a2)),P[1]-r*math.sin(math.radians(a2)))
    return f'<path d="M{p1[0]:.2f} {p1[1]:.2f} A{r} {r} 0 0 0 {p2[0]:.2f} {p2[1]:.2f}" fill="none" stroke="#000" stroke-width="0.5"/>'
  at=math.degrees(math.atan2(0.18,1));al=math.degrees(math.atan2(30,14))   # transversal & line directions (up-right)
  s+=arc(L1,180+at,180+al)+arc(L2,al,180+at)
  s+=f'<text x="{L1[0]-15}" y="{L1[1]+11}" font-size="6" text-anchor="middle" font-family="Times New Roman">122°</text><text x="{L2[0]-12}" y="{L2[1]-5}" font-size="6" text-anchor="middle" font-family="Times New Roman">58°</text>'
  return wrap(s,"-4 -6 108 70",66)
def f1H_g():  # C9 Ch4 #7: (a) line through (0,4) & (2,0); (b) horizontal line y=3
  def one(kind):
    W,H=60,56;ox,oy=24,36;u=6.5;P=lambda x,y:(ox+x*u,oy-y*u)
    s=axes(ox,oy,W,H)
    if kind=='a':a=P(-0.4,4.8);b=P(3.6,-3.2);s+=f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#000" stroke-width="0.8"/><text x="{ox-1.5}" y="{P(0,4)[1]+1.5}" font-size="5" text-anchor="end" font-family="Times New Roman">4</text><text x="{P(2,0)[0]+3}" y="{oy+6}" font-size="5" font-family="Times New Roman">2</text>'
    else:s+=f'<line x1="-2" y1="{P(0,3)[1]}" x2="{W+2}" y2="{P(0,3)[1]}" stroke="#000" stroke-width="0.8"/><path d="M{W+3} {P(0,3)[1]} l-3 -1.4 v2.8z M-3 {P(0,3)[1]} l3 -1.4 v2.8z"/><text x="{ox-1.5}" y="{P(0,3)[1]-1.5}" font-size="5" text-anchor="end" font-family="Times New Roman">3</text>'
    return s
  return f'<div style="display:flex;gap:10mm;margin:1mm 0 0 4mm">{wrap(one("a"),"-8 -8 78 72",44)}{wrap(one("b"),"-8 -8 78 72",44)}</div>'
