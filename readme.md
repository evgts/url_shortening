### Summary
Web Service to convert a URL to a short URL and from short URL get the original URL

### Requirements
Python 3.7

Dependencies: flask, flask_sqlalchemy, requests

### Set Up
Install the requirements:
```buildoutcfg
cd url_shortening
pip install --upgrade -r .\requirements.txt
```

Install the package:
```buildoutcfg
python setup.py install
```

or use develop if you planning to modify the package:
```buildoutcfg
python setup.py develop
```

Create the DB:
```buildoutcfg
python db\url_model.py
```

Start the server:
```buildoutcfg
python main/app.py
```

Run the tests:
```buildoutcfg
python tests/test_url_shortening.py
```

### Basic use:
The service supports POST and GET requests.
To convert a URL to a short URL use POST:
```buildoutcfg
    <hostname>/shorten
    :payload: {"url": "https://www.google.com/blah"}
    :return: {"url": "https://www.google.com/blah", "short_url": "http://127.0.0.1:5000/shorturl/wIJOrQ99KWNC7aA7QhGH"}
```
To convert short URL to the original URL use GET:
```buildoutcfg
    <hostname>/shorturl/<url_code>
    :request: http://127.0.0.1:5000/shorturl/wIJOrQ99KWNC7aA7QhGH
    :return: {"url": "https://www.google.com/blah", "short_url": "http://127.0.0.1:5000/shorturl/wIJOrQ99KWNC7aA7QhGH"}
```

### Test results:
```buildoutcfg
DEBUG:urllib3.connectionpool:Starting new HTTP connection (1): 127.0.0.1:5000
DEBUG:urllib3.connectionpool:http://127.0.0.1:5000 "POST /shorten HTTP/1.1" 200 286
DEBUG:root:200
DEBUG:root:{
  "short_url": "http://127.0.0.1:5000/shorturl/Lq1UQ2hngRdV9mo1sLkd",
  "url": "https://www.google.com/maps/place/2360+3rd+St,+San+Francisco,+CA+94107/@37.7597267,-122.3909953,17z/data=!3m1!4b1!4m5!3m4!1s0x808f7fb9c99118a7:0xa0ef6a150b3dc463!8m2!3d37.7597267!4d-122.3888066?hl=en"
}

DEBUG:urllib3.connectionpool:Starting new HTTP connection (1): 127.0.0.1:5000
DEBUG:urllib3.connectionpool:http://127.0.0.1:5000 "GET /shorturl/Lq1UQ2hngRdV9mo1sLkd HTTP/1.1" 200 286
DEBUG:root:200
DEBUG:root:{
  "short_url": "http://127.0.0.1:5000/shorturl/Lq1UQ2hngRdV9mo1sLkd",
  "url": "https://www.google.com/maps/place/2360+3rd+St,+San+Francisco,+CA+94107/@37.7597267,-122.3909953,17z/data=!3m1!4b1!4m5!3m4!1s0x808f7fb9c99118a7:0xa0ef6a150b3dc463!8m2!3d37.7597267!4d-122.3888066?hl=en"
}

.
----------------------------------------------------------------------
Ran 1 test in 0.134s

OK
```


### Assigment (took about 3 hours):
```
URL shortening


Write a web service in Python that:
1) Accepts a URL and returns a shortened version.
2) Takes a shortened url and returns the original longer URL
```
