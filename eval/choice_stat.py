#Copyright (2024) Bytedance Ltd.

import os
import re
import json
from typing import Union


"""
{"image_name": "1890572179.jpg", 
"question": ["What is the main title of the book depicted in the image?", "What is the author's name as depicted in the image?"], 
"choices": [["A.SEX, DRUGS.", "B.EINSTEIN,& ELVES", "C.Universes,and the Quest for Transcendence", "D.Sushi, Psychedelics, Parallel"], ["A.Clifford A. Eisen", "B.Sushi Psychedelic", "C.Psychedelics Parallel", "D.Clifford A. Pickover"]], 
"answer": ["C", "D"], 
"response_gemini": [" B.", " D."]}
"""

def load_jsonl(file_path):
    with open(file_path, 'r') as f:
        data = [json.loads(line) for line in f]
    # print(len(data))
    return data


def parse_response_to_choice(response:str):
    # 从response中提取出选项
    # 从左到右匹配第一个出现的选项大写字母
    response = response.replace('.', ' ')
    response = response.replace(':', ' ')
    response = response.replace(',', ' ')
    response = response.replace('(', ' ')   # 有些答案可能是 Answer(xx,yy) 暂时不能直接取第一个
    response = response.strip()

    # 最简单的匹配
    if response in ['A', 'B', 'C', 'D']:
        return response
    elif len(response.split()) and response.split()[0] in ['A', 'B', 'C', 'D']:
        return response.split()[0]
    elif "the answer is " in response:
        response = response.split('the answer is ')[1].strip()
        if response[0] in ['A', 'B', 'C', 'D']:
            return response[0]
        elif response[0] in ['a', 'b', 'c', 'd']:
            return response[0].upper()
    else:
        response = response.split()
        # 匹配结果中出现的每一个独立选项大写字母
        count = [False]*4
        for item in response:
            if item in ['A', 'B', 'C', 'D']:
                count[ord(item)-ord('A')] = True
        if sum(count) == 1:
            return chr(count.index(True)+ord('A'))
        else:
            # print(' '.join(response))
            return '[invalid]'



def preproc_answer_from_json(answer: Union[str, list, dict, int]):
    if isinstance(answer, str):
        return parse_response_to_choice(answer)
    elif isinstance(answer, list):
        return '[invalid]'
    elif isinstance(answer, dict):
        return answer.get('content', '') or answer.get('English', '') or answer.get('Translation', '')
    elif isinstance(answer, int):
        return chr(ord('A')+answer-1) if 1<= answer <= 4 else '[invalid]'
    else:
        return '[invalid]'


def choice_stat(data, model_name='gemini'):
    stats_dict = {
        "all_data": 0,
        "all_count": 0,
        "true_count": 0,
        "no_reply_count": 0,
    }
    for d in data:
        stats_dict['all_data'] += 1
        assert len(d['answer']) == len(d['response_'+model_name])
        for i in range(len(d['question'])):
            try:
                answer = preproc_answer_from_json(d['answer'][i])
            except Exception:
                print(d['image_name'], d['question'][i], d['choices'][i], d['answer'][i], d['response'+model_name][i])
            if not answer or answer=='[invalid]':
                continue
            stats_dict['all_count'] += 1
            
            response = d['response_'+model_name][i]

            if response == '[NOREPLY]':
                stats_dict['no_reply_count'] += 1
            else:
                response = parse_response_to_choice(response)
                if response == answer:
                    stats_dict['true_count'] += 1
                else:
                    pass
                    # print(f'{d["image_name"]}\t{d["question"][i]}\t{d["choices"][i]}\t{answer}\t{response}')
    return stats_dict


def choice_stat_from_new_benchmark(data, model_name='gemini'):
    model_data = load_jsonl(data)
    # sort by image_name
    model_data.sort(key=lambda x: x['image_name'])

    # reason data
    reason_stats_dict = {
        'model': model_name,
        'count': 0,
        'right': 0,
    }

    bench_choice_path = ""

    bench_choice_data = load_jsonl(bench_choice_path)
    bench_choice_data.sort(key=lambda x: x['image_name'])

    # hash choice data with image_name
    hash_index = [t['image_name'] for t in bench_choice_data]

    for i, d in enumerate(model_data):
        if d['image_name'] not in hash_index:
            continue
        bench_choice_data_i = bench_choice_data[hash_index.index(d['image_name'])]
        bench_choice_data_i = bench_choice_data_i['content']
        for ibcd in bench_choice_data_i:
            question = ibcd['question']['content']
            if question in d['question']:
                reason_stats_dict['count'] += 1
                answer = preproc_answer_from_json(ibcd['response']['answer'])
                response = d['response_'+model_name][d['question'].index(question)]
                if response == '[NOREPLY]':
                    continue
                else:
                    response = parse_response_to_choice(response)
                    if response == answer:
                        reason_stats_dict['right'] += 1

    reason_stats_dict['acc'] = reason_stats_dict['right']/reason_stats_dict['count']
    reason_stats_dict['acc'] = round(reason_stats_dict['acc'], 4)
    

    # return choice_stats_dict, reason_stats_dict
    return reason_stats_dict

    


if __name__ == '__main__':

    data_root = ''

    all_results = []

    for file in os.listdir(data_root):
        model_name = os.path.basename(file).split('.jsonl')[0]
        all_results.append(choice_stat_from_new_benchmark(os.path.join(data_root, file), model_name=model_name))
    
    for r in all_results:
        print(r)
