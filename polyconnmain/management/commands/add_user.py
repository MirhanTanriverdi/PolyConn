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

