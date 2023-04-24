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
DB_ENGINE=django.db.backends.postgresql  
DB_NAME=cts  
POSTGRES_USER=cts_user  
POSTGRES_PASSWORD=cts_user  
DB_HOST=127.0.0.1  
DB_PORT=5432  


Запуск проекта:  
Клонировать репозиторий и перейти в папку с проектом    
Установить виртуальное окружение 
```commandline
python3 -m venv venv
```
Активировать виртуальное окружение  
```commandline
source venv/bin/activate
```

Перейти в директорию cts/ и установить и файла requirements.txt зависимости
```commandline
pip install -r requirements.txt
```
Установить миграции 
```commandline
python manage.py migrate
```
Создать суперпользователя   
```commandline
python manage.py createsuperuser
```
Запустить сервер
```commandline
python manage.py migrate
```






