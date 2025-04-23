import pandas as pd

##################################################
# pokemon_cleaned.csv
##################################################

# Step 1: Load the original CSV files
# -----------------------------------
# Load the Pokémon base info (e.g., ID, name, is_default_form, etc.)
pokemon_df = pd.read_csv("data/pokemon.csv")

# Load the Pokémon base stats (e.g., HP, Attack, etc. are stored in rows)
stats_df = pd.read_csv("data/pokemon_stats.csv")

# Step 2: Map stat_id to descriptive stat names
# ---------------------------------------------
# According to the stat_id values:
# 1 = HP, 2 = Attack, 3 = Defense, 4 = Special Attack, 5 = Special Defense, 6 = Speed
stat_map = {
    1: "base_hp",
    2: "base_attack",
    3: "base_defense",
    4: "base_sp_attack",
    5: "base_sp_defense",
    6: "base_speed",
}

# Add a new column with readable stat names
stats_df["stat_name"] = stats_df["stat_id"].map(stat_map)

# Step 3: Pivot the stats table from long to wide format
# ------------------------------------------------------
# This will convert multiple rows per Pokémon into a single row with one column per stat
pivoted_stats = stats_df.pivot(
    index="pokemon_id", columns="stat_name", values="base_stat"
).reset_index()

# Step 4: Merge the wide-format stats back into the Pokémon DataFrame
# -------------------------------------------------------------------
# Match pokemon_df.id to pivoted_stats.pokemon_id
pokemon_full = pd.merge(
    pokemon_df, pivoted_stats, left_on="id", right_on="pokemon_id", how="left"
)

# Step 5: Clean up the merged DataFrame
# -------------------------------------
# Drop the duplicate 'pokemon_id' column (we already have 'id')
pokemon_full.drop(columns=["pokemon_id"], inplace=True)

# Step 6: Save the final merged DataFrame to a new CSV file
# ---------------------------------------------------------
# This file will be used by import_csv_to_db.py instead of the original pokemon.csv
pokemon_full.to_csv("processed_data/pokemon_cleaned.csv", index=False)

print("pokemon_cleaned.csv successfully in 'processed_data/' folder.")

##################################################
# moves_cleaned.csv
##################################################

# Step 1: Load the moves.csv
# -------------------------------------
# We load the 'moves.csv' file into a pandas DataFrame called 'moves_df'.
moves_df = pd.read_csv("data/moves.csv")

# Step 2: Map damage_class_id to corresponding names
# -------------------------------------
# We define a dictionary called 'damage_class_map' where each numeric ID corresponds to a string.
damage_class_map = {
    1: "Status",  # 1 corresponds to status
    2: "Physical",  # 2 corresponds to physical
    3: "Special",  # 3 corresponds to special
}

# Step 3: Map the damage_class_id to its respective names
# -------------------------------------
# We use the 'map' function to apply 'damage_class_map' to the 'damage_class_id' column.
# This will create a new column, 'damage_class_name', with the mapped values.
moves_df["damage_class_name"] = moves_df["damage_class_id"].map(damage_class_map)

# Step 4: Save the updated DataFrame to a new CSV
# -------------------------------------
# We save the DataFrame with the updated column names (now including 'damage_class_name') to a new CSV file.
# The 'index=False' ensures that pandas doesn't save the index as a separate column in the CSV.
moves_df.to_csv("processed_data/moves_cleaned.csv", index=False)

print("moves_cleaned.csv successfully in 'processed_data/' folder.")

##################################################
# pokemon_moves_cleaned.csv
##################################################

# Step 1: Load the pokemon_moves.csv
# -------------------------------------
pokemon_moves_df = pd.read_csv("data/pokemon_moves.csv")

# Step 2: Map pokemon_move_method_id to corresponding names
# -------------------------------------
move_method_map = {
    1: "level-up",
    2: "egg",
    3: "tutor",
    4: "machine",
    5: "stadium-surfing-pikachu",
    6: "light-ball-egg",
    7: "colosseum-purification",
    8: "xd-shadow",
    9: "xd-purification",
    10: "form-change",
    11: "zygarde-cube",
}

# Step 3: Map the pokemon_move_method_id to its respective names
# -------------------------------------
pokemon_moves_df["move_method_name"] = pokemon_moves_df["pokemon_move_method_id"].map(
    move_method_map
)

# Step 4: Filter to keep only the row with the highest version_group_id
# -------------------------------------
# Sorts the pokemon_moves_df in ascending order by version_group_id.
# Removes duplicates based on a combination of pokemon_id, move_id, and pokemon_move_method_id.
pokemon_moves_df = pokemon_moves_df.sort_values("version_group_id").drop_duplicates(
    subset=["pokemon_id", "move_id", "pokemon_move_method_id"], keep="last"
)

# Step 5: Sort pokemon_moves_df by 'pokemon_id' in ascending order, then version_group_id in descending order.
# -------------------------------------
pokemon_moves_df = pokemon_moves_df.sort_values(
    by=["pokemon_id", "version_group_id"], ascending=[True, False]
)

# Step 6: Save the updated DataFrame to a new CSV
# -------------------------------------
pokemon_moves_df.to_csv("processed_data/pokemon_moves_cleaned.csv", index=False)

print("pokemon_moves_cleaned.csv successfully in 'processed_data/' folder.")

##################################################
# pokemon_abilities_cleaned.csv
##################################################

# Read CSV
pokemon_abilities_df = pd.read_csv("data/pokemon_abilities.csv")

# Remove duplicates
pokemon_abilities_unique_df = pokemon_abilities_df.drop_duplicates(
    subset=["pokemon_id", "ability_id"], keep="first"
)

# Save cleaned data
pokemon_abilities_unique_df.to_csv(
    "processed_data/pokemon_abilities_cleaned.csv", index=False
)
