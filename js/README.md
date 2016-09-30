python -m SimpleHTTPServer
The http server will start  

http://192.168.1.2:8000
http://127.0.0.1:8000

If the directory has a file named index.html, that file will be served as the initial file. If there is no index.html, then the files in the directory will be listed.

If you wish to change the port that's used start the program via:

 python -m SimpleHTTPServer 8080