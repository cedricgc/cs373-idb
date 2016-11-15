angular.module('homeApp', [])
  .controller('homeController', function($scope, $http) {
    $scope.searchQuery = null;
    $scope.getSearchResults = function() {

      $scope.searchResultContext = "Displaying results for: \"" + $scope.searchQuery + "\"";
      var request_data = { 'data' : { 'query' : $scope.searchQuery }};
 
      $http.post('api/v1/search', request_data).success(function(data) {
        $scope.unitTestResults = data;
      });
    }

  });
