DROP TABLE IF EXISTS "types";
DROP TABLE IF EXISTS "type_effectiveness";
DROP TABLE IF EXISTS "pokemon";
DROP TABLE IF EXISTS "pokemon_types";
DROP TABLE IF EXISTS "abilities";
DROP TABLE IF EXISTS "pokemon_abilities";
DROP TABLE IF EXISTS "moves";
DROP TABLE IF EXISTS "pokemon_moves";
DROP TABLE IF EXISTS "evolutions";

CREATE TABLE types (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE type_effectiveness (
    attacking_type_id INTEGER,
    defending_type_id INTEGER,
    multiplier REAL,
    PRIMARY KEY (attacking_type_id, defending_type_id),
    FOREIGN KEY (attacking_type_id) REFERENCES types(id),
    FOREIGN KEY (defending_type_id) REFERENCES types(id)
);

CREATE TABLE pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    is_default_form BOOLEAN DEFAULT 1,  -- SQLite uses 0/1 for booleans
    base_hp INTEGER,
    base_attack INTEGER,
    base_defense INTEGER,
    base_sp_attack INTEGER,
    base_sp_defense INTEGER,
    base_speed INTEGER
);

CREATE TABLE pokemon_types (
    pokemon_id INTEGER,
    type_id INTEGER,
    slot INTEGER CHECK(slot IN (1, 2)),  -- Added to track primary/secondary type
    PRIMARY KEY (pokemon_id, type_id),
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(id),
    FOREIGN KEY (type_id) REFERENCES types(id)
);

CREATE TABLE abilities (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE pokemon_abilities (
    pokemon_id INTEGER,
    ability_id INTEGER,
    PRIMARY KEY (pokemon_id, ability_id),
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(id),
    FOREIGN KEY (ability_id) REFERENCES abilities(id)
);

CREATE TABLE moves (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,  
    type_id INTEGER,
    category TEXT CHECK(category IN ('Physical', 'Special', 'Status')),
    power INTEGER,
    accuracy INTEGER,
    pp INTEGER,
    FOREIGN KEY (type_id) REFERENCES types(id)
);

CREATE TABLE pokemon_moves (
    pokemon_id INTEGER,
    move_id INTEGER,
    method TEXT,
    level INTEGER,
    PRIMARY KEY (pokemon_id, move_id, method),  -- Include method in PK
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(id),
    FOREIGN KEY (move_id) REFERENCES moves(id)
);

CREATE TABLE evolutions (
    base_pokemon_id INTEGER,
    evolved_pokemon_id INTEGER,
    method TEXT,
    level INTEGER,
    item TEXT,
    counter INTEGER NOT NULL UNIQUE,
    PRIMARY KEY (base_pokemon_id, evolved_pokemon_id, counter),  
    FOREIGN KEY (base_pokemon_id) REFERENCES pokemon(id),
    FOREIGN KEY (evolved_pokemon_id) REFERENCES pokemon(id)
);