from jinja2 import Template

ru_ege_info_message_template = Template(
    """<u>{{date}}</u>\n\n<b>Орфоэпия</b>\n{{orthoepy}}\n\n<b>Паронимы</b>\n{{paronyms}}\n\n<b>Фразеологизм</b>\n{{phraseological_unit}}\n\n<b>Безударные в корне</b>\n{{unstressed_at_root}}"""
)
