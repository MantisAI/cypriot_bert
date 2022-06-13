from bs4 import BeautifulSoup
import requests
import typer

app = typer.Typer()


@app.command()
def url_extract(url, output_path, append_to_file=False):

    r = requests.get(url)

    html = requests.get(r.url).text

    soup = BeautifulSoup(html, "lxml")

    content = ""
    for td in soup.find("td", attrs={"class": ["paroimia"]}):
        content += td.text + "\n"

    if append_to_file == "False":
        arg = "w"
    else:
        arg = "a"

    try:
        with open(output_path, arg) as f:
            f.write(content)
    except IsADirectoryError:
        print(f"Error: {output_path} is a directory")


if __name__ == "__main__":
    app()
