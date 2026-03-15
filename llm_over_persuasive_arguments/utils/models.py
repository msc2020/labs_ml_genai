import os
os.environ['TRANSFORMERS_VERBOSITY'] = 'error'

from utils.dataset_utils import RATINGS, GRADING_PROMPT

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoConfig


MODEL_PATH = r'/home/msc/Downloads/hf_models'


class HFLlmModel:
    '''Ajuda a usar modelos disponibilizados na Hugging Face.'''

    def __init__(
        self,
        model_name: str = 'Qwen/Qwen3-0.6B',
        device: str = 'cuda',
        system_prompt: str = GRADING_PROMPT,
        max_new_tokens: int = 10,
        temperature: float = 0.0
    ):
        self.model_name = model_name
        self.device = device
        self.system_prompt = system_prompt
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature

        self.tokenizer = AutoTokenizer.from_pretrained(f'{MODEL_PATH}/{model_name}')

        self.model = AutoModelForCausalLM.from_pretrained(
            pretrained_model_name_or_path=f'{MODEL_PATH}/{model_name}',
            tie_word_embeddings=None,
            device_map='cuda',
            dtype=torch.float16  # torch.float32
        )

    def hf_llm_ans(
        self,
        claim: str,
        user_prompt: str,
        argument: str = None,
        verbose: bool = False,
    ) -> str:

        try:
            if argument:
                messages = [
                    {
                        'role': 'system',
                        'content': f'{self.system_prompt}. Add this argument to your context: {argument}'
                    },
                    {
                        'role': 'user',
                        'content': user_prompt.format(claim=claim)
                    }
                ]
            else:
                messages = [
                    {
                        'role': 'system',
                        'content': f'{self.system_prompt}'
                    },
                    {
                        'role': 'user',
                        'content': user_prompt.format(claim=claim)
                    }
                ]

            text_prompt = self.tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True,
                enable_thinking=False
            )

            model_inputs = self.tokenizer(
                [text_prompt],
                return_tensors='pt'
            ).to(self.model.device)

            if not self.temperature:
                generated_ids = self.model.generate(
                    **model_inputs,
                    max_new_tokens=self.max_new_tokens,
                    do_sample=False
                )
            else:
                generated_ids = self.model.generate(
                    **model_inputs,
                    max_new_tokens=self.max_new_tokens,
                    do_sample=True,
                    temperature=self.temperature,
                )
            output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist()

            rating = self.tokenizer.decode(
                output_ids,
                skip_special_tokens=True
            ).strip('\n')

            if verbose:
                print(f'Alegação: {claim}')
                if argument:
                    print(f'Rating (após saber do argumento): {rating}')
                else:
                    print(f'Rating: {rating}')

            return RATINGS[rating]

        except Exception as e:
            print(e)
            return None
