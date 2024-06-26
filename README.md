# Banana Clicker Bot

This Python script automates mouse clicks on a specific image found on your screen. It's useful for tasks that require repetitive clicking at a specific location. 


## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [How It Works](#how-it-works)
- [Contributing](#contributing)




## Prerequisites

Make sure you have the following libraries installed:

- `pyautogui`
- `pynput`
- `Pillow`

You can install these using pip:

```bash
pip install pyautogui pynput pillow
```

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/fast-clicker-bot.git
cd fast-clicker-bot
```

2. **Place the image you want to click on (banana.png in this example) in the same directory as the script:**



### Usage

1. **Run the script:**

```bash
python fast_clicker_bot.py
```

2. **Controls:**

    - **Press `p`**: Pause the clicking
    - **Press `c`**: Continue the clicking
    - **Press `Esc`**: Stop the script

### How It Works

1. The script uses `pyautogui` to locate the image on the screen and click on it.
2. The `pynput` library is used to listen for keyboard inputs to pause, continue, or stop the clicking.
3. The `Pillow` library (imported as `PIL`) is used to handle the image to be clicked.


## Demo Video

Watch the demo video on YouTube:

[![Fast Clicker Bot Demo](https://img.youtube.com/vi/FTtUtH62zKU/0.jpg)](https://www.youtube.com/watch?v=FTtUtH62zKU)


## Customization

You can adjust the speed of the clicking by modifying the `pyautogui.PAUSE` value and the `time.sleep()` duration.

```python
pyautogui.PAUSE = 0.00001
# Adjust the sleep time in the loop
time.sleep(0.1)
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.


![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![PyAutoGUI](https://img.shields.io/badge/pyautogui-0.9.52-green)
![Pillow](https://img.shields.io/badge/pillow-8.2.0-yellow)
