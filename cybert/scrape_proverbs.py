from bs4 import BeautifulSoup
import requests
import typer

app = typer.Typer()


@app.command()
def url_extract(url, output_path):

    r = requests.get(url)

    html = requests.get(r.url).text

    soup = BeautifulSoup(html, "lxml")

    content = ""
    for td in soup.find("td", attrs={"class": ["paroimia"]}):
        content += td.text + "\n"

    try:
        with open(output_path, "a") as f:
            f.write(content)
    except IsADirectoryError:
        print(f"Error: {output_path} is a directory")


if __name__ == "__main__":
    app()
