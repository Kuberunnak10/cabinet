## Description
Личный кабинет заказчика и исполнителя на Django 5.0  
База данных Postgres

## How to start

1. Склонировать проект с github.
2. Создать файл .env и вставить свои параметры по примеру файла .env-test
3. Запустить Docker desctop
4. В корневой папке проекта прописать:
```
docker-compose up
```
## Exploitation

Для входа в админ панель уже создан пользователь с логином и паролем для просмотра заказчиков и исполнителей:  
Username: admin  
Password: admin  

- Вы можете создать нового пользователя в админ панели или зарегистрироваться через главную страницу сайта по кнопке "Регистрация"

- После входа у вас будет доступена ваша карточка (Кабинет) по кнопке "Профиль"

- Там вы можете дополнить свои контактные данные и тд., а так же поменять свою роль с заказчика на исполнителя или наоборот.(Опыта у заказчика быть не может)

- Главная страница при запуске через Docker находится по URL: http://localhost:8000/ 


