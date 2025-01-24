# install
```
pip install hfl-healthcheck
```

# import 
`from healthcheck import health_check_sender`

# use
```python
from healthcheck import health_check_sender
import threading
threading.Thread(target=health_check_sender(0),name="healthcheck").start()
```