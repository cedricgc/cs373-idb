angular.module('pokedexApp', [])
    .controller('pokedexController', function($scope, $http) {
        $scope.pokedex = [];
        $scope.pokemon = [];
        $scope.getData = function (pokedex_id){
            $http.get('../static/testdata.json')
                .success(function(data) {
                var all_pokedexes = data["pokedexes"];
                var all_pokemon = data["pokemon"];
                angular.forEach(all_pokedexes, function(value, index){
                    if(value["id"] == pokedex_id) {
                        $scope.pokedex.push(value);
                    }
                });

                angular.forEach(all_pokemon, function(value, index){
                    var pokemon_id_index = $scope.pokedex[0]["pokemon"].indexOf(value["id"]);
                    if(pokemon_id_index != -1) {
                        $scope.pokemon.push(value);
                    }
                });
            });
        }
});
