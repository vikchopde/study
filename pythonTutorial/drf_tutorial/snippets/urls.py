from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
# from .views import SnippetListView, SnippetDetailView, SnippetDeleteView
from .views import snippet_list, snippet_detail, index_view, dashboard_view
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', snippet_list, name='snippet_list'),
    url(r'^(?P<pk>\d+)/$', snippet_detail, name='snippet_detail'),
    url(r'index.html/$', index_view, name='index'),
    url(r'dashboard.html/$', dashboard_view, name='dashboard')
]

# format_suffix_patterns() adds more urls to the urlspatterns
# by default it adds url.json and url.api to every url. This way you can specify
# the exact url (with the json or api suffix) to get a json response or a browseable api look.
# the function can take any list/tuple of suffixes you want to provide.
urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)