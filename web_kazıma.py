import requests
from bs4 import BeautifulSoup

# Buraya istediğin haber sitesinin linkini yaz
url = "https://www.cnnturk.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# CNN Türk ana sayfasında haber başlıkları <h3 class="card-title"> etiketiyle geliyor
for baslik in soup.find_all("h3", class_="card-title"):
    print(baslik.text.strip())