# BMF python rest client

description not ready yet.

## Getting Started

Just import and use the built-in context manager `bmfsession`

example:

```python
from bmf.api import bmfsession, get

with bmfsession(CONTROLLER_ADDR, USER, PASSWORD) as s:
    print(get(s, "/data/controller/core/switch"))
```

### Prerequisites

Project depends on python `requests` library.

### Installing

Packaging is not implemented.

## Authors

* **srozb** - [srozb](https://github.com/srozb)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
