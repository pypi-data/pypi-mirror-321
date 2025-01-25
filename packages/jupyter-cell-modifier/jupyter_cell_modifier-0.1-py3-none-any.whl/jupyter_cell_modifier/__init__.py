from IPython.core.magic import Magics, magics_class, cell_magic, line_magic
from IPython.core.getipython import get_ipython
from IPython.display import display, HTML
from IPython.core.formatters import DisplayFormatter
from IPython.utils.capture import capture_output

class UppercaseDisplayFormatter(DisplayFormatter):
    """Custom formatter that converts text output to uppercase."""
    def format(self, obj):
        format_dict, metadata_dict = super().format(obj)
        if 'text/plain' in format_dict:
            format_dict['text/plain'] = format_dict['text/plain'].upper()
        return format_dict, metadata_dict

@magics_class
class NotebookModifier(Magics):
    """Magic commands for modifying notebook cell execution."""
    def __init__(self, shell):
        super().__init__(shell)
        self.original_formatter = shell.display_formatter
        self.uppercase_formatter = UppercaseDisplayFormatter(parent=self.shell.display_formatter)
        
    def pre_run_cell(self, info):
        """Run before cell execution"""
        self.shell.display_formatter = self.uppercase_formatter
        
    def post_run_cell(self, result):
        """Run after cell execution"""
        try:
            if hasattr(result, 'result') and result.result is not None:
                output = str(result.result)
                print(output.upper())
        finally:
            self.shell.display_formatter = self.original_formatter
        
    @cell_magic
    def add_header_and_uppercase(self, line, cell):
        """Add header and convert output to uppercase."""
        self.shell.display_formatter = self.uppercase_formatter
        try:
            with capture_output() as captured:
                result = self.shell.run_cell(cell, store_history=False)
                if result.error_before_exec or result.error_in_exec:
                    return result
            
            code_output = captured.stdout.strip() if captured.stdout else None
            if code_output:
                print(code_output.upper())
            return None
        finally:
            self.shell.display_formatter = self.original_formatter

    @line_magic
    def notebook_help(self, line):
        """Show help for notebook modifier extension."""
        print("Notebook Modifier Extension Help:")
        print("\nCell Magics:")
        print("  %%add_header_and_uppercase - Adds header and converts output to uppercase")
        print("\nLine Magics:")
        print("  %notebook_help - Shows this help message")
        print("\nAutomatic Features:")
        print("  - All cell outputs are converted to uppercase")

_modifier = None

def load_ipython_extension(ipython):
    """Load the extension in IPython."""
    global _modifier
    _modifier = NotebookModifier(ipython)
    ipython.register_magics(_modifier)
    ipython.events.register('pre_run_cell', _modifier.pre_run_cell)
    ipython.events.register('post_run_cell', _modifier.post_run_cell)

def unload_ipython_extension(ipython):
    """Unload the extension."""
    global _modifier
    if _modifier is not None:
        ipython.events.unregister('pre_run_cell', _modifier.pre_run_cell)
        ipython.events.unregister('post_run_cell', _modifier.post_run_cell)
        _modifier = None
