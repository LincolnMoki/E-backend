serve:
	python3 manage.py runserver
superuser:
	python3 manage.py createsuperuser --username $(name) 
migrate:
	python3 manage.py migrate
app:
	django-admin startapp $(name)
migrations:
	python3 manage.py makemigrations $(app)
check:
	python manage.py check
collectstatic:
	python3 manage.py collectstatic
