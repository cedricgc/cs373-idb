angular.module('pokemonApp', [])
    .controller('pokemonController', function($scope, $http) {
    	$http.get('static/testdata.json').success(function(data) {
    		$scope.pokemon = data["pokemon"];
    	});
	});