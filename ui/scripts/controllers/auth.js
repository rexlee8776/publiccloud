'use strict';

/**
 * @ngdoc function
 * @name opnfvdashBoardAngularApp.controller:CaseController
 * @description
 * # TableController
 * Controller of the opnfvdashBoardAngularApp
 */
angular.module('opnfvApp')
    .controller('AuthController', ['$scope', '$state', '$stateParams', 'TableFactory', '$http', '$cookies', function($scope, $state, $stateParams, TableFactory, $http, $cookies) {

        init();

        function init() {
            $scope.login = login;
            $scope.register = register;
        }

        function login() {
            TableFactory.login($scope.username, $scope.password, function(resp){
                if(resp.data.status == 'success'){
                    $cookies.put('isLogin', 'true');
                    $state.go('home.services');
                }else{
                    alert(resp.data.msg);
                }
            }, function(err){
                alert('login error');
            });
        }

        function register(){

            TableFactory.register($scope.username, $scope.password, function(resp){
                if(resp.data.status == 'success'){
                    $cookies.put('isLogin', 'true');
                    $state.go('home.services');
                }else{
                }
            }, function(err){
                alert('register error');
            });
        }

    }]);
