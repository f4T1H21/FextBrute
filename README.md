# FextBrute
*File extension Brute*

***A brute force tool to find out what types of files with different extensions are allowed to be uploaded to a web server.***

### Getting Started
```bash
git clone https://github.com/f4T1H21/FextBrute.git
cd FextBrute
chmod +x fextbrute.py
python3 ./fextbrute.py
```
### Usage
```
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
    python3 fextbrute.py http://example.com/fileupload.php wordlist.txt -d
```
### Example ss
Didn't need to use ```-d``` or ```--dot```  flag, because we had already had our dots before each word in wordlist.
![ss1](https://github.com/f4T1H21/FextBrute/blob/main/ss1.png)

But in this example, we needed to specify ```-d``` or ```--dot``` option in order to make script put a dot before each word in wordlist.
![ss2](https://github.com/f4T1H21/FextBrute/blob/main/ss2.png)

Constructive feedback is appreciated, thanks!

*Written by f4T1H*
