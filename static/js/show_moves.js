angular.module('moveApp', [])
  .controller('moveController', function($scope, $http, $window) {
    $scope.moves = [];
    $scope.pokemon = [];
    $scope.getData = function (move_id) {
      $http.get('/api/v1/moves/' + move_id)
        .success(function(data) {
          $scope.moves.push(data["data"]);
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
