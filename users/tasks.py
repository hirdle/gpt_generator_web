# from celery import shared_task

# import subprocess
# from multiprocessing import Process

# thread = None
# t = None

# @shared_task
# def create_schedule_task(instance):
#     try:
#         thread.kill()
#     except: pass
#     thread = subprocess.run(["python", "poster.py"])
    



# from multiprocessing import Process

# def write_post(i):
#     # while True:
#     themes_list = i.themes.split('\n')
#     post_theme = themes_list[0]
#     themes_list.pop(0)
#     print("\n".join(themes_list))
#     # i.themes = "\n".join(themes_list)
#     i.template = ""
#     i.save()
#     time.sleep(5)

# @shared_task
# def create_schedule_task(instance):
    
#     objects = Channel.objects.all()

#     for i in objects:

#         print(i)

#         t = Process(target=write_post, args=[i])
#         t.start()
#         # threads.append(t)
    
#     # for t in threads:
#     #     t.join()