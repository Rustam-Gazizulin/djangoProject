import factory.django

from authentication.models import User
from vacancies.models import Vacancy


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = 'parol'


class VacancyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vacancy

    slug = 'test1'
    text = 'text test1'
    user = factory.SubFactory(UserFactory)
