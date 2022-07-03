import requests
import typer
import re

app = typer.Typer()


@app.command()
def url_extract(output_path):

    url = "https://diasporos.blogspot.com/feeds/posts/default"

    r = requests.get(url)

    data = requests.get(r.url).text

    # get content
    regex = re.compile("<content type='html'>(.+?)</content>")
    found_str = re.findall(regex, data)

    content = ""
    # remove english letters and chars
    for i in found_str:
        text = re.sub(r"[a-zA-Z0-9&#;?%=:+\/\-\_]", "", i)
        content += text

    patterns = [" (\.)\1*", " , ", " ! ", "é,"]
    discard_lst = []

    for i in patterns:
        matcher = re.compile(i)
        discard_lst += [match.group() for match in matcher.finditer(content)]

    # remove patterns
    for i in discard_lst:
        content = content.replace(i, "")

    # replace two or more repeated punctuations with a single punctuation
    rx = re.compile(r"([!.])\1+")
    content = rx.sub(r"\1 ", content).rstrip()

    with open(output_path, "w") as f:
        f.write(content)


if __name__ == "__main__":
    app()
