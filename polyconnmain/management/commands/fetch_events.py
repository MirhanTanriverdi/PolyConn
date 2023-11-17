from django.core.management.base import BaseCommand, CommandError
from polyconnmain.models import User, Event

class Command(BaseCommand):
    help = 'Finds events based on a user\'s district'

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, help='User ID')

    def handle(self, *args, **options):
        user_id = options['user_id']

        try:
            user = User.objects.get(id=user_id)
            events = Event.objects.filter(district=user.district)

            if events.exists():
                for event in events:
                    self.stdout.write(self.style.SUCCESS(f'Event: {event.name} in District: {event.district.name}'))
            else:
                self.stdout.write('No events found in the user\'s district.')
                
        except User.DoesNotExist:
            raise CommandError("User not found")
        except Exception as e:
            raise CommandError(f"Error finding events: {e}")
