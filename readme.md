python -m pip install django-cotton
python -m pip install pipx
pipx run shadcn_django@latest init

<!-- Tailwind Force -->
python -m pip install whitenoise
python -m pip freeze > requirements.txt

# build_files.sh
pip install -r requirements.txt
python manage.py collectstatic --no-input --clear