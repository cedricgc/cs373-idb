angular.module('moveApp', [])
    .controller('moveController', function($scope, $http, $window) {
        $scope.instance = [];

        $scope.initInstance = function (move_id){
            $http.get('../static/testdata.json')
                .success(function(data) {
                $scope.moves = data["moves"];
                angular.forEach($scope.moves, function(value, index){
                    if(value["id"] == move_id) {
                        $scope.instance.push(value);
                    }
                });
            });
        }
});
