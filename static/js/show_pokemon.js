angular.module('pokemonInfoApp', [])
  .controller('pokemonInfoController', function($scope, $http) {
    $scope.pokemon = [];
    $scope.pokedexes = [];
    $scope.moves = [];
    $scope.getData = function (pokemon_id) {
      $http.get('/static/testdata/pokemon/' + pokemon_id + '.json')
        .success(function(data) {
          $scope.pokemon.push(data["data"]);
          var pokedex_ids = data["data"]["pokedexes"];
          var move_ids = data["data"]["moves"];

          angular.forEach(pokedex_ids, function(value, index) {
            $http.get('/static/testdata/pokedexes/' + value + '.json')
              .success(function(pokedex_data) {
                $scope.pokedexes.push(pokedex_data["data"]);
              });
          });

          angular.forEach(move_ids, function(value, index) {
            $http.get('/static/testdata/moves/' + value + '.json')
              .success(function(move_data) {
                $scope.moves.push(move_data["data"]);
              });
          });

          $scope.pokemonLower = $scope.pokemon[0]["name"].toLowerCase();
      });
    }
  });
