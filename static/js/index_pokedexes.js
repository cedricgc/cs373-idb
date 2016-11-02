angular.module('pokedexesApp', ['tableApp'])
  .controller('pokedexesController', function($scope, $http, tableService) {
    $scope.currentPage = 4;
    $scope.totalPages = 10;


    $http.get('/static/testdata/pokedexes.json').success(function(data) {
      $scope.pokedexes = data["data"];
    });

    $scope.pageRange = function () {
      if ($scope.currentPage <= 2) {
        return [1, 2, 3];
      } else if ($scope.totalPages - $scope.currentPage <= 2) {
        return [$scope.totalPages - 2, $scope.totalPages - 1, $scope.totalPages];
      } else {
        return [$scope.currentPage - 1, $scope.currentPage, $scope.currentPage + 1];
      }
    }

    $scope.nextPage = function() {
      if($scope.currentPage < $scope.totalPages){
        $scope.currentPage++;
      }
    }

    $scope.prevPage = function() {
      if($scope.currentPage > 1){
        $scope.currentPage--;
      }
    }

    $scope.skipBack = function() {
      $scope.currentPage -= 2;
    }

    $scope.skipForward = function() {
      $scope.currentPage += 2;
    }

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
