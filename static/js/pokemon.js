angular.module('pokemonApp', [])
    .controller('pokemonController', function($scope, $http) {
    	$scope.sortPokemon = 'id';
    	$scope.reversePokemon = false;
    	$http.get('static/testdata.json').success(function(data) {
    		$scope.pokemon = data["pokemon"];
    	});
});
