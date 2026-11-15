"""Kept for old notes: G1 content now lives in mod_statistics.py (shared code in modified.py)."""
import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mod_statistics import W,main
if __name__=='__main__':main(W,sys.argv[1:])
