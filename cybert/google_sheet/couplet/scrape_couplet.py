from bs4 import BeautifulSoup
import requests
import typer

app = typer.Typer()


def write_to_file(text, output_path, arg):
    with open(output_path, arg) as f:
        f.write(text)


@app.command()
def url_extract(url, output_path, append_to_file=False):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    current_content = soup.find_all("p", attrs={"class": ["lyrics"]})
    final_content = ""

    if current_content is not None:
        for p in current_content:
            final_content += p.text
    else:
        div = soup.find("div", attrs={"class": ["u-theme-white"]})
        final_content = div.text.strip()

    if append_to_file == "False":
        try:
            write_to_file(final_content, output_path, "w")
        except IsADirectoryError:
            print(f"Error: {output_path} is a directory")
    else:
        write_to_file(final_content, output_path, "a")


if __name__ == "__main__":
    app()
