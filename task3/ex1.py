# 1.	Вывести информацию в консоль о логических дисках, именах, метке тома, 
# размере и типе файловой системы (модуль psutil).
import psutil

disks = psutil.disk_partitions()

# информация о каждом диске
for sdiskpart in disks:
    print(sdiskpart)
    break

