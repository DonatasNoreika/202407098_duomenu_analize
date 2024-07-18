from bs4 import BeautifulSoup
import requests
import csv

r = requests.get("https://www.delfi.lt/")
soup = BeautifulSoup(r.text, 'html.parser')

blokai = soup.find_all("article")

with open("delfi_naujienos.csv", 'w', encoding="UTF-8", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["KATEGORIJA", "PAVADINIMAS", "NUORODA"])
    for blokas in blokai:
        try:
            kategorija = blokas.find("div", class_="headline-labels__label").get_text().strip()
        except:
            kategorija = " "
        pavadinimas = blokas.find("h5", class_="headline-title").a.get_text().strip()
        nuoroda = blokas.find("h5", class_="headline-title").a['href']
        if nuoroda.startswith("/"):
            nuoroda = "https://www.delfi.lt" + nuoroda
        csv_writer.writerow([kategorija, pavadinimas, nuoroda])
        print(kategorija)
        print(pavadinimas)
        print(nuoroda)
        print("-------------------------------")