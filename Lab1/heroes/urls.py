from django.conf.urls import url

from .views import heroesView, cloudView, sunfloweyView, jesterView

urlpatterns = [
	url(r'^heroes/$', heroesView.as_view(), name='heroes'),
	url(r'^heroes/cloud$', cloudView.as_view(), name='Cloud'),
	url(r'^heroes/sunflowey$', sunfloweyView.as_view(), name='Sunflowey')
	url(r'^heroes/jester$', jesterView.as_view(), name='Jester')
]