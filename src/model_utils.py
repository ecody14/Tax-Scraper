import json
from transformers import AutoModelForCausalLM, AutoTokenizer

class ModelUtils:
    @staticmethod
    def save_to_jsonl(data, output_path):
        with open(output_path, "w") as f:
            for item in data:
                f.write(json.dumps(item) + "\n")

    @staticmethod
    def download_model(model_name):
        AutoModelForCausalLM.from_pretrained(model_name)
        AutoTokenizer.from_pretrained(model_name)
