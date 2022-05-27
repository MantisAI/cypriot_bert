from typer.testing import CliRunner
from url_extract import app

runner = CliRunner()


def test_app():
    result = runner.invoke(
        app, ["antonisgavrielpapas.wixsite.com/antonisgavrielpapa/deigmatisdouleias"]
    )
    assert result.exit_code == 0
