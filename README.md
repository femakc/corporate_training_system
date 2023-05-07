Проект CTS Корпоративная система обучения

Описание  
Система обучения персонала, включет в себя несколько ролей пользлвателей с разными правами. Возможно добавление фото и видео материалов.

http://host/admin Админ-панель  

Для реализации проекта используются:        
Python 3.11  
PostgreSQL  
Django 4.2  
gunicorn 20.1.0  
psycopg2-binary  
docker  
docker-compose  
    
Содержание .env
```
DB_ENGINE=django.db.backends.postgresql  
DB_NAME=cts

POSTGRES_USER=cts_user  
POSTGRES_PASSWORD=cts_user

DB_PORT=5432  

DB_HOST=192.168.0.11

WEB_SRV_HOST=192.168.0.22

PROXY_HOST=192.168.0.33

SUBNET_ADDR=192.168.0.0/24
```

Запуск проекта:  

Клонировать репозиторий и перейти в директорию проекта /cts

При помощи docker compose запустить проект
```commandline
docker-compose up -d
```

Подключиться к контейнеру с django-приложением
```commandline
docker exec -it <container_hash> /bin/sh
```
Внутри контейнера:

Установить миграции 
```commandline
python manage.py migrate
```
Создать суперпользователя   
```commandline
python manage.py createsuperuser
```