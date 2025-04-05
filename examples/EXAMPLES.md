Initializing the 2d main window:

```python
from dooGL import *

init_window(800, 600)                          

running = True
while running:
    running = magic()

# Add your drawing code here #

    end()
```
Initializing the 3d main window:

```python
from dooGL import *

d3_init_window(width=800, height=600, depth=2000.0)
d3_camera(camera_pos=[-495,495,495])

running = True
while running:
    running = magic()
    
    # Add your drawing code here #

    end()
```