'use strict';
module.exports = function(app) {
  var TaskList = require('../controllers/TaskListController');

  // TaskList Routes
  app.route('/tasks')
    .get(TaskList.list_all_tasks)
    .post(TaskList.create_a_task);


  app.route('/tasks/:taskId')
    .get(TaskList.read_a_task)
    .put(TaskList.update_a_task)
    .delete(TaskList.delete_a_task);
};
