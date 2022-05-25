from typer.testing import CliRunner

from .train import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["imdb", "bert-base-uncased", "--5"])
    assert result.exit_code == 0
    assert "Loading ..." in result.stdout
    assert "It's a better convention to use --epoch. Next time!" in result.stdout