FROM python:3.9.0

WORKDIR /home/

RUN echo "kjfdadgdfahh"

RUN git clone https://github.com/Lee-JuHwan/gis4_2.git

WORKDIR /home/gis4_2/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=djangoProject1.settings.deploy && python manage.py collectstatic --noinput --settings=djangoProject1.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=djangoProject1.settings.deploy djangoProject1.wsgi --bind 0.0.0.0:8000"]

