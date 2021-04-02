"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""

from urllib3_mock import Responses

from apivideo.api.account_api import AccountApi  # noqa: E501
from apivideo.exceptions import ApiException, NotFoundException

from helper import MainTest


responses = Responses()


class TestAccountApi(MainTest):
    """AccountApi unit test"""

    def setUp(self):
        super().setUp()
        self.api = AccountApi(self.client)  # noqa: E501

    @responses.activate
    def test_get(self):
        """Test case for get

        Show account  # noqa: E501
        """
        for status, json in self.load_json('account', 'get'):
            responses.reset()

            kwargs = {
            }
            url = '/account'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.get(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.get(**kwargs)

