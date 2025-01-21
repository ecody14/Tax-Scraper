import json
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

class ModelUtils:
    @staticmethod
    def save_to_jsonl(data, output_path):
        with open(output_path, "w") as f:
            for item in data:
                f.write(json.dumps(item) + "\n")

    @staticmethod
    def download_model(model_name):
        quantization_config = BitsAndBytesConfig(load_in_4bit=True)
        AutoModelForCausalLM.from_pretrained(model_name, quantization_config=quantization_config, device_map="auto")
        AutoTokenizer.from_pretrained(model_name)
