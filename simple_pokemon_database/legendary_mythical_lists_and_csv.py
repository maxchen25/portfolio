import json
import pandas as pd

def create_dataframe(json_path):
    """
    Reads a JSON file containing nest Pokemon species data and transforms
    it into a simplified Dataframe with one row per Pokemon.
    """
    with open(json_path, 'r') as f:
        data = json.load(f)

    # Converts the data into a list of dictionaries, ensuring each Pokemon corresponds to a single row.
    species_list = list(data.values())
    complete_df = pd.DataFrame(species_list)

    # Selects relevant columns for further analysis
    simplified_df = complete_df[['name', 'is_legendary', 'is_mythical', 'varieties']]

    # Expands each variety of Pokemon into its own row
    exploded_df = simplified_df.explode('varieties')

    # Extracts the Pokemon name and ID from the 'varieties' column and adds them as new columns
    exploded_df['variety_name'] = exploded_df['varieties'].apply(lambda x: x['pokemon']['name'])
    exploded_df['pokemon_id'] = exploded_df['varieties'].apply(lambda x: x['pokemon']['url'].split("/")[-2])

    return exploded_df

def get_legendaries(df):
    """
    Returns a list of all legendary Pokemon.
    """
    legendaries = []

    for row in df.itertuples():
        if row.is_legendary:
            legendaries.append(row.variety_name)

    return legendaries

def get_mythicals(df):
    """
    Returns a list of all mythical Pokemon.
    """
    mythicals = []

    for row in df.itertuples():
        if row.is_mythical:
            mythicals.append(row.variety_name)

    return mythicals

def create_csv_legendary_mythical(df):
    """
    Returns csv file with data on which Pokemon are legendary or mythical.
    """
    reordered_df = df[['pokemon_id', 'variety_name', 'is_legendary', 'is_mythical']]
    
    reordered_df.to_csv('processed_data/pokemon_legendaries_mythicals.csv', index=False)

if __name__ == "__main__":
    # Load the Pokemon species data into a DataFrame
    species_df = create_dataframe("data/all_pokemon_species.json")

    # Get a list of all legendary and mythical Pokemon
    legendaries = get_legendaries(species_df)
    mythicals = get_mythicals(species_df)

    # Print out lists to copy paste for add_legendary_mythical_columns.sql
    print('Legendaries:')
    print(legendaries)
    print('Mythicals:')
    print(mythicals)

    # Create a CSV file showing which Pokemon are legendary or mythical
    create_csv_legendary_mythical(species_df)