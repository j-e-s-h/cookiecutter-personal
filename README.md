# Cookiecutter Personal

## Requirements
---
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html). via pip or conda:

``` bash
pip install cookiecutter
```

or

``` bash
conda install -c conda-forge cookiecutter
```

## Creating a new project
In the folder where you want your project:

``` bash
cookiecutter https://github.com/j-e-s-h/cookiecutter-personal
```

## Directory structure

    ├── LICENSE
    ├── .gitignore
    ├── environment.yml    <- The requirements file for reproducing the analysis environment.
    ├── README.md          <- The top-level README for developers using this project.
    ├── install.md         <- Detailed instructions to set up the virtual
    |                         environment of this project.
    ├── data
    │   ├── raw            <- The original, immutable data dump.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   └── processed      <- The final, canonical data sets for modeling.
    │
    ├── utils              <- Scripts to help with common tasks.
    │
    ├── notebooks          <- Jupyter notebooks.
    |
    └── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
        └── figures        <- Generated graphics and figures to be used in reporting.

## Credits

This project is heavily influenced by [jvelezmagic's Cookiecutter Conda Data Science](https://github.com/jvelezmagic/cookiecutter-conda-data-science)