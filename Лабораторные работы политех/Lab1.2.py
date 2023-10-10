# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44
number_of_pages = 100
number_of_rows = 50
number_of_characters = 25
one_character = 4
disk_size *= (1024*1024)
one_book = number_of_pages * number_of_rows * number_of_characters * one_character
print("Количество книг, помещающихся на дискету:", int(disk_size // one_book))
