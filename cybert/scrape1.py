from bs4 import BeautifulSoup
import requests
import typer

app = typer.Typer()


@app.command()
def url_extract(url, output_path):

    if not url.startswith("https://") and not url.startswith("http://"):
        url = "http://" + url

    r = requests.get(url)

    html = requests.get(r.url).text


    soup = BeautifulSoup(html, "lxml")


    text = " ".join(
    list(
        set(
            [
                div.text
                for div in soup.find_all(
                    "div", attrs={"class": ["post-body"]}
                )
            ]
        )
    )
    )


    try:
        with open(output_path, "w") as f:
            f.write(text)
    except IsADirectoryError:
        print(f"Error: {output_path} is a directory")

if __name__ == "__main__":
    app()
