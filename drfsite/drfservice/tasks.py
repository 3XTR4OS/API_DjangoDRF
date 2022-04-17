from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

# @shared_task
# def count_Messages():
#     return Message.objects.count()
#
#
# @shared_task
# def rename_Message(Message_id, name):
#     w = Message.objects.get(id=Message_id)
#     w.name = name
#     w.save()
