'use strict';

/* App Module */

var phonecatApp = angular.module('phonecatApp', [
  'ngRoute',
  'phonecatControllers',
  'phonecatFilters',
  'youtube-embed',
  'ngCookies',

]);

phonecatApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: 'static/partials/code-page.html',
        controller: 'PhoneListCtrl'
      }).
      when('/video/:token', {
        templateUrl: 'static/partials/phone-detail.html',
        controller: 'PhoneDetailCtrl'
      }).
      when('/thanks/:token', {
          templateUrl: 'static/partials/thanks.html',
          controller: 'ThanksCtrl'
      }).
      when('/select/:token', {
          TemplateUrl: 'static/partials/select.html',
          controller: 'SelectGiftCtrl'
      }).
      otherwise({
        redirectTo: '/'
      });
  }]);


