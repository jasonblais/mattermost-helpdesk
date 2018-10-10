from pytest import fixture
from discourse_api_wrapper import Discourse
import vcr

@fixture
def discourse_posts():
    # Returns test data
    return ['id', 'name', 'username', 'created_at', 'post_number',
            'reply_count', 'reads']

@vcr.use_cassette('tests/vcr_cassettes/discourse-info.yml')
def test_discourse_info(discourse_posts):
    """Tests an API call to get a single post"""

    discourse_post = Discourse(100)
    response = discourse_post.info()
    
    assert isinstance(response, dict)
    assert response['id'] == 100, "The ID should be in the response"
    assert set(discourse_post()).issubset(response.keys()), "All keys should be in the response"
