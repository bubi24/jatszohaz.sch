from django.conf.urls import url

from . import views

app_name = 'inventory'
urlpatterns = [
    url(r'^$', views.InvListView.as_view(), name="list"),
    url(r'^(?P<game_pk>\d+)/$', views.InvListGameView.as_view(), name="gamepiece"),

    url(r'^new/$', views.NewInvView.as_view(), name="new"),
    url(r'^new/(?P<game_pk>\d+)/$', views.NewInvView.as_view(), name="new"),
    url(r'^edit/(?P<pk>\d+)/$', views.EditView.as_view(), name="edit"),

    url(r'^new-game-with-group/$', views.NewGameWithGroupView.as_view(), name="new-game-with-group"),
    url(r'^new-game/$', views.NewGameView.as_view(), name="new-game"),
    url(r'^edit-gamegroup/(?P<pk>\d+)/$', views.EditGameGroup.as_view(), name="edit-gamegroup"),
    url(r'^edit-gamepiece/(?P<pk>\d+)/$', views.EditGamePiece.as_view(), name="edit-gamepiece"),
]
