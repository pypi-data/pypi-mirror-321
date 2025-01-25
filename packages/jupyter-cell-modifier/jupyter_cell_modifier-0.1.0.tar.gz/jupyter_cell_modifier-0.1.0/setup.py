from setuptools import setup, find_packages

setup(
    name="jupyter-cell-modifier",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'ipython>=7.0.0',
        'jupyter>=1.0.0',
        'notebook>=6.0.0',
        'jupyter_server>=1.0.0'
    ],
    entry_points={
        'console_scripts': [
            'install-jupyter-cell-modifier=jupyter_cell_modifier.install:main',
        ],
        'ipython.extensions': [
            'jupyter_cell_modifier = jupyter_cell_modifier:load_ipython_extension',
        ],
        'jupyter_server.extensions': [
            'jupyter_cell_modifier = jupyter_cell_modifier.server_config:load_jupyter_server_extension',
        ]
    },
    include_package_data=True,
    data_files=[
        ('etc/jupyter/jupyter_notebook_config.d', ['jupyter_cell_modifier.json']),
        ('share/jupyter/nbextensions/jupyter_cell_modifier', ['jupyter_cell_modifier/static/custom/custom.js'])
    ],
    python_requires='>=3.7',
)
