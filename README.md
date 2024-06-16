# Banana Clicker Bot

This Python script automates mouse clicks on a specific image found on your screen. It's useful for tasks that require repetitive clicking at a specific location. 


## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [How It Works](#how-it-works)
- [License](#license)



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

1. Clone the repository:

```bash
git clone https://github.com/yourusername/fast-clicker-bot.git
cd fast-clicker-bot
```

2. Place the image you want to click on (banana.png in this example) in the same directory as the script:



### Usage

Run the script:

```bash
python fast_clicker_bot.py
```

### How It Works

1. The script uses `pyautogui` to locate the image on the screen and click on it.
2. The `pynput` library is used to listen for keyboard inputs to pause, continue, or stop the clicking.
3. The `Pillow` library (imported as `PIL`) is used to handle the image to be clicked.


### Customization

You can adjust the speed of the clicking by modifying the `pyautogui.PAUSE` value and the `time.sleep()` duration.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
