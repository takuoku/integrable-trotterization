# integrable-trotterization

This repository contains data and codes associated with the paper ["Conserved charges in the quantum simulation of integrable spin chains"](https://arxiv.org/abs/2208.00576) by 
Kazunobu Maruyoshi, Takuya Okuda, Juan W. Pedersen, Ryo Suzuki, Masahito Yamazaki, and Yutaka Yoshida.

- MAIN_public.ipynb performs the quantum simulation on a simulator with the circuits described in the paper.
- Use plot_results.ipynb to plot data in the result folders.  Computation of statistical uncertainties is omitted.
- Mathematica code recursion_to_q.nb generates files q3_plus_coefficients.dat, ..., q6_plus_coefficients.dat.  This code is based on the explicit recursion relations derived in the paper.  For degrees 3 and 4, the results have been checked against those obtained by a symbolic implementation of the boost relation, which is slower.
- In the folder "result", we place subfolders with data names, which contain simulation data and configuration files.  The data names for data in the figures in the paper can be found in the file names of the pdf files, which are available from the arXiv (click on "Other formats").  Some of the folders that contain large data are compressed.  Files in MEAS_RES contain the outcomes of individual measurements, which are used to compute the expectation value of the observable in each line of q{n}_plus_coefficients.dat.  
- In the paper we also compute the statistican uncertainties in the expectation values.  The codes used for this purpose are omitted here.
- For j=1,...,N-1, the j-th qubit in the paper is also the j-th qubit in our programs.  The N-th qubit in the paper is the 0-th qubit in the programs.
