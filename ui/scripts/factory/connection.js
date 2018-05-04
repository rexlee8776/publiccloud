'use strict';

/**
 * get data factory
 */
angular.module('opnfvApp')
    .factory('TableFactory', function($resource, $rootScope, $http) {

        function url(path){
            var BASE_URL = 'http://' + location.host;
            return BASE_URL + path;
        }

        function get(path, func1, func2){
            $http.get(url(path)).then(func1, func2);
        }

        function post(path, data, func1, func2){
            $http.post(url(path), data).then(func1, func2);
        }

        return {
            // User Interface
            register: function(username, passwd, func1, func2){
                var data = {'username': username, 'password': passwd};
                post('/users/register', data, func1, func2);
            },
            login: function(username, passwd, func1, func2){
                var data = {'username': username, 'password': passwd};
                post('/users/login', data, func1, func2);
            },
            logout: function(func1, func2){
                post('/users/logout', {}, func1, func2);
            },
            // Service Interface
            getServiceList: function(func1, func2){
                get('/containers/containers', func1, func2);
            },
            addService: function(name, func1, func2){
                post('/containers/create', {'name': name}, func1, func2);
            }
        };
    });
