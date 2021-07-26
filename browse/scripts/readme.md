folder for source code files

currently unarranged, can be structured into module folders when needed.


```
sort.py		- to be called individually to sort the database file

main.py                 - top level function (for now) to generate multiple files
 |-- gen-out.py	        - generate single output file
      |-- filter.py     - filter the database
      |-- gen-block.py  - create the output markdown block for a single word

```
