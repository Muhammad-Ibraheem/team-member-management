from django.shortcuts import render, redirect, HttpResponse
from .models import TeamMember
from .forms import TeamMemberForm


# Create your views here.

def team_list(request):
    if request.method == "GET":
        members = TeamMember.objects.all().order_by('-id')
        return render(request, 'list.html', {"members": members})


def add_member(request):
    if request.method == "POST":
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    form = TeamMemberForm()
    return render(request, 'new.html', {'form': form})


def edit_member(request, pk):
    member = TeamMember.objects.get(pk=pk)
    if request.method == "POST":
        if 'delete' in request.POST:
            member.delete()
            return redirect('team_list')
        form = TeamMemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    form = TeamMemberForm(instance=member)
    return render(request, 'edit.html', {"form": form, "member": member})


def delete_member(request, pk):
    member = TeamMember.objects.get(pk=pk)
    print(member)
    member.delete()
    return redirect('team_list')
