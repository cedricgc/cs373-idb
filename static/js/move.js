angular.module('moveApp', [])
    .controller('moveController', function($scope) {
        $scope.moves = [
            {id: 33, name: "Tackle", flavor_text: "A physical attack in which the user\ncharges and slams into the target\nwith its whole body.", short_effect: "Inflicts regular damage with no additional effect.", effect: "Inflicts regular damage.", damage_class: "physical", power_points: 35, power: 50, accuracy: 100},
            {id: 10, name: "Scratch", flavor_text: "Hard, pointed, sharp claws rake\nthe target to inflict damage.", short_effect: "Inflicts regular damage with no additional effect.", effect: "Inflicts regular damage.", damage_class: "physical", power_points: 35, power: 40, accuracy: 100},
            {id: 15, name: "Cut", flavor_text: "The target is cut with a scythe or claw.\nThis can also be used to cut down thin trees.", short_effect: "Inflicts regular damage with no additional effect.", effect: "Inflicts regular damage.", damage_class: "physical", power_points: 30, power: 50, accuracy: 95}
        ];


        $scope.instance = [];

        $scope.initInstance = function (move_id){
        	angular.forEach($scope.moves, function(value, index){
        		if(value["id"] == move_id) {
        			$scope.instance.push(value);
        		}
        	});
        }
});
