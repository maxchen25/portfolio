-- Generate DROP TABLE statements for each table in the database
SELECT 'DROP TABLE IF EXISTS "' || name || '";'
FROM sqlite_master
WHERE type = 'table';

-- Drop tables generated from the above query (if they exist)
DROP TABLE IF EXISTS "types";
DROP TABLE IF EXISTS "type_effectiveness";
DROP TABLE IF EXISTS "pokemon";
DROP TABLE IF EXISTS "pokemon_types";
DROP TABLE IF EXISTS "abilities";
DROP TABLE IF EXISTS "pokemon_abilities";
DROP TABLE IF EXISTS "moves";
DROP TABLE IF EXISTS "pokemon_moves";
DROP TABLE IF EXISTS "evolutions";
