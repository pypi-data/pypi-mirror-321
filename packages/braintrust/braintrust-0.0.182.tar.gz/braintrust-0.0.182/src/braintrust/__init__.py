"""
A Python library for interacting with [Braintrust](https://braintrust.dev/). This library
contains functionality for running evaluations, logging completions, loading and invoking
functions, and more.

`braintrust` is distributed as a [library on PyPI](https://pypi.org/project/braintrust/). It is open source and
[available on GitHub](https://github.com/braintrustdata/braintrust-sdk/tree/main/py).

### Quickstart

Install the library with pip.

```bash
pip install braintrust
```

Then, create a file like `eval_hello.py` with the following content:

```python
from braintrust import Eval

def is_equal(expected, output):
    return expected == output

Eval(
  "Say Hi Bot",
  data=lambda: [
      {
          "input": "Foo",
          "expected": "Hi Foo",
      },
      {
          "input": "Bar",
          "expected": "Hello Bar",
      },
  ],  # Replace with your eval dataset
  task=lambda input: "Hi " + input,  # Replace with your LLM call
  scores=[is_equal],
)
```

Finally, run the script with `braintrust eval eval_hello.py`.

```bash
BRAINTRUST_API_KEY=<YOUR_BRAINTRUST_API_KEY> braintrust eval eval_hello.py
```

### API Reference
"""

from .audit import *
from .framework import *
from .framework2 import *
from .functions.invoke import *
from .functions.stream import *
from .logger import *
from .logger import _internal_reset_global_state, _internal_with_custom_background_logger
from .oai import wrap_openai
from .types import *
from .util import BT_IS_ASYNC_ATTRIBUTE, MarkAsyncWrapper
