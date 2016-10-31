angular.module('pokedexApp', [])
  .controller('pokedexController', function($scope, $http) {
    $scope.pokemon = [];
    $scope.pokedex = [];
    $scope.getData = function (pokedex_id) {
      $http.get('/static/testdata/pokedexes/' + pokedex_id + '.json')
        .success(function(data) {
          $scope.pokedex.push(data["data"]);
          console.log($scope.pokedex);
          var pokemon_ids = data["data"]["pokemon"];

          angular.forEach(pokemon_ids, function(value, index) {
            $http.get('/static/testdata/pokemon/' + value + '.json')
              .success(function(pokemon_data) {
                $scope.pokemon.push(pokemon_data["data"]);
              });
          });
      });
    }
  });
