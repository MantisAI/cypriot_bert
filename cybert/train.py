from pyexpat import model
from transformers import BertTokenizer, BertForMaskedLM, TrainingArguments, Trainer
import typer

app = typer.Typer()


def train(data_path, model_path, epochs):
    
    tokenizer = BertTokenizer.from_pretrained(model_path)
    model = BertForMaskedLM.from_pretrained(model_path)

    model.to('cuda')

    training_args = TrainingArguments(
        output_dir=f"./out_fold",
        overwrite_output_dir = 'True',
        batch_size = 16,
        num_train_epochs=epochs
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=data_path
    )

    trainer.train(steps=1)

    trainer.save_model("Trained Model")

@app.command()
def main(data_path: str, model_path: str, epochs: bool = False):
  if epochs:
    typer.echo(f"Loading ...")
  else:
    typer.echo(f"It's a better convention to use --epoch. Next time! Loading ...")
  
  train(data_path, model_path, epochs)


if __name__ == "__train__":
    app()
    
    
    
