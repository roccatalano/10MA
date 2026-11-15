import json,re
H={ # (fluency, problem-solving, reasoning, enrichment) x (Foundation, Standard, Advanced) — read off the book's pathway bars
'1A':[('1–6(½)','1–6(½)','1–6(⅓)'),('7','7, 8','8'),('9','9, 10','10, 11'),('–','–','12')],
'1B':[('1–3(½), 5(½)','1–5(⅓)','1–5(⅓)'),('6–9','6(½), 7, 9, 10','6–7(½), 10–12'),('13','13','14'),('–','–','15, 16')],
'1C':[('1–4(½)','1–4(½)','1–4(⅓)'),('5, 6','5, 6','6, 7'),('8','8, 9','9, 10'),('–','–','11–12(½)')],
'1D':[('1–3(½)','1–3(½)','1–3(⅓)'),('4(½)','4(½), 5','4(⅓), 5–7'),('8','8, 9','8, 9'),('–','–','10, 11')],
'1E':[('1, 2–5(½)','1, 2–5(½)','1, 2–5(⅓)'),('6, 7','6–8','7–9'),('10','10, 11','11, 12'),('–','–','13')],
'1F':[('1(½), 2, 3(½)','1–4(½)','1(⅓), 2–4(½)'),('5','5, 6','6, 7'),('8','8, 9','8, 9'),('–','–','10')],
'1G':[('1–2(½)','1–2(½)','1–2(⅓)'),('3, 4–5(½)','3, 4–5(½)','4–5(½), 6'),('7','7, 8','8, 9(½)'),('–','–','10')],
'1H':[('1–3(½)','1–3(½)','1(⅓), 2–3(½)'),('4(½)','4–6(½)','4–6(½), 7'),('8','8, 9','8–10'),('–','–','11–13')],
'1I':[('1–2(½)','1–2(½)','1–2(⅓)'),('3, 4','3–5','4–6'),('7(½)','7(½), 8','7(½), 8, 9'),('–','–','10(½), 11')],
'1J':[('1–3(½)','1–3(½)','1–2(⅓), 3(½)'),('4','4, 5','5, 6'),('7','7, 8(½)','8, 9'),('–','–','10(½)')],
'1K':[('1–4','1, 3–5','2–5'),('6, 7','6–8','7–9'),('10','10, 11','11, 12'),('–','–','13, 14')],
'1L':[('1–2(½), 3, 4(½)','1–4(½)','1–2(½), 4(½)'),('5','5, 6(½)','5–6(½)'),('7(½)','7(½)','7, 8'),('–','–','9, 10')],
}
TIERS=[('Good','Minimum for your coursework tick'),('Better','The standard for doing well on assessments'),('Best','The full challenge')]
SEC=['Fluency','Problem-solving','Reasoning','Enrichment']
def box(sub,pages):
  rows=''.join(f'<tr><th><b>{t}</b><br><span>{d}</span></th>'+''.join(f'<td>{"Q"+H[sub][c][i] if H[sub][c][i]!="–" else "–"}</td>' for c in range(4))+'<td class="tk"></td></tr>' for i,(t,d) in enumerate(TIERS))
  return (f'<div class="box "><div class="hd">Coursework · Exercise {sub} (Cambridge {pages})<span>Your teacher will tell you which row to do</span></div><div class="bd">'
   '<style>.hwt{width:100%;border-collapse:collapse;font-size:10.5pt}.hwt th,.hwt td{border:1px solid #000;padding:1.5mm 2mm;text-align:left;vertical-align:middle}.hwt thead th{background:#eee;font-size:9.5pt;text-transform:uppercase;letter-spacing:.3px}.hwt tbody th{width:30%;font-weight:normal}.hwt tbody th span{font-size:8.5pt}.hwt td.tk{width:12mm}.hwt thead th:last-child{text-align:center}</style>'
   f'<table class="hwt"><thead><tr><th>Option</th>{"".join(f"<th>{s}</th>" for s in SEC)}<th>Done</th></tr></thead><tbody>{rows}</tbody></table>'
   '<p class="hwn"><b>(½)</b> = every second part (a, c, e, …) &nbsp;·&nbsp; <b>(⅓)</b> = every third part (a, d, g, …). Do the other parts for revision. Options follow the book\'s Foundation, Standard and Advanced pathways.</p>'
   '<div class="sig"><div class="stamp">Teacher stamp</div><div class="lines"><div><span>Student signature</span><i></i><span>Date</span><i class="d"></i></div><div><span>Parent signature</span><i></i><span>Date</span><i class="d"></i></div></div></div></div></div>')
