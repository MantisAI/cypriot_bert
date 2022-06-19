from typer.testing import CliRunner
import pytest

from scrape_proverb import app

runner = CliRunner()


@pytest.fixture
def output_path(tmp_path):
    return tmp_path


def test_app():
    result = runner.invoke(
        app,
        [
            "https://www.paroimies.gr/paroimies-kypriakes.php?pid=3#vraxos",
            str(output_path),
        ],
    )
    assert result.exit_code == 0
