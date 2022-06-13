from bs4 import BeautifulSoup
import requests
import typer

app = typer.Typer()


@app.command()
def url_extract(url, output_path, append_to_file=False):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    content = ""
    for p in soup.find_all("p", attrs={"class": ["lyrics"]}):
        content += p.text

    if not content:
        print(url.split("id=", 1)[1])
        return

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
