# UFCMachine

This repository contains a deep learning model designed to predict the outcome of future UFC fights based on the historical data from all UFC fights from 1993-2019. The model utilizes a neural network with five layers, and was trained using the difference in fight statistics between the winner and loser of each fight. UFC fighters' career stats were scraped from http://ufcstats.com/statistics/fighters, and compiled in a dataframe which allows for a prediction to be made based on the fighters' names.

The model was used in the backend for the UFCMachine website, which was created using Flask and Python, and can be viewed in the Webpage_files. The webpage was designed to provide users with a clean, easily usable interface to provide predictions who will win future fights based on the model. 
