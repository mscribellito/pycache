from django.db import models

class Type(models.Model):

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"

    id = models.BigAutoField(primary_key=True)
    
    type = models.CharField(blank=True, max_length=200)
    
    def __str__(self):
        return self.type

class CaliberGauge(models.Model):

    class Meta:
        verbose_name = "Caliber/Gauge"
        verbose_name_plural = "Calibers/Gauges"

    id = models.BigAutoField(primary_key=True)
    
    caliber_gauge = models.CharField(blank=True, max_length=200)
    
    def __str__(self):
        return self.caliber_gauge

class Firearm(models.Model):

    class Meta:
        verbose_name = "Firearm"
        verbose_name_plural = "Firearms"

    id = models.BigAutoField(primary_key=True)
    
    manufacturer_importer = models.CharField("Manufacturer/Importer", blank=True, max_length=200)
    model = models.CharField(blank=True, max_length=200)
    serial_number = models.CharField("Serial Number", blank=True, max_length=200)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    caliber_gauge = models.ForeignKey(CaliberGauge, verbose_name="Caliber/Gauge", on_delete=models.CASCADE)
    date_acquired = models.DateField("Date Acquired", blank=True)
    cost = models.CharField(blank=True, max_length=200)
    purchase_location = models.CharField("Purchase Location", blank=True, max_length=200)
    sold_transferred_to = models.CharField("Sold/Transferred to", blank=True, max_length=200)

    def __str__(self):
        return "{} {}".format(
            self.manufacturer_importer,
            self.model
        )