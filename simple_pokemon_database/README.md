# Simple Pokémon Database Project

This project involves building a simple Pokémon database using data from the PokeAPI.

## Database:
- **Complete Database File**: `pokemondb.db` (Updated as of 04/24/2025)

## What I Worked On:
- **Database Design and Setup**:
  Designed and created the database schema using SQLite.

- **Database Updates**:
  Enhanced the database by adding new columns with SQL queries (e.g., `add_legendary_mythical_columns.sql`, `add_species_column.sql`).

- **Data Scraping**:
  Developed Python scripts (`scrape_evolution_chain.py`, `scrape_legendary_mythical.py`) to scrape data from the PokeAPI. This was necessary due to missing data in the official CSV files.

- **JSON to CSV Conversion**:
  Converted the scraped JSON data into CSV format using Python scripts (`evolution_chain_json_to_csv.py`, `legendary_mythical_lists_and_csv.py`).

- **CSV Cleaning**:
  Cleaned and organized the CSV files to ensure compatibility with the database schema (`clean_csv_for_db.py`).

- **Data Import**:
  Used a Python script (`import_csv_to_db.py`) to import the cleaned CSV data into the database.

