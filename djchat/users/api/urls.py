from django.urls import path
from users.api.views import CurrentUserAPIView, UsersAPIView

urlpatterns = [
    path('me/', CurrentUserAPIView.as_view(), name='current-user'),
    path('users/', UsersAPIView.as_view()),

    # path('invitations', InvitationAPIView.as_view()),
    # path('invitations/<int:invitation_id>', InvitationAPIView.as_view()),
    # path('invitations?direction=sent|received', InvitationAPIView.as_view()),
    # path('invitations/create', CreateInvitationAPIView.as_view()),

    # path('invitations/<int:invitation_id>/accept', UsersAPIView.as_view()),
    # path('invitations/<int:invitation_id>/decline', UsersAPIView.as_view()),

    # path('users/friends', UsersAPIView.as_view()),
    # path('users/friends/<int:friend_id>', UsersAPIView.as_view()),
    # path('users/friends/<int:friend_id>/delete', UsersAPIView.as_view()),
    # path('users/friends/<int:friend_id>/block', UsersAPIView.as_view()),
]
