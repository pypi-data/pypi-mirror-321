from flask import render_template as flask_render_template
import os
import sys
import importlib

class Embed:
    """A Flask extension for embedding and running python code in HTML templates.
    """
    def __init__(self, app=None, auto_import_modules=True):
        self.auto_import_modules = auto_import_modules
        self.module_context = {}
        self.output = None
        if app is not None:
            self.init_app(app)
            
    def load_app_modules(self, app):
        """Dynamically load all modules in the app folder."""
        app_folder = os.path.dirname(app.root_path)
        sys.path.insert(0, app_folder)  # Add app folder to sys.path

        excluded_dirs = {".venv", "venv", "__pycache__", "Lib", "site-packages"}
        for root, dirs, files in os.walk(app_folder):
            # Filter out excluded directories
            dirs[:] = [d for d in dirs if d not in excluded_dirs]
            for file in files:
                if file.endswith(".py") and file != "__init__.py":
                    module_path = os.path.relpath(os.path.join(root, file), app_folder).replace(os.sep, ".")
                    module_name = module_path.replace(".py", "")  # Clean module name
                    try:
                        module = importlib.import_module(module_name)
                        self.module_context[module_name] = module
                        print(f"Loaded module: {module_name}")
                    except (ImportError, TypeError) as e:
                        print(f"Error importing module {module_name}: {e}")
                        
    def init_app(self, app):
        """
        Initialize this extension with the given Flask app.
        """
        if self.auto_import_modules:
            self.load_app_modules(app)

        app.extensions = getattr(app, "extensions", {})
        app.extensions["embed"] = self


    def render_template(self, template_name, **context):
        """
        Renders a Jinja template with a <Flask> component.
        Reads and executes the <Flask> component's Python code, preserving indentation.
        """
        rendered_html = flask_render_template(template_name, **context)
        lines = rendered_html.split("\n")
        
        flask_component = []
        in_flask = False

        # Extract the Python code within the <Flask> tags
        for line in lines:
            if "<Flask>" in line:
                in_flask = True
                continue
            elif "</Flask>" in line:
                in_flask = False
                break
            elif in_flask:
                flask_component.append(line)

        if not flask_component:
            return rendered_html


        # Combine the extracted lines, maintaining original indentation
        flask_code = "\n".join(flask_component)
        local_context = dict(context)
        try:
            exec(flask_code, self.module_context, local_context)
        except Exception as e:
            raise RuntimeError(f"Error executing <Flask> block: {e}")

        # Remove the <Flask> block from the final HTML
        cleaned_lines = []
        in_flask_block = False

        for line in lines:
            if "<Flask>" in line:
                in_flask_block = True
            elif "</Flask>" in line:
                in_flask_block = False
            elif not in_flask_block:
                cleaned_lines.append(line)
        
        final_lines = []
        for line in cleaned_lines:
            if "<FlaskOutput>" in line:
                output_content = str(local_context.get("output", ""))
                final_lines.append(line.replace("<FlaskOutput>", output_content))
            else:
                final_lines.append(line)

        # Return the processed HTML
        return "\n".join(final_lines)