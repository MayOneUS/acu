'use strict';

/* Controllers */

var acuControllers = angular.module('acuControllers', []);

acuApp.factory('Data', function() {
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

acuControllers.controller('PhoneListCtrl', ['$scope', '$http', '$location', 'Data',
  function($scope, $http, $location, Data) {
      $scope.Data = Data;
      $scope.answers = {};
      $scope.validCode = true;
    $scope.orderProp = 'age';
    $scope.alreadyUsed = true;
    $scope.testCode = function(token) {
    $http({method: 'GET', url: '/validate', params:{'token':token.toUpperCase()}}).
        success(function(data, status, headers, config) {
            ga('send', 'event', 'button', 'codeSubmit', token.toUpperCase());

            if('alreadyUsed' in data){
                $scope.alreadyUsed = false;
                return;
            }
            $scope.Data.setQuiz(data);
            $location.path('/video/' + token.toUpperCase());
        }).
        error(function(data, status, headers, config) {
            ga('send', 'event', 'button', 'codeSubmitFailure', token.toUpperCase());

            $scope.validCode = false;
        })
    }

  }]);
acuControllers.controller('SelectGiftCtrl', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http) {
    }]);


acuControllers.controller('ThanksCtrl', ['$scope', '$routeParams', '$http', '$location', '$anchorScroll',
    function($scope, $routeParams, $http, $location, $anchorScroll) {
        $http({method: 'GET', url: '/ListStores/' + $routeParams.token}).
            success(function(data) {
                $scope.stores = data['stores'];
                $scope.giftAmount = data.giftcard_amount;
            })
        $location.hash('top');
        $anchorScroll();
        $scope.emailSignupInput = true;
        $scope.validateEmail = function(email) {
            var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            return re.test(email);
        }
        $scope.payForward = function() {
            var data = {
                'token':$routeParams.token,
                'email':$scope.emailforward
            }
            if (typeof $scope.emailforward === "undefined" ||
                !$scope.validateEmail($scope.emailforward)) {
                return;
            }
            $http({method:'POST', url: '/PayItForward/', 'data':data}).
                success(function (data) {
                    $location.path('/thanks/')
                })
        }
        $scope.SaveStorePreference = function() {
           if(typeof $scope.email === "undefined" ||
               !$scope.validateEmail($scope.email)) {
               return;
           }
           var data = {
               'storeSelection': $scope.storeName,
               'token':$routeParams.token,
               'email':$scope.email,
               'storeemail':$scope.emailSignupInput
           }

   	    $http({method:'POST', url: 'https://pledge.mayday.us/r/subscribe/', 'data':$scope.emailSignupInput}).
		success(function (data) {
		})
            $http({method:'POST', url: '/SaveStoreSelection/', 'data':data}).
                success(function (data) {
                    $location.path('/thanks/');
            });
        };
    }]);



acuControllers.controller('PhoneDetailCtrl', ['$scope', '$routeParams', '$http', '$cookies', '$location', "Data",
    function($scope, $routeParams, $http, $cookies, $location, Data) {
	    $scope.playerVars = {
	        controls: 2,
	        autoplay: 0,
            wmode: "transparent"
	    }
        $scope.hideQuiz = true;
        $scope.token = $routeParams.token;
        $scope.answers = {};
        $scope.wrong_answers = {};
        $scope.Data = Data;
        $scope.nottrue = true;
        $scope.anotherGoodOne = $scope.Data.getQuiz().youtube_url;

        for(var i = 0; i < $scope.Data.getQuiz().questions.length; i++)
        {
            $scope.answers[$scope.Data.getQuiz().questions[i].id] = {};
            $scope.wrong_answers[$scope.Data.getQuiz().questions[i].id] = true;
        }
	    $scope.questions = $scope.Data.getQuiz().questions;

	    $scope.$on('youtube.player.ended', function($event, player) {
            $scope.hideQuiz = false;
            var data = {token:$routeParams.token}
            $http({method: 'POST', url: '/finished_watching/', data:data}).
                success(function(){})
	    });
        $scope.$on('youtube.player.playing', function($event, player) {
            var data = {token:$routeParams.token}
            $http({method: 'POST', url: '/started_watching/', data:data}).
                success(function(){})
        })

    $scope.validate_quiz = function() {
        var data = {'token':$scope.token,
            'answers':$scope.answers
        }

        $http({method: 'POST', url: '/ValidateQuiz/', data:{'data':data}}).
            success(function(data, status, headers, config) {
                for(var k in $scope.wrong_answers) $scope.wrong_answers[k] = true;

                if(data['charity'] == true)
                {
                    $location.path('/donation/' + $scope.token)
                }
                else {
                    $location.path('/thanks/' + $scope.token);
                }

            }).
            error(function(data, status, headers, config) {
                for(var k in $scope.wrong_answers) $scope.wrong_answers[k] = true;
                for(var i = 0; i < data.length; i++) $scope.wrong_answers[data[i]] = false;
                $scope.wrongAnswer = true;
            });
    };
  }
  ]);
