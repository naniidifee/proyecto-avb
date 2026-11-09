# primero descarga el proyecto
git clone "url-proyecto"

# segundo instala las librerias necesarias
pip o pipenv install -r requirements.txt

# luego hacer migraciones
py manage.py migrate

# si da error hacer makemigrations

# NO SE OLVIDEN DE SU RAMA 