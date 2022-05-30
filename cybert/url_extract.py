from bs4 import BeautifulSoup
import requests
from requests.exceptions import MissingSchema
import typer

app = typer.Typer()


@app.command()
def url_extract(url):
    if not url.startswith("https://") and not url.startswith("http://"):
        url = "http://" + url

    r = requests.get(url)

    html = requests.get(r.url).text

    soup = BeautifulSoup(html, "lxml")

    text = " ".join(
        list(
            set(
                [
                    span.text
                    for span in soup.find_all(
                        "span", attrs={"class": ["font_7", "bold"]}
                    )
                ]
            )
        )
    )

    print(text)


if __name__ == "__main__":
    app()
