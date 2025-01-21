
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class DataProcessor:
    def __init__(self, model_path):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16).to("cuda")
    
    def generate_qa_pairs(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
        inputs = {k: v.to(self.model.device) for k, v in inputs.items()}

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_length=150,
                num_return_sequences=5,
                no_repeat_ngram_size=2,
                early_stopping=True
            )

        qa_pairs = []
        for i, output in enumerate(outputs):
            qa_pair = self.tokenizer.decode(output, skip_special_tokens=True)
            question, answer = qa_pair.split('\nA:')
            qa_pairs.append({"question": question.strip(), "answer": answer.strip()})

        return qa_pairs
