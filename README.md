# pickemOdder
nfl games odds analyzer 

reads weekly game data from currently a single source (https://the-odds-api.com) puts it in a dataframe, groups and sorts by away wins 

# Development requirements
- python3
- virtualenv

# Installing

It's still in development so local install into a virtualenv

```bash
git clone https://github.com/danwald/pickemOdder.git
cd pickemOdder
mkvirtualenv pickem
workon pickem
pip install -e .
```

# Running
## Getting data

This pulls data from the-odds-api.com for the upcoming week. Set `ODDS_API_KEY` with your api key and save the output to a file

`python pickemOdder/get-odds-data.py > out.json`

## Sorting the data

__by away win %__

`python pickemOdder/cli.py < out.json`


# Running tests

> make test
