from django.urls import path
from .settings import SettingEndpoint
from .comments import (
    CommentListEndpoint,
    CommentItemEndpoint,
    CommentReplyEndpoint,
)
from .reactions import ReactionListEndpoint
from .threads import ThreadListEndpoint, ThreadStatusEndpoint

urlpatterns = [
    path('tenant/comment-setting', SettingEndpoint.as_view()),
    path('comments', CommentListEndpoint.as_view()),
    path('comments/<int:pk>', CommentItemEndpoint.as_view()),
    path('comments/<int:pk>/reply', CommentReplyEndpoint.as_view()),
    path('reactions', ReactionListEndpoint.as_view()),
    path('threads', ThreadListEndpoint.as_view()),
    path('threads/<pk>/status', ThreadStatusEndpoint.as_view()),
]
