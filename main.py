import jinja2   # Шаблонизатор jinja2
from aiohttp import web     # Основной модуль
import aiohttp_jinja2   # адаптация jinja2 k aiohttp


# в этой функции производится настройка url-путей для всего приложения
def setup_routes(applitation):
    from MyFirstApp.forum.routes import setup_routes as setup_forum_routes
    setup_forum_routes(applitation)


def setup_external_libraries(application: web.Application) -> None:
    # указываем где хранятся шаблоны
    aiohttp_jinja2.setup(application, loader=jinja2.FileSystemLoader('templates'))


def setup_app(application):
    setup_external_libraries(application)
    setup_routes(application)


app = web.Application()     # Создание веб-сервера


if __name__ == '__main__':
    setup_app(app)
    web.run_app(app)
