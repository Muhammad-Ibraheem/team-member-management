from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from .models import TeamMember


class TeamMemberForm(forms.ModelForm):
    ROLES_CHOICES = [
        ('regular', 'Regular - Can\'t delete members'),
        ('admin', 'Admin - Can delete members'),
    ]

    role = forms.ChoiceField(
        choices=ROLES_CHOICES,
        widget=forms.RadioSelect,  # You can choose another widget if needed
    )

    class Meta:
        model = TeamMember
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'role']
