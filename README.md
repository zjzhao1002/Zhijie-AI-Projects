# Zhijie-AI-Project

## Introduction
By this App, you can query the Particle Data Group (PDG) database or ask questions for Zhijie's publications. 
The SQL database file for PDG can be downloaded from [here](https://pdg.lbl.gov/2024/api/index.html). 
The academic papers for Retrieval Augmented Generation (RAG) are PDF files in the **data** folder. 
These publications can be also found [here](https://inspirehep.net/authors/1622480). 
The text is extracted by the **PyPDF2**. 

Here, the **Gemini** model from google has been used, but it can be switched to other model easily. 

## TODO
Actually, the performance of this app is not good. For example, if you write a prompt:
```
Find the value of Higgs mass in this database.
```
you do not get any results. To get the Higgs mass, a possible prompt may be:
```
Join the pdgid and pdgdata table by id = pdgid_id. Find the value of H MASS in the description.
```
This means that user has basic knowledge of this database and SQL. A more cleverer way is writing the SQL query by herself/himself... 

A possible way to improve the performance is editing the template of the prompt. This is the first thing I can try. 

For the PDF files, only the text is extracted. 
To get a better precision, the figures and tables should be considered. 
**Unstructured** may be a solution.
