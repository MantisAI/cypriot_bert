from typer.testing import CliRunner
import pytest

from extract_google_sheet import app

runner = CliRunner()


@pytest.fixture
def output_path(tmp_path):
    return tmp_path


def test_app():
    result = runner.invoke(app)
    assert result.exit_code == 0
