from bs4 import BeautifulSoup
import requests
import re
import typer

app = typer.Typer()


def parse_text_to_html_find_tag(text, tag="span"):
    soup = BeautifulSoup(text, "lxml")

    all_tags_content = soup.findAll(tag)

    return all_tags_content


@app.command()
def url_extract(url):
    # either it's http or https, since no client certificates are used => it will use http
    if url.startswith("https://"):
        url = url.replace("https://", "http://")

    if not url.startswith("http://"):
        url = "http://" + url

    replacements = [
        '<span class="bold">(.+?)</span>',
        '<span class="color_4">(.+?)</span>',
        '<span class="_2TTZA">(.+?)</span>',
    ]

    try:
        htmltext = requests.get(url).text

        tags_content = parse_text_to_html_find_tag(htmltext)

        # convert it to string and exclude all the content of the classes of the given tag that we don't want
        tags_content = str(tags_content)

        for x in replacements:
            # loop  through the not desired tags in the text string
            for m in re.finditer(x, tags_content):
                # get only the content of the regex match object
                content = str(m.group(0))

                # cannot remove the tags from the html because when parsing will lead to errors
                # get the content within the tags
                lst = [i.split("(.+?)")[0] for i in replacements]

                for i in lst:
                    content = content.replace(i, "")

                content = content.replace("</span>", "")

                tags_content = tags_content.replace(content, "")

        discard_list = [
            "Αντώνης ΓαβριήλΠαπά",
            "ΑΝΤΩΝΗΣ ΓΑΒΡΙΗΛ ΠΑΠΑ",
            "ΛΑΪΚΟΣ ΠΟΙΗΤΗΣ",
            "Κίτι-Λάρνακα",
        ]

        for i in discard_list:
            tags_content = tags_content.replace(i, "")

        # string does not have text attribute => convert it back to 'bs4.element.ResultSet' type
        tags_content = parse_text_to_html_find_tag(tags_content)

        # print the content of all tags
        for tag_content in tags_content:
            print(tag_content.text)
    except:
        print(
            "The given website does not exist or the given tag is not part of the given website. Try again!"
        )


if __name__ == "__main__":
    app()
