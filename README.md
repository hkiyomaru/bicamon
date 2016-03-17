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

I think the cells you're watching are not firing.

I prepared some test programs in the test directory.

Then, run the test code to fire cells.

```
$ python post_test.py
```

##Runtime Options

###Rate of aborting requests

Too many requests cause a severe delay.

You can change the rate by setting '--abortrate' option.

By default, XX is 0.

```
$ python server.py --abortrate XX
```
