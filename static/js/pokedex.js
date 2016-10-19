angular.module('pokedexApp', [])
    .controller('pokedexController', function($scope) {
        $scope.pokedexes = [
        	{id: 1, name: "national", official_name: "National", region: null, description: "Entire National dex"},
        	{id: 2, name: "kanto", official_name: "Kanto", region: "kanto", description: "Red/Blue/Yellow Kanto dex"},
        	{id: 7, name: "updated-johto", official_name: "Updated Johto", region: "johto", description: "HeartGold/SoulSilver Johto dex—Gold/Silver/Crystal's, extended to add move-based Generation IV evolutions" }
        ];


        $scope.instance = [];

		$scope.initInstance = function (pokedex_id){
			angular.forEach($scope.pokedexes, function(value, index){
				if(value["id"] == pokedex_id) {
					$scope.instance.push(value);
				}
			});
		}
});
