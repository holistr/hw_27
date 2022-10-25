from datetime import date

from poetry import factory


class UserFactory(factory.django.DjangoModelFactory):
    first_name = 'test',
    last_name = 'testiev',
    username = 'johny_test',
    email = 'johny@test.ru',
    password = '123456',
    birth_date = factory.Faker('date_object')

    class Meta:
        model = 'users.User'


class SelectionFactory(factory.django.DjangoModelFactory):
    name = 'test_name'
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = 'ads.Selection'


class AdFactory(factory.django.DjangoModelFactory):
    name = "Ad"
    author = factory.SubFactory(UserFactory)
    price = 1

    class Meta:
        model = 'ads.Ad '
