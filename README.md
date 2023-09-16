## duome-to-anki

This is a script to help automating the creation of [Anki](https://apps.ankiweb.net/) decks for [Duolingo](https://www.duolingo.com/) courses, based on the vocabularies provided at [Duome](https://duome.eu/).

### Installing

```sh
git clone git@github.com:gustavocovas/duome-to-anki.git
cd duome-to-anki
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Obtaining the Vocabulary List from Duome

- Go to the desired vocabulary pages by clicking on **Words** at Duome Home, and then selecting the desired **from** and **to** languages. For example:
  - [From English to Italian](https://duome.eu/vocabulary/en/it)
  - [From English to Romanian](https://duome.eu/vocabulary/en/ro)
  - [From English to Russian](https://duome.eu/vocabulary/en/ru)
- Save the html page to your computer

OR

```sh
wget -O romanian.html https://duome.eu/vocabulary/en/ro
```

### Run to prepare a CSV file

```sh
python3 duome_to_anki.py romanian.html > romanian.csv
```

Now you can edit the csv file on Excel / Sheets and then create a deck in Anki.
