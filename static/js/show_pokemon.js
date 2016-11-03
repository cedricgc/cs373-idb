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
            $http.get('/api/v1/pokedexes/' + value)
              .success(function(pokedex_data) {
                $scope.pokedexes.push(pokedex_data["data"]);
              });
          });

          angular.forEach(move_ids, function(value, index) {
            $http.get('/api/v1/moves/' + value)
              .success(function(move_data) {
                $scope.moves.push(move_data["data"]);
              });
          });

          $scope.pokemonLower = $scope.pokemon[0]["name"].toLowerCase();
      });
    }
  });
