MANAGE = python manage.py

run:
	$(MANAGE) runserver

migrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

superuser:
	$(MANAGE) createsuperuser

shell:
	$(MANAGE) shell

init:
	$(MANAGE) create_bank
	$(MANAGE) create_fruits
	$(MANAGE) create_users

celery_worker:
	celery -A my_fruit_shop worker --loglevel=info

celery_beat:
	celery -A my_fruit_shop beat