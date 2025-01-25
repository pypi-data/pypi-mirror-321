import re

DEFAULT_BEARER_TOKEN = (
    "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
)
AUTH_ACTION_REQUIRED_KEYS = ("LoginTwoFactorAuthChallenge", "LoginAcid", "LoginEnterAlternateIdentifierSubtask")

GUEST_TOKEN_REGEX = re.compile("gt=(.*?);")
MIGRATION_REGEX = re.compile(
    r"""(http(?:s)?://(?:www\.)?(twitter|x){1}\.com(/x)?/migrate([/?])?tok=[a-zA-Z0-9%\-_]+)+""", re.VERBOSE
)
