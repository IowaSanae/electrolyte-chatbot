from transformers import pipeline
import os


model_path = os.path.join(os.path.dirname(__file__), "model_save")
model_train = pipeline(task="text-generation", model=model_path, tokenizer=model_path)
