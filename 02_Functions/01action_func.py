# Store a log message in a file

def  write_log(message):
    with open(r"C:\Python\Python_Learning\02_Functions\log.txt", "a") as file:
        file.write(message + "\n")

print (write_log("This is a log message."))
print (write_log("App started successfully."))