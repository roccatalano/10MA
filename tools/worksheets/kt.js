const k=require('/home/claude/kx/node_modules/katex');const fs=require('fs');
const a=JSON.parse(fs.readFileSync(0,'utf8'));
const r=s=>s.replace(/\$\$(.+?)\$\$/gs,(m,x)=>k.renderToString(x,{displayMode:true,output:'html'})).replace(/\$(.+?)\$/gs,(m,x)=>k.renderToString(x,{output:'html'}));
process.stdout.write(JSON.stringify(a.map(r)));
