from bs4 import BeautifulSoup as soup
import pandas as pd
import requests
from IPython.display import display
import openpyxl
isim_liste =[]
forma_liste=[]
pozisyon_liste=[]
yas_liste=[]
url_listesi=[
    "https://www.foxsports.com/soccer/adana-demirspor-team-roster",
    "https://www.foxsports.com/soccer/alanyaspor-team-roster",
    "https://www.foxsports.com/soccer/ankaragucu-team-roster",
    "https://www.foxsports.com/soccer/antalyaspor-team-roster",
    "https://www.foxsports.com/soccer/istanbul-basaksehir-team-roster",
    "https://www.foxsports.com/soccer/besiktas-team-roster",
    "https://www.foxsports.com/soccer/caykur-rizespor-team-roster",
    "https://www.foxsports.com/soccer/fatih-karagumruk-sk-team-roster",
    "https://www.foxsports.com/soccer/fenerbahce-team-roster",
    "https://www.foxsports.com/soccer/galatasaray-team-roster",
    "https://www.foxsports.com/soccer/gazisehir-gaziantep-fk-team-roster",
    "https://www.foxsports.com/soccer/hatayspor-team-roster",
    "https://www.foxsports.com/soccer/istanbulspor-as-team-roster",
    "https://www.foxsports.com/soccer/kasimpasa-sk-team-roster",
    "https://www.foxsports.com/soccer/kayserispor-team-roster",
    "https://www.foxsports.com/soccer/konyaspor-team-roster",
    "https://www.foxsports.com/soccer/pendikspor-team-roster",
    "https://www.foxsports.com/soccer/samsunspor-team-roster",
    "https://www.foxsports.com/soccer/sivasspor-team-roster",
    "https://www.foxsports.com/soccer/trabzonspor-team-roster"
]


for url in url_listesi:
    sonuc= requests.get(url)
    doc= soup(sonuc.text,"html.parser")
    names=doc.find_all("h3")
    formalar=doc.find_all("sup")
    pozisyon= doc.find_all(class_="cell-text ff-h" , attrs={"data-index":"1"})
    yas= doc.find_all(class_="cell-text ff-h" , attrs={"data-index":"2"})
    for (i, j, k, y) in zip(names, formalar, pozisyon, yas):
        isim = i.text.strip()
        forma = j.text.strip()
        pozisyon = k.text[7].strip()
        yas = y.text[7:9].strip()

    # Append to the lists and fill NaN for empty lines
        isim_liste.append(isim if pd.notna(isim) else float('nan'))
        forma_liste.append(forma if pd.notna(forma) else float('nan'))
        pozisyon_liste.append(pozisyon if pd.notna(pozisyon) else float('nan'))
        yas_liste.append(yas if pd.notna(yas) else float('nan'))

df= pd.DataFrame(data={"oyuncu_adi":isim_liste,"forma_numarasi" : forma_liste , "pozisyon":pozisyon_liste, "yas": yas_liste})
df.to_excel("oyuncular.xlsx",index=False)