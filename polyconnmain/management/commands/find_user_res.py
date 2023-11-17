from django.core.management.base import BaseCommand, CommandError
from polyconnmain.models import Cafe, Reservation_Participants

class Command(BaseCommand):
    help = 'Finds users with reservations at a specified cafe'

    def add_arguments(self, parser):
        parser.add_argument('cafe_id', type=int, help='ID of the cafe')

    def handle(self, *args, **kwargs):
        cafe_id = kwargs['cafe_id']

        try:
            cafe = Cafe.objects.get(id=cafe_id)
            participants = Reservation_Participants.objects.filter(
                reservation__cafe=cafe
            ).select_related('user')

            for participant in participants:
                self.stdout.write(str(participant.user))
        except Cafe.DoesNotExist:
            raise CommandError('Cafe not found')
        except Exception as e:
            raise CommandError(f'Error finding users: {e}')
