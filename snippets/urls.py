from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from snippets import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetails.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
