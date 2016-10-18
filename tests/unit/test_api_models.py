# -*- coding: utf-8 -*-


import unittest

import website.api.models as models

pokedex = {
    'id': 1,
    'name': 'kanto',
    'official_name': 'Original Kanto',
    'region': 'Kanto',
    'description': 'This is a list of Pokémon in the order dictated by the Kanto regional Pokédex'
}

pokemon = {
    'id': 1,
    'name': 'Bulbasaur',
    'flavor_text': 'A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon.',
    'habitat': 'grassland',
    'color': 'green',
    'shape': 'quadruped'
}

move = {
    'id': 1,
    'name': 'Razor Wind',
    'flavor_text': 'A two-turn attack. Blades of wind hit opposing Pokémon on the second turn. Critical hits land more easily.',
    'short_effect': 'Requires a turn to charge before attacking.',
    'effect': 'Inflicts regular damage.  User\'s critical hit rate is one level higher when using this move.  User charges for one turn before attacking. This move cannot be selected by sleep talk.',
    'damage_class': 'special',
    'power_points': 10,
    'power': 80,
    'accuracy': 100,
}


class TestPokedex(unittest.TestCase):

    def test_create_pokedex(self):
        pd = models.Pokedex(**pokedex)

        self.assertEqual(pd.id, 1)
        self.assertEqual(pd.name, 'kanto')

    def test_pokedex_repr(self):
        pd = models.Pokedex(**pokedex)

        self.assertEqual(repr(pd), '<Pokedex kanto>')

    def test_pokedex_relationship(self):
        pd = models.Pokedex(**pokedex)
        po = models.Pokemon(**pokemon)
        pd.pokemon = [po]

        self.assertEqual(pd.pokemon, [po])


class TestPokemon(unittest.TestCase):

    def test_create_pokemon(self):
        po = models.Pokemon(**pokemon)

        self.assertEqual(po.id, 1)
        self.assertEqual(po.name, 'Bulbasaur')

    def test_pokemon_repr(self):
        po = models.Pokemon(**pokemon)

        self.assertEqual(repr(po), '<Pokemon Bulbasaur>')

    def test_pokemon_relationship(self):
        po = models.Pokemon(**pokemon)
        pd = models.Pokedex(**pokedex)
        po.pokedexes = [pd]

        self.assertEqual(po.pokedexes, [pd])

    def test_pokemon_relationship_2(self):
        po = models.Pokemon(**pokemon)
        m = models.Move(**move)
        po.moves = [m]

        self.assertEqual(po.moves, [m])


class TestMove(unittest.TestCase):

    def test_create_move(self):
        m = models.Move(**move)

        self.assertEqual(m.id, 1)
        self.assertEqual(m.name, 'Razor Wind')

    def test_move_repr(self):
        m = models.Move(**move)

        self.assertEqual(repr(m), '<Move Razor Wind>')

    def test_move_relationship(self):
        m = models.Move(**move)
        po = models.Pokemon(**pokemon)
        m.pokemon = [po]

        self.assertEqual(m.pokemon, [po])


if __name__ == "__main__":
    unittest.main()
