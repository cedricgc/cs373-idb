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
            $scope.moves.push(value);
          });
      });    
    }
  });
