from typer.testing import CliRunner
import pytest

from scrape_couplet import app

runner = CliRunner()


@pytest.fixture
def output_path(tmp_path):
    return tmp_path


def test_app():
    result = runner.invoke(
        app,
        [
            "https://www.domnasamiou.gr/?i=portal.el.songs&id=1002",
            str(output_path),
        ],
    )
    assert result.exit_code == 0
