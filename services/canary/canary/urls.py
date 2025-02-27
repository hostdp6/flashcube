"""canary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from towers import views

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet, 'Category')
router.register(r'collection', views.CollectionViewSet, 'Collection')
router.register(r'cube', views.CubeViewSet, 'Cube')
router.register(r'face', views.FaceViewSet, 'Face')
router.register(r'tower', views.TowerViewSet, 'Tower')
router.register(r'list', views.ListViewSet, 'List')
router.register(r'locale', views.LocaleViewSet, 'Locale')
router.register(r'user_preferences', views.UserPreferencesViewSet, 'UserPreferences')
router.register(r'user_subscription', views.UserSubscriptionViewSet, 'UserSubscription')

urlpatterns = [

    # admin UI urls
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),

    # authentication
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('register/', views.CreateUser.as_view()),

    # REST api
    path('api/', include(router.urls)),
    path('api/user/', views.GetUser.as_view()),
    path('api/user_image/', views.UploadProfileImage.as_view()),
    path('api/editlist/', views.ListAddRemove.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)