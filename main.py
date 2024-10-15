import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json_data = json.dumps(serializer.data)
    return json_data.encode("utf-8")


def deserialize_car_object(json: bytes) -> Car:
    car_data_dict = json.loads(json.decode("utf-8"))
    serializer = CarSerializer(data=car_data_dict)
    if serializer.is_valid():
        car_data = serializer.validated_data
        car = Car(
            manufacturer=car_data["manufacturer"],
            model=car_data["model"],
            horse_powers=car_data["horse_powers"],
            is_broken=car_data["is_broken"],
            problem_description=car_data.get("problem_description", "")
        )
        return car
    else:
        raise ValueError(f"Invalid data: {serializer.errors}")
