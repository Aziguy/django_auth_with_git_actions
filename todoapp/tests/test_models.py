from utils.setup_test import TestSetup
from accounts.models import User
from todoapp.models import Todo


class TestModel(TestSetup):

    def test_should_create_todo(self):
        user = self.create_test_user()
        todo = Todo(owner=user, title="Buy milk", description='get it done')
        todo.save()
        self.assertEqual(str(todo), 'Buy milk')