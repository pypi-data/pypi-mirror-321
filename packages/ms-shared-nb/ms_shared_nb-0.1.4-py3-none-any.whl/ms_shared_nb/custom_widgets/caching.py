import json
import os

from IPython.display import display


def cache_widget_state(cache_filename, cache_dir="./cache"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            widget = func(*args, **kwargs)

            # Construct the full cache file path
            if cache_dir is not None:
                cache_path = os.path.join(cache_dir, cache_filename)
            else:
                cache_path = cache_filename

            # Ensure the cache directory exists
            if cache_dir is not None and not os.path.exists(cache_dir):
                os.makedirs(cache_dir)

            # Function to collect widgets with _my_name attribute
            widgets_dict = {}

            def collect_widgets(w):
                if hasattr(w, "_my_name"):
                    widgets_dict[w._my_name] = w
                if hasattr(w, "children"):
                    for child in w.children:
                        collect_widgets(child)

            collect_widgets(widget)

            # Load the state from the cache file
            try:
                with open(cache_path, "r") as f:
                    state = json.load(f)
                if isinstance(state, dict):
                    # Set the widget values based on the state
                    for name, value in state.items():
                        if name in widgets_dict and hasattr(
                            widgets_dict[name], "value"
                        ):
                            widgets_dict[name].value = value
                else:
                    print("Warning: Cached state is not in the expected format.")
            except FileNotFoundError:
                print(
                    f"Cache file {cache_path} not found. Proceeding without loading state."
                )
            except json.JSONDecodeError:
                print(
                    f"Error decoding JSON from cache file {cache_path}. Proceeding without loading state."
                )

            # Function to save the state
            def save_state(change=None):
                # Save the widget values
                state = {}
                for name, w in widgets_dict.items():
                    if hasattr(w, "value"):
                        state[name] = w.value
                with open(cache_path, "w") as f:
                    json.dump(state, f)

            # Observe changes in the widget and save state
            for w in widgets_dict.values():
                if hasattr(w, "value"):
                    w.observe(save_state, names="value")

            display(widget)
            return widget

        return wrapper

    return decorator
