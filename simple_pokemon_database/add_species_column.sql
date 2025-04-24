-- import pokemon.csv into sql as pokemon_temp table

-- Populate species_id
UPDATE pokemon
SET species_id = (
    SELECT pokemon_temp.species_id
    FROM pokemon_temp
    WHERE pokemon_temp.id = pokemon.id
);

-- Drop temporary table
DROP TABLE pokemon_temp;