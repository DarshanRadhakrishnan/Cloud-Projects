"""
Simple Flask Todo API
- GET /health - Health check endpoint
- GET /todos - Get all todos
- POST /todos - Create a new todo
- GET /todos/<id> - Get specific todo
"""

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage
todos = {}
todo_counter = 1


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    }), 200


@app.route('/todos', methods=['GET'])
def get_todos():
    """Get all todos"""
    return jsonify({
        'todos': list(todos.values()),
        'count': len(todos)
    }), 200


@app.route('/todos', methods=['POST'])
def create_todo():
    """Create a new todo"""
    global todo_counter
    
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({'error': 'Missing title field'}), 400
    
    todo_id = todo_counter
    todo_counter += 1
    
    todo = {
        'id': todo_id,
        'title': data['title'],
        'completed': False,
        'created_at': datetime.now().isoformat()
    }
    
    todos[todo_id] = todo
    return jsonify(todo), 201


@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """Get specific todo by ID"""
    if todo_id not in todos:
        return jsonify({'error': 'Todo not found'}), 404
    
    return jsonify(todos[todo_id]), 200


@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Update a todo"""
    if todo_id not in todos:
        return jsonify({'error': 'Todo not found'}), 404
    
    data = request.get_json()
    
    if 'title' in data:
        todos[todo_id]['title'] = data['title']
    
    if 'completed' in data:
        todos[todo_id]['completed'] = data['completed']
    
    return jsonify(todos[todo_id]), 200


@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete a todo"""
    if todo_id not in todos:
        return jsonify({'error': 'Todo not found'}), 404
    
    deleted = todos.pop(todo_id)
    return jsonify({'message': 'Todo deleted', 'todo': deleted}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
