from decouple import config
from .base import *
import os

print("You are using production settings")
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'HOST': 'mongodb://admin:FiiQsn0VWmJBiV1j@SG-moviers-28158.servers.mongodirector.com:27017/admin'
    }
}

