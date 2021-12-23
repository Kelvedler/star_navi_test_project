from rest_framework_simplejwt import tokens


def get_tokens_for_user(user):
    refresh = tokens.RefreshToken.for_user(user)
    return {'refresh': str(refresh), 'access': str(refresh.access_token)}


def get_access_token(refresh_token):
    return refresh_token.access_token
