angular.module('pokedexesApp', ['tableApp'])
  .controller('pokedexesController', function($scope, $http, tableService) {
    $http.get('/static/testdata.json').success(function(data) {
      $scope.pokedexes = data["pokedexes"];
    });

    var tableVars = {"sortTerm" : 'id', "reverse" : false};

    $scope.switch = function (column_name) {
      return tableService.sortSwitch(column_name, tableVars);
    }

    $scope.isAscending = function(column_name) {
      return tableService.isAscending(column_name, tableVars);
    }

    $scope.isDescending = function(column_name) {
      return tableService.isDescending(column_name, tableVars);
    }

    $scope.getSortTerm = function () {
      return tableVars["sortTerm"];
    }

    $scope.getReverse = function () {
      return tableVars["reverse"];
    }
  });
