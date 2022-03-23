path_image = "C:\\Users\\Anton\\Desktop\\text\\img_enter_sandman.jpg"
path_to_img = "img\\pict.jpg"

'''
битовое чтение и запись
на вход функции передаем два модуля , битовый и то , что мы хотим сделать 

open(path, "b" + "r")

'''

my_bit_stream = open(path_image, "b" + "r")
my_pict = my_bit_stream.read()
my_bit_stream.close()

my_bit_stream = open(path_to_img, "b" + "w")
my_bit_stream.write(my_pict)
my_bit_stream.close()

print("type: ", type(my_pict))
print(my_pict)
