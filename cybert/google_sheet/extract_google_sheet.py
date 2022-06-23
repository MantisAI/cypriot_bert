import blogpost.scrape_blogpost as scrape_blogpost
import wordpress.scrape_wordpress as scrape_wordpress
import couplet.scrape_couplet as scrape_couplet
import proverb.scrape_proverb as scrape_proverb

import os
import pandas as pd
import typer

app = typer.Typer()


@app.command()
def extract_google_sheet():

    df = pd.read_csv(
        "https://docs.google.com/spreadsheets/d/e/2PACX-1vTd7ywEIF0KUgxO6j2-GfDPeTEltI5izSAa_yXbI0UmI1_9COoJyJQcl4c0AvpIEy33fFmH-JVIreiy/pub?output=csv"
    )

    output_dir_path = (
        os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "/extracted_text_data/"
    )

    for i in range(len(df)):
        check_script_column = df.loc[i, "Script"]

        if not pd.isnull(check_script_column):
            url = df["Link"][i]

            if check_script_column == "scrape_blogpost":
                scrape_blogpost.url_extract(url, output_dir_path + "blogpost.txt", True)

            elif check_script_column == "scrape_wordpress":
                scrape_wordpress.url_extract(
                    url, output_dir_path + "wordpress.txt", True
                )

            elif check_script_column == "scrape_couplet":
                scrape_couplet.url_extract(url, output_dir_path + "couplet.txt", True)

            elif check_script_column == "scrape_proverb":
                scrape_proverb.url_extract(url, output_dir_path + "proverb.txt", True)


if __name__ == "__main__":
    app()
