/* Do Now picker, shared by the planner and the Do Now sheet page.
   Each subchapter card holds a `retrieval` pool of verbatim questions about ITSELF.
   A lesson's Do Now draws from subchapters taught BEFORE it, spaced out:
   slot 1 = last lesson, slot 2 = about a week ago (3–6 lessons back), slot 3 = longer ago (7+ lessons back).
   Each question is used once per stream (reused only when a pool runs dry). */
(function(g){
const KINDS_WITH_DN={teach:1,practice:1};
function planFor(u,LP){const ids=new Set(u.items.map(x=>x.id)),p=(LP.plans||{})[u.stream+'|'+u.name];
  if(!p)return u.items.map(x=>({kind:'teach',items:[{id:x.id}]})).concat([{kind:'review',items:[]},{kind:'assess',items:[]}]);
  return p.map(l=>({...l,items:l.items.filter(x=>ids.has(x.id))}))}
function doNows(stream,UNITS,LP,IDX,N=3){
  const seq=[];UNITS.units.filter(u=>u.stream===stream).forEach((u,ui)=>planFor(u,LP).forEach((l,li)=>seq.push({u,ui,li,l})));
  const last={},used={},usedSub={},out={};
  seq.forEach((s,i)=>{
    const key=s.ui+'|'+s.li;
    if(KINDS_WITH_DN[s.l.kind]){
      const subsAt=(lo,hi)=>Object.keys(last).filter(id=>last[id]>=i-hi&&last[id]<=i-lo);
      const slots=[subsAt(1,2),subsAt(3,6),subsAt(7,1e9)],pick=[];
      const take=subs=>{const cands=[];subs.forEach(id=>{const c=IDX[id];(c&&c.retrieval||[]).forEach(q=>{if(stream==='10MAG'&&q.tenA)return;cands.push(q)})});
        cands.sort((a,b)=>(used[a.id]||0)-(used[b.id]||0)||(usedSub[a.sub]||0)-(usedSub[b.sub]||0));
        const q=cands.find(q=>!pick.includes(q)&&!pick.some(p=>p.sub===q.sub))||cands.find(q=>!pick.includes(q));
        if(q){pick.push(q);used[q.id]=(used[q.id]||0)+1;usedSub[q.sub]=(usedSub[q.sub]||0)+1;return true}return false};
      for(let k=0;k<N;k++){ if(!take(slots[k]||[])){ for(const alt of [slots[1],slots[2],slots[0]]) if(take(alt||[]))break } }
      out[key]={items:pick,unit:s.u,ui:s.ui,li:s.li};
    }
    s.l.items.forEach(x=>last[x.id]=i);
  });
  return out}
g.DN={planFor,doNows};
})(window);
