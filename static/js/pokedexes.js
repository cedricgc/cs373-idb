angular.module('pokedexesApp', [])
    .controller('pokedexesController', function($scope, $http) {
        $http.get('static/testdata.json').success(function(data) {
    		$scope.pokedexes = data["pokedexes"];
    	});

	});
