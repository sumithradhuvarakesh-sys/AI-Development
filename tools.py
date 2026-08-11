import requests
from bs4 import BeautifulSoup


def search_web(query):
    try:
        url = "https://html.duckduckgo.com/html/"

        data = {
            "q": query
        }

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://html.duckduckgo.com/"
        }

        response = requests.post(
            url,
            data=data,
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            return {
                "success": False,
                "error": "Search failed: " + str(response.status_code)
            }

        soup = BeautifulSoup(response.text, "html.parser")

        results = []

        for item in soup.select(".result")[:5]:
            link = item.select_one(".result__a")

            if link:
                results.append({
                    "title": link.get_text(strip=True),
                    "url": link.get("href")
                })

        if len(results) == 0:
            return {
                "success": False,
                "error": "No results found"
            }

        return {
            "success": True,
            "results": results
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def fetch_page(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            return {
                "success": False,
                "error": "Page fetch failed: " + str(response.status_code)
            }

        soup = BeautifulSoup(response.text, "html.parser")

        for item in soup(["script", "style"]):
            item.extract()

        text = soup.get_text(" ", strip=True)

        return {
            "success": True,
            "content": text[:5000]
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }