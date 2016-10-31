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

        // angular.forEach(all_pokemon, function(value, index) {
        //   var pokemon_id_index = $scope.pokedex[0]["pokemon"].indexOf(value["id"]);
        //   if(pokemon_id_index != -1) {
        //     $scope.pokemon.push(value);
        //   }
        // });
      });
    }
  });
