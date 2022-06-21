from app.tasks import django_huey_task, django_huey_db_task_create, \
    django_huey_db_task_cars, django_huey_db_task_delete

from ninja import NinjaAPI
from ninja import Schema


class CarInput(Schema):
    name: str
    color: str
    fuel_type: str


api = NinjaAPI()


@api.post("/huey_task")
def huey_task(request):
    django_huey_task.schedule(delay=3)
    return {"message": "success"}


@api.post("/huey_db_task_create")
def huey_db_task_create(request, payload: CarInput):
    # some_task.schedule((params), delay=123)
    django_huey_db_task_create.schedule(
        (payload.name, payload.color, payload.fuel_type),
        delay=5
    )
    return {"message": "successfully created a car"}


@api.get("/huey_db_task_cars")
def huey_db_task_cars(request):
    # no delay
    django_huey_db_task_cars()
    return {"message": "success"}


@api.delete("/huey_db_task_delete/{car_id}")
def huey_db_task_delete(request, car_id):
    # some_task.schedule((params), delay=123)
    django_huey_db_task_delete.schedule(car_id, delay=5)
    return {"message": "successfully deleted"}
