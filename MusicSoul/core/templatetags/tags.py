from django import template

register = template.Library()

@register.simple_tag
def active(current_path, expected_path, strict = False):
    if (strict):
        if (current_path == expected_path):
            return 'active'
    else:
        if (current_path[:len(expected_path)] == expected_path):
            return 'active'
    return ''
