from faker import Faker


def generate_fake_first_name():
    return Faker().first_name()
