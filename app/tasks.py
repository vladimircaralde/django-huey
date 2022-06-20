from huey.contrib.djhuey import task, db_task
from app.models import Car


@task()
def django_huey_task():
    output = 'Huey Task'
    print(output)
    return {"message": output}


@db_task()
def django_huey_db_task_create(name, color, fuel_type):
    resp = Car.objects.create(
        name=name,
        color=color,
        fuel_type=fuel_type
    )
    print(resp.name)
    return {"message": resp.name}


@db_task()
def django_huey_db_task_cars():
    resp = Car.objects.all()
    print(resp)
    return {"message": resp}


@db_task()
def django_huey_db_task_delete(car_id):
    Car.objects.get(pk=car_id).delete()
    print('deleted')
    return {"message": "success"}