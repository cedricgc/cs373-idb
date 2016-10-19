angular.module('pokedexApp', [])
    .controller('pokedexController', function($scope, $http) {
        $scope.instance = [];

        $scope.initInstance = function (pokedex_id){
            $http.get('../static/testdata.json')
                .success(function(data) {
                $scope.pokedexes = data["pokedexes"];
                angular.forEach($scope.pokedexes, function(value, index){
                    if(value["id"] == pokedex_id) {
                        $scope.instance.push(value);
                    }
                });
            });
        }
});
