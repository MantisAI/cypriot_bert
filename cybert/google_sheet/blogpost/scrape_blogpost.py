from bs4 import BeautifulSoup
import requests
import typer
import os

app = typer.Typer()


def write_to_file(text, output_path, arg):
    with open(output_path, arg) as f:
        f.write(text)


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
        try:
            write_to_file(text, output_path, "w")
        except IsADirectoryError:
            print(f"Error: {output_path} is a directory")
    else:
        try:
            write_to_file(text, output_path, "a")
        except OSError:
            # create parent dir
            os.makedirs(os.path.abspath(os.path.join(output_path, os.pardir)))
            write_to_file(text, output_path, "a")


if __name__ == "__main__":
    app()
