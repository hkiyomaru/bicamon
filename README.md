#BiCAmon

![screenshot](https://raw.github.com/wiki/kiyomaro927/MouseBrainVisualizationOnWeb/images/screen_shot.png)

##What is BiCAmon

BiCAmon is an abbreviation for "Biology inspired cognitive architecture monitor".

This provides visually understanding of a brain-inspired cognitive architecture.

##Getting Started

I wrote server-side scripts in Python2.7.6.

So if you have Python3, you should switch the Python-version.

Then, clone this repository.

```
$ git clone https://github.com/kiyomaro927/bicamon.git
```

You have to install some packages to run this program.

They are written in _requirements.txt_.

```cd inside```, and run the next command.

```
$ pip install -r requirements.txt
```

##Run

Then, run the program.

```
$ python server.py
```

Open your browser, and access _localhost:5000_.

If you cannot show the page well,

maybe your browser doesn't support WebGL.

For more information, please access [this page](http://caniuse.com/#search=webgl)(caniuse.com).

##Test

I know the cells you're watching are not firing.

I prepared some test programs in the test directory.

Open new terminal and run the test code to fire cells.

```
$ python post_test.py
```

##Combine

Let's combine your brain-inspired cognitive architecture.

The program to call API is in the test direcory.

Then, open _api.py_.

The function named 'send_to_viewer' can send POST request to BiCAmon.

Please put this function in the directory in the path.

And, insert the function call in your program.

##LICENSE

* Files other than third party's.
 - Revised BSD License

* Third party's files.
 - Follow the license written in the files.
