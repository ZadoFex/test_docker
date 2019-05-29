'use strict';
module.exports = function(app) {
  var Ping = require('../controllers/PingController');

  // Ping Routes
  app.route('/ping')
    .get(Ping.ping)
    ;



};