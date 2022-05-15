"""
created by 贝壳 on 2022/5/14
"""
__autor__ = 'shelly'
import os


import factory
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","tutorial.settings")
django.setup()

from snippets.models import MyUser,Organization

class OrganizationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Organization
    name = factory.faker.Faker('name')
    type = factory.Sequence(lambda n:"type-{}".format(n))
    contact_email = factory.faker.Faker('email')

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MyUser

    username = factory.faker.Faker('first_name',locale="zh_CN")
    age = factory.Sequence(lambda  n:n%100)
    sex = factory.Sequence(lambda n:'Male' if n%2 == 0 else 'Female')
    org = factory.SubFactory(OrganizationFactory)

def test():
    for i in range(10000):
        UserFactory()

if __name__ == '__main__':
   # test()
    value = {'math':'90'}
    print(list(value.values())[0])



