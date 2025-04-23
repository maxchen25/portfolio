import requests
import json
import time

# Custom headers for responsible API usage
HEADERS = {
    "User-Agent": "PokemonDataProject/1.0 (https://github.com/maxchen25)",
    "Accept": "application/json",
}


def get_total_evolution_chains():
    """
    Fetches the total number of evolution chains available from the PokeAPI.
    """
    url = "https://pokeapi.co/api/v2/evolution-chain/"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        total = data["count"]
        print(f"Total evolution chains available: {total}")
        return total
    else:
        print("Failed to fetch evolution chain count.")
        return None


def fetch_evolution_chain(chain_id):
    """
    Fetches a single evolution chain by ID.
    Returns the JSON data if successful, otherwise None.
    """
    url = f"https://pokeapi.co/api/v2/evolution-chain/{chain_id}/"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"Error fetching chain {chain_id}: Status {response.status_code}")
        return None

    return response.json()


def save_all_chains(output_file="all_evolution_chains.json"):
    """
    Fetches all evolution chains and saves them into one JSON file.
    Includes ethical delays to respect the PokeAPI rate limits.
    """
    total_chains = get_total_evolution_chains()
    if not total_chains:
        return

    all_chains = {}

    for i in range(1, total_chains + 1):
        data = fetch_evolution_chain(i)
        if data:
            all_chains[f"chain_{i}"] = data
            print(f"Fetched chain {i} of {total_chains}")

        # Wait 1 second between requests
        time.sleep(1)

        # Wait 60 seconds after every 30 requests
        if i % 30 == 0:
            print("Pausing for 60 seconds to avoid overloading the server...")
            time.sleep(60)

    # Save all data into one JSON file
    with open(output_file, "w") as f:
        json.dump(all_chains, f, indent=2)

    print(f"All evolution chains saved to: {output_file}")


# Entry point
if __name__ == "__main__":
    save_all_chains()
