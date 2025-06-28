# Yatube API

## Описание

API для социальной сети Yatube: посты, комментарии, подписки, группы. Аутентификация — JWT.

## Как запустить проект

Клонируйте репозиторий и перейдите в папку проекта:

```
git clone <url-репозитория>
cd api-final-yatube
```

Создайте и активируйте виртуальное окружение:

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```

Установите зависимости:

```
pip install -r requirements.txt
```

Выполните миграции:

```
cd yatube_api
python manage.py migrate
```

Создайте суперпользователя (По желанию):

```
python manage.py createsuperuser
```

Запустите сервер:

```
python manage.py runserver
```

## Документация

- ReDoc: http://localhost:8000/redoc/
