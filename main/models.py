from django.db import models

# Create your models here.


class Agt(models.Model):
    name = models.TextField()
    college = models.TextField()
    email = models.TextField()
    contactno = models.TextField()
    perform = models.TextField()

class Antra(models.Model):
    name = models.TextField(max_length=200)
    college = models.TextField(max_length=500)
    email = models.TextField()
    contactno = models.TextField(max_length=11)


class BigRoar(models.Model):
    name = models.TextField(max_length=200)
    college = models.TextField(max_length=500)
    email = models.TextField()
    contactno = models.TextField(max_length=11)


class Craftix(models.Model):
    name = models.TextField(max_length=200)
    college = models.TextField(max_length=500)
    email = models.TextField()
    contactno = models.TextField(max_length=11)


class kavyanjali(models.Model):
    name = models.TextField(max_length=200)
    college = models.TextField(max_length=500)
    email = models.TextField()
    contactno = models.TextField(max_length=11)


class TalkMasters(models.Model):
    name = models.TextField(max_length=200)
    college = models.TextField(max_length=500)
    email = models.TextField()
    contactno = models.TextField(max_length=11)
    topic = models.TextField(max_length= 600)


class ToTheBeat(models.Model):
    name = models.TextField(max_length=200)
    college = models.TextField(max_length=500)
    email = models.TextField()
    contactno = models.TextField(max_length=11)


class ToTheBeatGroup(models.Model):
    leader_name = models.TextField()
    college = models.TextField()
    email = models.TextField()
    leader_contactno = models.TextField()
    number_of_part = models.IntegerField()


class Vyaktitva(models.Model):
    name = models.TextField(max_length=200)
    college = models.TextField(max_length=500)
    email = models.TextField()
    contactno = models.TextField(max_length=11)
