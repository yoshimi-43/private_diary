from .settings_common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#i)dedt^odzs2f$+_vy87hhbud9#gwgiif3a+#t1*@m(ne9z15'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# ロギング設定
LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,

  # ロガーの設定
  'loggers': {
    'django': {
      'handlers': ['console'],
      'level': 'INFO'
    },
    'diary': {
      'handlers': ['console'],
      'level': 'DEBUG'
    }
  },

  # ハンドラの設定
  'handlers': {
    'console': {
      'level': 'DEBUG',
      'class': 'logging.StreamHandler',
      'formatter': 'dev'
    }
  },

  # フォーマッタの設定
  'formatters': {
    'dev': {
      'format': '\t'.join([
        '%(asctime)s',
        '[%(levelname)s]',
        '%(pathname)s(Line:%(lineno)d)',
        '%(message)s'
      ])
    }
  }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')