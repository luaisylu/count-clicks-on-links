# Обрезка ссылок с помощью Битли

Скрипт проект берет, сокращает переданную ссылку и выводит в консоль. Либо берет короткую ссылку (битли), получает информацию про клики и выводит в консоль.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Переменные окружение

Зарегистрироваться на сайте https://bit.ly/ . Создать токен с помощью генераторов токенов(генерация токена происходит в личном кабинете [bitlink](https://bitly.com/a/sign_in?rd=/settings/api/) и положить токен в переменную BITLY_TOKEN..
Для запуска необходимо создать файл .env. В нем хранятся переменные окружения для правильной работы кода. Пример содержимого файла .env:
```python
BITLY_TOKEN="85702846582048501379033"
```
### Примеры запуска скриптов
Для запуска скрипта необходимо ввести следующий код:
```python
python main.py --url *ссылка*
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
