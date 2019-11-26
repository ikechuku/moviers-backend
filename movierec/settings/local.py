from decouple import config
from .base import * 

print("This is local.py settings working")

DATABASES = {
    "default": {
        'ENGINE': 'djongo',
        'NAME': 'moviers',
        'HOST': 'localhost',
        'PORT': config('PORT', cast=int),
    }
}

INSTALLED_APPS += ['debug_toolbar', ]

MIDDLEWARE  += ['debug_toolbar.middleware.DebugToolbarMiddleware']