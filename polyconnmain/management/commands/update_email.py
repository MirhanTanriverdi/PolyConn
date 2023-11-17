from django.core.management.base import BaseCommand, CommandError
from polyconnmain.models import User

class Command(BaseCommand):
    help = 'Updates the email of a user with the given user ID'

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, help='ID of the user')
        parser.add_argument('new_email', type=str, help='New email address for the user')

    def handle(self, *args, **kwargs):
        user_id = kwargs['user_id']
        new_email = kwargs['new_email']

        try:
            user = User.objects.get(id=user_id)
            user.email = new_email
            user.save()
            self.stdout.write(self.style.SUCCESS(f"User's email updated: {user.email}"))
        except User.DoesNotExist:
            raise CommandError('User not found')
        except Exception as e:
            raise CommandError(f'Error updating user email: {e}')
