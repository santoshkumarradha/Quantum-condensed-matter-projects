Name a thing that is extremely polar and can move only in one direction !
- Time ordered Greens function ! ( ͡° ͜ʖ ͡°)

# Quantum_projects
Set of my own codes written during the course of my PhD. Almost all of them are in python and to make it easier, have rewritten in jupyter notebooks. There might be couple of C/FORTRAN or Julia codes sneaking in there which are specificaly designed to work with LAPACK and BLAS libraries (just a cautionary note to compile them right!). All the codes are for internal/personal use and is not meant to be a final user usable version. 




1) solving **finite chain Ionic hubbard model** using Exact Diognalization (possibly to show edge states) [NbViewer Link](https://nbviewer.jupyter.org/github/santoshkumarradha/Quantum-condensed-matter-projects/blob/master/finite%20chain%20ionic%20Hubbard%20model/Hubbard%20solver.ipynb)

![equation](https://latex.codecogs.com/gif.latex?%5Chat%7BH%7D%3D-t%5Csum%5Climits_%7B%3Ci%2Cj%3E%7D%5Bc%5E%5Cdagger_%7Bi%5Csigma%7Dc_%7Bj%5Csigma%7D&plus;h.c%5D&plus;U%5Csum%5Climits_%7Bi%7Dn_%7Bi%5Cdownarrow%7Dn_%7Bi%5Cuparrow%7D&plus;%5Cfrac%7BJ_e%7D%7B2%7D%5Csum%5Climits_%7Bi%5Cin%20CoO_2%7Dn_i)

------------------------------------------------------------------------------
2) **2DEG density calculation** from DFT electron density in n-layer Li_xCoO_2 system

  Free electron tight binding model in triangular lattice for the "anomolous" bands in monolayer [Nbviewer link](https://nbviewer.jupyter.org/github/santoshkumarradha/Quantum-condensed-matter-projects/blob/master/2DEG%20density/density%20calculation.ipynb)

------------------------------------------------------------------------------
3) **QUESTAAL** suit custom bands with color weight plotting added and also syml file generator for a general ctrl file (uses spglib and seekpath) [NbViewer Link](https://nbviewer.jupyter.org/github/santoshkumarradha/Quantum-condensed-matter-projects/blob/master/plotting%20bands/plot%20bands.ipynb)

------------------------------------------------------------------------------
4) **Structure generation using Delaunay triangulation algorithm** for Li placement on monolayer CoO2 and currosponding calculation of spatial depedence of energy and Magnetic moment [Nbviewer link](https://nbviewer.jupyter.org/github/santoshkumarradha/Quantum-condensed-matter-projects/blob/master/Structure%20generation%20and%20Mag%20mom/structures%20and%20Mag%20Mom.ipynb)

------------------------------------------------------------------------------
5) **Tightbinding models** for hexogonal non planar systems along with **berry curvature** calculation. Plotting of Conduction-Valence to show the topologica transition from Nodal Line Semimetal to Dirac semi metal by breaking the Parity symetry in the system. [NbViewer Link](https://nbviewer.jupyter.org/github/santoshkumarradha/Quantum-condensed-matter-projects/blob/master/Tight%20binding%20models/tight%20binding%20model.ipynb)

------------------------------------------------------------------------------
6) Clasical vector **Dipole strength in different lattices** as a function of nth neareast neibghor. (note the amazing effect of cubic symetry forcing the dipole to be short range) [NbViewer Link](https://nbviewer.jupyter.org/github/santoshkumarradha/Quantum-condensed-matter-projects/blob/master/Electrostatic%20Dipole%20strength/Dipole%20strength.ipynb) 

------------------------------------------------------------------------------
7) Calculation of all possible **theormodynamic reactions/decomposition of a given Quantum crystal** system (CsSiX3 in this case ) and calculation/plotting of 3D convex Hull of an 3 atom system using energies from Materials project and custom calculation from QUESTAAL suit for ther paper [https://doi.org/10.1002/pssa.201800962](https://doi.org/10.1002/pssa.201800962)
[Nbviewer Link](https://nbviewer.jupyter.org/github/santoshkumarradha/Quantum-condensed-matter-projects/blob/master/3D%20ConvexHull%20and%20MP%20Reactions/CsSnX3%20reactions%20and%20paper.ipynb)
------------------------------------------------------------------------------
8) **Quantum monte carlo** using Metropolis algorithm. Interesting part is using a realistic theory for the simulation (self consistant tight binding theory in this case, but DFT theories like LDA/GGA can be used too). This was done inorder to avoid the complx modeling of exchange parameters in the heisenburg hameltonian which was mapped from a pseudo spin -1/2 system. As seen, it is an almost XXZ hameltonian with an added theta term that complicates the sollution. [NbViewer Link](https://nbviewer.jupyter.org/github/santoshkumarradha/Quantum-condensed-matter-projects/blob/master/Quantum%20MonteCarlo/tbe%20QMC.ipynb)

![equation](https://i.ibb.co/nfRw069/Screen-Shot-2019-04-20-at-9-06-00-PM.png)


------------------------------------------------------------------------------
9) **Neural nets for structure generation** Very very early atempt on using Materials project rpository to create a crystal representation using 3D point cloud algorithms with both GAN and VAE type nets. Will update the idea and notes soon.[Nbviewer link](https://nbviewer.jupyter.org/github/santoshkumarradha/Quantum-condensed-matter-projects/blob/master/Neural%20Network%20Structure%20Generation/ann%20project.ipynb)


------------------------------------------------------------------------------
10) **[Atomic Simulation Environment](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwiqwr6ZneXhAhUBKKwKHdW2B-IQFjAAegQIBhAC&url=https%3A%2F%2Fwiki.fysik.dtu.dk%2Fase%2F&usg=AOvVaw2Ut7wXZpe1ynrtJKgrzNlU)** Interfaqce to QUESTAAL code in its very early stage couple of working example of the class are provided in the notebook.[Nbviewer link](https://nbviewer.jupyter.org/github/santoshkumarradha/Quantum-condensed-matter-projects/blob/master/ASE%20Interface/test.ipynb)
