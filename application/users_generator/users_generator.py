from application import fake_names
from random import choice


mailboxes = ["@gmail.com", "@ukr.net", "@ithillel.ua", "@business.com"]


def create_users_generator(count=100):

    users = (fake_names.generate_fake_first_name() for user in range(count))

    return users


def get_random_users_email(generator=None):

    if generator is None:
        generator = create_users_generator()

    for user in generator:
        yield f"{user} example{choice(mailboxes)}"
