angular.module('pokedexApp', [])
  .controller('pokedexController', function($scope, $http) {
    $scope.pokemon = [];
    $scope.pokedex = [];
    $scope.getData = function (pokedex_id) {
      $http.get('/api/v1/pokedexes' + pokedex_id)
        .success(function(data) {
          $scope.pokedex.push(data["data"]);
          var pokemon_ids = data["data"]["pokemon"];

          angular.forEach(pokemon_ids, function(value, index) {
            $http.get('/api/v1/pokemon/' + value)
              .success(function(pokemon_data) {
                $scope.pokemon.push(pokemon_data["data"]);
              });
          });
      });
    }
  });
