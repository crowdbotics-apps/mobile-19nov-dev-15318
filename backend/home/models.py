from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(
        max_length=150,
    )
    fdfgdrg = models.BigIntegerField(
        null=True,
        blank=True,
    )
    wqe = models.BigIntegerField(
        null=True,
        blank=True,
    )
    qw = models.BigIntegerField(
        null=True,
        blank=True,
    )
    ytu = models.BigIntegerField(
        null=True,
        blank=True,
    )
    oio = models.BigIntegerField(
        null=True,
        blank=True,
    )
    oiou = models.BigIntegerField(
        null=True,
        blank=True,
    )
    wqere = models.BigIntegerField(
        null=True,
        blank=True,
    )
    yjuy = models.BigIntegerField(
        null=True,
        blank=True,
    )
    opipuoii = models.BigIntegerField(
        null=True,
        blank=True,
    )
    iuuioyuy = models.BigIntegerField(
        null=True,
        blank=True,
    )
    yuogfgs = models.BigIntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
