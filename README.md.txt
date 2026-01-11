# Hybrid Spiking-Transformer IDS Code

This repository contains the source code used in the paper:

"Meta-heuristic optimized feature learning via hybrid spiking-transformer networks for adaptive real-time intrusion detection in edge-IoT systems"

## Files
- preprocess_nslkdd_final.py : Preprocessing script for NSL-KDD dataset
- train_model.py : Model training script
- model.py : Hybrid spiking-transformer network definition

## Dataset
NSL-KDD dataset from Zenodo:
https://doi.org/10.5281/zenodo.17424143

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Preprocess data:
   python preprocess_nslkdd_final.py

3. Train model:
   python train_model.py
