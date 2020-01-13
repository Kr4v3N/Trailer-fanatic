# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lruyv(_utt3vd7*ee4&%1m7p36md#b@uu$&zfp!c*6*q!(woi*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        # Backends disponibles : 'postgresql', 'mysql', 'sqlite3' et 'oracle'.
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'trailerfanatic',  # Nom de la base de données
        'USER': 'root',  # Nom de l'utilisateur
        'PASSWORD': 'password',  # Mot de passe utilisateur
        'HOST': '',  # Utile si votre base de données est sur une autre machine
        'PORT': '',  # ... et si elle utilise un autre port que celui par défaut
    }
}
