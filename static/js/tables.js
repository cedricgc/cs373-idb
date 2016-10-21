angular.module('tableApp', [])
  .service('tableService', function() {
    this.sortSwitch = function (column_name, tableVars) {
      if(column_name != tableVars["sortTerm"]) {
        tableVars["sortTerm"] = column_name;
        tableVars["reverse"] = false;
      } else {
        tableVars["reverse"] = !tableVars["reverse"];
      }
    }

    this.isAscending = function(column_name, tableVars) {
      if(column_name == tableVars["sortTerm"] && tableVars["reverse"]) {
        return true;
      }
      return false;
    }

    this.isDescending = function(column_name, tableVars) {
      if(column_name == tableVars["sortTerm"] && !tableVars["reverse"]) {
        return true;
      }
      return false;
    }
  });
