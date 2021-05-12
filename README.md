# SIMBA prototyping

This repository contains prototyping ideas for SIMBA: a Bayesing platform of particle physics simulations. There are several directions in which we have specific interest.

## Muography 

A nice introduction and overview of the topic is available from [L. Bonechi et al.](https://arxiv.org/abs/1906.03934).
Our starting point is [pumas](https://github.com/niess/pumas), a `C99` library for backward Monte-Carlo simulations of muons passing through matter, specifically designed for muography. 


As a first task, we propose to investigate the differential cross-sections in `pumas v1.0`. Consider the [bremsstrahlung](https://github.com/niess/pumas/blob/d04dce6388bc0928e7bd6912d5b364df4afa1089/src/pumas.c#L9155), [pair production](https://github.com/niess/pumas/blob/d04dce6388bc0928e7bd6912d5b364df4afa1089/src/pumas.c#L9221), [photonuclear](https://github.com/niess/pumas/blob/d04dce6388bc0928e7bd6912d5b364df4afa1089/src/pumas.c#L9515) and [ionisation](https://github.com/niess/pumas/blob/d04dce6388bc0928e7bd6912d5b364df4afa1089/src/pumas.c#L9620) processes: 


 * Re-implement the calculations in `python` using [numba](https://colab.research.google.com/github/cbernet/maldives/blob/master/numba/numba_cuda.ipynb) on both `CPU` and `CUDA` (we advise you to integrate `numba` with `pytorch`, cf. [examples](https://gist.github.com/grinisrit/280e4f14b17fe5ee37e2e254700d9fd0)). 
 * In a `jupyter` notebook, provide the exact formulas for the cross-sections used (you can have a look at [MUM](https://arxiv.org/abs/hep-ph/0010322) for initial reference).
 * Compare accuracy and performance across `CPU`/`CUDA`, varying the floating point precision (document your results).

 We recommend the [PENELOPE](https://www.oecd-nea.org/science/docs/2011/nsc-doc2011-5) manual as a good introductory read about Monte-Carlo simulations for the passage of particles through matter. Backward Monte-Carlo technique is well described by [V. Niess et al.](https://arxiv.org/abs/1705.05636)