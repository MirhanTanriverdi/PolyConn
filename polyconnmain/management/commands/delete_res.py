from django.core.management.base import BaseCommand, CommandError
from polyconnmain.models import Reservation

class Command(BaseCommand):
    help = 'Deletes a reservation with the given reservation ID'

    def add_arguments(self, parser):
        parser.add_argument('reservation_id', type=int, help='ID of the reservation to delete')

    def handle(self, *args, **kwargs):
        reservation_id = kwargs['reservation_id']

        try:
            reservation = Reservation.objects.get(id=reservation_id)
            reservation.delete()
            self.stdout.write(self.style.SUCCESS(f"Reservation deleted: {reservation_id}"))
        except Reservation.DoesNotExist:
            self.stdout.write(self.style.ERROR("Reservation not found"))
        except Exception as e:
            raise CommandError(f'Error deleting reservation: {e}')
