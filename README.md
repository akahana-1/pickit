# pickit : Pickle Iterator

iterator library for sequential pickled file

## Usage

```python
from pickit import PickIt

for item in PickIt("example.dump"):
	# Some process
```

## Bundle Tool

pcat : behave like zcat

### Usage

```
$ pcat example.dump | head
```
