from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static

from .views import home
from accounts.views import login_page, register_page, leaderboard_view


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^login/$', login_page, name='login'),
    url(r'^register/$', register_page, name='register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^leaderboard/$', leaderboard_view, name='leaderboard'),
    url(r'^questions/', include('questions.urls', namespace='question')),
    url(r'^question/', include('grader.urls', namespace='grader')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
