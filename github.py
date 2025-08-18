
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://github.com/trending"
HEADERS = {"User-Agent": "Mozilla/5.0", "Accept-Language": "en-US,en;q=0.9"}

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.text, "html.parser")

repos = soup.select("article.Box-row")[:10]
dados = []
for i, repo in enumerate(repos, start=1):
    project = repo.h2.a.get("href").strip("/")
    language = repo.select_one("span[itemprop=programmingLanguage]")
    language = language.text.strip() if language else ""
    stars = repo.select_one("a[href*='/stargazers']").text.strip().replace(",", "")
    stars_today = repo.select_one("span.d-inline-block.float-sm-right")
    stars_today = stars_today.text.strip().split(" ")[0] if stars_today else "0"
    forks = repo.select_one("a[href*='/network/members']")
    forks = forks.text.strip().replace(",", "") if forks else "0"
    dados.append([i, project, language, stars, stars_today, forks])

df = pd.DataFrame(dados, columns=["ranking", "project", "language", "stars", "stars_today", "forks"])
df.to_csv("github.csv", sep=";", index=False, encoding="utf-8")
print("✅ Arquivo github.csv gerado com sucesso!")
