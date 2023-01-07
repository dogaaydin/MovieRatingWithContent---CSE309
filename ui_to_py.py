from PyQt5 import uic

with open ("Anasayfa.py" ,"w" , encoding="utf-8") as fout:
    uic.compileUi("AnasayfaDeneme.ui" , fout)