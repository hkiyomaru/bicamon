# BiCAmon

![screenshot](https://raw.github.com/wiki/kiyomaro927/MouseBrainVisualizationOnWeb/images/screen_shot.png)

## What is BiCAmon

BiCAmon is an abbreviation for "biologically-inspired cognitive architecture monitor".

This provides visually understanding of a brain-inspired cognitive architecture via web browsers.

## Development environment

* Python 2.7.6
* Google Chrome 58.0 (64-bit)

## Getting Started

First, clone this repository.

```
$ git clone https://github.com/kiyomaro927/bicamon.git
```

You have to install some packages to start BiCAmon.
They are written in `requirements.txt`.

`cd bicamon`, and run the following command.

```
$ pip install -r requirements.txt
```

## Run

Then, run the program below.

```
$ python server.py
```

Open your browser, and access `localhost:5000`.

If you can not show the page well, your browser may not support __WebGL__.
For more information, please check [caniuse.com](http://caniuse.com/#search=webgl).

## Test

I know the cells in your browser are not firing.

I prepared some test programs in the test directory.
Open new terminal and run the test script to fire cells.

```
$ python post_test.py
```

## Combine

Let's combine your brain-inspired cognitive architecture with BiCAmon.

The program to call API is in the test direcory.
Open `api.py`.
The function named 'send_to_viewer' can send POST request to BiCAmon.
Please put this function in the directory in the path.
Finally, insert the function call in your program and launch the architecture.

## LICENSE

* Files other than third party's.
 - Revised BSD License

* Third party's files.
 - Follow the license written in the files.
