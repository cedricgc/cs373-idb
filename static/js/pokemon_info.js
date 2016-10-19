angular.module('pokemonInfoApp', [])
    .controller('pokemonInfoController', function($scope, $http) {
        $scope.instance = [];

        $scope.initInstance = function (pokemon_id){
            $http.get('../static/testdata.json')
                .success(function(data) {
                $scope.pokemon = data["pokemon"];
                angular.forEach($scope.pokemon, function(value, index){
                    if(value["id"] == pokemon_id) {
                        $scope.instance.push(value);
                    }
                });
            });
        }
});
