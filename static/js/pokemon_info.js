angular.module('pokemonInfoApp', [])
    .controller('pokemonInfoController', function($scope) {
        $scope.pokemon = [
            {id: 1, name: "Bulbasaur", flavor_text: "Bulbasaur can be seen napping in bright sunlight.\nThere is a seed on its back. By soaking up the sun\u2019s rays,\nthe seed grows progressively larger", habitat: "grassland", color: "green", shape: "quadruped"},
            {id: 4, name: "Charmander", flavor_text: "The flame that burns at the tip of its tail is an indication\nof its emotions. The flame wavers when Charmander\nis enjoying itself. If the Pok\u00e9mon becomes enraged,\nthe flame burns fiercely.", habitat: "mountain", color: "red", shape: "upright"},
            {id: 7, name: "Squirtle", flavor_text: "Squirtle\u2019s shell is not merely used for protection.\nThe shell\u2019s rounded shape and the grooves on its\nsurface help minimize resistance in water,\nenabling this Pok\u00e9mon to swim at high speeds.", habitat: "waters-edge", color: "blue", shape: "upright"}
        ];

        $scope.instance = [];

		$scope.initInstance = function (pokemon_id){
			angular.forEach($scope.pokemon, function(value, index){
				if(value["id"] == pokemon_id) {
					$scope.instance.push(value);
				}
			});
		}
});
