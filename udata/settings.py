# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from kombu import Exchange, Queue


class Defaults(object):
    DEBUG = False
    TESTING = False
    SEND_MAIL = True
    LANGUAGES = {
        'en': 'English',
        'fr': 'Français',
        'es': 'Español',
    }
    DEFAULT_LANGUAGE = 'en'
    SECRET_KEY = 'Default uData secret key'
    CONTACT_EMAIL = 'contact@example.org'
    TERRITORIES_EMAIL = 'territories@example.org'

    MONGODB_HOST = 'mongodb://localhost:27017/udata'

    # Elasticsearch configuration
    ELASTICSEARCH_URL = 'localhost:9200'
    ELASTICSEARCH_INDEX_BASENAME = 'udata'
    ELASTICSEARCH_REFRESH_INTERVAL = '1s'

    # BROKER_TRANSPORT = 'redis'
    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_BROKER_TRANSPORT_OPTIONS = {
        'fanout_prefix': True,
        'fanout_patterns': True,
    }
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'
    CELERY_TASK_SERIALIZER = 'pickle'
    CELERY_RESULT_SERIALIZER = 'pickle'
    CELERY_ACCEPT_CONTENT = ['pickle', 'json']
    CELERY_WORKER_HIJACK_ROOT_LOGGER = False
    CELERY_BEAT_SCHEDULER = 'udata.tasks.Scheduler'
    CELERY_MONGODB_SCHEDULER_COLLECTION = "schedules"

    # Default celery routing
    CELERY_TASK_DEFAULT_QUEUE = 'default'
    CELERY_TASK_QUEUES = (
        # Default queue (on default exchange)
        Queue('default', routing_key='task.#'),
        # High priority for urgent tasks
        Queue('high', Exchange('high', type='topic'), routing_key='high.#'),
        # Low priority for slow tasks
        Queue('low', Exchange('low', type='topic'), routing_key='low.#'),
    )
    CELERY_TASK_DEFAULT_EXCHANGE = 'default'
    CELERY_TASK_DEFAULT_EXCHANGE_TYPE = 'topic'
    CELERY_TASK_DEFAULT_ROUTING_KEY = 'task.default'
    CELERY_TASK_ROUTES = {
        # High priority for search tasks
        'udata.search.reindex': {
            'queue': 'high',
            'routing_key': 'high.search',
        },
        # Low priority for harvest operations
        'harvest': {
            'queue': 'low',
            'routing_key': 'low.harvest',
        },
        'udata.harvest.tasks.harvest_item': {
            'queue': 'low',
            'routing_key': 'low.harvest',
        },
        'udata.harvest.tasks.harvest_finalize': {
            'queue': 'low',
            'routing_key': 'low.harvest',
        },
    }

    CACHE_KEY_PREFIX = 'udata-cache'
    CACHE_TYPE = 'redis'

    # Flask mail settings

    MAIL_DEFAULT_SENDER = 'webmaster@udata'

    # Flask security settings

    SECURITY_TRACKABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_CONFIRMABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_CHANGEABLE = True

    SECURITY_PASSWORD_HASH = b'bcrypt'

    SECURITY_PASSWORD_SALT = b'Default uData secret password salt'
    SECURITY_CONFIRM_SALT = b'Default uData secret confirm salt'
    SECURITY_RESET_SALT = b'Default uData secret reset salt'
    SECURITY_REMEMBER_SALT = b'Default uData remember salt'

    SECURITY_EMAIL_SENDER = MAIL_DEFAULT_SENDER

    # Flask WTF settings
    CSRF_SESSION_KEY = 'Default uData csrf key'

    OAUTH2_PROVIDER_TOKEN_EXPIRES_IN = 30 * 24 * 60 * 60  # 30 days

    AUTO_INDEX = True

    SITE_ID = 'default'
    SITE_TITLE = 'uData'
    SITE_KEYWORDS = ['opendata', 'udata']
    SITE_AUTHOR_URL = None
    SITE_AUTHOR = 'Udata'
    SITE_GITHUB_URL = 'https://github.com/etalab/udata'
    USE_SSL = False

    PLUGINS = []
    THEME = 'default'

    STATIC_DIRS = []

    OAUTH2_PROVIDER_ERROR_ENDPOINT = 'oauth.oauth_error'

    MD_ALLOWED_TAGS = [
        'a',
        'abbr',
        'acronym',
        'b',
        'br',
        'blockquote',
        'code',
        'dd',
        'dl',
        'dt',
        'em',
        'i',
        'li',
        'ol',
        'pre',
        'small',
        'strong',
        'ul',
    ]

    MD_ALLOWED_ATTRIBUTES = {
        'a': ['href', 'title'],
        'abbr': ['title'],
        'acronym': ['title'],
    }

    MD_ALLOWED_STYLES = []

    # Cache duration for templates.
    TEMPLATE_CACHE_DURATION = 5  # Minutes.

    DELAY_BEFORE_REMINDER_NOTIFICATION = 30  # Days

    HARVEST_PREVIEW_MAX_ITEMS = 20
    # Harvesters are scheduled at midnight by default
    HARVEST_DEFAULT_SCHEDULE = '0 0 * * *'

    # Lists levels that shouldn't be indexed
    SPATIAL_SEARCH_EXCLUDE_LEVELS = tuple()

    ACTIVATE_TERRITORIES = False
    # The order is important to compute parents/children, smaller first.
    HANDLED_LEVELS = tuple()

    LINKCHECKING_ENABLED = True
    LINKCHECKING_IGNORE_DOMAINS = []
    LINKCHECKING_CACHE_DURATION = 60 * 5  # in seconds
    LINKCHECKING_DEFAULT_LINKCHECKER = 'no_check'

    # PIWIK_ID = # Demo = 11, Prod = 1
    # PIWIK_URL = 'stats.data.gouv.fr'
    # PIWIK_AUTH = '<32-chars-auth-token-from-piwik>'
    # # All keys are required.
    # PIWIK_GOALS = {
    #     'NEW_DATASET': # Demo = 1, Prod = 7
    #     'NEW_REUSE': # Demo = 2, Prod = 6
    #     'NEW_FOLLOW': # Demo = 3, Prod = 3
    #     'SHARE': , # Demo = 4, Prod = ?
    #     'RESOURCE_DOWNLOAD': , # Demo = 5, Prod = ?
    #     'RESOURCE_REDIRECT': , # Demo = 6, Prod = ?
    # }
    # TRACKING_BLACKLIST = ['api.notifications', 'api.check_dataset_resource']  # Default: []

    DELETE_ME = True

    # Optimize uploaded images
    FS_IMAGES_OPTIMIZE = True

    # Default resources extensions whitelist
    ALLOWED_RESOURCES_EXTENSIONS = [
        # Base
        'csv', 'txt', 'json', 'pdf', 'xml', 'rtf', 'xsd',
        # OpenOffice
        'ods', 'odt', 'odp', 'odg',
        # Microsoft Office
        'xls', 'xlsx', 'doc', 'docx', 'pps', 'ppt',
        # Archives
        'tar', 'gz', 'tgz', 'rar', 'zip', '7z', 'xz', 'bz2',
        # Images
        'jpeg', 'jpg', 'jpe', 'gif', 'png', 'dwg', 'svg', 'tiff', 'ecw', 'svgz', 'jp2',
        # Geo
        'shp', 'kml', 'kmz', 'gpx', 'shx', 'ovr', 'geojson',
        # Meteorology
        'grib2',
        # Misc
        'dbf', 'prj', 'sql', 'epub', 'sbn', 'sbx', 'cpg', 'lyr', 'owl',
        # RDF
        'rdf', 'ttl', 'n3',
    ]
    USE_METRICS = True

    # Avatar providers parameters
    # Overrides themes and default parameters
    # if set to anything else than `None`
    ###########################################################################
    # avatar provider used to render user avatars
    AVATAR_PROVIDER = None
    # Number of blocks used by the internal provider
    AVATAR_INTERNAL_SIZE = None
    # List of foreground colors used by the internal provider
    AVATAR_INTERNAL_FOREGROUND = None
    # Background color used by the internal provider
    AVATAR_INTERNAL_BACKGROUND = None
    # Padding (in percent) used by the internal provider
    AVATAR_INTERNAL_PADDING = None
    # Skin (set) used by the robohash provider
    AVATAR_ROBOHASH_SKIN = None
    # The background used by the robohash provider.
    AVATAR_ROBOHASH_BACKGROUND = None

    # Post settings
    ###########################################################################
    # Discussions on posts are disabled by default
    POST_DISCUSSIONS_ENABLED = False
    # Default pagination size on listing
    POST_DEFAULT_PAGINATION = 20

    # Dataset settings
    ###########################################################################
    # Max number of resources to display uncollapsed in dataset view
    DATASET_MAX_RESOURCES_UNCOLLAPSED = 6


