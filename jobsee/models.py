from django.db import models


class BaseLocation(models.Model):
    name = models.CharField(max_length=100)


class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    base_location = models.ForeignKey(
        BaseLocation,
        on_delete=models.PROTECT,
        related_name='companies'
    )
    technologies = models.CharField(max_length=100)  # later PK
    www = models.CharField(max_length=50)
    # TODO: rating


class JobAdvert(models.Model):
    WORK_FROM_CHOICES = (
        ('1', 'On site'),
        ('2', 'Hybrid'),
        ('3', 'Remote')
    )
    SENIORITY_LEVEL_CHOICES = (
        ('1', 'Entry Level'),
        ('2', 'Junior'),
        ('3', 'Medior'),
        ('4', 'Senior')
    )

    title = models.CharField(max_length=100)
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name='job_adverts'
    )
    seniority_level = models.CharField(
        choices=SENIORITY_LEVEL_CHOICES,
        max_length=1
    )
    tech_requested = models.CharField(max_length=100)
    tech_nice_to_have = models.CharField(max_length=100, null=True, blank=True)
    work_from = models.CharField(
        choices=WORK_FROM_CHOICES,
        max_length=1
    )
    discover_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


class Communication(models.Model):
    AUTHOR_CHOICES = (
        ('1', 'User'),
        ('2', 'Company')
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name='actions'
    )
    author = models.CharField(
        choices=AUTHOR_CHOICES,
        max_length=1
    )
    date = models.DateTimeField()


class Note(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name='notes'
    )
    advert = models.ForeignKey(
        JobAdvert,
        on_delete=models.PROTECT,
        related_name='notes',
        null=True
    )
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
