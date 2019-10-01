# pickemOdder
nfl games odds analyzer 

reads weekly game data from currently a single source (https://the-odds-api.com) puts it in a dataframe, groups and sorts by away wins 

# Development requirements
- python3
- pipenv

# Installing

Currently in developement so I have't added (fixed) the pip console_scripts cli. So just

```bash
git clone https://github.com/danwald/pickemOdder.git
cd pickemOdder
pipenv shell
pipenv install --dev 
```

# Running tests

After installing testing requirements inside `requirements/python/testing.txt`, you can run all tests, by running this command

> make test
