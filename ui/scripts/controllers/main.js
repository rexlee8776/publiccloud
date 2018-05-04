'use strict';

/**
 * @ngdoc function
 * @name opnfvdashBoardAngularApp.controller:MainPageController
 * @description
 * # TableController
 * Controller of the opnfvdashBoardAngularApp
 */
angular.module('opnfvApp')
    .controller('HomeController', ['$scope', '$state', '$stateParams', '$cookies', 'TableFactory', function($scope, $state, $stateParams, $cookies, TableFactory) {

        init();

        function init() {
            $scope.goTest = goTest;
            $scope.goLogin = goLogin;

            $scope.logout = logout;

            checkLogin();
        }

        function goTest() {
            $state.go("select.selectTestCase");
        }

        function goLogin() {
            $state.go("login");
        }

        function logout(){

            TableFactory.logout(function(resp){
                if(resp.data.status == 'success'){
                    $cookies.remove('isLogin');
                    $scope.isLogin = false;
                    $state.go('login');
                }else{
                    alert(resp.data.msg);
                }
            }, function(err){
                alert('unexpected error');
            });

        }

        function checkLogin(){
            if($cookies.get('isLogin') == 'true'){
                $scope.isLogin = true;
            }else{
                $scope.isLogin = false;
            }
        }

    }]);
