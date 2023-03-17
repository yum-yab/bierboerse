# Born again Bierboerse

A GUI application for a simulated stock market for selling stuff.

## Setup

[Install poetry](https://python-poetry.org/docs/) and run the following (on linux):

```bash
git clone https://gitea.v122.de/denis/bierboerse.git && cd bierboerse
poetry install &&
poetry run python bierboerse/bierboerse.py
```

## Resources

1. Genral introduction to `PyQt`: [Link](https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/)
2. Reference for `pyqtgraphs`: [Link](https://pyqtgraph.readthedocs.io/en/latest/)

## Planned features

### Core

* [ ] Make any number of stocks (beers) possible, in the range of 1-10
* [ ] Make it responsible to make it look good on every screen size
* [ ] Seperate the data from the visual representation to allow multiple configurations 
* [ ] Allow undoing multiple actions 
* [ ] save the state in certain intervals for backup
* [ ] make it configurable on the fly without restarting (removing/changing/adding a stock)
* [ ] Come up with some clever change functions with a bought stock


### Nice to have

* [ ] Actually implement multiple visual representations (one big plot vs. one for each stock)
