from django.template.defaultfilters import register

@register.filter('intcomma')
def intcomma(value):
    return "{:,}".format(value)
