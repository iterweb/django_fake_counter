from django.conf import settings

DAY = getattr(settings, 'MAX_COUNT_DAY', 500)
NIGHT = getattr(settings, 'MAX_COUNT_NIGHT', 200)