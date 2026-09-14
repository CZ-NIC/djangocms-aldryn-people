SECRET_KEY = "secret"

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://localhost:9001/solr/default',
        'TIMEOUT': 60 * 5,
        'INCLUDE_SPELLING': True,
        'BATCH_SIZE': 100,
        'EXCLUDED_INDEXES': ['thirdpartyapp.search_indexes.BarIndex'],
    },
    'en': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://my-solr-server/solr/my-site-en/',
        'TIMEOUT': 60 * 5,
        'INCLUDE_SPELLING': True,
        'BATCH_SIZE': 100,
    },
    'de': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://my-solr-server/solr/my-site-de/',
        'TIMEOUT': 60 * 5,
        'INCLUDE_SPELLING': True,
        'BATCH_SIZE': 100,
    },
}


TIME_ZONE = 'Europe/Zurich'

# HAYSTACK_CONNECTIONS = HAYSTACK_CONNECTIONS
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sites",
    "cms",
    "menus",
    "treebeard",
    # "django_meta_og",
    # "djangocms_meta_og",
# ]
# INSTALLED_APPS = [
    'aldryn_common',
    'aldryn_translation_tools',
    'djangocms_text_ckeditor',
    'easy_thumbnails',
    'filer',
    'parler',
    'sortedm2m',
    'aldryn_people',
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "tests",
    }
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

CMS_PERMISSION = True

# At present, testing requires bootstrap to be disabled.
# 'ALDRYN_BOILERPLATE_NAME': 'bootstrap3',
LANGUAGES = (
    ('en', 'English'),
    ('de', 'German'),
    ('fr', 'French'),
)

CMS_LANGUAGES = {
    1: [
        {
            'code': 'de',
            'name': 'Deutsche',
            'fallbacks': ['en', ]  # FOR TESTING DO NOT ADD 'fr' HERE
        },
        {
            'code': 'fr',
            'name': 'Française',
            'fallbacks': ['en', ]  # FOR TESTING DO NOT ADD 'de' HERE
        },
        {
            'code': 'en',
            'name': 'English',
            'fallbacks': ['de', 'fr', ]
        },
        {
            'code': 'it',
            'name': 'Italiano',
            'fallbacks': ['fr', ]  # FOR TESTING, LEAVE AS ONLY 'fr'
        },
    ],
}

# app-specific
PARLER_LANGUAGES = {
    1: [
        {
            'code': 'en',
            'fallbacks': ['de', 'fr'],
            'hide_untranslated': False
        },
        {
            'code': 'fr',
            'fallbacks': ['en'],
            'hide_untranslated': False
        },
        {
            'code': 'de',
            'fallbacks': ['en'],
            'hide_untranslated': False
        }
    ],
    'default': {
        'code': 'en',
        'fallbacks': ['en'],
        'hide_untranslated': False}
}

PARLER_ENABLE_CACHING = False

LANGUAGE_CODE = 'en'

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "cms.middleware.page.CurrentPageMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # "aldryn_people/tests/templates"
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "cms.context_processors.cms_settings",
                # "djangocms_meta_og.context_processors.meta",
            ],
            "loaders": ["django.template.loaders.filesystem.Loader", "django.template.loaders.app_directories.Loader"],
        },
    }
]

ROOT_URLCONF = "aldryn_people.urls"

# def run():
#     from djangocms_helper import runner
#     runner.cms('aldryn_people', extra_args=[])  # , extra_args=['--boilerplate']


# if __name__ == "__main__":
#     run()
