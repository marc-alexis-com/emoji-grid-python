# Emoji Grid Generator

This Python script generates grids of emojis from a specified folder and saves them as `.png` images. Each emoji is resized and placed into a customizable grid, which is then saved in the output folder.

## Features
- Generate a grid of emojis (default 3x3).
- Customizable grid size, cell size, and margins.
- Automatically saves the generated grid as `.png` images.

## Prerequisites

Before you begin, ensure you have Python installed on your machine, as well as the Pillow library.

### Install Pillow

To install Pillow, run the following command:

```bash
pip install Pillow
```

## Usage

1. **Clone the repository** (or download the script):
   ```bash
   git clone https://github.com/yourusername/emoji-grid-generator.git
   ```

2. **Prepare your emoji folder**:
   - Place all your emoji `.png` files in a folder (e.g., `emoji-selectionnes`).

3. **Run the script**:

   You can use the script by calling the `generate_emoji_grid` function. Here is an example of how to use it:

   ```python
   from emoji_grid import generate_emoji_grid

   generate_emoji_grid('path_to_emoji_folder', 'path_to_output_folder')
   ```

   - Replace `'path_to_emoji_folder'` with the path to your folder containing emoji `.png` files.
   - Replace `'path_to_output_folder'` with the folder where you want to save the output grid images.

4. **Customizable Parameters**:
   - **Grid Size**: Default is 3x3, but you can change it by passing a different value for `grid_size`.
   - **Cell Size**: Default is 64px, changeable via `cell_size`.
   - **Margin**: Default margin is 4px, customizable via `margin`.

   Example with custom parameters:
   ```python
   generate_emoji_grid('path_to_emoji_folder', 'path_to_output_folder', grid_size=4, cell_size=80, margin=5)
   ```

## Example

Given a folder of emojis, the script will generate grid images, with each emoji placed multiple times in a grid format. Example output file names would be: `1.png`, `2.png`, etc.



