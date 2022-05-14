# Heaps_and_Zipf_laws_examination
A program designed to perform tests and experiments on a set of books (texts) using Heaps and Zipf's law. 


# The goal
The aim of the programme was to test (and select) various classification, estimation and clustering methods in order to predict, on the basis of the predictors, the quality of wine with the highest possible accuracy. 

# Setup 
1. Git clone repository.
2. To install all nessesary dependecies type 'poetry install' (if you already have poetry installed on ypur machine you should just type 'poetry update')
3. To install all nessasary libraries for nltk type: poetry run 'python -m nltk.downloader popular'
4. To run the program type: 'poetry run python3 main.py' 

If you analised first graph, close a window to see another one.

# Program structure
The main file is in main. With this file you can check your document (or as many documents as you want!) and see does your document fulfill Heaps and Zip laws rules. 
Other files contains usefull classes and methods, which gives a tools to check meantioned laws.

The application is created of 5 files:
- main_HZ.py: main script, used to conduct data preprocessing and testing Heaps and Zipf laws,
- data_preprocessing: file contating methods used to "work" with data, "to clean" them. Mainly used to prepare data for further analysis, 
- Heaps_and_Zipf_laws.py: file contating all methods needed to calculate Heaps and Zipf parameters. Additionally methods inside class can be used to create useful graphs visualizing analized data. 

Creation of the README in progress...
