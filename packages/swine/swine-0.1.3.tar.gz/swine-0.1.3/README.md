# Swine Library

An SDK for starting and interacting with Pig Windows VMs.

**Note: This API (and associated infra) is not stable, and may change at any time. Use at your own risk.**

## Installation

```bash
pip install swine
```

## Quick Start

First, set up your API key:

```bash
export PIG_SECRET_KEY=your_api_key
```

The following code snippet will launch your first VM and interact with it:

```python
from swine import VM

vm = VM()
print("Starting VM...")
# The initial boot will take a few minutes.
conn = vm.connect()

# Once it's ready, you can start sending commands
conn.mouse_move(100, 100)  # Move mouse to coordinates
conn.left_click(100, 100)  # Click at coordinates
conn.type("Hello, World!") 

# Print our VM ID for later use
print(vm.id) # -> VM-ABCDEFG-ABCDEFG-ABCDEFG
```
This VM will remain running.

You may resume work on it by referencing it by ID:
```python
vm = VM(id="VM-ABCDEFG-ABCDEFG-ABCDEFG")

conn = vm.connect()
conn.type("Hello Again!")
```

Lastly, please clean up after yourself and stop your running VMs:
```python
vm.stop() # Persists to disk
# or
vm.terminate() # Deletes the disk, making the VM no longer usable.
```

For automated scripts where you want to ensure VMs are properly cleaned up, you can use the context manager:

```python
with VM().session() as conn:
    conn.mouse_move(100, 100)
    conn.left_click(100, 100)
    # VM automatically stops when leaving this block
```

**Tip:** During development and exploration, prefer using the imperative API (`vm.connect()`) so you can watch the VM and experiment. Use the context manager (`vm.session()`) once you're ready to automate tasks.

## Main Classes

### VM

VMs represent actual VM infrastructure on the Pig platform.

```python
vm = VM(
    id=None,              # Optional: If you want to point to an existing Pig VM
    image=None,              # Optional: Windows image configuration
    temporary=False,         # Whether to delete VM after use in a .session()
    api_key=None             # Your API key (or use PIG_SECRET_KEY env var)
)
```

Instantiating VM() will create an empty VM client object.

Manage the cloud lifecycle of the VM with basic methods:
- `create()`: Creates a new VM on Pig and performs its initial boot
  - Sets `vm.id` on the client object, tying it to the newly created machine.
- `start()`: Starts the VM. No-op if already running
- `stop()`: Stops the VM. No-op if already stopped
- `terminate()`: Terminates and deletes the VM. It will no longer be usable

The VM lifecycle can be managed with the `session` context manager:
```python
with vm.session() as conn:
    # do stuff with conn
```
- Creates VM if necessary
- Starts VM if necessary
- Yields a `Connection` object
- Stops the VM on scope exit

This ensures you don't leave machines running.

Alternatively, you can call `connect` directly:
```python
conn = vm.connect()
# do stuff with conn
```
- Creates VM if necessary
- Starts VM if necessary
- Returns a `Connection` object
- Prints URL where you can watch the desktop

This will leave the VM running, and it's up to you to stop it.

### Connection

Connections are the interface for sending commands into a running VM.

You create connections with:
```python
conn = vm.connect()
# or
with vm.session() as conn:
    # ...
```

Methods:
- `type(str)`: Type text into VM
- `cursor_position()`: Returns current cursor position as (x, y) tuple.
- `mouse_move(x, y)`: Move mouse to coordinates
- `left_click(x, y)`: Left click at coordinates
- `left_click_drag(x, y)`: Click at current position and drag to new coordinates
- `double_click(x, y)`: Double click at coordinates
- `right_click(x, y)`: Right click at coordinates
- `screenshot() -> bytes`: Take a screenshot. Returns bytes in PNG format

Getters:
- `width`: Get the width of the VM (1024) 
- `height`: Get the height of the VM (768)

## Advanced Usage

### Custom Images

You can boot Windows VMs with custom images:

```python
windows = (
    Windows(version="2025")    # Specify Windows version
    .install("Office")         # Add applications to install
)

vm = VM(image=windows)
vm.create()  # Boots Windows 2025 with Office installed
```

### Temporary VMs

If using the `vm.session()` context manager, you can flag the VM to be terminated after use with `temporary=True`:

```python
vm = VM(temporary=True)
with vm.session() as conn:
    # VM is terminated after this block
```

Note existing VM IDs cannot be used as temporary VMs.

## Environment Variables

- `PIG_SECRET_KEY`: Your API key
- `PIG_BASE_URL`: Custom API URL (default: https://api.pig.dev)
- `PIG_UI_BASE_URL`: Custom UI URL (default: https://pig.dev)

## Schema

Swine is best used as Tools called via [Anthropic Computer Use](https://docs.anthropic.com/en/docs/build-with-claude/computer-use).

To assist in configuring the computer use environment, we provide the tool specification:

```python
from swine.schema import claude

# claude = {
#   "properties": {
#       "action": {
#           "description": """The action to perform. The available actions are:
#               * `type`: Type a string of text on the keyboard.
#               * `cursor_position`: Get the current (x, y) pixel coordinate of the cursor on the screen.
#               ...
```