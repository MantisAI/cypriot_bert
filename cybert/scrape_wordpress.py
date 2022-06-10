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

@app.command()
def url_extract(url, output_path):

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
        except:
            continue


    try:
        with open(output_path, "w") as f:
            f.write(content.text.strip())
    except IsADirectoryError:
        print(f"Error: {output_path} is a directory")

if __name__ == "__main__":
    app()