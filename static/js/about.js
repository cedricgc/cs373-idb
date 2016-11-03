angular.module('aboutApp', [])
  .controller('aboutController', function($scope, $http) {
    $scope.runUnitTests = function() {
      $scope.unitTestWelcome = "Currently running the unit tests:";

      $http.get('/test/').success(function(data) {
        $scope.unitTestResults = data;
      });
    }

  });
