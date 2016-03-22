#WebGL Visualization of Mouse Brain

![screenshot](https://raw.github.com/wiki/kiyomaro927/MouseBrainVisualizationOnWeb/images/screen_shot.png)

##Instruction

First, clone this repository.

```
$ https://github.com/kiyomaro927/MouseBrainVisualizationOnWeb.git
```

You have to install some packages to run this program.

They are written in _requirements.txt_.

```cd inside```, and run the next script.

```
$ pip install -r requirements.txt
```

You don't have the necessary database file yet.

However, you have the seed to build it.

```cd database```, and run this.

```
$ ./makedb.sh
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

Then, run the test code to fire cells.

```
$ python post_test.py
```

##Combine

Let's combine your brain model.

The program to call API is in the test direcory.

Then, open _api.py_.

The function named 'send_to_viewer' can send POST request to the viewer.

Please put this function in the directory in the path.

And, insert the function call in your program.
