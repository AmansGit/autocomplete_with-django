from .models import Names

from faker import Faker

fake = Faker()


def seed_db():
	Names.objects.create(
		name = fake.name()
		)