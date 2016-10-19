angular.module('pokemonApp', [])
    .controller('pokemonController', function($scope, $http) {
    	$http.get('static/testdata.json').success(function(data) {
    		$scope.pokemon = data["pokemon"];
    	});

        $scope.sortTerm = 'id';
        $scope.reverse = false;

        $scope.switch = function (column_name) {
            console.log("switching to " + column_name)
            if(column_name != $scope.sortTerm) {
                $scope.sortTerm = column_name;
                $scope.reverse = false;
            } else {
                $scope.reverse = !$scope.reverse;
            }
        }

        $scope.isAscending = function(column_name) {
            if(column_name == $scope.sortTerm && $scope.reverse) {
                console.log("True!!!");
                return true;
            }

            return false;
        }

        $scope.isDescending = function(column_name) {
            if(column_name == $scope.sortTerm && !$scope.reverse) {
                return true;
            }

            return false;
        }

	});