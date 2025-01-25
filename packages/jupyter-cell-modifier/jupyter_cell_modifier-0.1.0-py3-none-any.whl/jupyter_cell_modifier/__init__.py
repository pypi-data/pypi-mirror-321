from IPython.core.magic import Magics, magics_class, cell_magic, line_magic
from IPython.utils.capture import capture_output
import logging

logger = logging.getLogger(__name__)

@magics_class
class CellModifier(Magics):
    def __init__(self, shell):
        super().__init__(shell)
        self.shell = shell
    
    def pre_run_cell(self, info):
        """Run before cell execution"""
        try:
            print("Running before cell execution...")
            print(f"Cell content:\n{info.raw_cell}")
        except Exception as e:
            logger.error(f"Error in pre_run_cell: {e}", exc_info=True)
    
    def post_run_cell(self, result):
        """Run after cell execution"""
        try:
            print("\nCell execution completed.")
            if hasattr(result, 'result') and result.result is not None:
                print(f"Result: {result.result}")
        except Exception as e:
            logger.error(f"Error in post_run_cell: {e}", exc_info=True)

_modifier = None

def load_ipython_extension(ipython):
    """Load the extension in IPython."""
    global _modifier
    if _modifier is not None:
        unload_ipython_extension(ipython)
    
    _modifier = CellModifier(ipython)
    ipython.events.register('pre_run_cell', _modifier.pre_run_cell)
    ipython.events.register('post_run_cell', _modifier.post_run_cell)

def unload_ipython_extension(ipython):
    """Unload the extension."""
    global _modifier
    if _modifier is not None:
        ipython.events.unregister('pre_run_cell', _modifier.pre_run_cell)
        ipython.events.unregister('post_run_cell', _modifier.post_run_cell)
        _modifier = None
