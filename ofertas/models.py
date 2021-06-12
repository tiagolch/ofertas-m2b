from django.db import models


class States(models.Model):
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.uf

    class Meta:
        verbose_name_plural = "States"


class Cities(models.Model):
    cities = models.CharField(max_length=100)

    def __str__(self):
        return self.cities

    class Meta:
        verbose_name_plural = "Cities"


class Apps(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Apps"


class Svas(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Svas"


class Ofertas(models.Model):
    promocao = models.CharField(max_length=200, unique=True)
    state = models.ManyToManyField(States, blank=True, null=True)
    cities = models.ManyToManyField(Cities, blank=True, null=True)
    is_special = models.BooleanField(default=False)
    special_text = models.CharField(max_length=200, default=None, blank=True, null=True)
    speed = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=200, blank=True, null=True)
    apps = models.ManyToManyField(Apps, blank=True)
    svas = models.ManyToManyField(Svas, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=8, decimal_places=2)
    tax = models.DecimalField(max_digits=8, decimal_places=2)
    installments = models.PositiveIntegerField(default=0)
    discount_description = models.CharField(max_length=200)
    payment_code = models.CharField(max_length=3)

    def __str__(self):
        return self.promocao

    class Meta:
        verbose_name_plural = "Ofertas"