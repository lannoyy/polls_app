from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from rest_framework import permissions

from api.client.views import UsersAnswers, CompletePolls, ActivePolls, PollInfo
from api.urls import router

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
      name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api_auth/', include('account.urls')),
    path('poll/<int:poll_pk>/user/<int:user_pk>/', UsersAnswers.as_view()),
    path('user/<int:user_pk>/polls/', CompletePolls.as_view()),
    path('polls/active/', ActivePolls.as_view()),
    path('poll/<int:poll_pk>/', PollInfo.as_view()),
] + router.urls
