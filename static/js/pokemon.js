angular.module('pokemonApp', [])
    .controller('pokemonController', function($scope) {
        $scope.pokemon = [
            {id: 1, name: "Bulbasaur", flavor_text: "Bulbasaur can be seen napping in bright sunlight.\nThere is a seed on its back. By soaking up the sun\u2019s rays,\nthe seed grows progressively larger", habitat: "grassland", color: "green", shape: "quadruped"},
            {id: 4, name: "Charmander", flavor_text: "The flame that burns at the tip of its tail is an indication\nof its emotions. The flame wavers when Charmander\nis enjoying itself. If the Pok\u00e9mon becomes enraged,\nthe flame burns fiercely.", habitat: "mountain", color: "red", shape: "upright"},
            {id: 7, name: "Squirtle", flavor_text: "Bulbasaur can be seen napping in bright sunlight.\nThere is a seed on its back. By soaking up the sun\u2019s rays,\nthe seed grows progressively larger", habitat: "waters-edge", color: "blue", shape: "upright"},
        ];
});
