# vulnerable-ping-server
This is a repo contains an en example of a simple vulnerabile ping server.Take this repo as the "Hello World" of cybersec world.
Try to leak the content of the `secret` file by exploiting the web server !

### Installation
In order to run the server just run the following lines:
```
git clone https://github.com/di3go-sona/vulnerable-ping-server.git
cd vulnerable-ping-server
pip3 install flask 
flask run
```

### Solution and explaination
Basically there are several different ways of exploiting this server, one of the most straightforward is: `127.0.0.1 && cat secret`, in fact we'll use sh shell expansion in order to execute arbitrary code
