# Copyright (C) 2023-2024 BlueLightAI, Inc. All Rights Reserved.
#
# Any use, distribution, or modification of this software is subject to the
# terms of the BlueLightAI Software License Agreement.

from threading import Timer
from typing import Dict, List, Optional, Tuple
from uuid import UUID

import ipyvuetify as v
import ipywidgets as w
import pandas as pd

from cobalt.cobalt_types import ColumnDataType
from cobalt.config import debug_logger, handle_cb_exceptions
from cobalt.groups.groups_ui import GroupSaveModal
from cobalt.schema.dataset import DatasetBase
from cobalt.schema.metadata import TextDataType
from cobalt.state import DataFilter, State, apply_filters_df
from cobalt.table.filter_chip import FilterChip
from cobalt.table.table_manager import TableManager
from cobalt.ui_utils import with_tooltip
from cobalt.widgets import (
    Autocomplete,
    Button,
    Checkbox,
    SearchableSelect,
    Select,
)

DEFAULT_NUMERIC_FORMAT = "{:.4g}"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
NUMBER_OF_DF_ROWS_TO_DISPLAY = 2000
CONTAINS = "contains"
IS = "is"
EQUALS = "eq"
default_operator_select_items = [
    {
        "text": "contains",
        "value": "contains",
    },
]
MANUAL_TEXT_SELECT_ITEMS = [
    {
        "header": "CATEGORICAL",
    },
    {
        "text": "is",
        "value": "is",
    },
]
MANUAL_NUMERIC_SELECT_ITEMS = [
    {
        "header": "CATEGORICAL",
    },
    {
        "text": "is",
        "value": "eq",
    },
]
NUMERICAL_OPERATOR_SELECT_ITEMS = [
    {
        "header": "NUMERICAL",
    },
    {
        "text": "equals",
        "value": "eq",
    },
    {
        "text": "more than",
        "value": "gt",
    },
    {
        "text": "less than",
        "value": "lt",
    },
    {
        "text": "more than or equal to",
        "value": "gte",
    },
    {
        "text": "less than or equal to",
        "value": "lte",
    },
]
CATEGORICAL_TEXT_OPERATOR_SELECT_ITEMS = [
    {
        "header": "CATEGORICAL",
    },
    {
        "text": "is",
        "value": "is",
    },
    {
        "text": "contains",
        "value": "contains",
    },
]

OPERATOR_MAP = {
    "is_case_sensitive_on": IS,
    "is_case_sensitive_off": CONTAINS,
    "contains_sensitive_on": CONTAINS,
    "contains_sensitive_off": CONTAINS,
    "eq": "=",
    "gt": ">",
    "lt": "<",
    "gte": ">=",
    "lte": "<=",
}


def get_text_operator(op):
    return OPERATOR_MAP.get(op)


