Certainly! Here's a more complex example that demonstrates how to use Python classes with Flask to create a basic RESTful API for managing tasks. In this example, we'll have a `Task` class and use Flask to implement endpoints for creating, retrieving, updating, and deleting tasks.

```python
from flask import Flask, request, jsonify
from flask.views import MethodView

app = Flask(__name)

# Sample initial data
tasks = [
    {"id": 1, "title": "Task 1", "completed": False},
    {"id": 2, "title": "Task 2", "completed": True},
]

class TaskAPI(MethodView):
    def get(self, task_id):
        if task_id is None:
            # Return a list of all tasks
            return jsonify(tasks)
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task is None:
            return "Task not found", 404
        return jsonify(task)

    def post(self):
        new_task = request.get_json()
        new_task['id'] = len(tasks) + 1
        tasks.append(new_task)
        return jsonify(new_task), 201

    def put(self, task_id):
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task is None:
            return "Task not found", 404
        data = request.get_json()
        task['title'] = data.get('title', task['title'])
        task['completed'] = data.get('completed', task['completed')
        return jsonify(task)

    def delete(self, task_id):
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task is None:
            return "Task not found", 404
        tasks.remove(task)
        return "Task deleted", 204

task_view = TaskAPI.as_view('task_api')
app.add_url_rule('/tasks/', defaults={'task_id': None}, view_func=task_view, methods=['GET'])
app.add_url_rule('/tasks/', view_func=task_view, methods=['POST'])
app.add_url_rule('/tasks/<int:task_id>', view_func=task_view, methods=['GET', 'PUT', 'DELETE'])

if __name__ == '__main__':
    app.run()
```

In this example, we define a `TaskAPI` class that inherits from `MethodView`, which allows us to map HTTP methods (GET, POST, PUT, DELETE) to class methods. The class handles various operations related to tasks, including listing all tasks, retrieving a single task, creating a new task, updating a task, and deleting a task.

We use the `add_url_rule` method to map the class methods to specific endpoints. For instance:

- `GET /tasks/` retrieves a list of all tasks.
- `GET /tasks/<task_id>` retrieves a specific task by ID.
- `POST /tasks/` creates a new task.
- `PUT /tasks/<task_id>` updates an existing task.
- `DELETE /tasks/<task_id>` deletes a task by ID.

This is a more complex example that demonstrates the power of using classes in Flask to organize and structure your code for building RESTful APIs or web applications.