class Testing(object):
    '''Sane values for testing. Should be applied as override'''
    TESTING = True
    SEND_MAIL = False
    WTF_CSRF_ENABLED = False
    AUTO_INDEX = False
    CELERY_TASK_ALWAYS_EAGER = True
    TEST_WITH_PLUGINS = False
    PLUGINS = []
    TEST_WITH_THEME = False
    THEME = 'default'
    CACHE_TYPE = 'null'
    CACHE_NO_NULL_WARNING = True
    DEBUG_TOOLBAR = False
    SERVER_NAME = 'localhost'
    DEFAULT_LANGUAGE = 'en'
    ACTIVATE_TERRITORIES = False
    LOGGER_HANDLER_POLICY = 'never'
    CELERYD_HIJACK_ROOT_LOGGER = False
    USE_METRICS = False


class Debug(Defaults):
    DEBUG = True
    SEND_MAIL = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG_TB_PANELS = (
        'flask_debugtoolbar.panels.versions.VersionDebugPanel',
        'flask_debugtoolbar.panels.timer.TimerDebugPanel',
        'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
        'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel',
        'flask_debugtoolbar.panels.template.TemplateDebugPanel',
        'flask_debugtoolbar.panels.logger.LoggingPanel',
        'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
        'flask_mongoengine.panels.MongoDebugPanel',
    )
    CACHE_TYPE = 'null'
    CACHE_NO_NULL_WARNING = True
