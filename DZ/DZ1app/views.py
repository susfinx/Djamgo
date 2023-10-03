from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def home(request):
    html = """
    <html>
    <head>
        <title>Мой первый Django сайт</title>
    </head>
    <body>
        <h1>Добро пожаловать на мой первый Django сайт</h1>
        <p>Это главная страница моего сайта.</p>
    </body>
    </html>
    """
    logger.info("Главная страница посещена")
    return HttpResponse(html)

def about(request):
    html = """
    <html>
    <head>
        <title>О себе</title>
    </head>
    <body>
        <h1>Обо мне</h1>
        <p>Привет, меня зовут ROMA. Я начинающий веб-разработчик и создал этот сайт с использованием Django.</p>
        <p>Здесь вы можете узнать больше о моих навыках и проектах.</p>
    </body>
    </html>
    """

    logger.info("Страница 'О себе' посещена")
    return HttpResponse(html)
