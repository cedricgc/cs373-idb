angular.module('pokemonInfoApp', [])
    .controller('pokemonInfoController', function($scope, $http) {
        $scope.pokemon = [];
        $scope.pokedexes = [];
        $scope.moves = [];
        $scope.getData = function (pokemon_id){
            $http.get('../static/testdata.json')
                .success(function(data) {
                var all_pokemon = data["pokemon"];
                var all_pokedexes = data["pokedexes"];
                var all_moves = data["moves"];
                angular.forEach(all_pokemon, function(value, index){
                    if(value["id"] == pokemon_id) {
                        $scope.pokemon.push(value);
                    }
                });

                angular.forEach(all_pokedexes, function(value, index){
                	var pokedex_id_index = $scope.pokemon[0]["pokedexes"].indexOf(value["id"]);
                	console.log(pokedex_id_index);
                    if(pokedex_id_index != -1) {
                        $scope.pokedexes.push(value);
                    }
                });

                angular.forEach(all_moves, function(value, index){
                	var move_id_index = $scope.pokemon[0]["moves"].indexOf(value["id"]);
                	console.log(move_id_index);
                    if(move_id_index != -1) {
                        $scope.moves.push(value);
                    }
                });

                $scope.pokemonLower = $scope.pokemon[0]["name"].toLowerCase();
            });
        }
	});
