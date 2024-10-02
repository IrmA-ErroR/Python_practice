# 1.	Вывести информацию в консоль о логических дисках, именах, метке тома, 
# размере и типе файловой системы (модуль psutil).

import psutil


def disks_information():   
    disks = psutil.disk_partitions() 
    disk_info = {}

    for disk in disks:

        try:
            usage = psutil.disk_usage(disk.mountpoint)
            disk_info[disk.device] = {
                    'mountpoint': disk.mountpoint,
                    'total': usage.total / (1024 ** 3),  # Переводим в гигабайты
                    'fstype': disk.fstype
                }

        except PermissionError:
            disk_info[disk.device] = 'Permission denied'

    return disk_info


def main():
    disks_data = disks_information()

    for disk_name, info in disks_data.items():
        if isinstance(info, dict):
            print(f"Имя: {disk_name}")
            print(f"Метка тома: {info['mountpoint']}")
            print(f"Размер диска: {info['total']:.2f} GB")
            print(f"Тип файловой системы: {info['fstype']}")
        else:
            print(f"Имя: {disk_name}")
            print(info)  
        print("-" * 50)


if __name__ == "__main__":
    main()
