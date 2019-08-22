from jinja2 import Template, FileSystemLoader, Environment

def render_template(template_name, **kwargs):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template(template_name)
    return template.render(**kwargs)
