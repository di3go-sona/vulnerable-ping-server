# vulnerable-ping-server
This is a repo containing a very simple vulnerabile server, (basically the "Hello World" of cybersec), try to make the content of `secret` appear into the browser !

### Installation
In order to run the server just run the following lines:
```
git clone https://github.com/di3go-sona/vulnerable-ping-server.git
cd vulnerable-ping-server
pip3 install flask 
flask run
```

### Solution and explaination
Basically there are several different ways of exploiting this server, one of the most straightforward is: `localhost && $(cat secret)`, in fact we'll use sh shell expansion in order to execute arbitrary code
