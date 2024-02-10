"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from blog.feeds import RssTutorialsFeeds
from blog.views import TutorialListView, TutorialDetailView, upload_image, image_view

urlpatterns = [
    path("admin", admin.site.urls),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path("feed", RssTutorialsFeeds(), name="tutorial_feed"),
    path("<slug:slug>", TutorialDetailView.as_view(), name="tutorial_detail"),
    path("", TutorialListView.as_view(), name="tutorial_list"),
    path("upload/", upload_image, name="upload_image"),
    path("images/<str:image_name>", image_view, name="image_view"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
