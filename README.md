# MCTBench

MCTBench: Multimodal Cognition towards Text-Rich Visual Scenes Benchmark


![head_image](./.asset/head.png)

We introduce a multimodal benchmark towards text-rich visual scenes designed to evaluate the cognitive capabilities of MLLMs via conducting visual reasoning and content-creation tasks. To mitigate potential evaluation bias from the varying distributions of datasets,  MTV incorporates several perception tasks (e.g., scene text recognition) to provide a consistent comparison of both the cognitive and perceptual capabilities of MLLMs.


## Data Distribition

![data_dist](./.asset/wordcount.png)
MTV comprises 5.3k text-rich images and 8.5k rigorously annotated question-answer pairs divided into three types of tasks: perception, reasoning and content-creation.

<!-- ## Leaderboard -->


## Leaderboard

| Model            | Params | Perception | Reasoning |Content-Creation  | Multiple-Choice | Cognition (R+C) | All |
|------------------|--------|------------|-----------|-----------|-----------|-----------|-----------|
| GPT-4V           | -      | 83.58      | 74.21     | 87.35     | 78.90     | 83.12     | 81.71     |
| Mini-Gemini      | 34B    | 83.83      | 73.33     | 86.76     | 78.58     | 82.67     | 81.31     |
| LLaVA-NeXT       | 34B    | 83.87      | 71.64     | 85.30     | 77.76     | 81.53     | 80.27     |
| InternLM-XComposer2 | 7B  | 78.05      | 72.10     | 74.45     | 75.08     | 74.76     | 74.87     |
| LLaVA-1.5        | 13B    | 78.09      | 72.56     | 66.47     | 75.33     | 70.90     | 72.37     |
| Qwen-VL-chat     | 7B     | 77.98      | 70.68     | 67.53     | 74.33     | 70.93     | 72.06     |
| Honeybee         | 7B     | 72.60      | 67.22     | 73.64     | 69.91     | 71.78     | 71.15     |
| SPHINX-v2        | 13B    | 78.02      | 71.94     | 62.30     | 74.98     | 68.64     | 70.75     |
| Monkey           | 7B     | 79.22      | 72.64     | 59.56     | 75.93     | 67.75     | 70.47     |
| Sharegpt4V       | 13B    | 74.54      | 69.49     | 66.19     | 72.02     | 69.10     | 70.07     |
| CogVLM           | 17B    | 71.40      | 69.52     | 65.61     | 70.46     | 68.04     | 68.84     |
| mPLUG-DocOwl     | 10B    | 75.05      | 70.06     | 60.87     | 72.56     | 66.71     | 68.66     |
| Gemini-Pro       | -      | 78.79      | 70.18     | 56.78     | 74.49     | 65.63     | 68.58     |
| Deepseek-VL      | 7B     | 76.74      | 68.79     | 57.25     | 72.77     | 65.01     | 67.59     |
| Yi-VL            | 6B     | 77.25      | 72.33     | 41.45     | 74.79     | 58.12     | 63.68     |
| CogAgent         | 34B    | 58.56      | 56.46     | 56.86     | 57.51     | 57.19     | 57.29     |
| TextMonkey       | 7B     | 71.80      | 69.45     | 22.81     | 70.63     | 46.72     | 54.69     |
| Otter            | 7B     | 58.12      | 54.42     | 31.70     | 56.27     | 43.99     | 48.08     |


## Download

[RawData (Google Drive)](https://drive.google.com/drive/folders/12-klr5vjGBzwTd10YLKIpzw0X5elDPSG?usp=drive_link)

<!-- 
## Direct Use
The data is designed to evaluate and enhance the multilingual textual vqa capabilities of multimodal models in the hope of facilitating the understanding of multilingual images, enabling AI to reach more people in the world.

## Out-of-Scope Use
Academic use only, not supported for commercial use -->

## Dataset Structure

### Data Instances

```python
{
        "id": 0, 
        "img": "014312224X.jpg", 
        "category": "perception", 
        "question": "What is the title of the book in the image?", 
        "choice": ["A. Your Medical Guide", "B. Your Medical Path", "C. Your Medical Mind", "D. Your Medical Journey"], 
        "answer": "C"
}
{
        "id": 2734, 
        "img": "19974.png", 
        "category": "reasoning", 
        "question": "Why does the slide emphasize the role of creation in an advertising medium's visibility?", 
        "choice": ["A. Because creation determines the medium's quality", "B. Because the medium is created by a person", "C. Because creation is the initial step in the advertising process", "D. Because creation has the highest share in advertising"], 
        "answer": "D"
}
{
        "id": 5336,
        "img": "175153.png", 
        "category": "content creation", 
        "question": "Create a marketing statement for the VICHY DERMABLEND product based on the image.", 
        "choice": [], 
        "answer": "Discover your true beauty with VICHY DERMABLEND, the skincare solution that effortlessly evens out your skin tone, letting your natural glow shine through."
}
```


### Data Fields

The dataset comprises the following fields:
- `id`: a unique number for each question-answer pair
- `img`: a path to image
- `category`: a string to identify the task type of question-answer pairs
- `question`: a string containing the question to be answered
- `choice`: a list of strings containing the possible answers to the question (not supplied for creation task)
- `answer`: a string containing the answer to the corresponding question



## Disclaimer

Your access to and use of this dataset are at your own risk. We do not guarantee the accuracy of this dataset. The dataset is provided “as is” and we make no warranty or representation to you with respect to it and we expressly disclaim, and hereby expressly waive, all warranties, express, implied, statutory or otherwise. This includes, without limitation, warranties of quality, performance, merchantability or fitness for a particular purpose, non-infringement, absence of latent or other defects, accuracy, or the presence or absence of errors, whether or not known or discoverable. In no event will we be liable to you on any legal theory (including, without limitation, negligence) or otherwise for any direct, special, indirect, incidental, consequential, punitive, exemplary, or other losses, costs, expenses, or damages arising out of this public license or use of the licensed material. The disclaimer of warranties and limitation of liability provided above shall be interpreted in a manner that, to the extent possible, most closely approximates an absolute disclaimer and waiver of all liability.

## License
[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)
