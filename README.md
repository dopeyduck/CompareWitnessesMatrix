# CompareWitnessesMatrix
Replaces qa-table-starter, this python script creates a pregenealogical coherence matrix of witnesses using the open-cbgm based on user input.

Copy the script to the same folder as the compare_witnesses script in the open-cbgm. Then run it from the terminal from that folder:
 
python3 CompareWitsMatrix.py
 
It will ask for two inputs. The witnesses you want to compare and the location of your cache.db (or whatever you named it) database file that you populated with the populate_db script.

For example:

Enter the witnesses to be compared (space or comma delimited): 0151 256 1913 1973 1978 1985 1987 1991 1992 2102 2576 2936 1962
Enter the location of the database: /open-cbgm-standalone/build/bin/cache.db
 
The result will be a csv file with all witnesses compared in a matrix and the averages. The values are all rounded to the nearest 100th. The csv file will output to the same directory as the script. 
