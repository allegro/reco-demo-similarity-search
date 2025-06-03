# Reco-demo-similarity-search

Welcome to the workshop **"Behind the Scenes of Recommender System: Two-Tower Models in Action"** by Allegro.

This repository provides a hands-on demonstration of product similarity search for recommender systems. Explore notebooks that delve into product embeddings and their vector space representations. You'll learn about efficient search methods like Nearest Neighbors (NN) and Approximate Nearest Neighbors (ANN), and how to adapt it for diverse recommendation scenarios.

## Contents
1. Embeddings exploration
2. Product representations in embeddings space (2D)
3. Nearest Neighbors search
4. Approximate Nearest Neighbors search
5. Similarity search in recommendation scenarios

## Setup

1. Make sure you have **Python 3.10.** installed (you can use e.g. [pyenv](https://github.com/pyenv/pyenv))
    ```bash
    brew install pyenv
    pyenv install 3.10
    pyenv local 3.10  # run this in the repository directory
    ```
2. Execute commands below to create new virtual environment. Once you do it, activate and prepare your venv.
    ```bash
    make virtual-env
    source .venv/bin/activate
    make compile-requirements
    make install-requirements
    make jupyter-kernel
    ```
3. Run jupyter notebook by command `jupyter notebook` and open `demo_notebook.ipynb` file. Make sure you use correct kernel (Kernel > Change Kernel > venv). Now you can explore the code!