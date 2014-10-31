'use strict';

/* App Module */

var acuApp = angular.module('acuApp', [
  'ngRoute',
  'acuControllers',
  'phonecatFilters',
  'youtube-embed',
  'ngCookies'
]);

acuApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: 'static/partials/code-page.html',
        controller: 'PhoneListCtrl'
      }).
      when('/video/:token', {
        templateUrl: 'static/partials/video-and-quiz.html',
        controller: 'PhoneDetailCtrl'
      }).
      when('/done', {
        templateUrl: 'static/partials/done.html',
        controller:'DoneCtrl'
      }).
        when('/thanks/:token', {
          templateUrl: 'static/partials/thanks.html',
          controller: 'ThanksCtrl'
        }).

      when('/donation/:token', {
        templateUrl: 'static/partials/donation.html',
        controller: 'ThanksCtrl'
      }).
      otherwise({
        redirectTo: '/'
      });
  }]);


