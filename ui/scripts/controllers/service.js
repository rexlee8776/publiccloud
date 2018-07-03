'use strict';

/**
 * @ngdoc function
 * @name opnfvdashBoardAngularApp.controller:TableController
 * @description
 * # TableController
 * Controller of the opnfvdashBoardAngularApp
 */
angular.module('opnfvApp')
    .controller('ServiceController', ['$scope', '$state', '$stateParams', '$http', 'TableFactory', '$timeout', 'ngDialog',
        function($scope, $state, $stateParams, $http, TableFactory, $timeout, ngDialog) {

            init();

            function init(){
                $scope.services = [];
                $scope.serviceName = '';

                $scope.openAddServiceModal = openAddServiceModal;
                $scope.addService = addService;

                _getServiceList();
            }

            function addService(name){
                TableFactory.addService(name, function(resp){
                    if(resp.data.status == 'success'){
                        $scope.services.push(resp.data.service);
                        ngDialog.close();
                    }else{
                        alert(resp.data.msg);
                    }
                }, function(err){
                    alert('Add service error!');
                });
            }

            function openAddServiceModal(){
                ngDialog.open({
                    preCloseCallback: function() {},
                    template: 'views/modal/addServiceModal.html',
                    scope: $scope,
                    className: 'ngdialog-theme-default',
                    width: 950,
                    showClose: true,
                    closeByDocument: true
                });
            }

            function _getServiceList(){

                TableFactory.getServiceList(function(resp){
                    if(resp.data.status == 'success'){
                        $scope.services = resp.data.services;
                    }else{
                        alert(resp.data.msg);
                    }
                }, function(err){
                    if(err.status == 400){
                        $state.go('login');
                    }else{
                        alert('get service error');
                    }
                });
            }

        }
    ]);
