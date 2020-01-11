from django import template

register = template.Library()

# {{ +79833839583|phone }} +7(983)383-95-83
@register.filter
def phone_format(value):
    value = value.replace(' ', '').replace('-', '')
    return f'{value[:-10]} ({value[-10:-7]}) {value[-7:-4]}-{value[-4:-2]}-{value[-2:]}'