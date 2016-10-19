angular.module('movesApp', [])
    .controller('movesController', function($scope, $http) {

        $http.get('static/testdata.json').success(function(data) {
    		$scope.moves = data["moves"];
    	});
});
