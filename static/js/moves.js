angular.module('movesApp', [])
    .controller('movesController', function($scope, $http, $window) {
        $http.get('static/testdata.json').success(function(data) {
    		$scope.moves = data["moves"];
    	});
});
