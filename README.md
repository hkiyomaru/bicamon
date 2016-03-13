#WebGL Visualization of Mouse Brain


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
