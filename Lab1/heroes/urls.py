from django.conf.urls import url

from .views import heroesView, cloudView, sunfloweyView, jesterView

urlpatterns = [
	url(r'^heroes/$', heroesView.as_view(), name='heroes_show'),
	url(r'^heroes/cloud$', cloudView.as_view(), name='cloud_show'),
	url(r'^heroes/sunflowey$', sunfloweyView.as_view(), name='sunflowey_show')
	url(r'^heroes/jester$', jesterView.as_view(), name='jester_show')
]