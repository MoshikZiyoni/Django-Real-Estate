from django.template.defaultfilters import register

@register.filter('intcomma')
def intcomma(value):
    if type(value) != int:
            return value
    else:
        return format(int(value), ",")