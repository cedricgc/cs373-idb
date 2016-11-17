angular.module('otherGroupApp', [])
  .controller('otherGroupController', function($scope, $http) {
    $scope.loadData = function(page_id) {
      $http.get('/api/v1/otherGroup/').success(function(data) {
        $scope.authors = data;
      });

    }
  });