"""House-style SVG sketches for the slides (black axes, Times italic labels; solution marks in red)."""
R='#d00000'
def _t(x,y,s,anchor='middle',size=15,it=False,col='#000'):
    st=' font-style="italic"' if it else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" font-family="Times New Roman"{st} fill="{col}">{s}</text>'
def _arrow(x,y,dx,dy,col):
    import math
    a=math.atan2(dy,dx);L=9;w=4
    p=[(x,y),(x-L*math.cos(a)+w*math.sin(a),y-L*math.sin(a)-w*math.cos(a)),(x-L*math.cos(a)-w*math.sin(a),y-L*math.sin(a)+w*math.cos(a))]
    return '<path d="M%.1f %.1fL%.1f %.1fL%.1f %.1fz" fill="%s"/>'%(p[0][0],p[0][1],p[1][0],p[1][1],p[2][0],p[2][1],col)

def numberline(lo,hi,labels=None,left=None,right=None,col=R,w=300,var='x'):
    """lo..hi tick range. left/right = (value, closed) end of the solution; None = ray to that side.
    left=None & right=(2,False) -> x<2. Both given -> segment."""
    u=(w-50)/(hi-lo+1.0);X=lambda v:25+(v-lo+0.5)*u;y=22
    o=[f'<line x1="6" y1="{y}" x2="{w-14}" y2="{y}" stroke="#000" stroke-width="1.5"/>',_arrow(w-12,y,1,0,'#000'),_arrow(4,y,-1,0,'#000'),_t(w-4,y+5,var,'start',16,True)]
    labels=list(range(lo,hi+1)) if labels is None else labels
    for v in range(lo,hi+1):
        o.append(f'<line x1="{X(v):.1f}" y1="{y-5}" x2="{X(v):.1f}" y2="{y+5}" stroke="#000" stroke-width="1.2"/>')
    for v in labels: o.append(_t(X(v),y+24,str(v).replace('-','−'),size=16))
    a=X(left[0]) if left else 8; b=X(right[0]) if right else w-18; yy=y-12
    o.append(f'<line x1="{a:.1f}" y1="{yy}" x2="{b:.1f}" y2="{yy}" stroke="{col}" stroke-width="2.5"/>')
    if not left:o.append(_arrow(a-4,yy,-1,0,col))
    if not right:o.append(_arrow(b+4,yy,1,0,col))
    for e in (left,right):
        if e:o.append(f'<circle cx="{X(e[0]):.1f}" cy="{yy}" r="5" fill="{col if e[1] else "#fff"}" stroke="{col}" stroke-width="2"/>')
    return f'<svg class="fig" width="{(w+10)*1.35:.0f}" height="{56*1.35:.0f}" viewBox="0 -6 {w+10} 56">{"".join(o)}</svg>'

def plane(x0,x1,y0,y1,items=(),w=230,h=None,ticks=False):
    """Cartesian sketch. items: ('line',(xa,ya),(xb,yb)[,col,dash]) extended across the box;
    ('pt',(x,y),'label',dx,dy) ; ('lab',(x,y),'text',anchor) ; ('dash',[(x,y),...]) ; ('poly',[(x,y)...]) shaded region;
    ('hline',y,'label') ; ('vline',x,'label')"""
    u=w/(x1-x0); h=h or (y1-y0)*u; v=h/(y1-y0)
    X=lambda x:(x-x0)*u; Y=lambda y:(y1-y)*v
    o=[]
    for it in items:
        if it[0]=='poly':
            pts=' '.join('%.1f,%.1f'%(X(a),Y(b)) for a,b in it[1]); o.append(f'<polygon points="{pts}" fill="#f4b6b6" stroke="none"/>')
    ox,oy=X(0),Y(0)
    o.append(f'<line x1="0" y1="{oy:.1f}" x2="{w:.1f}" y2="{oy:.1f}" stroke="#000" stroke-width="1.3"/>'+_arrow(w+2,oy,1,0,'#000')+_arrow(-2,oy,-1,0,'#000'))
    o.append(f'<line x1="{ox:.1f}" y1="0" x2="{ox:.1f}" y2="{h:.1f}" stroke="#000" stroke-width="1.3"/>'+_arrow(ox,-2,0,-1,'#000')+_arrow(ox,h+2,0,1,'#000'))
    o.append(_t(w+10,oy+5,'x','start',17,True)+_t(ox+8,-6,'y','start',17,True)+_t(ox-5,oy+16,'O','end',15,True))
    if ticks:
        for i in range(int(x0)+1,int(x1)):
            if i: o.append(f'<line x1="{X(i):.1f}" y1="{oy-4:.1f}" x2="{X(i):.1f}" y2="{oy+4:.1f}" stroke="#000"/>')
        for j in range(int(y0)+1,int(y1)):
            if j: o.append(f'<line x1="{ox-4:.1f}" y1="{Y(j):.1f}" x2="{ox+4:.1f}" y2="{Y(j):.1f}" stroke="#000"/>')
    def clip(p,q):
        (xa,ya),(xb,yb)=p,q;ts=[]
        dx,dy=xb-xa,yb-ya
        for t in [(x0-xa)/dx if dx else None,(x1-xa)/dx if dx else None,(y0-ya)/dy if dy else None,(y1-ya)/dy if dy else None]:
            if t is None:continue
            x,y=xa+t*dx,ya+t*dy
            if x0-1e-9<=x<=x1+1e-9 and y0-1e-9<=y<=y1+1e-9: ts.append(t)
        ta,tb=min(ts),max(ts); return (xa+ta*dx,ya+ta*dy),(xa+tb*dx,ya+tb*dy)
    for it in items:
        k=it[0]
        if k=='line':
            col=it[3] if len(it)>3 and it[3] else R; dash=' stroke-dasharray="8 6"' if len(it)>4 and it[4] else ''
            a,b=clip(it[1],it[2]);
            import math
            ax,ay,bx,by=X(a[0]),Y(a[1]),X(b[0]),Y(b[1]);L=math.hypot(bx-ax,by-ay);ux,uy=(bx-ax)/L,(by-ay)/L
            ax+=ux*6;ay+=uy*6;bx-=ux*6;by-=uy*6
            o.append(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{col}" stroke-width="2.5"{dash}/>')
            o.append(_arrow(bx+ux*4,by+uy*4,ux,uy,col)+_arrow(ax-ux*4,ay-uy*4,-ux,-uy,col))
        elif k=='pt':
            (x,y),lab=it[1],it[2];dx=it[3] if len(it)>3 else 8;dy=it[4] if len(it)>4 else -8
            col=it[5] if len(it)>5 else R
            o.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="4" fill="{col}"/>')
            if lab:o.append(_t(X(x)+dx,Y(y)+dy+5,lab.replace('-','−'),'start' if dx>=0 else 'end',15,False,col))
        elif k=='lab':
            (x,y),s=it[1],it[2];an=it[3] if len(it)>3 else 'start';col=it[4] if len(it)>4 else R
            o.append(_t(X(x),Y(y),s.replace('-','−'),an,15,False,col))
        elif k=='dash':
            pts=' '.join('%.1f,%.1f'%(X(a),Y(b)) for a,b in it[1]);col=it[2] if len(it)>2 else R
            o.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="1.5" stroke-dasharray="5 4"/>')
    return f'<svg class="fig" width="{(w+40)*1.15:.0f}" height="{(h+40)*1.15:.0f}" viewBox="-15 -20 {w+40:.0f} {h+40:.0f}">{"".join(o)}</svg>'
