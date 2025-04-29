# Simple Pokémon Database Project

📁 [Download pokemondb.db](./pokemondb.db)

## Project Overview

This project focuses on creating a simple Pokémon database to store and organize data about Pokémon. The database is built using SQLite and the data is sourced from the PokeAPI.

## Goals

- Build a database to store simple Pokémon-related data.

## Data Source

PokeAPI: [https://pokeapi.co/](https://pokeapi.co/)
Raw Data: [View folder](./data)
Processed Data: [View folder](./processed_data)

## Tools & Skills Used

- **SQLite**: For designing and managing the database.
- **Python**: For scraping, cleaning, and importing data. Used libraries like `pandas`, `sqlalchemy`, and `requests`.
- **CSV**: For organizing and structuring data before import.
- **PokeAPI**: Primary source for Pokémon data.

## Project Workflow

1. **Database Design**: Created the database schema using SQLite.
2. **Data Gathering**: Collected CSV data from the PokeAPI GitHub. Used Python scripts to scrape additional missing data when needed.
3. **JSON to CSV Conversion**: Converted scraped JSON data into CSV format.
4. **CSV Cleaning**: Cleaned and formatted CSV files to match the database schema.
5. **Data Import**: Imported cleaned CSV data into the SQLite database using Python.
6. **Data Updates**: Ran SQL scripts to add new columns and update the database with additional data.

## Visuals

![ERD Diagram](./docs/ERD%20Diagram.png)

## What I Learned

- How to design and manage a simple database using SQLite.
- How to scrape and extract data from an API using Python.
- How to clean and convert data for database integration.
- How to use GitHub to organize and share my project.
