from transformers import BertTokenizer, BertForMaskedLM, TrainingArguments, Trainer
import typer

app = typer.Typer()


def train(data_path, model_path, epochs){
    dataset = data_path.rpartition('/')[2]


    training_args = TrainingArguments(
        output_dir='out',
        batch_size =16,
        epochs=2
    )

    trainer = Trainer(
        model=model_path,
        args=args,
        train_dataset=dataset
    )

    trainer.train()

    trainer.save(model_path)
}

@app.command()
def main(data_path: str, model_path: str, epochs: bool = False):
  if epochs:
    typer.echo(f"Loading ...")
  else:
    typer.echo(f"It's a better convention to use --epoch. Next time! Loading ...")
  
  train(data_path, model_path, epochs)


if __name__ == "__train__":
    app()
    
    
    
