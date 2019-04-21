
![equation](https://i.ibb.co/nfRw069/Screen-Shot-2019-04-20-at-9-06-00-PM.png)

This code is a very rudimentry way to simulate quantum monte carlo for finding macroscopic averages. 

This works using the usual Metropolis algorithm. The interesting part is, to simulate a realistic atomic simulation ( as the ising model's parameter to solve map the spin system has a more complex structure) using self consistant tightbinding theory from QUESTAAL suit package. This was done inorder to circumvent the complicated calculation of the exchange parameters as shown in the above equation (especially the theta term that makes the sollution non trival from the regular XXZ model) Implementation is in Beta statge. 




PS: most probly would be abandoned as TBE formalisim does not seem to capture the required physics ie. dipole interaction, even while using the self constiant TBE theory with EWALD corrections. A much better approach would be LDA like DFT, which can techinically be done but is extremely time consuming even for 2x2x2 supercell simpulations. But the approach of using TBE and semi-realistic theory to solve the hameltonian using QMC instead of using the approximate ising parameters seems to be interesting and might try to develop the theory and test it for other cases if time permits.
