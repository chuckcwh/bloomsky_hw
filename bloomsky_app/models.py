from django.db import models

# Create your models here.

class Q1_weatherInfo(models.Model):
    #HeadInfo
    deviceId = models.CharField(max_length=40)
    sc = models.CharField(max_length=100)
    sv = models.CharField(max_length=100)
    firmwareVer = models.CharField(max_length=100)
    hardwareVer = models.CharField(max_length=100)
    productType = models.CharField(max_length=20)
    productModel = models.CharField(max_length=20)
    queueNum = models.PositiveIntegerField()
    tS = models.PositiveIntegerField()

    #BodyInfo
    enR = models.CharField(max_length=40)
    isOffline = models.PositiveSmallIntegerField()
    isAtNight = models.SmallIntegerField()

    #BodyInfo - APData
    lowVoltage = models.PositiveSmallIntegerField()
    voltage = models.PositiveSmallIntegerField()
    temperature = models.PositiveIntegerField()
    humidity = models.PositiveSmallIntegerField()
    uv = models.PositiveSmallIntegerField()
    aPData_ts = models.PositiveIntegerField()
    searialnum = models.PositiveSmallIntegerField()
    photosensitive = models.PositiveSmallIntegerField()
    outAtmosphericPressure = models.PositiveIntegerField()
    rainfall = models.SmallIntegerField()
    voltageStatus = models.SmallIntegerField()
    poweradapterStatus = models.SmallIntegerField()
    oVErr = models.SmallIntegerField()
    cCErr = models.SmallIntegerField()

    #BodyInfo - DeviceData
    powerOnTime = models.PositiveIntegerField()
    wlanTime = models.PositiveIntegerField()
    dHCPTime = models.PositiveIntegerField()
    uploadTime = models.PositiveIntegerField()
    device_ts = models.PositiveIntegerField()
    isCharging = models.SmallIntegerField()
    isEffective = models.PositiveIntegerField()

    #Picture
    picture = models.TextField()

    def __unicode__(self):
        return u"{} {}".format(self.deviceId, self.tS)


class Q2_timestamp(models.Model):
    tS = models.PositiveIntegerField()

    def __unicode__(self):
        return u"{}".format(self.tS)

class Q3_table1(models.Model):
    tS = models.DateTimeField()

    def __unicode__(self):
        return u"{}".format(self.tS)

class Q3_table2(models.Model):
    tS = models.DateTimeField()
    closest_table1_Id = models.SmallIntegerField(blank=True, null=True)

    def __unicode__(self):
        return u"{}".format(self.tS)
