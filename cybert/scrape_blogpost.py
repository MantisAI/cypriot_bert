from bs4 import BeautifulSoup
import requests
import typer

app = typer.Typer()


@app.command()
def url_extract(url, output_path, append_to_file=False):

    if not url.startswith("https://") and not url.startswith("http://"):
        url = "http://" + url

    r = requests.get(url)

    html = requests.get(r.url).text

    soup = BeautifulSoup(html, "lxml")

    text = ""
    for div in soup.find("div", attrs={"class": ["post-body"]}):
        text += div.text

    if append_to_file == "False":
        arg = "w"
    else:
        arg = "a"

    try:
        with open(output_path, arg) as f:
            f.write(text.strip())
    except IsADirectoryError:
        print(f"Error: {output_path} is a directory")


if __name__ == "__main__":
    app()
