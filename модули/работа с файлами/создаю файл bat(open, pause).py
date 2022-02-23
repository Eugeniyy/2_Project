# Создаю файл bat, который открывает файл и ждёт действие пользователя
# перед закрытием.

import os.path

if not os.path.exists(r"C:\Users\Евгений\Desktop\project\10\click_counter\click_counter.bat"):
    my_file = open(r"C:\Users\Евгений\Desktop\project\10\click_counter\click_counter.bat", "w")
    my_file.write("click_counter.py\npause")
    my_file.close()