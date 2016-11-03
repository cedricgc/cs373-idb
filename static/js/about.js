angular.module('aboutApp', [])
  .controller('aboutController', function($scope, $http) {
    $scope.runUnitTests = function() {
      $scope.unitTestWelcome = "Currently running the unit tests";
      //run unit tests here?

      $scope.unitTestResults = "Results!";
    }


  });
