import importlib
import os

def register_routes(app):
    routes_folder = os.path.dirname(__file__)

    for filename in os.listdir(routes_folder):
        if filename.endswith(".py") and filename != '__init__.py':
            module_name = filename[:-3]  # remove .py
            module_path = f'app.routes.{module_name}'
            module = importlib.import_module(module_path)

            if module_name.endswith('_routes'):
                base_name = module_name.replace('_routes', '')
                blueprint = getattr(module, f"{base_name}_bp", None)

                if blueprint:
                    app.register_blueprint(blueprint)


