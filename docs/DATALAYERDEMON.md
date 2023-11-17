### 1. Creating a New User (Create Operation)

To Create/Add new User, you the run the following code in the Terminal/Shell. 

```python
python manage.py create_user <username> <email> <password> <district_name> [--age AGE] [--gender GENDER] [--nationality NATIONALITY] [--german_proficiency_level PROFICIENCY_LEVEL] [--native_language NATIVE_LANGUAGE] [--learning_languages LEARNING_LANGUAGES] [--hobbies HOBBIES]
```

EXAMPLE; 

```python
python manage.py create_user john_doe john@example.com password123 Downtown --age 30 --learning_languages German
```

Implemented Script; 

```python
from django.core.management.base import BaseCommand, CommandError
from polyconnmain.models import User, District

class Command(BaseCommand):
    help = 'Creates a new user'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='User username')
        parser.add_argument('email', type=str, help='User email')
        parser.add_argument('password', type=str, help='User password')
        parser.add_argument('district_name', type=str, help='User district name')
        parser.add_argument('--age', type=int, help='User age', default=None)
        parser.add_argument('--gender', type=str, help='User gender', default=None)
        parser.add_argument('--nationality', type=str, help='User nationality', default=None)
        parser.add_argument('--german_proficiency_level', type=str, help='User German proficiency level', default=None)
        parser.add_argument('--native_language', type=str, help='User native language', default=None)
        parser.add_argument('--learning_languages', type=str, help='User learning languages', default=None)
        parser.add_argument('--hobbies', type=str, help='User hobbies', default=None)

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']
        district_name = options['district_name']
        age = options['age']
        gender = options['gender']
        nationality = options['nationality']
        german_proficiency_level = options['german_proficiency_level']
        native_language = options['native_language']
        learning_languages = options['learning_languages']
        hobbies = options['hobbies']

        try:
            district, _ = District.objects.get_or_create(name=district_name)
            user = User.objects.create(
                username=username,
                email=email,
                password=password,
                district=district,
                age=age,
                gender=gender,
                nationality=nationality,
                german_proficiency_level=german_proficiency_level,
                native_language=native_language,
                learning_languages=learning_languages,
                hobbies=hobbies
            )
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created user {username}'))
        except Exception as e:
            raise CommandError(f'Error creating user: {e}')
```

### 2. Fetching Events in a User's District (Read Operation)

To fetch events based on user’s district, you the run the following code in the Terminal/Shell. 

```python
python manage.py find_events_by_user_district <user_id>
```

EXAMPLE; 
P.S - A 1001 Mock Users Exists. 

```python
python manage.py find_events_by_user_district 1000
```

Implemented Script;

```python
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
                    self.stdout.write(self.style.SUCCESS(
                        f'Event: {event.event_name}, Type: {event.event_type}, '
                        f'Date: {event.date}, District: {event.district.name}'
                    ))
            else:
                self.stdout.write('No events found in the user\'s district.')

        except User.DoesNotExist:
            raise CommandError("User not found")
        except Exception as e:
            raise CommandError(f"Error finding events: {e}")

```

### 3. Updating User's Email (Update Operation)

To Update emails based on user’s Table, you the run the following code in the Terminal/Shell. 

```python
python manage.py update_email <user_id> <new_email>
```

EXAMPLE; 
P.S - A 1001 Mock Users Exists.

```python
python manage.py update_email 777 thth@gmail.com
```

Implemented Script;

```python
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
```

### 4. Deleting a Reservation (Delete Operation)

To Delete from Reservatino Table, you the run the following code in the Terminal/Shell. 

```python
python manage.py delete_res <reservation_id>
```

EXAMPLE; 
P.S - 500 Mock Reservation exist.

```python
python manage.py delete_res 333
```

Implemented Script;

```python
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

```

### 5. Complex Query: Find Users with Reservations at a Specific Cafe (Complex Query)

To Find Users with Reservation at a specific cafe while using Cafe and User Tables, you the run the following code in the Terminal/Shell. 

```python
python manage.py find_user_res <cafe_id>
```

EXAMPLE; 
P.S - 481 - 540 Mock Cafe exist. (Numbers are auto Generated By DataGrip)
- It is advised to use user Id 518 due to lack of data.. 

```python
python manage.py find_user_res 518
```

Implemented Script;

```python
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

```

###