import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from typing import List

import plotly.graph_objects as go
import plotly.express as px


def rating_changes_graph(
    df: pd.DataFrame,
    label_title: str = '',
    cols: List[str] = ['rating_initial', 'rating_final'],
    graph_path: str = None
) -> None:

    transition = pd.crosstab(
        df[cols[0]],
        df[cols[1]],
        dropna=False
    )

    plt.figure(figsize=(15, 5))

    sns.heatmap(
        transition,
        annot=True,
        fmt='g',
        cmap='Oranges'
    )

    plt.xlabel('Resposta inicial')
    plt.ylabel('Resposta final (após argumento persuasivo)')
    plt.title(f'Mudanças de respostas {label_title}')
    plt.savefig(graph_path, dpi=200, bbox_inches='tight') if graph_path else None
    plt.show()
