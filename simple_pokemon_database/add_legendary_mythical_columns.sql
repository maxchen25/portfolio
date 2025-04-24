-- Adds is_legendary and is_mythical to pokemon table
ALTER TABLE pokemon ADD COLUMN is_legendary INTEGER DEFAULT 0;
ALTER TABLE pokemon ADD COLUMN is_mythical INTEGER DEFAULT 0;

-- Set is_legendary = 1 for all legendary Pokemon
UPDATE pokemon 
SET is_legendary = 1 
WHERE name IN (
'articuno', 'articuno-galar', 'zapdos', 'zapdos-galar', 'moltres', 'moltres-galar', 
'mewtwo', 'mewtwo-mega-x', 'mewtwo-mega-y', 'raikou', 'entei', 'suicune', 
'lugia', 'ho-oh', 'regirock', 'regice', 'registeel', 'latias', 'latias-mega', 
'latios', 'latios-mega', 'kyogre', 'kyogre-primal', 'groudon', 'groudon-primal', 
'rayquaza', 'rayquaza-mega', 'uxie', 'mesprit', 'azelf', 'dialga', 'dialga-origin', 
'palkia', 'palkia-origin', 'heatran', 'regigigas', 'giratina-altered', 'giratina-origin', 
'cresselia', 'cobalion', 'terrakion', 'virizion', 'tornadus-incarnate', 'tornadus-therian', 
'thundurus-incarnate', 'thundurus-therian', 'reshiram', 'zekrom', 'landorus-incarnate', 
'landorus-therian', 'kyurem', 'kyurem-black', 'kyurem-white', 'xerneas', 'yveltal', 'zygarde-50', 
'zygarde-10-power-construct', 'zygarde-50-power-construct', 'zygarde-complete', 'zygarde-10', 
'type-null', 'silvally', 'tapu-koko', 'tapu-lele', 'tapu-bulu', 'tapu-fini', 'cosmog', 
'cosmoem', 'solgaleo', 'lunala', 'necrozma', 'necrozma-dusk', 'necrozma-dawn', 'necrozma-ultra', 
'zacian', 'zacian-crowned', 'zamazenta', 'zamazenta-crowned', 'eternatus', 'eternatus-eternamax', 
'kubfu', 'urshifu-single-strike', 'urshifu-rapid-strike', 'urshifu-single-strike-gmax', 
'urshifu-rapid-strike-gmax', 'regieleki', 'regidrago', 'glastrier', 'spectrier', 'calyrex', 
'calyrex-ice', 'calyrex-shadow', 'enamorus-incarnate', 'enamorus-therian', 'wo-chien', 
'chien-pao', 'ting-lu', 'chi-yu', 'koraidon', 'koraidon-limited-build', 'koraidon-sprinting-build', 
'koraidon-swimming-build', 'koraidon-gliding-build', 'miraidon', 'miraidon-low-power-mode', 
'miraidon-drive-mode', 'miraidon-aquatic-mode', 'miraidon-glide-mode', 'okidogi', 'munkidori', 
'fezandipiti', 'ogerpon', 'ogerpon-wellspring-mask', 'ogerpon-hearthflame-mask', 
'ogerpon-cornerstone-mask', 'terapagos', 'terapagos-terastal', 'terapagos-stellar'
);

-- Set is_mythical = 1 for all mythcial Pokemon
UPDATE pokemon
SET is_mythical = 1
WHERE name IN (
    'mew', 'celebi', 'jirachi', 'deoxys-normal', 'deoxys-attack', 'deoxys-defense', 'deoxys-speed', 
    'phione', 'manaphy', 'darkrai', 'shaymin-land', 'shaymin-sky', 'arceus', 'victini', 'keldeo-ordinary', 
    'keldeo-resolute', 'meloetta-aria', 'meloetta-pirouette', 'genesect', 'diancie', 'diancie-mega', 
    'hoopa', 'hoopa-unbound', 'volcanion', 'magearna', 'magearna-original', 'marshadow', 'zeraora', 
    'meltan', 'melmetal', 'melmetal-gmax', 'zarude', 'zarude-dada', 'pecharunt'
);