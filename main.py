from database import Database
from save_json import writeAJson

db = Database(database="dex", collection="pokemons")
db.resetDatabase()
pokemons = db.collection.find()

#1 - Filtrando os pokemons com Speed(velocidade) <= 50
def Speed_less_than_50(speed: int):
    return db.collection.find({"base.Speed":{"$lte":speed}})

speed = Speed_less_than_50(50)
writeAJson(speed, "Velocidade_do_pokemon")

#2-Retornando o pokemon de id = 146
def getPokemonById(number: id):
    return db.collection.find({"id": number})

pokemon_misterioso = getPokemonById(146)
writeAJson(pokemon_misterioso, "pokemon_id_146")

#3 - Filtrando os Pokemons pelo tipo "Poision"
def getPokemonByType(type: str):
    return db.collection.find({"type": type})

fire = getPokemonByType("Poison")
writeAJson(fire, "Pokemon_tipo_Poison")

#4 - Filtrando os nomes dos pokemons que possuem menos ou 8 letras em ingles e frances
def get_5_letters_or_less(collection):
    names = collection.find({}, {"name.english": 1, "name.french": 2})
    five_letters = []
    for name in names:
        if len(name["name"].keys()) <= 8:
            if all(len(word) <= 8 for word in name["name"].values()):
                five_letters.append(name["name"].values())
    return five_letters

writeAJson(get_5_letters_or_less(db.collection), "pokemon_8_letras")

#5 - Filtrando os Pokemons pelo tipo("Fire") e velocidade(<=20)
def Type_And_Speed(type:str, speed: int):
    return db.collection.find({"type":type, "base.Speed":{"$lte":speed}})

type_speed = Type_And_Speed("Fire", 20)
writeAJson(type_speed, "type_and_speed")


