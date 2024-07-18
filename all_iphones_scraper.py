from bs4 import BeautifulSoup
import requests
import csv

with open("all_telia_iphones.csv", 'w', encoding="UTF-8", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Telefonas", "Kaina mėn.", "Kaina"])
    for page in range(1, 5):
        r = requests.get(f"https://www.telia.lt/prekes/telefonai-ir-priedai/mobilieji-telefonai?page={page}")
        soup = BeautifulSoup(r.text, 'html.parser')
        blokai = soup.find_all("div", class_="mobiles-product-card card card__product card--anim js-product-compare-product")
        for blokas in blokai:
            pavadinimas = blokas.find("a", class_="mobiles-product-card__title js-open-product").get_text().strip()
            kaina_men = float(blokas.find_all("div", class_="mobiles-product-card__price-marker")[0].get_text().strip().replace(" €/mėn.", "").replace(",", "."))
            kaina = int(blokas.find_all("div", class_="mobiles-product-card__price-marker")[1].get_text().strip().replace(" ", "").replace(" €", ""))
            csv_writer.writerow([pavadinimas, kaina_men, kaina])
            print(pavadinimas)
            print(kaina_men)
            print(kaina)