## ENVIRONMENT
virtual-env:
	python -m venv .venv

## REQUIREMENTS
compile-requirements:
	python -m pip install -U pip-tools
	python -m piptools compile requirements/base.in --output-file requirements/base.txt --no-emit-index-url

install-requirements:
	python -m pip install -r requirements/base.txt

## JUPYTER NOTEBOOK
jupyter-kernel:
	python -m ipykernel install --user --name=venv