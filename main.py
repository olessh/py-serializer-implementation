import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json_data = json.dumps(serializer.data, separators=(",", ":"))
    return json_data.encode("utf-8")


def deserialize_car_object(byte_data: bytes) -> Car:
    car_data_str = byte_data.decode("utf-8")
    car_data_dict = json.loads(car_data_str)
    car = Car(**car_data_dict)
    return car
