# Copyright (C) 2023-2024 BlueLightAI, Inc. All Rights Reserved.
#
# Any use, distribution, or modification of this software is subject to the
# terms of the BlueLightAI Software License Agreement.

from typing import List, Optional, Tuple
from uuid import UUID

import ipyvuetify as v
import pandas as pd

from cobalt.table.table_utils import is_datetime_col
from cobalt.table.table_view import TableView
from cobalt.widgets import (
    Chip,
)

DEFAULT_NUMERIC_FORMAT = "{:.4g}"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def format_df_for_display(
    df: pd.DataFrame,
    num_rows: Optional[int] = None,
    numeric_format: str = DEFAULT_NUMERIC_FORMAT,
) -> pd.DataFrame:
    if num_rows is not None and len(df) > num_rows:
        df = df.head(num_rows)
    df = df.copy()

    for col in df.columns:
        if is_datetime_col(df[col]):
            df[col] = df[col].dt.strftime(DATETIME_FORMAT)

    for c in df.columns:
        if pd.api.types.is_float_dtype(df[c]):
            df[c] = df[c].apply(numeric_format.format)
    return df


class TableManager(v.Layout):
    def __init__(
        self,
        df: pd.DataFrame,
        workspace_id: Optional[UUID] = None,
        num_rows=None,
        image_columns: Optional[List[str]] = None,
        html_columns: Optional[List[str]] = None,
        show_filter_widget: bool = False,
        image_size: Tuple[int, int] = (80, 80),
        numeric_format: str = DEFAULT_NUMERIC_FORMAT,
        style: Optional[str] = "",
    ):
        super().__init__(column=True)
        if image_columns is None:
            image_columns = []
        if html_columns is None:
            html_columns = []

        self.image_columns = image_columns
        self.html_columns = html_columns
        self.image_size = image_size
        self.workspace_id = workspace_id
        self.style_ = style

        # this DataFrame is a copy of the data with all display-only transformations applied
        displayed_df = format_df_for_display(
            df, num_rows=num_rows, numeric_format=numeric_format
        )

        headers = [
            {"text": col, "value": col, "class": "text-no-wrap"}
            for col in displayed_df.columns
        ]
        items = displayed_df.to_dict(orient="records")

        self.data_table = TableView(
            workspace_id=self.workspace_id,
            headers=headers,
            items=items,
            footer_props={"itemsPerPageOptions": [5, 10, 25]},
            image_columns=self.image_columns,
            html_columns=self.html_columns,
            image_size=self.image_size,
        )
        self.filter_selects_wrapper = None
        if show_filter_widget:
            self.show_filters_view()
        else:
            self.hide_filters()

    def hide_filters(self):
        self.children = [
            self.data_table,
        ]

    def show_filters_view(self):
        if self.filter_selects_wrapper is not None:
            self.children = [
                self.filter_selects_wrapper,
                self.data_table,
            ]
        else:
            self.children = [
                self.data_table,
            ]

    def update_or_create_filters_view(
        self,
        filter_chip_item: List[Chip],
        columns_to_filter_selector: v.Select = None,
        filter_input_value: v.TextField = None,
        filter_autocomplete_value: v.Select = None,
        filter_select_operator: v.Select = None,
        checkbox_wrapper: v.Flex = None,
        clear_filters_button: v.Btn = None,
        apply_button: v.Btn = None,
    ):

        self.filter_selects_wrapper = v.Flex(
            children=[
                *filter_chip_item,
                clear_filters_button,
                v.Flex(
                    children=[
                        columns_to_filter_selector,
                        filter_select_operator,
                        filter_input_value,
                        filter_autocomplete_value,
                        checkbox_wrapper,
                        apply_button,
                    ],
                    style_="gap: 8px",
                    class_="d-flex justify-space-between mt-2",
                ),
            ],
            class_="px-6",
        )
