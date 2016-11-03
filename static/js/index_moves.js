angular.module('movesApp', ['tableApp'])
  .controller('movesController', function($scope, $http, tableService) {
    $scope.loadData = function(page_id) {
      $http.get('/static/testdata/moves' + page_id + '.json').success(function(data) {
        $scope.moves = data["data"];
        $scope.hasPrevious = data["has_previous"];
        $scope.hasNext = data["has_next"];
        $scope.totalPages = data["total_pages"];
      });
    }

    //default page to 1
    $scope.currentPage = 1;

    //load data initially
    $scope.loadData($scope.currentPage);

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
      $scope.loadData($scope.currentPage);
    }

    $scope.prevPage = function() {
      if($scope.currentPage > 1){
        $scope.currentPage--;
      }
      $scope.loadData($scope.currentPage);
    }

    $scope.skipBack = function() {
      $scope.currentPage -= 2;
      $scope.loadData($scope.currentPage);
    }

    $scope.skipForward = function() {
      $scope.currentPage += 2;
      $scope.loadData($scope.currentPage);
    }

    $scope.setPage = function(page) {
      $scope.currentPage = page;
      $scope.loadData($scope.currentPage);
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
