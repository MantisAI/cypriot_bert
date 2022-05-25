import typer


def main(data_path: str, model_path: str, epochs: bool = False):
  if formal:
    typer.echo(f"Loading ...")
  else:
    typer.echo(f"It's a better convention to use --epoch. Next time!")
    typer.echo(f"Loading ...")


if __name__ == "__main__":
    typer.train(data_path, model_path, epochs)
