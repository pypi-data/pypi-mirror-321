import logging
from IPython.core.magic import Magics, magics_class, cell_magic, line_magic
from IPython.utils.capture import capture_output

# Set up logging
logger = logging.getLogger(__name__)

# Define the class with decorator
@magics_class
class NotebookModifier(Magics):
    """Magic commands for modifying notebook cell execution."""
    
    def __init__(self, shell):
        logger.debug("Initializing NotebookModifier")
        try:
            # Must call parent's __init__ first
            super().__init__(shell)
            self.shell = shell
            logger.debug("Successfully initialized NotebookModifier")
        except Exception as e:
            logger.error("Failed to initialize NotebookModifier", exc_info=True)
            raise
    
    @cell_magic
    def add_header_and_uppercase(self, line, cell):
        """Add header and convert output to uppercase."""
        logger.debug("Executing add_header_and_uppercase magic")
        header = "# This cell was modified\n"
        modified_cell = header + cell
        
        try:
            with capture_output() as captured:
                result = self.shell.run_cell(modified_cell)
                if result.error_before_exec or result.error_in_exec:
                    logger.error("Cell execution failed")
                    return result
            
            if captured.stdout:
                print(captured.stdout.upper())
            
            if result.result is not None:
                print(str(result.result).upper())
            
            logger.debug("Successfully executed magic command")
            return None
        except Exception as e:
            logger.error("Error in magic command", exc_info=True)
            print(f"Error in magic command: {e}")
            return None

    @line_magic
    def notebook_help(self, line):
        """Show help for notebook modifier extension."""
        logger.debug("Executing notebook_help magic")
        print("Notebook Modifier Extension Help:")
        print("\nCell Magics:")
        print("  %%add_header_and_uppercase - Adds header and converts output to uppercase")
        print("\nLine Magics:")
        print("  %notebook_help - Shows this help message")

# Create a class factory to ensure decorator is applied
def create_notebook_modifier(shell):
    logger.debug("Creating NotebookModifier instance via factory")
    return NotebookModifier(shell) 