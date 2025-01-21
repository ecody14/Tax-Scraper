
import json

class ModelUtils:
    @staticmethod
    def save_to_jsonl(data, output_path):
        with open(output_path, "w") as f:
            for item in data:
                f.write(json.dumps(item) + "\n")
