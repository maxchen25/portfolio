import requests;
import json;
import time;

HEADERS = {
    "User-Agent": "PokemonDataProject/1.5 (https://github.com/maxchen25)",
    "Accept": "application/json",
}

def get_total_pokemon_species():
    """ 
    Fetches the total number of pokemon species available from the PokeAPI.
    """
    url = "https://pokeapi.co/api/v2/pokemon-species/"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        total = data["count"]
        print(f"Total pokemon species: {total}")
        return total
    else:
        print("Failed to fetch pokemon species count.")
        return None

def fetch_pokemon_species(species_id):
    """
    Fetches a single pokemon species by ID.
    Returns the JSON data if successful, otherwise NONE.
    """
    url = f"https://pokeapi.co/api/v2/pokemon-species/{species_id}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"Error fetching species {species_id}: {response.status_code}")
        return None
    
    return response.json()

def save_all_species(output_file="all_pokemon_species.json"):
    """
    Fetches all pokemon species and saves them into one JSON file.
    Includes ethical delays to respect the PokeAPI rate limits.
    """
    total_species = get_total_pokemon_species()
    if not total_species:
        return
    
    all_species = {}

    for i in range(1, total_species + 1):
        data = fetch_pokemon_species(i)
        if data:
            all_species[f"species_{i}"] = data
            print(f"Fetched species {i} of {total_species}")

        # Ethical delays
        time.sleep(1)
        if i % 30 == 0:
            print("Pausing for 60 seconds to avoid overloading the server...")
            time.sleep(60)
        
        # Save all data to one JSON file
        with open(output_file, "w") as f:
            json.dump(all_species, f, indent=2)
    
    print(f"All species saved to: {output_file}")

# Entry point
if __name__ == "__main__":
    save_all_species()