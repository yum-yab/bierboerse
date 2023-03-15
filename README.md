# Born again Bierboerse

A GUI application for a simulated stock market for selling stuff.

## Setup

[Install poetry](https://python-poetry.org/docs/) and run the following (on linux):

```bash
poetry install &&
poetry shell &&
python bierboerse/bierboerse.py
```


## Planned features

### Core

* [ ] Make any number of stocks (beers) possible, in the range of 1-10
* [ ] Make it repsonsible to make it look good on every screen size
* [ ] Seperate the data from the visual representation to allow multiple configurations 
* [ ] Make it error prone, so allow undoing multiple actions and save the state in certain intervals for backup
* [ ] make it configurable on the fly without restarting (removing/changing/adding a stock)
* [ ] Come up with same clever change functions with a bought stock


### Nice to have

* [ ] Actually implement multiple visual representations (one big plot vs. one for each stock)
