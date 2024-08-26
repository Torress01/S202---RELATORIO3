from database import Database
from pokedex import Pokedex

if __name__ == '__main__':
    database = Database(database="pokedex", collection="pokemons")
    pokedex = Pokedex(database)

    pokedex.get_pokemon_by_name('Charmander')
    pokedex.get_pokemon_by_num('015')
    pokedex.get_pokemon_by_type('Water')
    pokedex.get_pokemon_by_id(23)
    pokedex.get_pokemon_by_weakness('Fire')

