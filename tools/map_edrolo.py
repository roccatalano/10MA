import json,re
V=json.load(open('edrolo_vcaa.json'))
R=[ # (G11 sub, regex on text, optional tag regex)
('2H',r'box ?plot|outlier|fence'),('2I',r'back-to-back|parallel box|compar\w* .*distribut'),
('2G',r'68%|95%|99\.7%|standard deviations? (above|below)|standardi[sz]ed|z-score|z score'),
('2F',r'standard deviation|interquartile|IQR|range of'),('2E',r'\bmedian\b|\bmean\b|average'),
('2D',r'stem ?plot|stem-and-leaf|dot plot|skew|symmetric'),('2C',r'histogram|log scale|frequency table.*numerical'),
('2B',r'bar chart|segmented|percentage frequency|mode'),('2A',r'categorical|nominal|ordinal|discrete|continuous'),
('7C',r'correlation coefficient|\br\s*=|Pearson'),('7E',r'predict|extrapolat|interpolat|residual'),
('7D',r'least squares|regression line|line of best fit|equation of the (least|regression)'),('7B',r'association|direction|strength|form'),('7A',r'scatter ?plot|explanatory|response variable'),
('3H',r'compound interest|depreciat.*(%|per cent)|reducing balance|interest.*compound'),('3E',r'simple interest|flat rate|unit cost depreciation|depreciat'),
('3G',r'geometric.*recurrence|recurrence.*×|V_?n\s*\+\s*1\s*=\s*R'),('3I',r'geometric.*term|growth and decay'),('3F',r'geometric|common ratio'),
('3D',r'arithmetic.*recurrence|recurrence relation'),('3C',r'arithmetic|common difference'),('3A',r'sequence|pattern|term'),
('4H',r'transition'),('4E',r'inverse|determinant|simultaneous'),('4F',r'communication|road.*matrix|matrix.*road|one-step|two-step'),
('4D',r'multipl|product\b|order of (the )?matri'),('4C',r'scalar'),('4B',r'add|subtract|sum of'),('4I',r'matri'),('4A',r'element|order|matri'),
('8H',r'spanning tree|Prim|minimum.*cable|connector'),('8G',r'shortest|weighted|Dijkstra'),('8F',r'Hamilton'),('8E',r'Euler(ian)? (trail|circuit|path)|every (road|edge|bridge)'),
('8C',r'planar|faces|Euler.s formula|v\s*\+\s*f'),('8D',r'walk|trail|path|circuit|cycle'),('8B',r'adjacency|isomorph|equivalent'),('8A',r'vertex|vertices|edges|degree|graph|network'),
('1F',r'unitary|per (kg|litre|item)|best buy'),('1C',r'GST'),('1E',r'divided? .* ratio|shared .* ratio'),('1D',r'ratio|proportion'),
('1B',r'percentage (increase|decrease|change)|discount|mark-?up|increased by|decreased by'),('1A',r'per ?cent|%'),
]
DOM={'2':r'data|Data|Core','7':r'data|Data|Core','3':r'Number patt|Business|Recursion|financial|Core','4':r'Matri','8':r'Network|decision','1':r'Business|Number patt|Core|Recursion|financial'}
seen={};out={}
for q in V:
  key=q['tag'];
  if key in seen: seen[key]['also_in'].append(f"E11-{q['edrolo']} Q{q['q']}"); continue
  q['also_in']=[]; seen[key]=q
  for s,rx in R:
    if re.search(DOM[s[0]],q['tag']) and re.search(rx,q['text_locator'],re.I):
      q['g11']=s; break
  else:
    t=q['tag']; q['g11']=('3C' if re.search(r'Number patt',t) else '3D' if re.search(r'Recursion',t) else '4D' if re.search(r'Matri',t) else '8A' if re.search(r'Network',t) else None)
    if q['g11']: q['map']='module fallback'
  q.setdefault('map','keyword')
for q in seen.values(): q['text_locator']=q['text_locator'][:240]
U=list(seen.values()); json.dump(U,open('edrolo_vcaa_mapped.json','w'),indent=0,ensure_ascii=False)
from collections import Counter
c=Counter(q['g11'] for q in U); print(len(U),sorted(c.items(),key=lambda x:str(x[0])))
