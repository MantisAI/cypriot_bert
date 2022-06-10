import scrape_blogpost
import scrape_wordpress

import pandas as pd
import typer

app = typer.Typer()


@app.command()
def extract_google_sheet():

    df = pd.read_csv(
        "https://docs.google.com/spreadsheets/d/e/2PACX-1vTd7ywEIF0KUgxO6j2-GfDPeTEltI5izSAa_yXbI0UmI1_9COoJyJQcl4c0AvpIEy33fFmH-JVIreiy/pub?output=csv"
    )

    for i in range(len(df) - 1):
        if not pd.isnull(df["Link"][i]):
            check_script_column = df.loc[i, "Script"]
            url = df["Link"][i]

            if check_script_column == "scrape_blogpost":
                scrape_blogpost.url_extract(url, "blogpost_content.txt", True)
            elif check_script_column == "scrape_wordpress":
                scrape_wordpress.url_extract(url, "wordpress_content.txt", True)


if __name__ == "__main__":
    app()
