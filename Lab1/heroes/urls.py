from django.conf.urls import url

from .views import HeroesView, CloudView, SunfloweyView, JesterView

urlpatterns = [
		url(r'^heroes/$', HeroesView.as_view(), name='heroes_show'),
		url(r'^hero/cloud$', CloudView.as_view(), name='cloud_show'),
		url(r'^hero/sunflowey$', SunfloweyView.as_view(), name='sunflowey_show')
		url(r'^hero/jester$', JesterView.as_view(), name='jester_show')
]