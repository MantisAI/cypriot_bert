from typer.testing import CliRunner
import pytest

from scrape_default_feed import app

runner = CliRunner()


@pytest.fixture
def output_path(tmp_path):
    return tmp_path


def test_app():
    result = runner.invoke(
        app,
        [
            str(output_path),
        ],
    )
    assert result.exit_code == 0
