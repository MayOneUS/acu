'use strict';

/* Controllers */

var phonecatControllers = angular.module('phonecatControllers', []);

phonecatApp.factory('Data', function() {
    var quiz = { Quiz: ''}
    return {
        getQuiz: function() {
            return quiz.Quiz;
        },
        setQuiz: function(Quiz) {
            quiz.Quiz = Quiz;
        }
    }
    }
);

phonecatControllers.controller('PhoneListCtrl', ['$scope', '$http', '$location', 'Data',
  function($scope, $http, $location, Data) {
      $scope.Data = Data;
      $scope.answers = {};
      $scope.validCode = true;
    $scope.orderProp = 'age';

    $scope.testCode = function(token) {
    $http({method: 'GET', url: '/validate', params:{'token':token}}).
        success(function(data, status, headers, config) {
            $scope.Data.setQuiz(data);
            console.log(data)
            $location.path('/video/' + token);
        }).
        error(function(data, status, headers, config) {
            $scope.validCode = false;
        })
    }

  }]);
phonecatControllers.controller('SelectGiftCtrl', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http) {
        console.log('in the select gift control')
    }]);
phonecatControllers.controller('ThanksCtrl', ['$scope', '$routeParams', '$http', '$location',
    function($scope, $routeParams, $http, $location) {
        $http({method: 'GET', url: '/ListStores/'}).
            success(function(data) {
                $scope.stores = data;
            })
        $scope.payForward = function() {
            var data = {
                'token':$routeParams.token,
                'email':$scope.emailforward
            }
            $http({method:'POST', url: '/PayItForward/', 'data':data}).
                success(function (data) {
                    $location.path('/thanks/')
                })
        }
        $scope.SaveStorePreference = function() {
            var data = {
                'storeSelection': $scope.storeName,
                'token':$routeParams.token,
                'email':$scope.email
            }

            console.log($scope.storeName)
            $http({method:'POST', url: '/SaveStoreSelection/', 'data':data}).
                success(function (data) {
                    $location.path('/thanks/');
            });
        };
    }]);
phonecatControllers.controller('PhoneDetailCtrl', ['$scope', '$routeParams', '$http', '$cookies', '$location', "Data",
    function($scope, $routeParams, $http, $cookies, $location, Data) {
	    $scope.anotherGoodOne = 'https://www.youtube.com/watch?v=18-xvIjH8T4';
	    $scope.playerVars = {
	        controls: 2,
	        autoplay: 0
	    }
        $scope.hideQuiz = true;
        $scope.token = $routeParams.token;
        $scope.answers = {};
        $scope.wrong_answers = {};
        $scope.Data = Data;
        $scope.nottrue = true;
        console.log($scope.Data.getQuiz())
        for(var i = 0; i < $scope.Data.getQuiz().questions.length; i++)
        {
            $scope.answers[$scope.Data.getQuiz().questions[i].id] = {};
            $scope.wrong_answers[$scope.Data.getQuiz().questions[i].id] = true;
        }
        console.log($scope.wrong_answers)
        console.log('logging quiz')
        console.log(Data.getQuiz())
	    $scope.questions = $scope.Data.getQuiz().questions;

	    $scope.$on('youtube.player.ended', function($event, player) {
	        console.log(player);
            $scope.hideQuiz = false;
	    });

    $scope.validate_quiz = function() {
        console.log($cookies.csrf_token)
        var data = {'token':$scope.token,
            'answers':$scope.answers
        }

        $http({method: 'POST', url: '/ValidateQuiz/', data:{'data':data}}).
            success(function(data, status, headers, config) {
               console.log('success!');
                for(var k in $scope.wrong_answers) $scope.wrong_answers[k] = true;
                $location.path('/thanks/' + $scope.token);

            }).
            error(function(data, status, headers, config) {


                console.log($scope.wrong_answers)
                console.log(data);
                for(var k in $scope.wrong_answers) $scope.wrong_answers[k] = true;
                for(var i = 0; i < data.length; i++) $scope.wrong_answers[data[i]] = false;
                console.log($scope.wrong_answers)
            });
        console.log(data)
    };
  }
  ]);
