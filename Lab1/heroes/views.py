from django.views.generic.base import TemplateView


class HeroesView(TemplateView):
	template_name = 'heroes.html'


class CloudView(TemplateView):
	template_name = 'detail_cloud.html'


class SunfloweyView(TemplateView):
	template_name = 'detail_sunflowey.html'


class JesterView(TemplateView):
	template_name = 'detail_jester.html'