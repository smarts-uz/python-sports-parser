import os

file_path = "C:\\Users\\user\\Desktop\\p\\python-sports-parser\\orm\\db\\models.py"

# Faylni o'qish
with open(file_path, "r") as file:
    lines = file.readlines()

# Qatorlarni tahrirlash
with open(file_path, "w") as file:
    for line in lines:
        if (
            "id = models.AutoField()" in line
            or "id = models.BigAutoField(db_comment='1|41')" in line
            or "id = models.AutoField(db_comment='ID')" in line
        ):
            file.write("# " + line)  # Izohga olish
        else:
            file.write(line)
