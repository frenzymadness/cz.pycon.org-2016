from django.conf.urls import url

from pyconcz_2017.team.views import team_list


urlpatterns = [
    url('^$', team_list, name="team_list"),
]
