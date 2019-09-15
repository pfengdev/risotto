from social_core.backends.oauth import BaseOAuth2

class GeniusOauth2(BaseOAuth2):
    name = 'genius'
    AUTHORIZATION_URL = 'https://api.genius.com/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://api.genius.com/oauth/token'
    ACCESS_TOKEN_METHOD = 'POST'
    # TODO: the scope separator needs to be a space, but it
    # somehow becomes a +
    SCOPE_SEPARATOR = ' '
    DEFAULT_SCOPE = ['me']
    REDIRECT_STATE = False

    def get_user_details(self, response):
        fullname, first_name, last_name = self.get_user_names(
            response.get('display_name')
        )
        return {'username': response.get('id'),
                'email': response.get('email'),
                'fullname': fullname,
                'first_name': first_name,
                'last_name': last_name}

    def user_data(self, access_token, *args, **kwargs):
        return self.get_json(
            'https://api.genius.com/account',
            headers={'Authorization': 'Bearer {0}'.format(access_token)}
        )
