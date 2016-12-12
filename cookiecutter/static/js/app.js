(function() {
var app = angular.module('MyApp', []);

app.controller('ProfileController', ['$scope', '$http', function ($scope, $http) {
              $http.get('http://127.0.0.1:8000/profile/all/').success(
                function (response) {
                  console.log(response);
                  $scope.profiles = response;
                });
      }]);
})();
