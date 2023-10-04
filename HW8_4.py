# Написати валідації за допомогою регулярних виразів:
# - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
import re
pattern_for_the_full_name = r'\w{3,25}[-\s\']\w{3,25}[-\s\']\w{3,25}'
full_name_provide_now = "Снитко Катерина Андреевна"
if re.match(pattern_for_the_full_name, full_name_provide_now):
    print("True.")
else:
    print("False")