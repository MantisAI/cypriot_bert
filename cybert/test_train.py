from typer.testing import CliRunner
import pytest

from train import app

runner = CliRunner()


@pytest.fixture
def model_path(tmp_path):
    return tmp_path


def test_app(model_path):
    result = runner.invoke(
        app,
        [
            "imdb",
            str(model_path),
            "prajjwal1/bert-tiny",
            "--max-steps",
            "1",
            "--sample-size",
            "16",
        ],
    )
    assert result.exit_code == 0
