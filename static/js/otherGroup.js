angular.module('otherGroupApp', [])
  .controller('otherGroupController', function($scope, $http) {
  	$scope.authors = [];
  	$scope.author = {};
  	$scope.authorName = "";
  	$scope.book = "";

    $scope.loadData = function() {
      $http.get('/api/v1/otherGroup/').success(function(data) {
        $scope.authors = data;
        $scope.getNewAuthor();
      });


    }

    $scope.getNewAuthor = function() {
    	$scope.author = $scope.authors[Math.floor(Math.random() * $scope.authors.length)];
    	$scope.authorName = $scope.author["name"];
    	$scope.getNewBook();
    }

    $scope.getNewBook = function() {
    	$scope.book = $scope.author["books"][Math.floor(Math.random() * $scope.author["books"].length)]["title"];
    }

  });