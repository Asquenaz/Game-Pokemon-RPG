from random import randint, random
import pokemon
from pokemon import *




class Pessoa:
    def __init__(self, nome = None, pokemons=[]):
        self.pokemons = []

        if not nome and len(pokemons) == 0:
            nome = str(input("Informe o seu nome: "))
            self.nome = nome
            print("Olá, {}.".format(nome))
            print("")
            self.pokemons.append(Pokemon.escolha_inicial(self))

            mostrar_lista_pokemons(self)
        else:
            self.nome = "Player 1"



def mostrar_lista_pokemons (self):
    if len(self.pokemons) == 0:
        print("Você ainda não tem nenhum pokemon")
    else:
        print("Sua lista de pokemons capturados: ")
        for pokemon in self.pokemons:
            print(pokemon)


class player(Pessoa):
    tipo = "player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("")
        print("{} capturou {}".format(self.nome, pokemon))
        print("")


class inimigo(Pessoa):
    # tipo = "inimigo"

    # noinspection PyTypeChecker
    def escolherInimigo(pos):
        personagens_pokemon = [
            "Ash Ketchum", "Misty", "Brock", "May", "Dawn", "Serena", "Clemont", "Lillie", "Kiawe",
            "Goh", "Lt. Surge", "Erika", "Sabrina", "Blaine", " Giovanni",
            "Jessie", "James", "Meowth", "Red", "Blue", "Ethan", "Lyra",
            "Brendan", 'May', "Lucas", "Dawn", "Hilbert", "Hilda", "Calem", "Serena"
        ]
        personagem_aleatorio = personagens_pokemon[pos]
        return "BEM VINDO AO GINÁSIO POKEMÓN, SEU(A) OPONENTE SE CHAMA '{}' ... ".format(personagem_aleatorio).upper()
        # print

    def pokemon_inimigo(self=None):
        poke_inimigo = Pokemon.pokemons_genericos(random.randint(1, 40))
        print("")
        return "Ele utilizará o pokemon {}\nBOA SORTE".format(poke_inimigo)
