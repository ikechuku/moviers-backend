from decouple import config
from .base import *
import os

print("You are using production settings")
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'HOST': config('DB_URL')
    }
}

