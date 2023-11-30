from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TeamMember
from .forms import TeamMemberForm


class TeamMemberListView(ListView):
    model = TeamMember
    template_name = 'list.html'
    context_object_name = 'members'
    ordering = ['-id']


class TeamMemberCreateView(CreateView):
    model = TeamMember
    template_name = 'new.html'
    form_class = TeamMemberForm
    success_url = reverse_lazy('team_list')


class TeamMemberUpdateView(UpdateView):
    model = TeamMember
    template_name = 'edit.html'
    form_class = TeamMemberForm
    success_url = reverse_lazy('team_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member'] = self.object
        return context


class TeamMemberDeleteView(DeleteView):
    model = TeamMember
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('team_list')
