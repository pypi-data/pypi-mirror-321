# GEMTIP-ML
Pre-trained implementation of the Generalized Effective Medium Theory of Induced Polarization (GEMTIP) neural network. This code allows fast and accurate rock-scale anisotropic induced polarization modelling.

![plot](./assets/figures/timing-comparison-IPW.png)

## Citation
Please cite our [*Geophysics* paper](https://library.seg.org/doi/10.1190/geo2024-0107.1) if your research projects use this code.

@article{berube_anisotropic_2024,  
    title = {Anisotropic induced polarization modeling with neural networks and effective medium theory},  
    author = {Bérubé, Charles L. and Gagnon, Jean-Luc},  
    journal = {Geophysics},  
    volume = {90},  
    number = {2},  
    year = {2024},  
    pages = {1--68},  
    doi = {10.1190/geo2024-0107.1},  
}

The original submitted version of the manuscript is also available as an open access preprint:  
http://arxiv.org/abs/2402.11313 

## Dependencies
This code uses scientific and plotting librairies available in the Anaconda Python distribution: 
- numpy
- matplotlib
- scipy

It also uses specific librairies for deep learning and numerical integration:
- pytorch
- torchquad 

## Usage
For now, the codes only reproduce the validation experiments (Figures 2 and 3) from the published paper.
- The script validate_Zhdanov2008.py reproduces Figure 2.
- The script validate_Zhdanov2018.py reproduces Figure 3.

## Roadmap
### 2024 
Upload code base for reproducing the validation experiments from the published paper.

### 2025 
The codes will be refactored into a more user friendly Python package.

### 2026 
In addition to forward modelling, the code will be updated to support inverse modelling. 

## Acknowledgements
The authors contributed equally to the work. C. L. Bérubé acknowledges funding from the FRQNT Research Support for
New Academics under the project titled Petrophysical modelling of the induced polarization effect with machine learning (grant no. 326054). J.-L. Gagnon is supported by an NSERC Undergraduate Student Research Award.