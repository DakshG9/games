
try:
    file_name = text.txt
except NameError:
    msg = "Make sure sure you typed 'text.txt' like this!"
 
    print(msg)

try:
    with open(file_name, encoding='utf-8') as f_oj:
        contents = f_obj.read()

except FileNotFoundError:
    msg = "We can't find " + file_name
    print(msg)
