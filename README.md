# Insta - Private Instagram API for Python and .NET

Insta is a small wrapper built for giving private API access to python/.NET users.
Implementations may include:
  - Login Validation
  - Upload pictures from cloud scripts
  - Many, many more

### Version
0.1.3 - BETA!

###Changes in 0.1.3
  	- Added certificate bypass for some experiencing cert issues with IG
	- Introducing Insta.cs, a .NET couterpart for use in .NET applications. Works flawlessly.

####Changes in 0.1.2
	- Added GET functionality
	- PEP8 compliant and docstrings
	- Small optimization fixes

### Usage
A simple usage example was provided within the pacakge. Simply import Insta from the Insta package, instantiate an instance of the Insta class with your username and password (or Facebook email and password), and then call the login function. It will return either -1 (fail) or 0 (success). This should not be used in commercial products, it does use
the Instagram private API and therefore may or may not cease to work at some point.
*Note: The point of this is to be as minimal as possible. I will more than likely not support functions like uploading images, searching, etc... as it just adds clutter
to the module which is meant to be as a minimalist solution for developers to use.

### Tech

Insta uses a number of open source projects to work properly:

*Python [requests] - HTTP Requests for humans!
*.NET [RestSharp] - HTTP Library for .NET
### Installation Python

You need to install the requests library

```sh
pip install requests
```

### Installation .NET

You need to install the RestSharp library with NuGet

```sh
Install-Package RestSharp
```

### Todos

 - Ensure module is working without bugs


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
