import json
import os

import pandas as pd
import traitlets
from ipydatagrid import DataGrid, HyperlinkRenderer, VegaExpr
from IPython.display import display
from ipywidgets import Button, HBox, Layout, VBox, widgets

CACHE_DIR = ".cache"


class DataStore(traitlets.HasTraits):
    data = traitlets.Any()


class MSDatagrid(DataGrid):
    """MSDatagrid which takes list of column names to use as filters. This class dynamically identifies the widget type for columns and adds them to the grid.
    For date columns, it adds a date picker widget. For int and float columns it adds a range slider.
    For columns with two unique values it uses radio. For columns with more than two and less than 10 unique values it uses a dropdown.
    For columns with more than 10 unique values, it uses a text input widget. For bool columns it uses a checkbox.
    """

    def __init__(self, df, height="800px", link_cols=None, **kwargs):
        renderers = {}
        if link_cols:
            for col in link_cols:
                link_renderer = HyperlinkRenderer(
                    url=VegaExpr("cell.value[0]"),
                    url_name=VegaExpr("cell.value[0]"),
                    background_color="moccasin",
                    text_color="blue",
                    font="bold 14px Arial, sans-serif",
                )
                renderers[col] = link_renderer

        super().__init__(
            df,
            base_row_size=30,
            base_column_size=300,
            layout=Layout(height=height),
            theme="material-dark",
            renderers=renderers,
            **kwargs,
        )


