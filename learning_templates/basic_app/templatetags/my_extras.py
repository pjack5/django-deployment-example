from django import template

register = template.Library()

def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!

    """

    #passing what we're looking for, and replacing it with the second argument below
    return value.replace(arg,'')

#string that you call the function, and then the function itself
register.filter('cut', cut)
