from django.urls import path
from .endpoints import (
    ThreadItemEndpoint,
    ThreadResolveEndpoint,
    CommentsEndpoint,
    ReactionsEndpoint,
)
from .turnstile import turnstile_view


urlpatterns = [
    path('embed/turnstile', turnstile_view),
    path('threads/resolve', ThreadResolveEndpoint.as_view()),
    path('threads/<thread_id>', ThreadItemEndpoint.as_view()),
    path('threads/<thread_id>/comments', CommentsEndpoint.as_view()),
    path('threads/<thread_id>/reactions', ReactionsEndpoint.as_view()),
]
