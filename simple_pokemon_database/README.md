# Pokémon Database Project

This project is about building a simple Pokémon database using data from the PokeAPI. 

## What I Worked On:
- **Database Design and Creation**:  
  Built the structure of the database using SQLite.

- **Data Scraping**:  
  Wrote a Python script (`scrape_evolution_chain.py`) to get evolution chain data from PokeAPI. I did this because the official CSV file wasn’t usable.

- **JSON to CSV Conversion**:  
  Converted the scraped JSON data into CSV format so it could be imported into the database.

- **CSV Cleaning**:  
  Cleaned and organized the CSV files to make sure they worked with the database.

- **Data Import**:  
  Used a Python script to load the cleaned CSV data into the database.

## How to Set It Up

### Prerequisites:
- **SQLite**: Make sure you have SQLite installed.
- **(Optional)** DB Browser for SQLite: Helpful if you want a visual interface to explore the database.

### Steps:

1. **Create the Database Tables**  
   Run `pokemondb_reset.py` or use the SQL in `pokemon.sql` to set up the tables.

2. **Import the Data**  
   Run `import_csv_to_db.py` to load the data from the CSV files into the database.

