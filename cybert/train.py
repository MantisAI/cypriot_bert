from transformers import (
    AutoTokenizer,
    AutoModelForMaskedLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling,
)
from datasets import load_dataset
import typer

app = typer.Typer()


@app.command()
def train(
    data_path,
    model_path,
    pretrained_model,
    epochs: int = 5,
    batch_size: int = 16,
    max_steps: int = -1,
    sample_size: int = None,
):
    tokenizer = AutoTokenizer.from_pretrained(pretrained_model)
    model = AutoModelForMaskedLM.from_pretrained(pretrained_model)

    dataset = load_dataset(data_path)
    if sample_size:
        dataset = dataset["train"].select(range(sample_size))

    dataset = dataset.map(
        lambda x: tokenizer(
            x["text"], truncation=True, padding="max_length", max_length=512
        ),
        batched=True,
        num_proc=4,
        remove_columns=dataset.column_names,
    )

    data_collator = DataCollatorForLanguageModeling(tokenizer, mlm_probability=0.15)

    training_args = TrainingArguments(
        output_dir=model_path,
        per_device_train_batch_size=batch_size,
        num_train_epochs=epochs,
        max_steps=max_steps,
        optim="adamw_torch",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        data_collator=data_collator,
    )

    trainer.train()

    trainer.save_model(model_path)


if __name__ == "__main__":
    app()