class TableSelector(w.VBox):
    def __init__(
        self,
        source_data: DatasetBase,
        state: State,
        workspace_id: Optional[UUID] = None,
        columns: Optional[List[str]] = None,
        image_columns: Optional[List[dict]] = None,
        html_columns: Optional[List[str]] = None,
        columns_to_filter: Optional[List[str]] = None,
        filter_criteria: Optional[Dict] = None,
        image_size: Tuple[int, int] = (80, 80),
        max_rows_to_display: Optional[int] = None,
        run_server: bool = True,
    ):
        super().__init__()
        self.source_data = source_data
        self.state = state
        self.workspace_id = workspace_id
        self.columns = columns
        self.image_columns = image_columns or []
        self.html_columns = html_columns or []
        self.image_size = image_size
        self.columns_to_filter = columns_to_filter
        self.filter_criteria = filter_criteria or {}
        self.show_filters = False
        self.max_rows_to_display = max_rows_to_display
        self.run_server = run_server
        self._debounce_timer = None

        self.df = self._get_data_from_source()

        self._initialize_widgets()
        self._setup_widget_list()
        self._check_and_open_filters()

    def _get_data_from_source(self) -> pd.DataFrame:
        data = self.source_data
        table_df = data.create_rich_media_table(run_server=self.run_server)
        filtered_df = self.filter_df(table_df)
        return filtered_df

    def _initialize_widgets(self):
        self.columns_to_filter_selector = self._generate_columns_to_filter_selector()
        self.filter_input_value = self._create_filter_select_value()
        self.filter_autocomplete_value = self._create_filter_autocomplete_value()
        self.filter_select_operator = self._create_filter_select_operator()
        self.match_case_checkbox = self._create_match_case_checkbox()
        self.match_entire_cell_checkbox = self._create_match_entire_cell_checkbox()
        self.checkbox_wrapper = self._create_checkbox_wrapper()
        self.clear_filters_button = self._create_clear_filters_button()
        self.apply_button = self._create_apply_button()
        self.filter_chip_item = self._create_filter_chip_item()
        self.table_view = self._generate_table(self.workspace_id)
        self.select_all_text = "Select All"
        self._init_column_selector()
        self._init_filtering()
        self._init_save_group_modal()
        self.update_filter_view()

    def _init_save_group_modal(self):
        filtered_indices = self.state.dataset.df.index.get_indexer(self.df.index)
        filtered_data_points = self.state.dataset.subset(filtered_indices)
        self.group_save_modal = GroupSaveModal(
            state=self.state, data_points=filtered_data_points
        )
        self.group_save_modal_with_tooltip = with_tooltip(
            self.group_save_modal, "Create Group from Table Data"
        )

    def _init_column_selector(self):
        self.column_selector = Autocomplete(
            items=[self.select_all_text, *self.df.columns],
            v_model=self.columns,
            multiple=True,
            clearable=True,
            placeholder="All columns displayed by default. Adjust as needed.",
        )
        self.column_selector.on_event("change", self._on_change_with_debounce)

    def _init_filtering(self):
        self.filter_icon_button = Button(
            icon=True,
            children=[v.Icon(children=["mdi mdi-filter-variant"], color="primary")],
        )

        self.filters_counter = v.Flex(
            children="",
            style_="position: absolute; right: 2px; bottom: 0px;",
        )

        self.filter_button_container = v.Flex(
            style_="max-width: 36px; height: 36px; position: relative;",
            class_="mx-4",
            children=[self.filter_icon_button, v.Flex(children=[self.filters_counter])],
        )
        self.filter_icon_button.on_event("click", self.switch_filters_layout)

        self.filter_button_container_with_tooltip = with_tooltip(
            self.filter_button_container, "Show/Hide Filters"
        )

    def switch_filters_layout(self, *_):
        self.show_filters = not self.show_filters
        if self.show_filters:
            self.show_filters_action()
        else:
            self.table_view.hide_filters()

    def show_filters_action(self):
        self.enable_filter_fields()
        if self.table_view.filter_selects_wrapper is None:
            self.update_filter_view()
        self.table_view.show_filters_view()

    def _setup_widget_list(self):
        self.selector_controls = v.Html(
            tag="div",
            children=[
                self.column_selector,
                self.filter_button_container_with_tooltip,
                self.group_save_modal_with_tooltip,
            ],
            class_="d-flex align-center justify-center px-6",
        )
        self.children = [self.selector_controls, self.table_view]

    def _check_and_open_filters(self):
        if len(self.state.data_filters.filters) > 0:
            self.filters_counter.children = str(len(self.state.data_filters.filters))
            self.switch_filters_layout()

    def _generate_table(self, workspace_id: Optional[UUID] = None):
        df = self.df[self.columns] if self.columns else self.df
        return TableManager(
            df,
            workspace_id=workspace_id,
            num_rows=self.max_rows_to_display,
            image_columns=self.image_columns,
            html_columns=self.html_columns,
            show_filter_widget=self.show_filters,
            image_size=self.image_size,
        )

    def _generate_columns_to_filter_selector(self):
        available_filter_columns = [
            c
            for c in self.df.columns
            if not pd.api.types.is_datetime64_any_dtype(self.df[c])
        ]

        columns_to_filter = SearchableSelect(
            items=available_filter_columns,
            label="Select column to filter",
            attach=True,
            style_="max-width: 210px",
            hide_details=False,
            multiple=False,
            v_model=self.columns_to_filter,
        )

        columns_to_filter.on_event("change", self.on_column_select)

        return columns_to_filter

    def hide_checkbox_wrapper(self, *_):
        self.checkbox_wrapper.class_ = "d-none"

    def show_checkbox_wrapper(self, *_):
        self.checkbox_wrapper.class_ = "d-flex justify-space-around"

    def show_input_value(self, *_):
        self.filter_autocomplete_value.class_ = "d-none"
        self.filter_input_value.class_ = "d-block my-2"

    def show_autocomplete_value(self, *_):
        self.filter_autocomplete_value.class_ = "d-block my-2"
        self.filter_input_value.class_ = "d-none"

    def clear_fields_except_column(self, *_):
        self.clear_field_errors()
        self.filter_input_value.v_model = ""
        self.filter_autocomplete_value.v_model = None
        self.match_case_checkbox.v_model = None
        self.match_entire_cell_checkbox.v_model = None
        self.filter_select_operator.v_model = None
        self.hide_checkbox_wrapper()
        self.show_input_value()

    @handle_cb_exceptions
    def on_column_select(self, widget, event, column_name):
        available_filter_columns = [
            c
            for c in self.df.columns
            if not (pd.api.types.is_datetime64_any_dtype(self.df[c]))
        ]

        if column_name not in available_filter_columns:
            self.columns_to_filter_selector.error_messages = [
                f"Selected column '{column_name}' is not valid."
            ]
            return

        self.columns_to_filter_selector.error_messages = []

        self.clear_fields_except_column()
        columns_metadata = self.state.dataset.metadata.data_types

        column_type = columns_metadata.get(column_name).col_type
        column_text_type = columns_metadata.get(column_name).text_type
        is_categorical = columns_metadata.get(column_name).is_categorical
        is_manual = columns_metadata.get(column_name).explicit_categorical

        column_values = columns_metadata.get(column_name).cat_values

        if is_categorical and column_text_type != TextDataType.long_text:
            self.show_autocomplete_value()
            self.filter_autocomplete_value.items = column_values

            if is_manual:
                if column_type == ColumnDataType.text:
                    self.filter_select_operator.items = MANUAL_TEXT_SELECT_ITEMS
                    self.filter_select_operator.v_model = IS
                if column_type == ColumnDataType.numerical:
                    self.filter_select_operator.items = MANUAL_NUMERIC_SELECT_ITEMS
                    self.filter_select_operator.v_model = EQUALS

            elif column_type == ColumnDataType.text:

                self.filter_select_operator.items = (
                    CATEGORICAL_TEXT_OPERATOR_SELECT_ITEMS
                )
                self.filter_select_operator.v_model = IS
            else:

                # condition for the categorical numerical columns
                self.filter_select_operator.items = NUMERICAL_OPERATOR_SELECT_ITEMS
        else:
            # condition for all non categorical columns
            self.show_input_value()
            if column_type == ColumnDataType.text:

                self.show_checkbox_wrapper()
                self.filter_select_operator.items = default_operator_select_items
                self.filter_select_operator.v_model = CONTAINS
            else:

                # condition for the numerical columns
                self.hide_checkbox_wrapper()
                self.filter_select_operator.items = NUMERICAL_OPERATOR_SELECT_ITEMS

        self.update_filter_view()

    @staticmethod
    def _create_filter_select_value(*_):
        def on_input_change(*args):
            filter_value.error_messages = []

        filter_value = v.TextField(
            label="Value",
            v_model="",
            class_="my-2",
            outlined=True,
            dense=True,
        )

        filter_value.on_event("input", on_input_change)

        return filter_value

    @staticmethod
    def _create_filter_autocomplete_value(*_):
        def on_value_select(widget, event, data):
            widget.error_messages = []

        autocomplete_value = Autocomplete(
            items=[],
            v_model=None,
            clearable=True,
            hide_details=False,
            deletable_chips=True,
            placeholder="Value",
            class_="d-none",
        )

        autocomplete_value.on_event("change", on_value_select)

        return autocomplete_value

    def _create_filter_select_operator(self, *_):

        filter_select_operator = Select(
            label="Operator",
            attach=True,
            items=default_operator_select_items,
            hide_details=False,
            v_model=None,
            multiple=False,
            style_="max-width: 140px",
        )

        filter_select_operator.on_event("change", self.on_operator_select)

        return filter_select_operator

    @handle_cb_exceptions
    def on_operator_select(self, widget, event, operator):
        widget.error_messages = []
        if self.columns_to_filter_selector.v_model:
            columns_metadata = self.state.dataset.metadata.data_types
            column_type = columns_metadata.get(
                self.columns_to_filter_selector.v_model
            ).col_type

            is_categorical = columns_metadata.get(
                self.columns_to_filter_selector.v_model
            ).is_categorical

            if is_categorical and column_type == ColumnDataType.text:
                if operator == CONTAINS:
                    self.show_input_value()
                    self.show_checkbox_wrapper()
                else:
                    self.show_autocomplete_value()
                    self.hide_checkbox_wrapper()
                self.update_filter_view()

    def _create_match_case_checkbox(self, *_):
        return Checkbox(label="Match Case", v_model=None, class_="mt-3")

    def _create_match_entire_cell_checkbox(self, *_):
        return Checkbox(
            label="Match entire cell",
            v_model=None,
            class_="mt-3",
        )

    def _create_checkbox_wrapper(self, *_):
        return v.Flex(
            children=[self.match_case_checkbox, self.match_entire_cell_checkbox],
            class_="d-none",
        )

    def _create_filter_chip_item(self, *_):
        filter_chip_items = []
        for filter_item in self.state.data_filters.filters:
            data_filter = DataFilter(
                column=filter_item.column, op=filter_item.op, value=filter_item.value
            )

            chip_text = (
                f"{data_filter.column.name} "
                f"{get_text_operator(data_filter.op)} "
                f"{data_filter.value}"
            )

            def on_click_callback(filter_item=data_filter):
                self._handle_chip_click(filter_item)

            chip_item = FilterChip(
                chip_text=chip_text,
                on_click=on_click_callback,
            )
            filter_chip_items.append(chip_item)
        return filter_chip_items

    def _handle_chip_click(self, data_filter: DataFilter):
        self.state.remove_filter(data_filter)
        remaining_filters = len(self.state.data_filters.filters)

        self.df = self._get_data_from_source()
        if remaining_filters == 0:
            self.clear_filters_button.class_ = "d-none"
            self.filters_counter.children = ""
        else:
            self.filters_counter.children = str(remaining_filters)

        self.update_chips()
        self.update_table(None, None, None)
        self.enable_filter_fields()

    def _create_clear_filters_button(self, *_):
        clear_filters_button = Button(
            tile=True,
            text=True,
            children=[
                v.Icon(
                    children=["mdi-close"],
                ),
                "clear all",
            ],
            class_="my-2 d-none",
        )

        clear_filters_button.on_event("click", self.clear_all_filters)

        return clear_filters_button

    def disable_filter_fields(self, *_):
        self.filter_select_operator.disabled = True
        self.filter_input_value.disabled = True
        self.filter_autocomplete_value.disabled = True
        self.columns_to_filter_selector.disabled = True
        self.match_case_checkbox.disabled = True
        self.match_entire_cell_checkbox.disabled = True
        self.apply_button.disabled = True
        self.clear_filters_button.disabled = True

    def enable_filter_fields(self, *_):
        self.filter_select_operator.disabled = False
        self.filter_input_value.disabled = False
        self.filter_autocomplete_value.disabled = False
        self.columns_to_filter_selector.disabled = False
        self.match_case_checkbox.disabled = False
        self.match_entire_cell_checkbox.disabled = False
        self.apply_button.disabled = False
        self.clear_filters_button.disabled = False

    def clear_all_filters(self, *_):
        self.state.data_filters.clear()
        self.clear_chips()

        del self.df
        self.df = None
        self.df = self._get_data_from_source()

        self.update_table(None, None, None)

        self.clear_filter_fields()

        self.filters_counter.children = ""
        self.clear_filters_button.class_ = "d-none"

    def clear_chips(self):
        self.update_chips()
        for widget in self.table_view.filter_selects_wrapper.children:
            if isinstance(widget, FilterChip):
                self.table_view.filter_selects_wrapper.children.remove(widget)

    def clear_filter_fields(self, *_):
        self.clear_field_errors()
        self.filter_input_value.v_model = ""
        self.columns_to_filter_selector.v_model = None
        self.filter_autocomplete_value.v_model = None
        self.match_case_checkbox.v_model = None
        self.match_entire_cell_checkbox.v_model = None
        self.filter_select_operator.v_model = None
        self.hide_checkbox_wrapper()
        self.show_input_value()

    def _create_apply_button(self, *_):
        apply_button = Button(
            children=["apply filter"],
            class_="my-2",
            color="primary",
        )

        apply_button.on_event("click", self.on_apply_button_click)

        return apply_button

    def get_column_value(self, *_):
        operator = self.filter_select_operator.v_model
        columns_metadata = self.state.dataset.metadata.data_types
        is_categorical = columns_metadata.get(
            self.columns_to_filter_selector.v_model
        ).is_categorical
        column_type = columns_metadata.get(
            self.columns_to_filter_selector.v_model
        ).col_type

        if is_categorical and column_type == ColumnDataType.text:
            if operator == IS:
                return self.filter_autocomplete_value.v_model
            elif operator == CONTAINS:
                return self.filter_input_value.v_model
            else:
                # this shouldn't happen
                return self.filter_autocomplete_value.v_model
        elif is_categorical:
            if column_type == ColumnDataType.numerical:
                return float(self.filter_autocomplete_value.v_model)
            # this also shouldn't happen
            return self.filter_autocomplete_value.v_model
        else:
            if column_type == ColumnDataType.text:
                return self.filter_input_value.v_model
            else:
                return float(self.filter_input_value.v_model)

    def get_selected_checkboxes_value(self, *_):
        if self.match_case_checkbox.v_model and self.match_entire_cell_checkbox.v_model:
            return "is_case_sensitive_on"
        elif (
            self.match_case_checkbox.v_model
            and not self.match_entire_cell_checkbox.v_model
        ):
            return "contains_sensitive_on"
        elif (
            not self.match_case_checkbox.v_model
            and self.match_entire_cell_checkbox.v_model
        ):
            return "is_case_sensitive_off"
        else:
            return "contains_sensitive_off"

    def get_operator(self, *_):
        operator = self.filter_select_operator.v_model
        columns_metadata = self.state.dataset.metadata.data_types
        is_categorical = columns_metadata.get(
            self.columns_to_filter_selector.v_model
        ).is_categorical
        column_type = columns_metadata.get(
            self.columns_to_filter_selector.v_model
        ).col_type

        if is_categorical and column_type == ColumnDataType.text:
            if operator == CONTAINS:
                return self.get_selected_checkboxes_value()
            else:
                return "is_case_sensitive_on"
        elif column_type == ColumnDataType.numerical:
            return operator
        else:
            return self.get_selected_checkboxes_value()

    def is_autocomplete_hidden(self) -> bool:
        return "d-none" in self.filter_autocomplete_value.class_.split()

    def is_selected_numerical_col(self) -> bool:
        if (
            self.columns_to_filter_selector.v_model
            and self.columns_to_filter_selector.v_model != []
        ):
            column_name = self.columns_to_filter_selector.v_model

            columns_metadata = self.state.dataset.metadata.data_types
            column_type = columns_metadata.get(column_name).col_type
            is_categorical = columns_metadata.get(column_name).is_categorical
            is_manual = columns_metadata.get(column_name).explicit_categorical
            if (
                column_type == ColumnDataType.numerical
                and not is_categorical
                and not is_manual
            ):
                return True
        return False

    def validate_filters(self, *_):
        def is_float(value):
            try:
                float(value)
                return True
            except ValueError:
                return False

        column = self.columns_to_filter_selector.v_model
        operator = self.filter_select_operator.v_model
        input_value = self.filter_input_value.v_model
        autocomplete_value = self.filter_autocomplete_value.v_model

        is_valid = True

        if column == [] or not column:
            is_valid = False
            self.columns_to_filter_selector.error_messages = ["No column selected"]

        if not operator:
            is_valid = False
            self.filter_select_operator.error_messages = ["Operator should be selected"]

        if not input_value.strip() and self.is_autocomplete_hidden():
            is_valid = False
            self.filter_input_value.error_messages = ["Value should be filled in"]
        elif self.is_autocomplete_hidden() and self.is_selected_numerical_col():
            if not is_float(input_value):
                is_valid = False
                self.filter_input_value.error_messages = ["Should be a numeric value"]

        if autocomplete_value is None and not self.is_autocomplete_hidden():
            is_valid = False
            self.filter_autocomplete_value.error_messages = ["Value should be selected"]

        return is_valid

    def clear_field_errors(self, *_):
        self.columns_to_filter_selector.error_messages = []
        self.filter_select_operator.error_messages = []
        self.filter_input_value.error_messages = []
        self.filter_autocomplete_value.error_messages = []

    @handle_cb_exceptions
    def on_apply_button_click(self, *_):
        is_valid = self.validate_filters()
        if not is_valid:
            return

        self.disable_filter_fields()
        column_value = self.get_column_value()

        operator = self.get_operator()

        self.state.add_filter(
            column=self.columns_to_filter_selector.v_model,
            op=operator,
            value=column_value,
        )
        self.update_chips()
        self.clear_filter_fields()
        self.filters_counter.children = str(len(self.state.data_filters.filters))

        try:
            self.update_table(None, None, None)
        except Exception as e:
            debug_logger.error(f"Error updating table: {e}")
            self._update_table_view()
        finally:
            self.clear_filters_button.class_ = "my-2 d-initial"
            self.enable_filter_fields()
            self.show_filters_action()

    def update_chips(self, *_):
        self.filter_chip_item = self._create_filter_chip_item()

    def update_columns(self, widget, event, data):
        if self.select_all_text in self.column_selector.v_model:
            if self.select_all_text == "Select All":
                self.column_selector.v_model = list(self.df.columns)
                self.select_all_text = "Deselect All"
            else:
                self.column_selector.v_model = []
                self.select_all_text = "Select All"

            self.column_selector.items = [self.select_all_text, *self.df.columns]
        else:
            if (
                set(self.column_selector.v_model) != set(self.df.columns)
                and self.select_all_text == "Deselect All"
            ):
                self.select_all_text = "Select All"
                self.column_selector.items = [
                    self.select_all_text,
                    *self.df.columns,
                ]

    def _on_change_with_debounce(self, widget, event, data, delay=1):
        self.update_columns(widget, event, data)

        if self._debounce_timer:
            self._debounce_timer.cancel()

        def trigger_update_table():
            self.update_table(widget, event, data)

        self._debounce_timer = Timer(delay, trigger_update_table)
        self._debounce_timer.start()

    def update_filter_view(self):
        self.table_view.update_or_create_filters_view(
            columns_to_filter_selector=self.columns_to_filter_selector,
            filter_input_value=self.filter_input_value,
            filter_autocomplete_value=self.filter_autocomplete_value,
            filter_select_operator=self.filter_select_operator,
            checkbox_wrapper=self.checkbox_wrapper,
            clear_filters_button=self.clear_filters_button,
            apply_button=self.apply_button,
            filter_chip_item=self.filter_chip_item,
        )

    @handle_cb_exceptions
    def update_table(self, widget, event, data):
        self.columns = self.column_selector.v_model

        # Clear old dataframe references
        del self.df
        self.df = self._get_data_from_source()

        self._update_table_view()

        filtered_indices = self.state.dataset.df.index.get_indexer(self.df.index)
        filtered_data_points = self.state.dataset.subset(filtered_indices)
        self.group_save_modal.update_data_points(filtered_data_points)

        if self.show_filters:
            self.show_filters_action()

    def _update_table_view(self):
        self.table_view = self._generate_table(self.workspace_id)
        self.children = [self.selector_controls, self.table_view]

    def filter_df(self, df) -> pd.DataFrame:
        return apply_filters_df(df, self.state.data_filters)
