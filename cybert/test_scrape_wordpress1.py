from typer.testing import CliRunner
import pytest

from scrape_wordpress1 import app

runner = CliRunner()


@pytest.fixture
def output_path(tmp_path):
    return tmp_path


def test_app():
    result = runner.invoke(
        app,
        [
            "https://pattixa.wordpress.com/2015/05/03/%ce%b3%ce%b9%ce%b1-%cf%84%ce%b1-%ce%bc%ce%bc%ce%ac%ce%b8%ce%ba%ce%b9%ce%b1-%cf%84%ce%b7%cf%82-%ce%b7%ce%b3%ce%bf%cf%85%ce%bc%ce%ad%ce%bd%ce%b7%cf%82-%ce%bc%ce%ad%cf%81%ce%bf%cf%82-2%ce%bf/",
            str(output_path),
        ],
    )
    assert result.exit_code == 0
