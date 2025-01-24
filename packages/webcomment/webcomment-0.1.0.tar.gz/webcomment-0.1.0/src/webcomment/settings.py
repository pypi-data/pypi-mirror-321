from saas_base.settings import Settings


DEFAULTS = {
    'TURNSTILE_SITE_KEY': '',
    'COMMENT_SECURITY_RULES': [],
    'THREAD_RESOLVER': {
        'backend': 'webcomment.resolver.ModelThreadResolver',
    },
}


class CommentSettings(Settings):
    IMPORT_PROVIDERS = [
        'COMMENT_SECURITY_RULES',
        'THREAD_RESOLVER',
    ]


comment_settings = CommentSettings('WEB_COMMENT', defaults=DEFAULTS)
