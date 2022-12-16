from importlib import import_module
from pathlib import Path
from typing import Iterable

from django.apps import AppConfig
from django.conf import settings
from rest_framework.viewsets import ViewSetMixin
from rest_framework_extensions.routers import ExtendedDefaultRouter


class ApiRouter(ExtendedDefaultRouter):

    @classmethod
    def from_apps(cls, app_configs: Iterable[AppConfig]):
        api_router = ExtendedDefaultRouter()
        print('\nApp urls:')
        for app_config in app_configs:
            if Path(app_config.path).parent != settings.BASE_DIR:
                continue
            try:
                views = import_module(f'{app_config.module.__name__}.views', app_config.module)
            except ModuleNotFoundError:
                continue
            print(f'\n  {app_config.module.__name__}')
            for attribute_name in dir(views):
                if attribute_name.startswith('_'):
                    continue
                attribute = getattr(views, attribute_name)
                if attribute.__class__.__name__ != 'type' or not issubclass(attribute, ViewSetMixin):
                    continue
                api_route = getattr(attribute, 'api_route', None)
                if api_route:
                    api_route = f"{getattr(attribute, 'api_route_prefix', app_config.name)}/{api_route}"
                    api_router.register(api_route, attribute)
                    print(f'    /api/{api_route} => {attribute}')
        print('')
        return api_router
