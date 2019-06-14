Quick python functions to make syml files and plot bands from QUESTAAL files 

Note making syml uses spglib and seekpath modules.
Ofcourse pymatgen is needed too. 

copy the .py files to the bin directory and do chmod +x *.py with both the .py files and then you can see the content with --help


files needed - syml.ctrl and bnds.ctrl 
the code is self explanatory. 


- 5/18/2019 - added support for spin/color weights 
- 5/20/2019 - Need to be updated with DOS plot by side
- 6/13/2019 - Added a syml file maker that checks the ctrl's symetry and makes a syml file containing all high sym points
- 6/13/2019 - added argpraser interface for plotting bands
- 6/13/2019 - refined the module and added support for --rpos
