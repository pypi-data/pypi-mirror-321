# Dokkey

**Dokkey** is a lightweight Python package designed to detect key presses on Windows. It captures keyboard input and returns the ASCII code of the key pressed. This package has been tested on **Windows 11**.

---

## Features

- Detects keypresses on Windows.
- Returns the ASCII code of the key pressed.
- Lightweight and easy to integrate into your projects.

---

## Requirements

- Python 3.7 or higher
- Windows OS (Tested on Windows 11)

---

## Installation

Install the package using pip:

```bash
pip install dokkey
```

## Usage
Here is an example of how to use Dokkey:

```python
import signal
import dokkey

def cleanup_and_exit(signum, frame):
    try:
        dokkey.uninstall_hook()
    except Exception as e:
        print(f">>> Error during cleanup: {e}")
    finally:
        print(">>> Exiting gracefully.")
        exit(0)

signal.signal(signal.SIGINT, cleanup_and_exit)

# Install the hook and run the message loop
def on_key_press(key_code):
    print(f">>> Key pressed: {key_code}")

print("Listening for key presses. Press Ctrl+C to stop.")
try:
    dokkey.install_hook(on_key_press)
    dokkey.run_message_loop()
except Exception as e:
    print(f">>> Error: {e}")
finally:
    dokkey.uninstall_hook()
```
## Output Example
```plaintext
Listening for key presses. Press Ctrl+C to stop.
Key pressed: 65  # (A key)
Key pressed: 98  # (b key)
```

## How It Works
Dokkey leverages Windows APIs to capture global keyboard events and converts the input to ASCII codes. It ensures minimal interference with other running applications.

## Limitations
This package works only on Windows.
It may require administrator privileges for certain use cases.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request if you have suggestions or improvements.

## Local Development
To set up a local development environment, follow these steps:

1. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    venv/Scripts/activate
    ```
2. Build & install the project
    ```bash
    python setup.py build
    python setup.py install
    ```
The module is now installed in the virtual environment. You can test it by running the example script:

```bash
python examples/example.py
```


## License
This project is licensed under the Apache-2.0 License. See the LICENSE file for details.

## Author
Developed by Sekiraw

## Acknowledgements
Thanks to the Python and Windows development communities for providing tools and resources to make this project possible.

```vbnet
This styling ensures clarity, proper sectioning, and good readability. Let me know if you`d like any further adjustments!
```
