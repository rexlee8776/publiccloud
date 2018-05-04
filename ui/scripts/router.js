'use strict'
/**
 * @ngdoc function
 * @name opnfvdashBoardAngularApp.config:config.router.js
 * @description config of the ui router and lazy load setting
 * config of the opnfvdashBoardAngularApp
 */
angular.module('opnfvApp')
    .run([
        '$rootScope', '$state', '$stateParams',
        function($rootScope, $state, $stateParams) {

            $rootScope.$state = $state;
            $rootScope.$stateParams = $stateParams;

        }
    ]).config(['$stateProvider', '$urlRouterProvider',
        function($stateProvider, $urlRouterProvider) {

            $urlRouterProvider.otherwise('/home/services');

            $stateProvider
                .state('home', {
                    url: "/home",
                    controller: 'HomeController',
                    templateUrl: "views/home.html",
                    data: { pageTitle: 'index', specialClass: 'landing-page' },
                    resolve: {
                        controller: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([

                            ])
                        }]
                    }
                })
                .state('home.services', {
                    url: "/services",
                    controller: 'ServiceController',
                    templateUrl: "views/commons/service.html",
                    resolve: {
                        controller: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([
                            ])
                        }]
                    }
                })
                .state('login', {
                    url: "/login",
                    controller: 'AuthController',
                    templateUrl: "views/login.html",
                    data: { pageTitle: 'login', specialClass: 'landing-page' },
                    resolve: {
                        controller: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([
                            ])
                        }]
                    }
                })
                .state('register', {
                    url: "/register",
                    controller: 'AuthController',
                    templateUrl: "views/register.html",
                    data: { pageTitle: 'register', specialClass: 'landing-page' },
                    resolve: {
                        controller: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([

                            ])
                        }]
                    }
                })
        }
    ])
    .run();
