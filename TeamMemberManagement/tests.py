from django.test import TestCase
from django.urls import reverse
from .models import TeamMember


class TeamMemberViewsTest(TestCase):
    # create dummy user
    def setUp(self):
        self.team_member = TeamMember.objects.create(
            first_name='John',
            last_name='Doe',
            phone_number='123-456-7890',
            email='john@example.com',
        )

    # test case for create view
    def test_team_member_create_view(self):
        data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'phone_number': '987-654-3210',
            'email': 'jane@example.com',
            'role': 'admin',
        }
        response = self.client.post(reverse('add_member'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('team_list'))

    # test case for list view
    def test_team_member_list_view(self):
        response = self.client.get(reverse('team_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')

    # test case for update view
    def test_team_member_update_view(self):
        data = {
            'first_name': 'Updated',
            'last_name': 'Name',
            'phone_number': '555-555-5555',
            'email': 'updated@example.com',
            'role': 'admin',
        }
        response = self.client.post(reverse('edit_member', args=[self.team_member.id]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('team_list'))
        self.team_member.refresh_from_db()
        self.assertEqual(self.team_member.first_name, 'Updated')

    # test case for delete view
    def test_team_member_delete_view(self):
        response = self.client.post(reverse('delete_member', args=[self.team_member.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('team_list'))
        self.assertFalse(TeamMember.objects.filter(id=self.team_member.id).exists())