#Copyright (2024) Bytedance Ltd.

from PIL import Image
import io
import json
import base64
from typing import List, Dict, Any

# import openai


template = """Below is a content creation task based on the image, paired with two answers.

Question: <question>

Answer #1: <answer1>

Answer #2: <answer2>

###
Please evaluate the answer with the following evaluation criteria:
- Relevance: Whether the text information in the image is effectively used by the answer.
- Faithfulness: Whether the generated answer is faithful to the given image and free of hallucination.
- Template Following: Whether the generated answer accurately meets the content type of the task requirements.
- Creativity: Whether the generated answer is original, unique and engaging.

Then, for each criterion, please reply which one is better with a single number (#1 or #2) for the better one. If they are similar, reply "similar".
For example: "Relevance: #1, Faithfulness: #2, Template Following: similar, Creativity: #1"

Finally, based on the results, please give the final evaluation of the answers with a single word directly.
For example: "final: #1" means answer #1 is better. If they are both well, reply "final: similar".
"""

def filling_instruction(question, answer1, answer2):
    return template.replace('<question>', question).replace('<answer1>', answer1).replace('<answer2>', answer2)





def convert_image_to_bin(image_path):
    with open(image_path, 'rb') as f:
        image_data = f.read()
    return image_data


def load_jsonl(file_path):
    with open(file_path, 'r') as f:
        data = [json.loads(line) for line in f]
    return data



def get_gpt_response(data_dict):
    
    image_path = data_dict['img_path']
    image_bin = convert_image_to_bin(image_path)
    image = Image.open(io.BytesIO(image_bin))
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode()
    
    if len(data_dict['question']):
        data_dict['judge_gsb'] = []

    instruction = filling_instruction(data_dict['question'], data_dict['answer'], data_dict['response'])
    # print(instruction)

    # call gpt or other models, and get response
    # data_dict["response"] = ...
    raise NotImplementedError





if __name__ == "__main__":
    # load data
    model_responsed_data = ""

    sample_data = load_jsonl(model_responsed_data)
    print(len(sample_data))
    
    for i, data in enumerate(sample_data):
        get_gpt_response(data)
