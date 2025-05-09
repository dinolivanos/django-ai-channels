from django import template

register = template.Library()


@register.inclusion_tag("aichannels/tfjs_coco_ssd.html", takes_context=True)
def coco_ssd_js(context, config_variable="undefined"):
    return {
        "host": context['request'].get_host(),
        "config_variable": config_variable,
    }
