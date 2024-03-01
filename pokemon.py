import random


class Pokemon:
    def __init__(self, especie=None, level= random.randint(1,100), nome=None):
        self.especie = especie
        self.level = level

        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return "{} ({})".format(self.nome, self.level)


    def pokemons_genericos (numero ):
        pokemons_genericos = [
            "Pikachu", "Raichu", "Jolteon", "Electabuzz", "Ampharos", "Magnezone", "Rotom", "Zapdos",
            "Electivire", "Eelektross", "Charmander", "Charizard", "Arcanine", "Vulpix", "Ninetales",
            "Magmar", "Flareon", "Typhlosion", "Entei", "Infernape", "Squirtle", "Vaporeon", "Blastoise",
            "Gyarados", "Lapras", "Suicune", "Milotic", "Empoleon", "Rotom forma lavadora", "Greninja",
            "Mewtwo", "Mew", "Alakazam", "Espeon", "Gardevoir", "Metagross", "Gallade", "Jirachi", "Uxie", "Meowstic"
        ]

        return pokemons_genericos[numero]

    def escolha_inicial(self):
        print("Aqui estã suas opções para iniciar sua jornada ")
        print("1-Charmander\n2-Squitle\n3-Bulbasaur\n")

        op = int(input("Escolha: "))
        pokemon_inicial = ["", "Charmander", "Squitle", "Bulbasaur"]
        print("")
        print("Ótima opção escolhida, boa sorte na sua jornada pokemon. ")

        return pokemon_inicial[op]

class PokemonEletrico (Pokemon):
    tipo = "Elétrico"
    pokemons_eletricos = ["Pikachu", "Raichu", "Jolteon", "Electabuzz", "Ampharos", "Magnezone", "Rotom", "Zapdos",
                          "Electivire", "Eelektross"]

    def atacar(self, pokemon):
        print("{} usou o raio do trovão em {}".format(self, pokemon, self.level))


class PokemonFogo(Pokemon):
    tipo = "Fogo"
    pokemons_fogo = ["Charmander", "Charizard", "Arcanine", "Vulpix", "Ninetales", "Magmar", "Flareon", "Typhlosion",
                     "Entei", "Infernape"]

    def atacar(self, pokemon):
        print("{} usou bola de fogo em {}".format(self, pokemon, self.level))


class PokemonAgua(Pokemon):
    tipo = "Aquático"
    pokemons_agua = ["Squirtle", "Vaporeon", "Blastoise", "Gyarados", "Lapras", "Suicune", "Milotic", "Empoleon",
                     "Rotom (forma lavadora)", "Greninja"]

    def atacar(self, pokemon):
        print("{} usou bola d'agua em {}".format(self, pokemon, self.level))


class Polemon_psiquicos(Pokemon):
    tipo = "psiquicos"
    pokemons_psiquicos = ["Mewtwo", "Mew", "Alakazam", "Espeon", "Gardevoir", "Metagross", "Gallade", "Jirachi", "Uxie", "Meowstic"]

    def atacar(self, pokemon):
        print("{} usou ataque de ikusão  em {}".format(self, pokemon, self.level))