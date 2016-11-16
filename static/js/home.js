angular.module('homeApp', [])
  .controller('homeController', function($scope, $http) {
    $scope.searchQuery = null;
    $scope.multi = false;
    $scope.pokemon_and = [];
    $scope.pokedexes_and = [];
    $scope.moves_and = [];
    $scope.pokemon_or = [];
    $scope.pokedexes_or = [];
    $scope.moves_or = [];

    $scope.getSearchResults = function() {
      $scope.searchResultContext = "Displaying results for: \"" + $scope.searchQuery + "\"";
      $scope.pokemon_and = [];
      $scope.pokedexes_and = [];
      $scope.moves_and = [];
      $scope.pokemon_or = [];
      $scope.pokedexes_or = [];
      $scope.moves_or = [];

      var query_terms = $scope.searchQuery.split(' ');

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

      if(query_terms.length > 1) {
        $scope.multi = true;
        var query_or = query_terms.join(" or ");
        var request_data_or = { 'data' : { 'query' : query_or }};
        
        $http.post('api/v1/search', request_data_or).success(function(data) {
          var pokemon_or_ids = data["data"]["pokemon"];
          var pokedexes_or_ids = data["data"]["pokedexes"];
          var moves_or_ids = data["data"]["moves"];

          angular.forEach(pokemon_or_ids, function(value, index) {
            $scope.pokemon_or.push(value);
          });

          angular.forEach(pokedexes_or_ids, function(value, index) {
            $scope.pokedexes_or.push(value);
          });

          angular.forEach(moves_or_ids, function(value, index) {
            $scope.moves_or.push(value);
          });
        });
      }else {
        $scope.multi = false;
      }
      
    }

  });
