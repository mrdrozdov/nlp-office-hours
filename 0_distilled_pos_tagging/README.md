# Download corenlp models.

```
python -c "import stanfordnlp; stanfordnlp.download('en')"
```

# Download wikipedia.

- https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2 (approx. 14GB)

Can also browse here for a smaller dump:

- https://dumps.wikimedia.org/enwiki/latest/
- Here's an example: https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles1.xml-p10p30302.bz2

# Use WikiExtractor

- https://github.com/attardi/wikiextractor

```
python WikiExtractor.py ~/Downloads/enwiki-latest-pages-articles1.xml-p10p30302.bz2 --json --processes 4
```

# References

- https://www.inesc-id.pt/ficheiros/publicacoes/8885.pdf
