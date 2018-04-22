from django.conf import settings

def export_vars(request):
    data = {}
    data['CONTEXT'] = settings.CONTEXT

    return data
