Quick python functions to make syml files and plot bands from QUESTAAL files 

Note making syml uses spglib and seekpath modules.
Ofcourse pymatgen is needed too. 

copy the .py files to the bin directory and do chmod +x *.py with both the .py files and then you can see the content with --help


download instructions -

wget https://raw.githubusercontent.com/santoshkumarradha/Quantum-condensed-matter-projects/master/plotting%20bands/mksyml.py

wget https://raw.githubusercontent.com/santoshkumarradha/Quantum-condensed-matter-projects/master/plotting%20bands/plotquestaal.py


chmod +x mksyml.py
chmod +x plotquestaal.py

ex usage for the figure given -
plotquestaal.py -c sb --dos --erange -6 6 --lst "1:25,101:125,226:250|Sb-edgestates" --out sb_p --band --col Bulk:white Edge-state:red

files needed - syml.ctrl and bnds.ctrl 
the code is self explanatory. 


- 5/18/2019 - added support for spin/color weights 
- 5/20/2019 - Need to be updated with DOS plot by side
- 6/13/2019 - Added a syml file maker that checks the ctrl's symetry and makes a syml file containing all high sym points
- 6/13/2019 - added argpraser interface for plotting bands
- 6/13/2019 - refined the module and added support for --rpos
- 6/14/2019 - made it better and refined errors and added examples
