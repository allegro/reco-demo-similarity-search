import numpy as np
import pandas as pd

from bokeh.io import output_notebook
from bokeh.plotting import figure, show
from bokeh.palettes import all_palettes
from bokeh.models import ColumnDataSource, Legend
from typing import List, Dict

MAX_CATEGORIES=20

class BokehPlotter:
    def __init__(self, colormap_entities: List[str], features: List[str]):
        self.tools = ["pan", "wheel_zoom", "reset"]
        self.features = features
        self.tooltips = [(x, "@" + x) for x in self.features] + [
            ("label", "@label"),
            ("(x,y)", "($x, $y)"),
        ]
        self.colormap = self.set_colormap(colormap_entities)

    @staticmethod
    def set_colormap(unique_entities: List[str]) -> Dict[str, str]:
        num_entities = len(unique_entities)
        if 2 < num_entities <= MAX_CATEGORIES:
            colors = all_palettes["Category20"][num_entities]
        elif num_entities <= 256:
            colors = viridis(num_entities)
        else:
            raise (NotImplementedError)
        return dict(zip(unique_entities, colors))

    def prepare_input(
        self, embeddings: np.ndarray, fmap: pd.DataFrame, labels: List[str]
    ) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "x": embeddings[:, 0],
                "y": embeddings[:, 1],
                **dict([(x, fmap[x]) for x in self.features]),
                "label": labels,
                "color": [self.colormap[label] for label in labels],
            }
        )

    def run(
        self,
        data: pd.DataFrame,
        plot_title: str = "Embedding plot",
    ) -> None:
        fig = figure(
            width=1000,
            height=700,
            tooltips=self.tooltips,
            tools=self.tools,
            title=plot_title,
        )
        fig.add_layout(Legend(), "right")
        fig.legend.click_policy = "hide"

        for label in self.colormap.keys():
            split = data[data.label == label]
            source_data = ColumnDataSource(data=split.to_dict("series"))
            fig.scatter(
                "x",
                "y",
                fill_color="color",
                alpha=0.7,
                size=3,
                line_alpha=0,
                line_width=0.01,
                legend_group="label",
                source=source_data,
            )
        output_notebook()
        show(fig)