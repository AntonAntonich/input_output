"""
path - относителный , абсолютный путь , экранирование
битовые данные
"""

'''
- r (Read). Файл открывается для чтения. Если файл не найден, то генерируется исключение FileNotFoundError
- w (Write). Файл открывается для записи. Если файл отсутствует, то он создается. 
    Если файл уже есть, то он создается заново, и соответственно старые данные в нем стираются.
- a (Append). Файл открывается для дозаписи.
    Если файл отсутствует, то он создается. Если подобный файл уже есть, то данные записываются в его конец.
- b (Binary). Используется для работы с бинарными файлами. Применяется вместе с другими режимами - w или r.
'''

path_text = "C:\\Users\\Anton\\Desktop\\text\\metallica_enter_sandman.txt"
path_image = "C:\\Users\\Anton\\Desktop\\text\\img_enter_sandman.jpg"
path_to_img = "img\\pict.jpg"
path_to_text = "song.txt"

verse_four = '''
[Verse 4]
Something's wrong, shut the light
Heavy thoughts tonight
And they aren't of Snow White
Dreams of war
Dreams of liars
Dreams of Dragons Fire
And of things that will bite, yeah !!!
'''

# my_input = open(path, "r") - по умолчанию
# my_input = open(path_text)
# song_text = my_input.read()
# my_input.close()
#
# my_input = open(path_image, "b")
# my_output = open(path_to_img, "b")
#
# my_output.write(my_input.read())

'''
read, write
'''

my_input = open(path_text)
song_text = my_input.read()
my_input.close()

my_output = open(path_to_text, "w")
my_output.write(song_text)
my_output.close()

'''
append -  добавляет в конец файла , если файл отсутствует , то зодается
'''

my_append = open(path_to_text, "a")
my_append.write(verse_four)

'''
FileNotFoundError - при отсутсвии файла 
try with resources
'''

wrong_path = "C:\\Users\\Anton\\Desktop\\text\\metallica_enter_sandman.tx"

# try:
#     my_input = open(wrong_path)
#     song_text = my_input.read(wrong_path)
# except ArithmeticError as e:
#     print(f"error path {wrong_path}")
# finally:
#     print("in finally: closing input stream")
#     my_input.close()
#
# print("Everything is ok")

# with open(wrong_path) as my_input:
#     try:
#         song_text = my_input.read()
#     except FileNotFoundError as e:
#         print(e)


'''
read - считывается все в одну строку
readline - считывает одну строку
readlines - считывает в массив из строк
'''
with open(path_text) as my_input:
    try:
        # song_text = my_input.read()
        # song_text = my_input.readline()
        # song_text_next = my_input.readline()
        song_all_strings = my_input.readlines()
        print(song_all_strings)
    except Exception as e:
        print(e)


