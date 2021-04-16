"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""

from dateutil.parser import parse as dateutil_parser
from urllib3_mock import Responses

from apivideo.api.videos_delegated_upload_api import VideosDelegatedUploadApi  # noqa: E501
from apivideo.exceptions import ApiException, NotFoundException
from apivideo.model.metadata import Metadata
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from apivideo.model.token_create_payload import TokenCreatePayload
from apivideo.model.token_list_response import TokenListResponse
from apivideo.model.upload_token import UploadToken
from apivideo.model.video import Video

from helper import MainTest


responses = Responses()


class TestVideosDelegatedUploadApi(MainTest):
    """VideosDelegatedUploadApi unit test"""

    def setUp(self):
        super().setUp()
        self.api = VideosDelegatedUploadApi(self.client)  # noqa: E501

    @responses.activate
    def test_delete_token(self):
        """Test case for delete_token

        Delete an upload token  # noqa: E501
        """
        pass

    @responses.activate
    def test_list_tokens(self):
        """Test case for list_tokens

        List all active upload tokens.  # noqa: E501
        """
        for status, json in self.load_json('videos_delegated_upload', 'list_tokens'):
            responses.reset()

            kwargs = {
            }
            url = '/upload-tokens'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.list_tokens(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.list_tokens(**kwargs)

    @responses.activate
    def test_get_token(self):
        """Test case for get_token

        Show upload token  # noqa: E501
        """
        for status, json in self.load_json('videos_delegated_upload', 'get_token'):
            responses.reset()

            kwargs = {
                'upload_token': "to1tcmSFHeYY5KzyhOqVKMKb",
            }
            url = '/upload-tokens/{upload_token}'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.get_token(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.get_token(**kwargs)

    @responses.activate
    def test_upload(self):
        """Test case for upload

        Upload with an upload token  # noqa: E501
        """
        for status, json in self.load_json('videos_delegated_upload', 'upload'):
            responses.reset()

            kwargs = {
                'token': "to1tcmSFHeYY5KzyhOqVKMKb",
                'file': open('test_file', 'rb'),
            }
            url = '/upload'.format(**kwargs)

            responses.add('POST', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.upload(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.upload(**kwargs)

    @responses.activate
    def test_create_token(self):
        """Test case for create_token

        Generate an upload token  # noqa: E501
        """
        for status, json in self.load_json('videos_delegated_upload', 'create_token'):
            responses.reset()

            kwargs = {
            }
            url = '/upload-tokens'.format(**kwargs)

            responses.add('POST', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.create_token(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.create_token(**kwargs)

