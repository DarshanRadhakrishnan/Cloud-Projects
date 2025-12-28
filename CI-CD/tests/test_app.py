"""
Unit tests for Flask Todo API
Tests cover:
- Health check endpoint
- Todo CRUD operations
"""

import unittest
import json
from app.app import app, todos, reset_todos


def reset_todos():
    """Reset todos for each test"""
    global todos
    todos.clear()
    globals()['todo_counter'] = 1


class TodoAPITestCase(unittest.TestCase):
    
    def setUp(self):
        """Set up test client before each test"""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        todos.clear()
    
    def test_health_check_returns_200(self):
        """Test health check endpoint returns 200"""
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')
    
    def test_get_todos_empty(self):
        """Test getting todos when empty"""
        response = self.client.get('/todos')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['count'], 0)
        self.assertEqual(len(data['todos']), 0)
    
    def test_create_todo_success(self):
        """Test creating a todo successfully"""
        response = self.client.post('/todos',
            data=json.dumps({'title': 'Test Todo'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Test Todo')
        self.assertEqual(data['completed'], False)
        self.assertIn('id', data)
    
    def test_create_todo_missing_title(self):
        """Test creating a todo without title returns 400"""
        response = self.client.post('/todos',
            data=json.dumps({}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)
    
    def test_get_todos_after_create(self):
        """Test getting todos after creation"""
        self.client.post('/todos',
            data=json.dumps({'title': 'Todo 1'}),
            content_type='application/json'
        )
        self.client.post('/todos',
            data=json.dumps({'title': 'Todo 2'}),
            content_type='application/json'
        )
        
        response = self.client.get('/todos')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['count'], 2)
    
    def test_get_single_todo(self):
        """Test getting a single todo by ID"""
        create_response = self.client.post('/todos',
            data=json.dumps({'title': 'Get Me'}),
            content_type='application/json'
        )
        todo_id = json.loads(create_response.data)['id']
        
        response = self.client.get(f'/todos/{todo_id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Get Me')
    
    def test_get_nonexistent_todo(self):
        """Test getting a todo that doesn't exist"""
        response = self.client.get('/todos/999')
        self.assertEqual(response.status_code, 404)
    
    def test_update_todo(self):
        """Test updating a todo"""
        create_response = self.client.post('/todos',
            data=json.dumps({'title': 'Original'}),
            content_type='application/json'
        )
        todo_id = json.loads(create_response.data)['id']
        
        response = self.client.put(f'/todos/{todo_id}',
            data=json.dumps({'title': 'Updated', 'completed': True}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Updated')
        self.assertEqual(data['completed'], True)
    
    def test_delete_todo(self):
        """Test deleting a todo"""
        create_response = self.client.post('/todos',
            data=json.dumps({'title': 'Delete Me'}),
            content_type='application/json'
        )
        todo_id = json.loads(create_response.data)['id']
        
        response = self.client.delete(f'/todos/{todo_id}')
        self.assertEqual(response.status_code, 200)
        
        # Verify it's gone
        get_response = self.client.get(f'/todos/{todo_id}')
        self.assertEqual(get_response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
