###                     ب                      ###
## File upload extension brute force tool by f4T1H.
## See https://github.com/f4T1H21/FextBrute
## Constructive feedback is appreciated.
#!/usr/bin/python3
import sys
import os
import requests

eleman = len(sys.argv)
version = "v1.0"
opening = f"""   ____        __  ___           __
  / __/____ __/ /_/ _ )______ __/ /____
 / _// -_) \ / __/ _  / __/ // / __/ -_)
/_/  \__/_\_\\\__/____/_/  \_,_/\__/\__/ {version}
Brute 'Em All!
"""
help = f"""FextBrute {version} <Written by f4T1H>
# See https://github.com/f4T1H21/FextBrute
A brute force tool to find out what types of files
with different extensions are allowed to be uploaded to a web server.

Usage: python3 fextbrute.py <URL> <wordlist> [OPTIONS]
FLAGS:
    -h, --help    Print this help menu and exit.
    -v, --version Print version information and exit.
OPTIONS:
    -d, --dot     Add "." before each extension in wordlist. (Use if there aren't)
ARGUMENTS:
    <URL>      Web page to upload files
    <wordlist> File extenions wordlist
EXAMPLES:
    python3 fextbrute.py http://127.0.0.1:88/wiki/upload.php wordlist.txt
    python3 fextbrute.py http://example.com/fileupload.php wordlist.txt -d"""
UnknownErr = "Unknown option, use -h flag for help menu."

if eleman == 1: # Check for arguments comes after "python3".
    print(f"""FextBrute {version} <Written by f4T1H>
Usage: python3 fextbrute.py <URL> <wordlist> [OPTIONS]
Try 'python3 fextbrute.py -h' for more information.""")
    sys.exit()
elif eleman == 2:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print(help)
        sys.exit()
    elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
        print(f"FextBrute {version} <Written by f4T1H>")
        sys.exit()
    elif sys.argv[1].startswith('http'):
        print("Missing argument <wordlist>, use -h for help menu.")
        sys.exit(1)
    else:
        print(UnknownErr)
        sys.exit(1)
elif (eleman == 3 or eleman == 4) & sys.argv[1].startswith('http'):
    print(opening)
    url = sys.argv[1]
    wordlist = sys.argv[2]
    with open(wordlist, 'r') as f:
        extensions = f.read().strip().split('\n')   # Make a list that contains all extensions in wordlist.
        if "/" in extensions:
            ovyea = extensions.index("/")   # Remove "/" in list if any. (As "/" makes file into a folder.)
            extensions.pop(ovyea)
    if eleman == 4:
        if sys.argv[3] == "-d" or sys.argv[3] == "--dot":
            for extension in extensions:    # Add dot "." before each extension if parameter specified.
                extensions.remove(extension)
                appended = "." + extension
                extensions.insert(0, appended)
            extensions.reverse()
        else:
            print(UnknownErr)
            sys.exit(1)
    errmsg = input("[+] Please insert the exact error message which server returns: ")  # As the loop checks error msg in r.text.
    print("===========================STARTING===========================")
    name = "filetobeuploaded"   # Name of the files which will be uploaded.
    file = name + ".somextension"
    os.system(f"touch {file}")  # Create a file.
else:
    print(UnknownErr)
    sys.exit(1)

for extension in extensions:
    file_new = name + extension
    os.rename(file, file_new)   # Rename the file with the next extension in list.
    files = {"file": open(file_new, "rb")}
    r = requests.post(url, files=files) # Make a POST request to upload the file.
    if errmsg in r.text:    # Check if the given error message exists.
        print(f"[-] {extension} is not allowed.")
    else:
        print(f"[***] {extension} IS ALLOWED!!!")
    file = file_new
os.system(f"rm {file}") # Delete the previously created upload file.
print("=============================DONE=============================")
