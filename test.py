import unittest
from apps import create_app, create_celery
from celery import states
from celery.result import AsyncResult
from time import sleep

class TaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.celery = create_celery(self.app)
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_send_async_email(self):
        task = self.celery.send_task('tasks.send_async_email', args=[1])
        sleep(5)
        result = AsyncResult(task.id, app=self.celery)
        self.assertEqual(result.status, states.SUCCESS)

if __name__ == '__main__':
    unittest.main()