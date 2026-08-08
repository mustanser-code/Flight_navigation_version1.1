 
# Flight Data ETL Pipeline

A beginner-friendly ETL pipeline built with Python and OOP.

This project extracts real-time flight data from the OpenSky Network API, transforms and cleans the data using Pandas, and prepares it for loading into a database.

## ETL Architecture

```text
OpenSky API
     ↓
FlightExtractor
     ↓
Raw JSON Data
     ↓
FlightTransformer
     ↓
Clean Pandas DataFrame
     ↓
Database Loader
=======
# Flight_navigation_version1.1

