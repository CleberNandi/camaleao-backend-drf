import uuid
from django.db import models
from chameleon_user.admin import ChameleonUser


class Person(models.Model):
    my_uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, verbose_name="Nome")
    last_name = models.CharField(max_length=200, verbose_name="Sobrenome")

    pk_user = models.ForeignKey(
        ChameleonUser, verbose_name="Usuário", on_delete=models.PROTECT)

    class Meta:
        db_table = "person"
        verbose_name_plural = "persons"
        ordering = ["first_name"]

    def __str__(self):
        return self.name


class Address(models.Model):
    my_uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    street = models.CharField(max_length=200, verbose_name="Endereço")

    class Meta:
        db_table = "address"
        verbose_name_plural = "addresses"
        ordering = ["street"]

    def __str__(self):
        return self.street


class PersonAddress(models.Model):
    my_uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    person_id = models.ManyToManyField(Person)
    address_id = models.ManyToManyField(Address)
    pk_user = models.ForeignKey(
        ChameleonUser, verbose_name="Usuário", on_delete=models.PROTECT)

    class Meta:
        db_table = "personaddress"
        verbose_name_plural = "personsaddresses"

    def __str__(self):
        return self.person
