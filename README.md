# Обрезка ссылок с помощью Битли

Проект берет сокращает ссылки или смотрит сколько раз прошли по короткой ссылке.

### Как установить

Зарегистрироваться на сайте https://bit.ly/ . Создать токен с помощью генераторов токенов и положить токен в переменную bitly_token.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
## Переменные окружение
Для запуска необходимо создать файо .env. В нем хранятся переменные окружения для правильной работы кода. Пример содержимого файла .env:
```python
"bitly_token="85702846582048501379033"
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
