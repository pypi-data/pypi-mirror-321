# python-template-test

Testing GitHub Repository Template functionality with an eye toward standardizing our approach with Python.

Ideally, using this repo as a template should give you the following for free:

> [x] Enough of a file structure so that users can infer where they need to put their code, tests, etc.
> 
> [x] Basic unit tests to guide testing patterns
> 
> [ ] Workflows to handle unit testing on push to the repo
> 
> [x] `uv` support
> 
> [x] A reasonable starting place for the pyproject.toml file
> 
> [ ] A README file the details what to do after you've cloned the repo
> 
> [ ] Variants for CLI tools and APIs (check out Typer to see if it'll meet needs, if so, FastAPI is probably the way to go)
> 
> [ ] A guide for publishing the package to PyPI
> 

# Recommended extensions setup:

# Recommended IDE Configuration

# Post-template setup

1. Run `uv sync` to install any needed dependencies on your system.

2. Rename the existing folder at `src/hello` to the name of your choosing. You should pay attention to PEP-8's [package and module naming guidelines](https://peps.python.org/pep-0008/#package-and-module-names) as well as the [broader guidelines found in PEP-423](https://peps.python.org/pep-0423/#overview).

3. Update the contents of `pyproject.toml` with the appropriate values for your project. At a minimum, you should be updating the following fields:

- project.name
- project.description
- tool.setuptools.package-dir (replace `hello` with your module name from step #2)
