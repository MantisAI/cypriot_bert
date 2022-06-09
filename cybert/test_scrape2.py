from typer.testing import CliRunner
import pytest

from scrape2 import app

runner = CliRunner()


@pytest.fixture
def output_path(tmp_path):
    return tmp_path


def test_app():
    result = runner.invoke(
        app,
        [
            "https://patinios.wordpress.com/2022/04/19/%ce%b1%ce%bd%ce%ac%ce%b4%ce%bf%ce%be%ce%b5%ce%bd-%ce%bc%ce%bf%cf%85/",
            str(output_path),
        ],
    )
    assert result.exit_code == 0
