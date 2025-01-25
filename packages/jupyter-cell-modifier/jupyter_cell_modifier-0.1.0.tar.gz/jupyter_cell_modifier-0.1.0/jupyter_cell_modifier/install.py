import subprocess
import sys
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def main():
    """Main installation function that runs when package is installed via pip."""
    try:
        # Enable the server extension
        subprocess.run([
            'jupyter', 'server', 'extension', 'enable', 'jupyter_cell_modifier'
        ], check=True)

        # Install and enable the notebook extension
        subprocess.run([
            'jupyter', 'nbextension', 'install', '--py', 'jupyter_cell_modifier',
            '--sys-prefix'
        ], check=True)
        subprocess.run([
            'jupyter', 'nbextension', 'enable', 'jupyter_cell_modifier',
            '--py', '--sys-prefix'
        ], check=True)

        print("Successfully installed jupyter-cell-modifier")
        print("\nTo use in a notebook, run:")
        print("    %load_ext jupyter_cell_modifier")

    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
