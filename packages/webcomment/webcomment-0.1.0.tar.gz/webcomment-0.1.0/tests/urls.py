from django.urls import path, include

urlpatterns = [
    path('api/', include('webcomment.management_api.urls')),
    path('api/browser/', include('webcomment.widget.urls')),
    path('s/', include('webcomment.webmention.urls')),
]
