from django import template
 
register = template.Library()
 
@register.filter(name='cursos')
def saludo(valor):
    return f"<h1 style='background:green; color:white;'> Bienvenido, {valor} </h1>"