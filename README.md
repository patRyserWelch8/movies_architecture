# Introduction

This simple Python project aims to demonstrate how sql, json and csv data can be captured and consumed in using a FAIR and micro-services data architecture.  It is a basic proof of a concept for to demonstrates how data capture and consumption requires a different journey, but complement each other.  

We simulate using four streamers 

1. CCD - based on a national broadcasting services.
2. OduFlix - An entertainment provider based on monthly payments.
3. BigForest - An international streaming services based on rental and purchase for each movie.
4. PearTV - Another international streaming services based on rental and purchase for each movie.

# What problems are we aiming to solve?
##  How can I capture data from various streamers and meeting their unique data needs?
The data for each streamer varies greatly in term of schema and data storage. This is immutable. We may wish to capture data from other streamer in the future - we are not aware of their schema, and data storage.

##  How can I capture movies, series and programmes in an seamless manner?
Capturing data for each streamer should be transparent for my friends and myself. We are not interested in using several systems. 

##  How can I capture data about movies and other programmes without a user interaction?
Capturing data for BigForest and PearTV can pushed in to the system on a daily basis. Therefore, no user interaction is required. 

##  How can I analyse the movies and other data as a whole?
It would be itneresting  to analyse the data about movies and other programmes.  We would aim to apply some advanced statistical methodologies, ML techniques and visualisation. It would help to transform data into knowledge and wisdom for our movies consumption within our community. 




#  Data capture 
We start from the User interaction and moving down to each type of movies and programmes streamers.

## Front end: User Interaction 
__Link to the code :__ [User interaction](https://github.com/patRyserWelch8/movies_architecture/tree/main/poc)

The user interaction is a basic command line interface. A flow is hard coded to capture data specific for each streamers based on their onw unique data needs. It would be anticipated an graphical user interface based on web or mobile technologies could be implemented instead. 

## Remote capture through integration of system
__link to the code:__ [remote integration with other systems](https://github.com/patRyserWelch8/movies_architecture/tree/main/poc/remote_interaction)

__remote storage:__ [Remote data storage](https://github.com/patRyserWelch8/movies_architecture/tree/main/poc/remote_data)

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
| PearTV| SQL (sqlite)| CREATE TABLE Film ( film_id INTEGER PRIMARY KEY, title TEXT NOT NULL, classification TEXT NOT NULL, country TEXT NOT NULL,rental FLOAT NOT NULL, purchase FLOAT NOT NULL, stars INT NOT NULL, year INT  NOT NULL);|



 ## Connections to each streamer data 
__Link to the code:__ [Connection and management of the data](https://github.com/patRyserWelch8/movies_architecture/tree/main/poc/streamers_connection) 

This code provides the tools that connects to the various type of storages. Use of existing connections and connectors to data storage is encouraged. In this proof of concept, each streamer inherits on of the classes to manage the data; JSON, CSV, SQL.  The data management simulates the following functionalities:

1. upload data and metadata (schemas)
2. upload data into a dataframe for data analysis and consumption
3. Capture data before insert to storage
4. Validate data captured before inserting into the storage
5. Insert physically to the storage
6. Confirm insert to the storage

New type of data management can be added or removed without impacting on the above layers, if well managed. 

## Integrating all the streamsers

__link to the code:__ [The streamer layer](https://github.com/patRyserWelch8/movies_architecture/tree/main/poc/integration_streamers)


This layer brings some transparency to the front end and remote integration.  Those components interacts with the layer so that data is captured. Therefore, a bespoke UI and a bespoke streamer storage can be added and use again existing code. 


#  Integrating the front and the back end
__link to the code:__ [Integration](https://github.com/patRyserWelch8/movies_architecture/tree/main/poc/front_back_integration)

This type integrations would be completed through REST-API call and potentially other methods of integrating the user interaction to the back-end.  The class _communicate_ aims at capturing remotetly data as well as through the user interaction.

This component can be extended to develop search facilities. The latter would continue to make some calls through the _integrating all the streamers_ component.


# Data consumption

The data consumption is concerned about transforming data into knowledge and decision making. We would hope to apply some statistical methodologies and machine learning techniques for classification and predictions.  

We adopt a Extract-Transform-Load approach. The data is transformed and loaded into a secondary storage. Alternatives, bring the computation to the data - as demonstrated in [SAFEST(https://www.longdom.org/open-access-pdfs/safest-a-safeguarding-analytical-framework-for-decentralised-sensitive-data.pdf), [DataShield](https://www.datashield.org/).

We approach data consumption from top to bottom

## Dashboard
__Link to the script__ : [Dashboard](https://github.com/patRyserWelch8/movies_architecture/tree/main/poc/dashboard)

__Secondary data:__ (Secondary data)[https://github.com/patRyserWelch8/movies_architecture/tree/main/poc/secondary_data)

The script aims at show how some simple map-and-reduce grouping could be completed. 

# Data pipeline

## Integrating all the streamsers

__link to the code:__ [The streamer layer](https://github.com/patRyserWelch8/movies_architecture/tree/main/poc/integration_streamers)


This layer implement an ETL data pipeline. This layer ingest the data from each data source, transformand and upload using a set of columns. Some data harmonisation occurs so that all the streamers data are integrated in one dataset.  The columns of the secondary data are the following: 

- 'Streamer'
- 'Title'
- 'Classification'
- 'Country'
- 'Year'
- 'Rental'
- 'Purchase'
- 'Stars'

The data is ingested into dataframe using the upload data functionality provided by each streamer. The ingested data is transformed for each streamer, before being concatenated and stored as secondary storage. A csv in our case, for simplicity.

















 





