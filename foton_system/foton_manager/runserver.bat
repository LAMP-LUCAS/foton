call "c:\Users\Lucas\OneDrive\LAMP ARQUITETURA\foton\foton_system\foton_manager\Scripts\activate.bat"

cd "c:\Users\Lucas\OneDrive\LAMP ARQUITETURA\foton\foton_system\foton_manager\"

set GOOGLE_CLOUD_PROJECT=foton-393716

set USE_CLOUD_SQL_AUTH_PROXY=true

python manage.py runserver 8080

python manage.py browser
