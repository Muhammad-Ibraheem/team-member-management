from django.urls import path
from .views import TeamMemberListView, TeamMemberCreateView, TeamMemberUpdateView, TeamMemberDeleteView

urlpatterns = [
    path('', TeamMemberListView.as_view(), name='team_list'),
    path('add/', TeamMemberCreateView.as_view(), name='add_member'),
    path('edit/<int:pk>/', TeamMemberUpdateView.as_view(), name='edit_member'),
    path('delete/<int:pk>/', TeamMemberDeleteView.as_view(), name='delete_member'),
]
