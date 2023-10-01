# from background_task import background

# @background(schedule=5)  
# def my_background_task():
#     print("Task çalıştı")


# myapp/tasks.py

from background_task import background


@background(schedule=600)  # Her 10 saniyede bir çalışacak
def my_background_task():
    print("Görevçalıştı")
    
