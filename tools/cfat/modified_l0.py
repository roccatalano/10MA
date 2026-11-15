"""10MAG Modified CFAT items (level L0): shared helpers. One generator per chapter (gen_ch<n>m.py) builds L0={(sub,n):[items]} and calls apply().
Run each gen_ch<n>m.py AFTER its gen_ch<n>.py (which rewrites the blocks without L0)."""
import json,os
HERE=os.path.dirname(os.path.abspath(__file__))
def load_helpers(gen):
    """table, stemleaf, axis, boxplot, mc, sa, R ... from the 10MAG generator, without its blocks"""
    src=open(os.path.join(HERE,gen)).read();g={'__file__':os.path.join(HERE,gen)};exec(src[:src.index('B={}')],g);return g
C7='Cambridge Essential Mathematics 7 (3rd Ed)';C8='Cambridge Essential Mathematics 8 (3rd Ed)';C9='Cambridge Essential Mathematics 9 (3rd Ed)'
PARTS='adapted: parts chosen'
def apply(L0,subs,label):
    for sub in subs:
        p=os.path.join(HERE,f'C10-{sub}.json');b=json.load(open(p))
        b['levels']['L0']=label
        for s in b['skills']:
            s['items']=[x for x in s['items'] if x['level']!='L0']+L0.get((sub,s['n']),[])
        json.dump(b,open(p,'w'),indent=1,ensure_ascii=False);print('L0 added',sub,sum(1 for s in b['skills'] for x in s['items'] if x['level']=='L0'))
