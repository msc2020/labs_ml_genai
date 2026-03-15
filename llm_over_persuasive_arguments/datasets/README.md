---
license: cc-by-nc-sa-4.0
language:
- en
size_categories:
- 1K<n<10K
---
# Dataset Card for Persuasion Dataset

## Dataset Summary
The Persuasion Dataset contains claims and corresponding human-written and model-generated arguments, along with persuasiveness scores. 
This dataset was created for research on measuring the persuasiveness of language models, as described in this blog post: [Measuring the Persuasiveness of Language Models](https://www.anthropic.com/news/measuring-model-persuasiveness).

## Dataset Description

The dataset consists of a CSV file with the following columns:
- **worker\_id**: Id of the participant who annotated their initial and final stance on the claim.
- **claim**: The claim for which the argument was generated.
- **argument**: The generated argument, either by a human or a language model.
- **source**: The source of the argument (model name or "Human").
- **prompt\_type**: The prompt type used to generate the argument.
- **rating\_initial**: The participant's initial rating of the claim.
- **rating\_final**: The participant's final rating of the claim after reading the argument.

## Usage
```python
from datasets import load_dataset
# Loading the data
dataset = load_dataset("Anthropic/persuasion")
```
## Contact
For questions, you can email esin at anthropic dot com

## Citation
If you would like to cite our work or data, you may use the following bibtex citation:

```
@online{durmus2024persuasion,
author = {Esin Durmus and Liane Lovitt and Alex Tamkin and Stuart Ritchie and Jack Clark and Deep Ganguli},
title = {Measuring the Persuasiveness of Language Models},
date = {2024-04-09},
year = {2024},
url = {https://www.anthropic.com/news/measuring-model-persuasiveness},
}

```
