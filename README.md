# Introduction

This simple Python project aims to demonstrate how sql, json and csv data can be captured and consumed in using a FAIR and micro-services data architecture.  It is a basic proof of a concept for to demonstrates how data capture and consumption requires a different journey, but complement each other.  

We simulate using four streamers 

1. CCD - based on a national broadcasting services.
2. OduFlix - An entertainment provider based on monthly payments.
3. BigForest - An international streaming services based on rental and purchase for each movie.
4. PearTV - Another international streaming services based on rental and purchase for each movie.

#  Data capture 
We start from the User interaction and moving down to each type of movies and programmes streamers.

## User Interaction 
__Link to the code :__ [User interaction](https://github.com/patRyserWelch8/movies_architecture/tree/main/poc)

The user interaction is a basic command line interface. A flow is hard coded to capture data specific for each streamers based on their onw unique data needs. 

## Remote capture through integration of system
__link to the code:__ [remote integration with other systems]https://github.com/patRyserWelch8/movies_architecture/tree/main/poc/remote_interaction)

__remote storage:__ [Remote datastorage](https://github.com/patRyserWelch8/movies_architecture/tree/main/poc/remote_data)

Some movies are pushed from another system. We simulate this scenario using some files. A flow redirects the data to unique streamers.  In this case we push data forward to BigForest and and PearTV.

## Data and its storage 

