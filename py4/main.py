# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pprint import pprint
from random import randint
import pymongo


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def search_movie(movie_name, db):
    paramount_movie_info = {'paramount_movie_info': '/'+movie_name+'/'}
    result = db.reviews.find(paramount_movie_info)
    if result != '':
        for x in result:
            print("Found it: "+x['paramount_movie_info'])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mongodb_url = input("粘贴云数据库的地址")
    client = pymongo.MongoClient(mongodb_url)
    db = client.paramount
    serverStatusResult = db.command("serverStatus")
    # pprint(serverStatusResult)
    filelocation = input("粘贴文件路径")
    paramount_movie = open(filelocation, "r", encoding='utf8')

    movie_input = input("input movie name : ")
    search_movie(movie_input, db)

    # List all from txt file
    # txt_line_count = len(paramount_movie.readlines())
    # paramount_movie.seek(0)
    # for x in paramount_movie.readlines():
    #     if x != '\n':
    #         if x[len(x)-1:] == "\n":
    #             pprint(x[:len(x) - 1])
    #         else:
    #             pprint(x)
    # pprint('txt_line_count : '+str(txt_line_count))

    # Find all movies from database
    # for x in paramount_movie.readlines():
    #         if x != "\n":
    #             if x != '\n':
    #                 if x[len(x)-1:] == "\n":
    #                     paramount_movie_info = {'paramount_movie_info': x[:len(x) - 1]}
    #                     result = db.reviews.find_one(paramount_movie_info)
    #                     pprint(result['paramount_movie_info'])
    #                 else:
    #                     paramount_movie_info = {'paramount_movie_info': x}
    #                     result = db.reviews.find_one(paramount_movie_info)
    #                     pprint(result['paramount_movie_info'])

    # Counting elements in one collection['reviews']
    # countnum = db.reviews.find().count()

    # Delete for each
    # for x in paramount_movie.readlines():
    #     if x != "\n":
    #         paramount_movie_info = {'paramount_movie_info': x[:len(x) - 1]}
    #         result = db.reviews.delete_one(paramount_movie_info)
    #         pprint("delete:"+str(result))

    # Merge txt content to cloud database
    # paramount_movie_info = {}
    # for x in paramount_movie.readlines():
    #     if x != '\n':
    #         if x[len(x) - 1:] == "\n":
    #             paramount_movie_info = {'paramount_movie_info': x[:len(x) - 1]}
    #         else:
    #             paramount_movie_info = {'paramount_movie_info': x[:len(x)]}
    #     result = db.reviews.find(paramount_movie_info).count()
    #     if result == 0:
    #         inserted_result = db.reviews.insert_one(paramount_movie_info)
    #         pprint('insert {0} and its _id {1}'.format(paramount_movie_info, inserted_result.inserted_id))
    #     elif result > 1:
    #         while result > 1:
    #             delete_result = db.reviews.delete_one(paramount_movie_info)
    #             pprint('delete {0} and its _id {1}'.format(paramount_movie_info, delete_result.deleted_id))
    #     else:
    #         pprint(x[:len(x) - 1] + "————already insist")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