class MSDataGridWithFilter(MSDatagrid):
    def __init__(
        self,
        df,
        filter_cols=[],
        summary_cols=None,
        app_name="default_app",
        link_cols=None,
        height="800px",
        after_filter_callback=None,
        **kwargs,
    ):
        self.original_data = df  # Store the original DataFrame
        super().__init__(df, height=height, link_cols=link_cols, **kwargs)
        self.filter_cols = filter_cols
        self.summary_cols = summary_cols
        self.link_cols = link_cols if link_cols else []
        self.app_name = app_name
        self.cache_file = os.path.join(CACHE_DIR, f"{app_name}_filter_cache.json")
        self.filter_widgets = {}
        self.after_filter_callback = after_filter_callback
        self.create_filter_widgets()
        self.load_cached_filters()
        total_listings = len(self.original_data)
        self.total_listings_widget = widgets.HTML(
            value=f"Total Listings: {total_listings}"
        )

        # Add show_summary checkbox if summary_cols are provided
        if self.summary_cols:
            self.show_summary_checkbox = widgets.Checkbox(
                value=False, description="Show Summary", disabled=False
            )
            self.show_summary_checkbox.observe(self.toggle_summary_view, names="value")
        self.create_layout()

    def create_layout(self):
        filter_box = HBox([widget for widget in self.filter_widgets.values()])
        apply_button = Button(description="Apply Filter")
        apply_button.on_click(self.apply_filter)
        display_all_button = Button(description="Display All")
        display_all_button.on_click(self.display_all)

        controls = (
            HBox([filter_box, apply_button, display_all_button])
            if self.filter_cols
            else None
        )

        # Add show_summary checkbox to controls if summary_cols are provided
        if self.summary_cols:
            controls = (
                HBox([controls, self.show_summary_checkbox])
                if controls
                else HBox([self.show_summary_checkbox])
            )

        # Only include controls in VBox if it exists
        children = [self]
        if controls is not None:
            children.insert(0, controls)
        self.main_layout = VBox(children)

    def create_filter_widgets(self):
        for col in self.filter_cols:
            if col in self.link_cols:
                continue  # Skip creating filters for link columns
            col_type = self.original_data[col].dtype
            unique_values = self.original_data[col].nunique()

            if pd.api.types.is_datetime64_any_dtype(col_type):
                self.filter_widgets[col] = widgets.DatePicker(description=col)
            elif pd.api.types.is_numeric_dtype(col_type):
                min_val = self.original_data[col].min()
                max_val = self.original_data[col].max()
                if pd.api.types.is_integer_dtype(col_type):
                    step = 1
                else:
                    step = (max_val - min_val) / 100  # 100 steps for float
                self.filter_widgets[col] = widgets.FloatRangeSlider(
                    value=[min_val, max_val],
                    min=min_val,
                    max=max_val,
                    step=step,
                    description=col,
                    continuous_update=False,
                )
            elif unique_values == 2:
                options = self.original_data[col].unique().tolist()
                self.filter_widgets[col] = widgets.RadioButtons(
                    options=options, description=col
                )
            elif 2 < unique_values <= 10:
                options = self.original_data[col].unique().tolist()
                self.filter_widgets[col] = widgets.Dropdown(
                    options=options, description=col
                )
            elif unique_values > 10:
                self.filter_widgets[col] = widgets.Text(description=col)
            elif pd.api.types.is_bool_dtype(col_type):
                self.filter_widgets[col] = widgets.Checkbox(description=col)

    def load_cached_filters(self):
        if os.path.exists(self.cache_file):
            with open(self.cache_file, "r") as f:
                cached_filters = json.load(f)

            for col, value in cached_filters.items():
                if col in self.filter_widgets:
                    widget = self.filter_widgets[col]
                    if isinstance(widget, widgets.Text):
                        widget.value = value
                    elif isinstance(widget, (widgets.Dropdown, widgets.RadioButtons)):
                        if value in widget.options:
                            widget.value = value
                    elif isinstance(widget, widgets.DatePicker):
                        widget.value = pd.to_datetime(value).date()
                    elif isinstance(widget, widgets.Checkbox):
                        widget.value = value
                    elif isinstance(widget, widgets.FloatRangeSlider):
                        widget.value = value

    def save_filters_to_cache(self):
        cached_filters = {}
        for col, widget in self.filter_widgets.items():
            if isinstance(widget, widgets.DatePicker):
                cached_filters[col] = widget.value.isoformat() if widget.value else None
            elif isinstance(widget, widgets.FloatRangeSlider):
                cached_filters[col] = list(widget.value)
            else:
                cached_filters[col] = widget.value
        if not os.path.exists(CACHE_DIR):
            os.makedirs(CACHE_DIR)
        with open(self.cache_file, "w") as f:
            json.dump(cached_filters, f)

    def display_all(self, button):
        # Reset the data to the original dataframe
        self.data = self.original_data.copy()
        self.total_listings_widget.value = f"Total Listings: {len(self.data)}"

        if self.after_filter_callback:
            self.after_filter_callback(self)

    def apply_filter(self, button):
        filtered_df = self.original_data.copy()
        for col, widget in self.filter_widgets.items():
            if isinstance(widget, widgets.Text):
                if widget.value:
                    filtered_df = filtered_df[
                        filtered_df[col]
                        .astype(str)
                        .str.contains(widget.value, case=False)
                    ]
            elif isinstance(widget, widgets.Dropdown) or isinstance(
                widget, widgets.RadioButtons
            ):
                if widget.value:
                    filtered_df = filtered_df[filtered_df[col] == widget.value]
            elif isinstance(widget, widgets.DatePicker):
                if widget.value:
                    filtered_df = filtered_df[filtered_df[col].dt.date == widget.value]
            elif isinstance(widget, widgets.Checkbox):
                filtered_df = filtered_df[filtered_df[col] == widget.value]
            elif isinstance(widget, widgets.FloatRangeSlider):
                min_val, max_val = widget.value
                filtered_df = filtered_df[
                    (filtered_df[col] >= min_val) & (filtered_df[col] <= max_val)
                ]
        self.save_filters_to_cache()

        # Apply summary view if checkbox is checked and summary_cols are provided
        if (
            self.summary_cols
            and hasattr(self, "show_summary_checkbox")
            and self.show_summary_checkbox.value
        ):
            # find summary cols in the original data
            summary_cols = [
                col for col in self.summary_cols if col in self.original_data.columns
            ]
            filtered_df = filtered_df[summary_cols]

        self.on_data_changed(filtered_df, overwrite_original_data=False)

        if self.after_filter_callback:
            self.after_filter_callback(self)

    def add_callback_on_filter_applied(self, callback):
        self.after_filter_callback = callback

    def on_data_changed(self, new_df, overwrite_original_data=True):
        # Check if the summary checkbox is checked and summary_cols are provided
        # Only overwrite original data if new data is loaded to the grid.
        if (
            self.summary_cols
            and hasattr(self, "show_summary_checkbox")
            and self.show_summary_checkbox.value
        ):
            # Ensure summary columns exist in the new dataframe
            summary_cols = [col for col in self.summary_cols if col in new_df.columns]
            self.data = new_df[summary_cols]
        else:
            self.data = new_df  # Reset to full dataframe if checkbox is not checked

        if overwrite_original_data:
            self.original_data = new_df
        self.total_listings_widget.value = f"Total Listings: {len(new_df)}"

    def display(self):
        display(self.total_listings_widget)
        display(self.main_layout)

    def toggle_summary_view(self, change):
        if change["new"]:  # If checkbox is checked
            if hasattr(self, "summary_cols") and all(
                col in self.original_data.columns for col in self.summary_cols
            ):
                self.data = self.original_data[self.summary_cols]
            else:
                # If summary_cols not properly defined, keep full data
                self.data = self.original_data
        else:
            self.data = self.original_data  # Reset to full dataframe
        self.apply_filter(None)  # Reapply filters after changing columns


# Modify the MSDataGridWithFilter to update the data store
class ReactiveDataGrid(MSDataGridWithFilter):
    def __init__(self, data_store, *args, **kwargs):
        df = data_store.data
        super().__init__(df, *args, **kwargs)
        self.observe(self._on_data_changed, names="data")
        self.data_store = data_store

    def _on_data_changed(self, change):
        new_data = change["new"]
        super().on_data_changed(new_data)
