from PIL import Image

from fastapi import APIRouter, BackgroundTasks
from fastapi import File, UploadFile
from worker.celery_app import celery_app

router = APIRouter()


def celery_on_message(body):
    print(body)


def background_on_message(task):
    print(task.get(on_message=celery_on_message, propagate=False))


@router.post("/send_photo")
async def send_photo(
        background_task: BackgroundTasks,
        file: UploadFile = File(...)):
    img = Image.open(file.file)
    img.save("resources/{}".format(file.filename))
    task = celery_app.send_task(
        "worker.celery_worker.send_photo", args=[file.filename])
    print(task, file.filename)
    background_task.add_task(background_on_message, task)
    return {"message": "Send photo received"}


@router.post("/test_celery/{word}")
async def root(word: str, background_task: BackgroundTasks):
    task = celery_app.send_task(
        "worker.celery_worker.test_celery", args=[word])
    print(task)
    background_task.add_task(background_on_message, task)
    return {"message": "Word received"}
