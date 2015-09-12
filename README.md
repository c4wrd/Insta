# Insta - Private Instagram API for Python

Insta is a small wrapper built for giving private API access to python users. 
Implementations may include:
  - Login Validation
  - Upload pictures from cloud scripts
  - Many, many more

### Version
0.1.1 - BETA!

### Usage
A simple usage example was provided within the pacakge. Simply import Insta from the Insta package, instantiate an instance of the Insta class with your username and password (or Facebook email and password), and then call the login function. It will return either -1 (fail) or 0 (success).

### Tech

Insta uses a number of open source projects to work properly:

* [requests] - HTTP Requests for humans!
### Installation

You need to install the requests library

```sh
pip install requests
```

### Todos

 - GET functionality
 - Concurrent requests

License
----

MIT

Copyright (c) 2015 Cory Forward

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.