# CompareWitnessesMatrix
This **replaces** the qa-table-starter.sh script. This python script creates a pregenealogical coherence matrix of witnesses using the open-cbgm's compare_witnesses module. There are two scripts. One responds to user input (CompareWitsMatrix.py) and the other (CompareWitsFromFile.py) compares witnesses provided in a JSON file. The final matrix is exported as a .csv file.

**CompareWitsMatrix.py**

The script must be run from the same directory as the open-cbgm's compare_witnesses module and the populated database. If you have not populated a database, start at #1 below. If you already have a database, skip to #6.

1. There are two open-cbgm modules that you will need, the populate_db and the compare_witnesses modules. These can be found in the "Example" folder.
2. Copy these two modules into the same directory as your xml collation file. A sample file, "john_6_23_collation.xml", is provided in the "Example" folder.
3. In the terminal, navegate to the directory.
4. Once in the directory, execute the following commands to create the database.

````./populate_db yourColationFile.xml YourDatabase.db````

5. This will create a databse based on the collation file. For further instructions on database creation and all available options, see the instructions provided by jjmccollum at https://github.com/jjmccollum/open-cbgm-standalone.
6. In the terminal, execute the following command.
*For Mac:*
````python3 -m CompareWitsMatrix```
*For Windows*
````python CompareWitsMatrix.py````
7. The script will prompt you to provide the following information.
````
Enter the witnesses to be compared (space or comma delimited): Your Witnesses
Enter the location of the database: YourDatabase.db
````
8. When the script has finished, it prompts you to name your csv file **(without the extension)**.
````
Please enter the name for the CSV file (without extension): YourFileName
````
The csv file will be saved to the same directory as the script.
 
python3 CompareWitsMatrix.py
 
It will ask for two inputs. The witnesses you want to compare and the location of your cache.db (or whatever you named it) database file that you populated with the populate_db script. The values in the output are all rounded to the nearest 100th.

**CompareWitsMatrixFromFile.py**

The instructions for this script are **the same for steps #1-5 above**. To use this script, you will need to configure the JSON file included in the "Example" folder. Use this script when you have so many witnesses that the terminal cannot handle them. The terminal has a character limit and you may not be able to compare all your witnesses using the above method.

*Configure the JSON file*
1. The JSON file has three parts to it: 1. Header information, 2. Included Witnesses, and 3. Excluded Witnesses.
2. Here is a sample of what it looks like.
````
"id": "john_6_23",
    "name": "john_6_23",
    "base_text": "basetext",
    "managingEditor": "dopeyduck",
    "editors": [
        "dopeyduck"
    ],
    "witnesses": [
        "basetext",
        "1",
        "13",
        "18",
        "22",
        "33"
 ],
    "excluded_witnesses": [
        "2768",
        "2786",
        "2790",
        "2886",
        "2561"
    ]
}
````
Whatever witnesses you want to compare must be included in "witnesses" and must be in double quotes and followed by a comma. Note that **the last witness in the list is not followed by a comma**. Whatever witnesses are in the "excluded_witnesses" will be ignored by the script. You can use David Flood's Criticus to modify this script with a simple GUI. Criticus can be found at https://github.com/d-flood/criticus.

3. Once the JSON file is configured, execute the following command from the Terminal:
*For Mac:*
````python3 -m CompareWitsMatrixFromFile````
*For Windows*
````python CompareWitsMatrixFromFile.py````
4. The script will prompt you for the location of the database.
````Enter the location of the database: cache100.db````
5. When the script is finishd executing, it will automatically save the csv file as output.csv to the same directory as the script. You will get a notification.
````Comparison matrix saved to YourDirectory/output.csv````



