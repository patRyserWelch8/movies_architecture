# Introduction

This simple Python project aims to demonstrate how sql, json and csv data can be captured and consumed in using a FAIR and micro-services data architecture.  It is a basic proof of a concept for to demonstrates how data capture and consumption requires a different journey, but complement each other.  

We simulate using four streamers 

1. CCD - based on a national broadcasting services.
2. OduFlix - An entertainment provider based on monthly payments.
3. BigForest - An international streaming services based on rental and purchase for each movie.
4. PearTV - Another international streaming services based on rental and purchase for each movie.

#  Data capture 
We start from the User interaction and moving down to each type of movies and programmes streamers.

## Front end: User Interaction 
__Link to the code :__ [User interaction](https://github.com/patRyserWelch8/movies_architecture/tree/main/poc)

The user interaction is a basic command line interface. A flow is hard coded to capture data specific for each streamers based on their onw unique data needs. 

## Remote capture through integration of system
__link to the code:__ [remote integration with other systems]https://github.com/patRyserWelch8/movies_architecture/tree/main/poc/remote_interaction)

__remote storage:__ [Remote datastorage](https://github.com/patRyserWelch8/movies_architecture/tree/main/poc/remote_data)

Some movies are pushed from another system. We simulate this scenario using some files. A flow redirects the data to unique streamers.  In this case we push data forward to BigForest and and PearTV.

# Back-end : Data storage, management and integration of streamers
We starts from a bottom up approach

## Primary source of data
__Data source__: [Simulated data](https://github.com/patRyserWelch8/movies_architecture/tree/main/poc/primary_data)

This folder holds all the data.  Table 1 summarises the data, its type of storage, and metadata.

| Streamer | Type of storage | Metadata|
| :---| :--- | :--- |
| CCD | Comma-Separated-Values | Title (String), TypeOfProgram (String), Classification (String), Country(String), Year (int), Category (String), Channel (string) 
| Oduflix | JSON | Title (String), Producer (String), Year (int), Country(String), Classification (String), Stars (int), Actors (Arrays of String)|
| BigForest| JSON | Title (String), Year (int),  Category (String),  Rental (float), Purchase (float), stars (int), Classification (String), Country(String)|
| PearTV| SQL (sqlite)| CREATE TABLE Film ( film_id INTEGER PRIMARY KEY, title TEXT NOT NULL, classification TEXT NOT NULL, country TEXT NOT NULL,
 rental FLOAT NOT NULL, purchase FLOAT NOT NULL, stars INT NOT NULL, year INT  NOT NULL);|





