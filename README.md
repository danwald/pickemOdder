# pickemOdder
nfl games odds analyzer

reads weekly game data from currently a single source (https://the-odds-api.com) puts it in a dataframe, groups and sorts by away wins

# Development requirements
- python3
- [uv](https://docs.astral.sh/uv/)

# Installing

To install as a dependency in another project:

```bash
uv add pickemOdder
```

To set up the project locally for development:

```bash
uv sync
```

# Running
## Getting data

This pulls data from the-odds-api.com for the upcoming week. Set `ODDS_API_KEY` with your api key and save the output to a file

`uv run getOddsData > out.json`

## Sorting the data

__by away win %__

`uv run pickemOdder < out.json`

# Running tests

```bash
uv run pytest
```
