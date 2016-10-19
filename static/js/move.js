angular.module('moveApp', [])
    .controller('moveController', function($scope, $http, $window) {
        $scope.moves = [];
        $scope.pokemon = [];
        $scope.getData = function (move_id){
            $http.get('../static/testdata.json')
                .success(function(data) {
                var all_moves = data["moves"];
                var all_pokemon = data["pokemon"];
                angular.forEach(all_moves, function(value, index){
                    if(value["id"] == move_id) {
                        $scope.moves.push(value);
                    }
                });

                angular.forEach(all_pokemon, function(value, index){
                    var pokemon_id_index = $scope.moves[0]["pokemon"].indexOf(value["id"]);
                    if(pokemon_id_index != -1) {
                        $scope.pokemon.push(value);
                    }
                });
            });

        }
});
