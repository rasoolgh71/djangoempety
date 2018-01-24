from django.test import TestCase
from mock import patch
from task.models import Post_Email
from mock import Mock

class Post_Emailtestcase(TestCase):

    @patch('internal_api.api_call', return_value=1)
    def test_api_call(self,mock_api_call):
        Post_Email.do_api_call()
        self.assertEqual(Post_Email.api_value, 1)
        self.assertEqual(mock_api_call.call_count, 1)