from bs4 import BeautifulSoup
import requests
import typer

app = typer.Typer()


def pattixa_wordpress(soup):
    content = soup.find("div", attrs={"class": ["entry-content"]})

    return content


def xenihtikon_wordpress(soup):
    content = soup.find("div", attrs={"class": ["entry"]})

    return content


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

    for fn in (pattixa_wordpress, xenihtikon_wordpress):
        try:
            content = fn(soup)

            unwanted = content.find("div", attrs={"class": ["sharedaddy"]})
            unwanted.extract()
            break
        except AttributeError:
            continue

    content = content.text.strip()

    if append_to_file == "False":
        try:
            write_to_file(content, output_path, "w")
        except IsADirectoryError:
            print(f"Error: {output_path} is a directory")
    else:
        write_to_file(content, output_path, "a")


if __name__ == "__main__":
    app()
