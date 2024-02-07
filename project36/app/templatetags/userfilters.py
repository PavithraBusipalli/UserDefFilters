from django import template

# Register custom filters --> we can register it in 2 ways
# 1. Using register.filter()
# 2. By decorating filter

# Library - > instance
register = template.Library()

def lower(value):
    return value.lower()

register.filter('lower', lower)

@register.filter()
def swap(value):
    return value.swapcase()

@register.filter()
def remove(value,arg):
    return value.replace(arg,'')

@register.filter()
def counting(value,arg):
    c = 0
    for ip in range(len(value)):
        if arg == value[ip:len(arg)+ip:1]:
            c += 1
    return c


'''
register.filter('counting',counting)
register.filter('swap',swap)
register.filter('remove',remove)

'''