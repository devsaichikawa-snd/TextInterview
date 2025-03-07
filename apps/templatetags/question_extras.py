from django import template


register = template.Library()


@register.filter
def question_dict_unpack(dict, key):
    """qtop.htmlのquestionsを展開する補助関数"""
    if key in dict.keys():
        return dict[key]
