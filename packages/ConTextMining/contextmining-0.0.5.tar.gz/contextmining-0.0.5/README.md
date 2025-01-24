`ConTextMining` is a package generate interpretable topics labels from the keywords of topic models (e.g, `LDA`, `BERTopic`) through few-shot in-context learning. 


[![pypi package](https://img.shields.io/badge/pypi_package-v0.0.5-brightgreen)](https://pypi.org/project/ConTextMining/) [![GitHub Source Code](https://img.shields.io/badge/github_source_code-source_code?logo=github&color=green)](https://github.com/cja5553/ConTextMining) 


## Requirements  
### Required packages
The following packages are required for `ConTextMining`. 

- `torch` (to learn how to install, please refer to [pytorch.org/](https://pytorch.org/))
- `transformers`
- `tokenizers`
- `huggingface-hub`
- `accelerate`

To install these packages, you can do the following:

```bash
pip install torch transformers tokenizers huggingface-hub flash_attn accelerate
```

### GPU requirements
You require at least one GPU to use `ConTextMining`.  
VRAM requirements depend on factors like number of keywords or topics used to topic labels you wish to generate.  
However, at least 8GB of VRAM is recommended

### huggingface access token
You will need a huggingface access token. To obtain one:  
1. you'd first need to create a [huggingface](https://huggingface.co) account if you do not have one. 
2. Create and store a new access token. To learn more, please refer to [huggingface.co/docs/hub/en/security-tokens](https://huggingface.co/docs/hub/en/security-tokens).  
3. Note: Some pre-trained large language models (LLMs) may require permissions. For more information, please refer to [huggingface.co/docs/hub/en/models-gated](https://huggingface.co/docs/hub/en/models-gated).  



## Installation
To install in python, simply do the following: 
```bash
pip install ConTextMining
```

## Quick Start
Here we provide a quick example on how you can execute `ConTextMining` to conveniently generate interpretable topics labels from the keywords of topic models. 
```python
from ConTextMining import get_topic_labels

# specify your huggingface access token. To learn how to obtain one, refer to huggingface.co/docs/hub/en/security-tokens
hf_access_token="<your huggingface access token>" 

# specify the huggingface model id. Choose between "microsoft/Phi-3-mini-4k-instruct", "meta-llama/Meta-Llama-3.1-8B-Instruct" or "google/gemma-2-2b-it"
model_id="meta-llama/Meta-Llama-3.1-8B-Instruct"

# specify the keywords for the few-shot learning examples
keywords_examples = [
    "olympic, year, said, games, team",
    "mr, bush, president, white, house",
    "sadi, report, evidence, findings, defense",
    "french, union, germany, workers, paris",
    "japanese, year, tokyo, matsui, said"
]

# specify the labels CORRESPONDING TO THE INDEX of the keywords of 'keyword_examples' above. 
labels_examples = [
    "sports",
    "politics",
    "research",
    "france",
    "japan"
]

# specify your topic modeling keywords of wish to generate coherently topic labels. 
topic_modeling_keywords ='''Topic 1: [amazing, really, place, phenomenon, pleasant],
Topic 2: [loud, awful, sunday, like, slow],
Topic 3: [spinach, carrots, green, salad, dressing],
Topic 4: [mango, strawberry, vanilla, banana, peanut],
Topic 5: [fish, roll, salmon, fresh, good]'''


print(get_topic_labels(topic_modeling_keywords=topic_modeling_keywords, keywords_examples=keywords_examples, labels_examples=labels_examples, model_id=model_id, access_token=hf_access_token))
```
You will now get the interpretable topic model labels for all 5 topics! 

## Documentation

```python
ConTextMining.get_topic_labels(*, topic_modeling_keywords, labels_examples,keywords_examples, model_id, access_token)
```

- `topic_modeling_keywords` *(str, required)*: keywords stemming from the outputs of topic models (keywords representing each cluster) for `ConTextMining` to label.  
- `keywords_examples` *(list, required)*: list-of-string(s) containing topic modeling keywords which serves as training examples for few-shot learning.  
- `labels_examples` *(list, required)*: list-of-string(s) containing the labels CORRESPONDING TO THE INDEX of the keywords of `keyword_examples` above.   
- `model_id` *(str, required)*: huggingface model_id of choice. For now, its a choice between "microsoft/Phi-3-mini-4k-instruct", "meta-llama/Meta-Llama-3.1-8B-Instruct", or "google/gemma-2-2b-it". Defaults to "google/gemma-2-2b-it".  
- `access_token` *(str, required)*: Huggingface access token. To learn how to obtain one, refer to [huggingface.co/docs/hub/en/security-tokens](https://huggingface.co/docs/hub/en/security-tokens). Defaults to `None`


## Citation
C Alba "ConText Mining: Complementing topic models with few-shot in-context learning to generate interpretable topics" Forthcoming at IEEE Symposium Series on Computational Intelligence. 

## Questions?

Contact me at [alba@wustl.edu](mailto:alba@wustl.edu)
