from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from web import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.HomeView.as_view(), name="home"),

    # User management related pages
    url(r'^profile/$', views.MyProfileView.as_view(), name="profile"),
    url(r'^profile/$', views.ProfileView.as_view(), name="profile"),

    # Games and renting related pages
    url(r'^games/$', views.GamesView.as_view(), name="games"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
