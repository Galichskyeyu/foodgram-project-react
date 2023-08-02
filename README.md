# Дипломный проект «Продуктовый помощник»

## Описание:
Foodgram - это сайт, на котором пользователи могут публиковать собственные рецепты,
добавлять чужие рецепты в избранное и подписываться на публикации других авторов.
Сервис «Список покупок» позволит пользователям создавать список продуктов,
которые нужно купить для приготовления выбранных блюд.

## Технологии:
- Django
- Git
- VSC
- DRF
- Docker
- NGINX
- PostgreSQL
- CI/CD
- Gunicorn
- GitHub Actions
- Я.Облако

## Как запустить проект на удаленном сервере с использованием Docker и DockerHub:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Galichskyeyu/foodgram-project-react.git
```

```
cd foodgram-project-react
```

Отредактировать файл docker-compose.yml в директории /infra:

```
backend:
  image: <ваш логин на DockerHub>/foodgram_backend:latest
frontend:
  image: <ваш логин на DockerHub>/foodgram_frontend:latest
```

Отредактировать файл nginx.conf в директории /infra:

```
server {
    listen 80;
    server_name <ваш сервер/домен>;
    ...
}
```

Создать файл .env в директории в директории /infra и прописать константы:

```
POSTGRES_DB='foodgram'
POSTGRES_USER='foodgram_user'
POSTGRES_PASSWORD='foodgram_user_password'
DB_HOST='db'
DB_PORT='5432'
ALLOWED_HOSTS='127.0.0.1, backend, <ваш сервер/домен>'
SECRET_KEY='<ваш secret_key>'
DEBUG = False
```

Собираем и пушим образы на DockerHub:

```
# Выполнить в директории /backend:
docker build -t <ваш логин на DockerHub>/foodgram_backend .
docker push <ваш логин на DockerHub>/foodgram_backend
# Выполнить в директории /frontend:
docker build -t <ваш логин на DockerHub>/foodgram_frontend .
docker push <ваш логин на DockerHub>/foodgram_frontend
```

На удаленном сервере создать директорию infra.
Скопировать файлы docker-compose.yml и .env из директории infra в директорию infra на удаленном сервере:
```
scp -i path_to_SSH/SSH_name docker-compose.yml username@server_ip:/home/username/infra/docker-compose.yml
scp -i path_to_SSH/SSH_name .env username@server_ip:/home/username/infra/.env

- path_to_SSH — путь к файлу с SSH-ключом;
- SSH_name — имя файла с SSH-ключом (без расширения);
- username — ваше имя пользователя на сервере;
- server_ip — IP вашего сервера.
```

Открыть файл конфигурации веб-сервера и вставить код из листинга:
```
sudo nano /etc/nginx/sites-enabled/default
```

```
server {
    server_name <ваш сервер/домен>;
    location / {
        proxy_set_header Host $http_host;
        proxy_pass http://127.0.0.1:8000;
    }
}
```

Запускаем проект на удаленном сервере из директории /infra:

```
docker compose -f docker-compose.yml up -d
```

Создаем и выполняем миграции:

```
sudo docker compose -f docker-compose.yml exec backend python manage.py makemigrations
sudo docker compose -f docker-compose.yml exec backend python manage.py migrate
```

Собираем статику бэкенда:

```
sudo docker compose -f docker-compose.yml exec backend python manage.py collectstatic
```

Создаем суперпользователя:

```
sudo docker compose -f docker-compose.yml exec backend python manage.py createsuperuser
```

Загружаем теги:

```
sudo docker compose -f docker-compose.yml exec backend python manage.py load_tags
```

Загружаем ингридиенты:

```
sudo docker compose -f docker-compose.yml exec backend python manage.py load_ingrs
```

Информация для самого лучшего ревьюера ٩(◕‿◕)۶ : 

```
http://yp-foodgram2023.ddns.net
Логин: admin@yandex.ru
Пароль: admin2023
```

## Автор: 
### [Эмин Галичский](https://github.com/Galichskyeyu "Эмин Галичский")