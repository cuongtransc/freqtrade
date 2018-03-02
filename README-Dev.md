
# Build

```bash
docker build -t freqtrade .

```

# Run

```bash
docker run --rm -v `pwd`/config.json:/freqtrade/config.json -it freqtrade

```


```bash
docker run -it --rm \
  --name freqtrade \
  -v ~/data/config.json:/freqtrade/config.json \
  -v ~/data/tradesv3.sqlite:/freqtrade/tradesv3.sqlite \
  freqtrade



```



Fake Bittrix Crendential

