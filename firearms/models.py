from django.db import models

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

    FIREARM_TYPES = {
        "pistol": "Pistol",
        "revolver": "Revolver",
        "rifle": "Rifle",
        "shotgun": "Shotgun",
        "frame": "Frame",
        "receiver": "Receiver",
        "other": "Other"
    }

    id = models.BigAutoField(primary_key=True)
    
    manufacturer_importer = models.CharField(blank=True, max_length=200)
    model = models.CharField(blank=True, max_length=200)
    serial_number = models.CharField(blank=True, max_length=200)
    type = models.CharField(blank=True, choices=FIREARM_TYPES, max_length=200)
    caliber_gauge = models.ForeignKey(CaliberGauge, on_delete=models.CASCADE)
    date_acquired = models.DateField(blank=True)
    cost = models.CharField(blank=True, max_length=200)
    purchase_location = models.CharField(blank=True, max_length=200)
    sold_transferred_to = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return "{} {}".format(
            self.manufacturer_importer,
            self.model
        )