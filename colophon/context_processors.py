from django.conf import settings
from colophon.constants import PARAM_CODES

def export_vars(request):
    data = {}
    data['CONTEXT'] = settings.CONTEXT

    return data

def message_params(request):
    data = {}
    messageParam = request.GET.get('m')

    if messageParam:
        data['MESSAGE'] = PARAM_CODES[messageParam]

    return data
