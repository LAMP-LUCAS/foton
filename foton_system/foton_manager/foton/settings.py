import io
import os
import environ
from pathlib import Path
from urllib.parse import urlparse
from google.cloud import secretmanager
import configparser
print('iniciando o settings.py')
# Definição do diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuração do ambiente e leitura das variáveis de ambiente
env = environ.Env(DEBUG=(bool, False))
env_file = os.path.join(BASE_DIR, ".env")
print('arquivo .env configurado')
config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR, "2.env"))
print('arquivo 2.env configurado')

# Verificação e leitura do arquivo .env local, se disponível
if os.path.isfile(env_file):
    env.read_env(env_file)
    print('arquivo .env encontrado')

# Configurações condicionais para ambientes diferentes
elif os.getenv("TRAMPOLINE_CI", None):
    print('trampoline sendo utilizado')
    # Cria configurações locais para testes de unidade em ambientes de CI
    database_settings = config["database"]
    
    # Construa o DATABASE_URL usando as informações do arquivo 2.env
    db_user = database_settings["USER"]
    db_password = database_settings["PASSWORD"]
    db_host = database_settings["HOST"]
    db_port = database_settings["PORT"]
    db_name = database_settings["NAME"]

    database_url = f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    
    print(database_url)
    # Configure o DATABASE_URL no ambiente de CI
    os.environ["DATABASE_URL"] = database_url

    '''
    placeholder = (
        f"SECRET_KEY=a\n"
        f"DATABASE_URL=mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
    env.read_env(io.StringIO(placeholder))
    '''

# Definição do tipo de banco de dados (local ou online)
DATABASE_TYPE = os.getenv("DATABASE_TYPE", "local")  # Padrão para "online" se não definido
print(f'DATABASE_TYPE configurado COMO: {DATABASE_TYPE[:]}')
# Se DATABASE_TYPE for "online", tenta acessar o banco de dados do Google
if DATABASE_TYPE == "online" and os.environ.get("GOOGLE_CLOUD_PROJECT", None):
    print('\nINICIANDO DATABASE_TYPE ONLINE E CONFIGURANDO INFORMAÇÕES DO GOOGLE PROJET E SECRET\n')
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    client = secretmanager.SecretManagerServiceClient()
    settings_name = os.environ.get("SETTINGS_NAME", "django_settings")
    name = f"projects/{project_id}/secrets/{settings_name}/versions/latest"
    print(f'acesso ao google cloud configurado como `{name}\nIniciar tentativas de acesso:\n')
    
    try:
        print('1 - tentando acessar o secret')
        secret_version = client.access_secret_version(name=name)
        print(f'Secret version definido como:\n {secret_version,} \n')
        payload = secret_version.payload.data.decode("UTF-8")
        print('\n\ncarregando a versão no formato UTF8: ',payload)
        print('Lendo o arquivo .env: \n',env)
        env.read_env(io.StringIO(payload))
        print('arquivo env lido com sucesso, seguindo..\n')
    except google.api_core.exceptions.NotFound as e:
        print(f"Erro: O segredo '{settings_name}' não foi encontrado no Google Secret Manager.")
        # Trate o erro conforme necessário, por exemplo, definindo uma configuração padrão ou levantando uma exceção personalizada.
        DATABASE_TYPE = "local"
    except Exception as e:
        print(f"Erro ao acessar o banco de dados do Google: {e}")
        # Trate o erro conforme necessário, por exemplo, definindo uma configuração padrão ou levantando uma exceção personalizada.
        DATABASE_TYPE = "local"

# Configuração da chave secreta e opções de segurança
SECRET_KEY = env("SECRET_KEY")
print(f'secret key definida como: {SECRET_KEY}')
DEBUG = True  # Altere para "False" em ambiente de produção

# Configuração de segurança para o uso do App Engine
APPENGINE_URL = env("APPENGINE_URL", default=None)
if APPENGINE_URL:
    if not urlparse(APPENGINE_URL).scheme:
        APPENGINE_URL = f"https://{APPENGINE_URL}"
    ALLOWED_HOSTS = [urlparse(APPENGINE_URL).netloc]
    CSRF_TRUSTED_ORIGINS = [APPENGINE_URL]
    SECURE_SSL_REDIRECT = True
else:
    ALLOWED_HOSTS = ['foton.arqlamp.com','www.foton.arqlamp.com','foton-393716.uw.r.appspot.com', 'localhost', '127.0.0.1',]
print(f'APPENGINE_URL DEFINIDA COMO: {APPENGINE_URL}')
# Definição das aplicações instaladas e configuração de autenticação
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.apple',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.microsoft',
    'foton',  # Aplicação principal do projeto
    'fotonAdmin', #Aplicação de gestão do sistema
    'fotonUser', # Aplicação dos usuários do sistema
    'GestaoContrato',  # Aplicação de gestão de contrato
    'GestaoCliente',  # Aplicação de gestão de cliente
    'GestaoOrcamento',  # Aplicação de gestão de orçamento
    'GestaoRequisitos', #Aplicação de gestão de Requisitos do contrato
    # outras aplicações...
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = 'none'
LOGIN_REDIRECT_URL = "fotonUser:fotonUser_home"

# Configuração de middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuração das URLs do aplicativo
ROOT_URLCONF = 'foton.urls'

# Configuração de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuração da aplicação WSGI
WSGI_APPLICATION = 'foton.wsgi.application'

print(f'\nBANCO DE DADOS DEFINIDO COMO : {DATABASE_TYPE}')

# Configuração do banco de dados
if DATABASE_TYPE == "local":
    # Configurar o banco de dados local a partir das configurações do arquivo 2.env
    DATABASES = {
        "default": {
            "ENGINE": config.get("database", "ENGINE"),
            "NAME": config.get("database", "NAME"),
            "USER": config.get("database", "USER"),
            "PASSWORD": config.get("database", "PASSWORD"),
            "HOST": config.get("database", "HOST"),
            "PORT": config.get("database", "PORT"),
        }
    }
else:
    # Configurar o banco de dados do Google a partir das configurações obtidas do Secret Manager
    print('UTILIZANDO O DATABASE DO ARQUIVO .ENV - DO GOOGLE')
    DATABASES = {"default": env.db()}
    print(DATABASES)

# Configuração adicional do banco de dados, se necessário
if os.getenv("USE_CLOUD_SQL_AUTH_PROXY", None):
    DATABASES["default"]["HOST"] = "127.0.0.1"
    if DATABASE_TYPE=='local':
        DATABASES["default"]["PORT"] = 3306
    else:
        DATABASES["default"]["PORT"] = 3307

# Configuração para uso de banco de dados em memória durante testes em ambientes de CI
# TODO(glasnt) VERIFIQUE SE ISSO É NECESSÁRIO porque estamos configurando acima
if os.getenv("TRAMPOLINE_CI", None):
    print('\n CONFIGURANDO O TRAMPOLINE_CI')
    DATABASES = {
    'default': {
        'ENGINE': config.get('database', 'ENGINE'),
        'NAME': config.get('database', 'NAME'),
        'USER': config.get('database', 'USER'),
        'PASSWORD': config.get('database', 'PASSWORD'),
        'HOST': config.get('database', 'HOST'),
        'PORT': config.get('database', 'PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
#print('\nvalidando passwords')
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

ll_CC = 'pt_BR'

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = "static"
STATIC_URL = "/static/"
STATICFILES_DIRS = []

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


print(f'Configuração do banco de dados: \n {DATABASES}')
print('\nFim do settings.py')