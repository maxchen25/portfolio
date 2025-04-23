import pandas as pd
from sqlalchemy import create_engine, text

# Create SQLAlchemy engine (for SQLite)
engine = create_engine("sqlite:///pokemondb.db")

# Define your CSV-to-table mapping
csv_table_map = [
    {
        "csv": "data/types.csv",
        "table": "types",
        "column_map": {"id": "id", "identifier": "name"},  # csv file col: table col
    },
    {
        "csv": "data/type_efficacy.csv",
        "table": "type_effectiveness",
        "column_map": {
            "damage_type_id": "attacking_type_id",
            "target_type_id": "defending_type_id",
            "damage_factor": "multiplier",
        },
    },
    {
        "csv": "processed_data/pokemon_cleaned.csv",
        "table": "pokemon",
        "column_map": {
            "id": "id",
            "identifier": "name",
            "is_default": "is_default_form",
            "base_hp": "base_hp",
            "base_attack": "base_attack",
            "base_defense": "base_defense",
            "base_sp_attack": "base_sp_attack",
            "base_sp_defense": "base_sp_defense",
            "base_speed": "base_speed",
        },
    },
    {
        "csv": "data/pokemon_types.csv",
        "table": "pokemon_types",
        "column_map": {
            "pokemon_id": "pokemon_id",
            "type_id": "type_id",
            "slot": "slot",
        },
    },
    {
        "csv": "data/abilities.csv",
        "table": "abilities",
        "column_map": {
            "id": "id",
            "identifier": "name",
        },
    },
    {
        "csv": "processed_data/pokemon_abilities_cleaned.csv",
        "table": "pokemon_abilities",
        "column_map": {
            "pokemon_id": "pokemon_id",
            "ability_id": "ability_id",
        },
    },
    {
        "csv": "processed_data/moves_cleaned.csv",
        "table": "moves",
        "column_map": {
            "id": "id",
            "identifier": "name",
            "type_id": "type_id",
            "damage_class_name": "category",
            "power": "power",
            "accuracy": "accuracy",
            "pp": "pp",
        },
    },
    {
        "csv": "processed_data/pokemon_moves_cleaned.csv",
        "table": "pokemon_moves",
        "column_map": {
            "pokemon_id": "pokemon_id",
            "move_id": "move_id",
            "move_method_name": "method",
            "level": "level",
        },
    },
    {
        "csv": "processed_data/all_evolution_chains.csv",
        "table": "evolutions",
        "column_map": {
            "base_pokemon_id": "base_pokemon_id",
            "evolved_pokemon_id": "evolved_pokemon_id",
            "method": "method",
            "level": "level",
            "item": "item",
            "counter": "counter",
        },
    },
]


def print_table_column_map(conn):
    """
    Queries the database for all table names and their column names,
    then prints the information in a formatted, copy-paste incomplete
    draft style.

    Steps:
    1. Fetches table names from the database.
    2. Retrieves column names for each table using PRAGMA.
    3. Prints the table and columns in a structured format.

    Args:
    conn: The database connection object.
    """

    # Get all table names
    tables = conn.execute(
        text("SELECT name FROM sqlite_master WHERE type='table';")
    ).fetchall()

    for i, (table_name,) in enumerate(tables):
        # Get column names using PRAGMA
        result = conn.execute(text(f"PRAGMA table_info({table_name});")).fetchall()

        # Extract just the column names
        column_names = [row[1] for row in result]

        # Print in copy-paste format
        print("{")
        print(f'    "csv": "",')
        print(f'    "table": "{table_name}",')
        print(f'    "column_map": {{')

        for j, col in enumerate(column_names):
            comma = "," if j < len(column_names) - 1 else ""  # Avoid trailing comma
            print(f'        "": "{col}"{comma}')

        print("    }")

        if i < len(tables) - 1:
            print("},")
        else:
            print("}")


def import_csvs_to_db(csv_table_map, engine):
    """
    Imports CSVs to database tables based on a mapping configuration.

    Args:
        csv_table_map (list): A list of dictionaries specifying the CSV path, table name, and column mapping.
        engine: SQLAlchemy database engine.
    """
    for entry in csv_table_map:
        print(f"Importing {entry['csv']} into {entry['table']}...")

        # Load the CSV file
        df = pd.read_csv(entry["csv"])

        # Rename columns to match the database schema
        df = df.rename(columns=entry["column_map"])

        # Reorder columns (optional, but cleaner and safer)
        db_columns = list(entry["column_map"].values())
        df = df[db_columns]

        # Write to the database
        df.to_sql(entry["table"], engine, if_exists="append", index=False)

    print("All CSV files imported successfully.")


if __name__ == "__main__":
    import_csvs_to_db(csv_table_map, engine)

    # Create basic structure for csv_to_table mapping
    # with engine.connect() as conn:
    #     print_table_column_map(conn)
    pass
