from .models import Names

from faker import Faker

fake = Faker()


def seed_db(num):
	for _ in range(num):
		Names.objects.create(
			name = fake.name()
		)
		Names.objects.create(
			address = fake.address()
		)