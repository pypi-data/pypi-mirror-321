
import pandas as pd
import ipywidgets as widgets
from IPython.display import display


class MultipleSampleTypeWidget:
    def __init__(self, dataframe, samples_config_dict, no_of_samples=1):
        self.dataframe = dataframe
        self.no_of_samples = no_of_samples

        self.sample_widgets = []
        self.__apply_button = widgets.Button(description='Apply')
        self.__apply_button.on_click(self.handle_input)

        for i in range(self.no_of_samples):
            for key, value in samples_config_dict.items():
                if key not in ['periods', 'n_data_points']:
                    raise ValueError(f'Invalid key {key} in samples_dict. Valid keys are periods and n_data_points.')
                for _sample_config in value:
                    sample_widget = self.create_sample_widget(i, key, _sample_config)
                    self.sample_widgets.append(sample_widget)

    def create_sample_widget(self, sample_index, sample_type, sample_dict):
        sample_widget = [
            widgets.Dropdown(options=['periods', 'n_data_points'], value=sample_type, description='Sample Type:'),
        ]
        if sample_type == 'periods':
            sample_widget.append(widgets.Text(description='Period Value:', value='1w'))
        else:
            sample_widget.append(widgets.Text(description='N Data Points:', value='10'))
        if 'before_date' in sample_dict:
            sample_widget.append(widgets.DatePicker(description='Before Date:', value=pd.to_datetime(sample_dict['before_date'])))
        if 'start_date' in sample_dict:
            sample_widget.append(widgets.DatePicker(description='Start Date:', value=pd.to_datetime(sample_dict['start_date'])))
        if 'end_date' in sample_dict:
            sample_widget.append(widgets.DatePicker(description='End Date:', value=pd.to_datetime(sample_dict['end_date'])))

        return sample_widget

    def get_sample(self, sample_type, period_value=None):
        # Replace the logic here to extract the desired sample from the DataFrame
        # Return the sample DataFrame
        return None

    def handle_input(self, change):
        for sample_widget in self.sample_widgets:
            sample_type = sample_widget['sample_type_dropdown'].value

            if sample_type == 'Periods':
                period_value = sample_widget['period_value_input'].value
                if sample_widget['date_picker'].value:
                    sample = self.get_sample('Periods before given date', period_value)
                elif sample_widget['start_date_picker'].value and sample_widget['end_date_picker'].value:
                    sample = self.get_sample('Periods between given dates', period_value)
                else:
                    sample = self.get_sample('Periods', period_value)  # Default to periods with end date as max date

            elif sample_widget['date_picker'].value:
                sample = self.get_sample('N Data Points before given date')
            else:
                sample = self.get_sample('N Data Points')  # Default to last n data points

            # Display the sample DataFrame
            display(sample)


    def display_widgets(self):
        for i in range(self.no_of_samples):
            _sample_widgets = self.sample_widgets[i]
            display(widgets.HBox(_sample_widgets))
        display(self.__apply_button)