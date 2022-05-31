from typer.testing import CliRunner
import pytest

from url_extract import app

runner = CliRunner()


@pytest.fixture
def output_path(tmp_path):
    return tmp_path


def test_app():
    result = runner.invoke(
        app,
        [
            "antonisgavrielpapas.wixsite.com/antonisgavrielpapa/deigmatisdouleias",
            str(output_path),
        ],
    )
    assert result.exit_code == 0
