import os
import tempfile
import webbrowser

import ipywidgets as widgets
from IPython.display import HTML, display


class ScrollableText:
    def __init__(self, height="200px", width="100%"):
        self.height = height
        self.width = width
        self.output = None
        self.button = None
        self._create_css()
        self._create_output()
        self._create_copy_button()
        self._create_display_in_browser_button()

    def _create_css(self):
        custom_css = f"""
        <style>
        .scrollable-output {{
            height: {self.height};
            width: {self.width};
            overflow: auto;
            white-space: nowrap;
            border: 1px solid #ccc;
            padding: 10px;
        }}
        .scrollable-output::-webkit-scrollbar {{
            width: 10px;
            height: 10px;
        }}
        .scrollable-output::-webkit-scrollbar-track {{
            background: #f1f1f1;
        }}
        .scrollable-output::-webkit-scrollbar-thumb {{
            background: #888;
        }}
        .scrollable-output::-webkit-scrollbar-thumb:hover {{
            background: #555;
        }}
        </style>
        """
        display(HTML(custom_css))

    def _create_output(self):
        self.output = widgets.Output(
            layout={"height": self.height, "width": self.width, "overflow": "auto"}
        )
        self.output.add_class("scrollable-output")

    def _create_copy_button(self):
        self.copy_button = widgets.Button(
            description="Copy", button_style="info", tooltip="Copy content to clipboard"
        )
        self.copy_button.on_click(self._copy_to_clipboard)

    def _create_display_in_browser_button(self):
        self.display_button = widgets.Button(
            description="Display in Browser",
            button_style="info",
            tooltip="Open content in a new browser tab",
        )
        self.display_button.on_click(self._display_in_browser)

    def _copy_to_clipboard(self, b):
        content = self.output.outputs[0]["text"]
        copy_js = f"""
        var dummy = document.createElement("textarea");
        document.body.appendChild(dummy);
        dummy.value = {repr(content)};
        dummy.select();
        document.execCommand("copy");
        document.body.removeChild(dummy);
        """
        display(HTML(f"<script>{copy_js}</script>"))

    def _display_in_browser(self, b):
        content = self.output.outputs[0]["text"]
        html_content = f"""
        <html>
        <head>
            <style>
                pre {{
                    white-space: pre-wrap;       /* CSS 3 */
                    white-space: -moz-pre-wrap;  /* Mozilla */
                    white-space: -pre-wrap;      /* Opera 4-6 */
                    white-space: -o-pre-wrap;    /* Opera 7 */
                    word-wrap: break-word;       /* Internet Explorer 5.5+ */
                    width: 80%;                  /* Limit width to 80% of viewport */
                    margin: 20px auto;           /* Center content with some padding */
                }}
            </style>
        </head>
        <body>
            <pre>{content}</pre>
        </body>
        </html>
        """

        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".html") as f:
            f.write(html_content)
        webbrowser.open("file://" + os.path.realpath(f.name))

    def add_content(self, content):
        with self.output:
            print(content)

    def display(self):
        display(
            widgets.VBox(
                [self.output, widgets.HBox([self.copy_button, self.display_button])]
            )
        )

    def clear(self):
        self.output.clear_output()

    def update_content(self, content):
        self.output.clear_output()
        self.add_content(content)
