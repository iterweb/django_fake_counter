from django.template import Library
from random import randint
from datetime import datetime
from fake_count.app_settings import DAY, NIGHT


register = Library()

night = 235922861933
morning = 100129385257
current_time = str(datetime.now().time()).replace(':', '').replace('.', '')


@register.inclusion_tag('_count.html')
def fake_counter():
    time = randint(4, 9)
    if morning < int(current_time):
        random_num = randint(1, (DAY / 100 * 5))
        res = DAY - random_num
        return {
            'counter': str(res),
            'time': time,
        }

    elif night > int(current_time):
        random_num = randint(1, (NIGHT / 100 * 5))
        res = NIGHT - random_num
        return {
            'counter': str(res),
            'time': time,
        }
