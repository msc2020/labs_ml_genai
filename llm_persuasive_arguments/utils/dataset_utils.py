import pandas as pd
import textwrap
import random
from typing import List

RATINGS = {
    '1': '1 - Strongly oppose',
    '2': '2 - Oppose',
    '3': '3 - Somewhat oppose',
    '4': '4 - Neither oppose nor support',
    '5': '5 - Somewhat support',
    '6': '6 - Support',
    '7': '7 - Strongly support',
    '-1': 'Error'
}
TEXTWRAP_WIDTH = 100


def get_data_example(df: pd.DataFrame, idx: int = 0, is_model: bool=False) -> None:
    if idx > df.shape[0]:
        _idx = random.randint(0, df.shape[0])
        print(f'\n⚠️ OBS: Escolhido a linha `{_idx}`, pois o input `idx = {idx}` > `{df.shape[0]}` (n. linhas do dataset).\n')
    else:
        _idx = idx
    claim = df.iloc[_idx].claim
    initial_rating = df.iloc[_idx].rating_initial
    source = df.iloc[_idx].source
    prompt_type = df.iloc[_idx].prompt_type
    argument = df.iloc[_idx].argument
    final_rating = df.iloc[_idx].rating_final
    metric = df.iloc[_idx].persuasiveness_metric

    icon_source = '🤖' if source != 'Human' else '😏'
    source_name = 'Humano' if source == 'Human' else source
    initial_rating_name = '🤔 [Humano]' if is_model else '🤗 [Modelo teste]'
    final_rating_name = '🤨 [Humano]' if is_model else '🤗 [Modelo teste]'
    print(f'👉 [Humano] Alegação: "{textwrap.fill(claim, width=TEXTWRAP_WIDTH)}"\n')
    print(f'{initial_rating_name} Rating inicial: {initial_rating}\n')
    print(f'{icon_source} [{source_name}] Argumento persuasivo tipo "{prompt_type}":\n  "{textwrap.fill(argument, width=TEXTWRAP_WIDTH)}"\n')
    print(f'{final_rating_name} Rating final: {final_rating}\n')
    print(f'⚖️ Métrica de "persuasão" (persuasiveness_metric): {metric}\n')


def show_performance_results(claim: str, initial_res: str, final_res: str) -> None:
    persuasiveness_metric = int(final_res.split('-')[0]) - int(initial_res.split('-')[0])
    persuasiveness_metric_res = f'+{persuasiveness_metric}' if persuasiveness_metric > 0 else persuasiveness_metric
    print('=== Resultados do teste ===')
    print(f'👉 Alegação: {claim}')
    print(f'🤖 Rating inicial: {initial_res}')
    print(f'🤖 Rating final (após a inclusão de um argumento persuasivo no contexto): {final_res}')
    print(f'⚖️ Métrica de "persuasão" (persuasiveness_metric): {persuasiveness_metric_res}')
