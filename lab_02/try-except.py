# try:
#     print("Hello")
# except:
#     print("Something went wrong")
# else:
#     print("Nothing went wrong")


# try:
#     print(x)
# except:
#     print("An exception occurred")

# # try:
# #   print(x)
# # except NameError:
# #   print("Variable x is not defined")
# # except:
# #   print("Something else went wrong")

# # try:
# #   print(x)
# # except:
# #   print("Something went wrong")
# # finally:
# #   print("The 'try except' is finished")

try:
    f = open("Python_Basic\lab_02\demofile.txt","a")
    print("read file : demofile.txt done")
    try:
        f.write("Lorum Ipsum\n")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file2")
