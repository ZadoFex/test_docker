// 'use strict';
// const express = require('express');
// // Constants
// const PORT = 8585;
// const HOST = '0.0.0.0';
// // App
// const app = express();
// app.get('/', (req, res) => {
//   res.send('Ba Hello world\n');
// });
// app.listen(PORT, HOST);
// console.log(`Running on http://${HOST}:${PORT}`);

var express = require('express'),
  app = express(),
  port = process.env.PORT || 8585,
  mongoose = require('mongoose'),
  Task = require('./api/models/TaskListModel'), //created model loading here
  bodyParser = require('body-parser');
  
// mongoose instance connection url connection
mongoose.Promise = global.Promise;
mongoose.connect('mongodb://mongodb/blog'); 


app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());



// var routes = require('./api/routes/TaskListRoutes'); //importing route
// routes(app); //register the route

var prroutes = require('./api/routes/PingRoutes'); //importing route
prroutes(app); //register the route


app.listen(port);


console.log('todo list RESTful API server started on: ' + port);
