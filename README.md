# pickemOdder
nfl games odds analyzer

reads weekly game data from currently a single source (https://the-odds-api.com) puts it in a dataframe, groups and sorts by away wins

# Development requirements
- python3
- virtualenv

# Installing

```bash
pjp install pickemOdder
```
# Running
## Getting data

This pulls data from the-odds-api.com for the upcoming week. Set `ODDS_API_KEY` with your api key and save the output to a file

`getOddsData > out.json`

## Sorting the data

__by away win %__

`pickemOdder < out.json`

# Running tests

> make test
