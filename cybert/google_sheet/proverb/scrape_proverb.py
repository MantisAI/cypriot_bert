from bs4 import BeautifulSoup
import requests
import typer
import time

app = typer.Typer()


def write_to_file(text, output_path, arg):
    with open(output_path, arg) as f:
        f.write(text)


@app.command()
def url_extract(url, output_path, append_to_file=False):

    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        r = requests.get(url)

    html = requests.get(r.url).text

    soup = BeautifulSoup(html, "lxml")

    content = ""
    for td in soup.find("td", attrs={"class": ["paroimia"]}):
        content += td.text + "\n"

    if append_to_file == "False":
        try:
            write_to_file(content, output_path, "w")
        except IsADirectoryError:
            print(f"Error: {output_path} is a directory")
    else:
        write_to_file(content, output_path, "a")


if __name__ == "__main__":
    app()
