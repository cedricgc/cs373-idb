angular.module('homeApp', [])
  .controller('homeController', function($scope, $http) {
    $scope.searchQuery = null;
    $scope.multi = false;
    $scope.pokemon_and = [];
    $scope.pokedexes_and = [];
    $scope.moves_and = [];

    $scope.getSearchResults = function() {
      $scope.searchResultContext = "Displaying results for: \"" + $scope.searchQuery + "\"";

      var request_data = { 'data' : { 'query' : $scope.searchQuery }};
 
      $http.post('api/v1/search', request_data).success(function(data) {
          var pokemon_and_ids = data["data"]["pokemon"];
          var pokedexes_and_ids = data["data"]["pokedexes"];
          var moves_and_ids = data["data"]["moves"];

          angular.forEach(pokemon_and_ids, function(value, index) {
            $scope.pokemon_and.push(value);
          });

          angular.forEach(pokedexes_and_ids, function(value, index) {
            $scope.pokedexes_and.push(value);
          });

          angular.forEach(moves_and_ids, function(value, index) {
            $scope.moves_and.push(value);
          });

      });
      
    }

  });
