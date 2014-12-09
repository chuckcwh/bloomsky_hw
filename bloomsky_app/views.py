import json
from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from bloomsky_app.models import Q1_weatherInfo, Q2_timestamp, Q3_table1, Q3_table2


def index(request):
    return render(request, 'index.html')

# Question 1
@csrf_exempt
def post_weather_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        weather_data = Q1_weatherInfo.objects.get_or_create(
            # HeadInfo
            deviceId = data['headInfo']['DeviceId'],
            sc = data['headInfo']['Sc'],
            sv = data['headInfo']['Sv'],
            firmwareVer = data['headInfo']['FirmwareVer'],
            hardwareVer = data['headInfo']['HardwareVer'],
            productType = data['headInfo']['ProductType'],
            productModel = data['headInfo']['ProductModel'],
            queueNum = data['headInfo']['QueueNum'],
            tS = data['headInfo']['TS'],

            #BodyInfo
            enR = data['bodyInfo']['EnR'],
            isOffline = data['bodyInfo']['IsOffline'],
            isAtNight = data['bodyInfo']['IsAtNight'],

            #BodyInfo - APData
            lowVoltage = data['bodyInfo']['APData'][0]['LowVoltage'],
            voltage = data['bodyInfo']['APData'][0]['Voltage'],
            temperature = data['bodyInfo']['APData'][0]['Temperature'],
            humidity = data['bodyInfo']['APData'][0]['Humidity'],
            uv = data['bodyInfo']['APData'][0]['UV'],
            aPData_ts = data['bodyInfo']['APData'][0]['Ts'],
            searialnum = data['bodyInfo']['APData'][0]['Searialnum'],
            photosensitive = data['bodyInfo']['APData'][0]['Photosensitive'],
            outAtmosphericPressure = data['bodyInfo']['APData'][0]['OutAtmosphericPressure'],
            rainfall = data['bodyInfo']['APData'][0]['Rainfall'],
            voltageStatus = data['bodyInfo']['APData'][0]['VoltageStatus'],
            poweradapterStatus = data['bodyInfo']['APData'][0]['PoweradapterStatus'],
            oVErr = data['bodyInfo']['APData'][0]['OVErr'],
            cCErr = data['bodyInfo']['APData'][0]['CCErr'],

            #BodyInfo - DeviceData
            powerOnTime = data['bodyInfo']['DeviceData'][0]['PowerOnTime'],
            wlanTime = data['bodyInfo']['DeviceData'][0]['WlanTime'],
            dHCPTime = data['bodyInfo']['DeviceData'][0]['DHCPTime'],
            uploadTime = data['bodyInfo']['DeviceData'][0]['UploadTime'],
            device_ts = data['bodyInfo']['DeviceData'][0]['Ts'],
            isCharging = data['bodyInfo']['DeviceData'][0]['IsCharging'],
            isEffective = data['bodyInfo']['DeviceData'][0]['isEffective'],

            #picture
            picture = data['picture']
        )
        status = "successfully save or find"
    else:
        status = "action error"
    response = status
    return HttpResponse(json.dumps(response),
                        content_type='application/json')

@csrf_exempt
def get_weather_data(request):
    weather_objects = Q1_weatherInfo.objects.all()
    collection = []
    for item in weather_objects:
        collection.append(model_to_dict(item))
    return HttpResponse(json.dumps(collection),
                        content_type='application/json'
    )


# Question 2
@csrf_exempt
def post_timestamp(request):
    timestamp_object = Q2_timestamp.objects.get_or_create(
        tS = 1404721291
    )
    if request.method == 'POST':
        data = json.loads(request.body)
        diff = int(data) - int(timestamp_object[0].tS)
        if -10 <= diff <= 10:
            status = "Timestamp varified ok"
        else:
            status = "Server Timestamp: " + str(timestamp_object[0].tS)
    else:
        status = "action error"
    response = status
    return HttpResponse(json.dumps(response),
                        content_type='application/json'
    )


# Question 3
@csrf_exempt
def post_time_compare(request):
    table1_collection = []
    table2_collection = []
    if request.method == 'POST':
        data = json.loads(request.body)
        for x in data['table1_data']:
            table1_object = Q3_table1.objects.get_or_create(
                tS = x
            )
            table1_collection.append({
                'id': table1_object[0].pk,
                'tS': str(table1_object[0].tS)[:21],
            })
        for y in data['table2_data']:
            table2_object = Q3_table2.objects.get_or_create(
                tS = y
            )
            table2_collection.append({
                'id': table2_object[0].pk,
                'tS': str(table2_object[0].tS)[:21],
            })
    collection = [table1_collection, table2_collection]
    return HttpResponse(json.dumps(collection),
                        content_type='application/json'
    )


def get_closest_table1_obj(dt):
    closest_greater_qs = Q3_table1.objects.filter(tS__gt=dt).order_by('tS')
    closest_less_qs = Q3_table1.objects.filter(tS__lt=dt).order_by('-tS')
    try:
        closest_greater = closest_greater_qs[0]
    except IndexError:
        return closest_less_qs[0]
    try:
        closest_less = closest_less_qs[0]
    except IndexError:
        return closest_greater_qs[0]
    if (closest_greater.tS - dt) > (dt - closest_less.tS):
        return closest_less
    else:
        return closest_greater


@csrf_exempt
def get_acquire_id(request):
    collection = []
    if request.method == 'GET':
        table2_objects = Q3_table2.objects.all()
        for table2_object in table2_objects:
            dt=table2_object.tS
            id_object = get_closest_table1_obj(dt)
            table2_object.closest_table1_Id = id_object.pk
            table2_object.save()
            collection.append({
                'id': table2_object.pk,
                'tS': str(table2_object.tS)[:21],
                'closest_table1_Id': table2_object.closest_table1_Id
            })
    return HttpResponse(json.dumps(collection),
                        content_type='application/json'
    )