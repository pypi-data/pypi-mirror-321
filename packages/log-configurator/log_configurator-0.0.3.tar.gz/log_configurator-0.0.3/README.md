# log configurator
Simple configurator for the python logging package that allows simultaneous file and shell logging

## installation
The log configurator can easily be installed from pypi
```
pip install log-configurator
```

## usage

Import the package and the default python logging

```python
import log_configurator
import logging
```

Configure python logging
```python
log_configurator.setup_root_logger()
```

Create a logging instance in your module as usual and log with it
```python
logger = logging.getLogger(__name__)
logger.info('Log Horizon')
```

### buffer initial output
If you need more complex argument parsing before you can configure the logger you can buffer it and have it logged once you configure your logger.

```python
initial_log = log_configurator.buffer_log()
logger = logging.getLogger(__name__)
logger.info('Early log information')

# <your setup code goes here>

log_configurator.setup_root_logger()
logger.debug(initial_log.getvalue())
```
The early log output currently can only be logged with one severity level.
