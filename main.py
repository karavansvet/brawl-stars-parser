
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

URL = "https://lzt.market/supercell?order_by=pdate_to_down_upload#title"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 "
        "Mobile/15E148 Safari/604.1"
    )
}

try:
    response = requests.get(
        URL,
        headers=headers,
        timeout=25
    )

    print("HTTP:", response.status_code)
    print("Адрес:", response.url)

    soup = BeautifulSoup(response.text, "html.parser")

    print("Заголовок:", soup.title.get_text(strip=True) if soup.title else "Не найден")

    print("\nПервые объявления:")

    count = 0
    for link in soup.find_all("a", href=True):
        href = link["href"]
        text = link.get_text(" ", strip=True)

        if "/market/" in href or (
            href.rstrip("/").split("/")[-1].isdigit()
        ):
            print(text[:180])
            print(urljoin(URL, href))
            print("---")
            count += 1

        if count >= 10:
            break

    print("\nНайдено ссылок:", count)

except Exception as error:
    print("Ошибка:", repr(error))
