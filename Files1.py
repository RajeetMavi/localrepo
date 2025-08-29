"""
FILES :-
-> files are used to store data persistently on a storage medium, such as a hard drive. 
-> Python provides built-in functionality to handle files for reading, writing, and appending content.
----------Types of files-----------
1) Text Files: Contain human-readable data, such as .txt, .csv, or .html files.
2) Binary Files: Contain non-readable data in binary format, such as .jpg, .png, or .exe files.

----------File opening modes---------
'r' - Opens the file in read mode. The file must exist; otherwise, it raises a FileNotFoundError.
'w'	- Opens the file in write mode. Overwrites the file if it exists, or creates a new file.
'x'	- Opens the file in exclusive creation mode. Fails if the file already exists.
'a'	- Opens the file in append mode. Adds data at the end without erasing existing content.
'b'	- Opens the file in binary mode (used with other modes like 'rb', 'wb').
't'	- Opens the file in text mode (default).
'+'	- Opens the file for both reading and writing. Used with other modes like 'r+', 'w+'mbo

---------Common Mode Combinations-------------
'rt' (default): Read a text file.
'rb': Read a binary file.
'wt': Write to a text file (overwrites the file).
'wb': Write to a binary file.
'r+': Read and write to a file.
'a+': Append to a file and read it.
'x+': Exclusive creation, read and write.

The argument mode points to a string beginning with one of the following
 sequences (Additional characters may follow these sequences.):

 "r"    Open text file for reading.  The stream is positioned at the
         beginning of the file.

 "r+"   Open for reading and writing.  The stream is positioned at the
         beginning of the file.

 "w"    Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.

 "w+"   Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.

 "a"    Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

 "a+"   Open for reading and writing.  The file is created if it does not
        exist.  The stream is positioned at the end of the file.  Subse-
        quent writes to the file will always end up at the then current
        end of file, irrespective of any intervening fseek(3) or similar.
"""

#usinf write (w) mode
"""
f = open("demo.txt",'w')
# f.read() --> cannot be read as it is opened in only write mode
data = input("Enter what you want to write: ")
f.write(data)
f.close()
"""

#using read mode (r)
"""
with open("demo.txt",'r') as f:
    # data = f.read()
    if(f.readable() == True):
        data = f.readline()
    print(data)
    f.close()
"""

#using append mode (a)
with open("demo.txt",'a') as f:
    f.writelines("Hello dude!")

#Deleting a file
# import os
# os.remove("practice.txt")