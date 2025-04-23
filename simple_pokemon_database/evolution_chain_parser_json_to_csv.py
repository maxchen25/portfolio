import json
import csv
import re


def get_pokemon_id_from_url(url):
    """
    Extracts the Pokémon species ID from a given URL.

    Parameters:
        url (str): The URL string containing the Pokémon species ID.

    Returns:
        int: The extracted Pokémon ID as an integer.
    """
    return int(re.search(r"/pokemon-species/(\d+)/", url).group(1))


def parse_chain(chain, base_id, rows):
    """
    Recursively parses an evolution chain and extracts evolution data.

    Parameters:
        chain (dict): The current stage of the evolution chain.
        base_id (int): The ID of the base Pokémon evolving from.
        rows (list): A list to collect rows of evolution data.

    Appends:
        Dicts with keys: base_pokemon_id, evolved_pokemon_id, method, level, item.
    """
    for evo in chain.get("evolves_to", []):
        evolved_id = get_pokemon_id_from_url(evo["species"]["url"])

        for detail in evo.get("evolution_details", []):

            method = detail["trigger"]["name"] if detail.get("trigger") else None
            level = detail.get("min_level")
            item = detail["item"]["name"] if detail.get("item") else None

            rows.append(
                {
                    "base_pokemon_id": base_id,
                    "evolved_pokemon_id": evolved_id,
                    "method": method,
                    "level": level,
                    "item": item,
                }
            )

        # Recurse to handle multi-stage evolutions
        parse_chain(evo, evolved_id, rows)


def main():
    """
    Main function that loads the JSON file, parses evolution chains,
    assigns a unique counter to each row, and writes the data into a CSV file.
    The counter is used as a unique identifier for each evolution entry.
    """
    with open("data/all_evolution_chains.json", "r") as f:
        data = json.load(f)

    rows = []

    for chain_key in data:
        chain_data = data[chain_key]["chain"]
        base_id = get_pokemon_id_from_url(chain_data["species"]["url"])
        parse_chain(chain_data, base_id, rows)

    # Assign a unique counter after collecting all rows
    for i, row in enumerate(rows, start=1):
        row["counter"] = i

    with open("processed_data/all_evolution_chains.csv", "w", newline="") as csvfile:
        fieldnames = [
            "base_pokemon_id",
            "evolved_pokemon_id",
            "method",
            "level",
            "item",
            "counter",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
