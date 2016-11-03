angular.module('moveApp', [])
  .controller('moveController', function($scope, $http, $window) {
    $scope.moves = [];
    $scope.pokemon = [];
    $scope.getData = function (move_id) {
      $http.get('/static/testdata/moves/' + move_id + '.json')
        .success(function(data) {
          $scope.moves.push(data["data"]);
          var pokemon_ids = data["data"]["pokemon"];

          angular.forEach(pokemon_ids, function(value, index) {
            $http.get('/static/testdata/pokemon/' + value + '.json')
              .success(function(pokemon_data) {
                $scope.pokemon.push(pokemon_data["data"]);
              });
          });
      });    }
  });
