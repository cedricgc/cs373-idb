angular.module('pokemonInfoApp', [])
  .controller('pokemonInfoController', function($scope, $http) {
    $scope.pokemon = [];
    $scope.pokedexes = [];
    $scope.moves = [];
    $scope.getData = function (pokemon_id) {
      $http.get('/api/v1/pokemon/' + pokemon_id)
        .success(function(data) {
          $scope.pokemon.push(data["data"]);
          var pokedex_ids = data["data"]["pokedexes"];
          var move_ids = data["data"]["moves"];

          angular.forEach(pokedex_ids, function(value, index) {
            $scope.pokedexes.push(value);
          });

          angular.forEach(move_ids, function(value, index) {
            $scope.moves.push(value);
          });

          $scope.pokemonLower = $scope.pokemon[0]["name"].toLowerCase();
      });
    }
  });
