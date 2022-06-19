from typer.testing import CliRunner
import pytest

from scrape_blogpost import app

runner = CliRunner()


@pytest.fixture
def output_path(tmp_path):
    return tmp_path


def test_app():
    result = runner.invoke(
        app,
        [
            "http://acerasanthropophorum.blogspot.com/2007/01/blog-post.html",
            str(output_path),
        ],
    )
    assert result.exit_code == 0
