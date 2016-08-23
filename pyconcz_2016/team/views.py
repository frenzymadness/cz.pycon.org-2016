from django.template import RequestContext
from django.template.response import TemplateResponse

from pyconcz_2016.team.models import Organizer


def team_list(request):
    organizers = Organizer.objects.all().filter(published=True)

    return TemplateResponse(
        request,
        template='team/organizers_list.html',
        context={
            'organizers': organizers
        }
    )
