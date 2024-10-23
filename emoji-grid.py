import os
from PIL import Image

def generate_emoji_grid(emoji_folder, output_folder, grid_size=3, cell_size=64, margin=4):
    """
    Generates a grid of emojis from the specified folder and saves them as PNG images.
    
    Parameters:
    - emoji_folder: Folder containing the emoji PNG files.
    - output_folder: Folder where the generated images will be saved.
    - grid_size: Size of the grid (default is 3x3).
    - cell_size: Size of each cell in the grid.
    - margin: Margin around each emoji in the grid.
    """
    
    # Check if emoji folder exists
    if not os.path.exists(emoji_folder):
        print(f"Error: The folder '{emoji_folder}' does not exist.")
        return

    # Verify or create output folder
    os.makedirs(output_folder, exist_ok=True)

    # Get list of emoji files in the folder
    emoji_files = [f for f in os.listdir(emoji_folder) if f.endswith('.png')]

    # Check if there are any emojis to process
    if not emoji_files:
        print(f"No emoji PNG files found in '{emoji_folder}'.")
        return

    # Sort emoji files to maintain order
    emoji_files.sort()

    # Constants for image creation
    image_size = grid_size * cell_size
    emoji_size = cell_size - 2 * margin  # Size of emoji within the cell

    # Process each emoji file
    for index, emoji_filename in enumerate(emoji_files, start=1):
        emoji_path = os.path.join(emoji_folder, emoji_filename)

        # Open and resize emoji
        emoji_image = Image.open(emoji_path).convert("RGBA")
        emoji_resized = emoji_image.resize((emoji_size, emoji_size), resample=Image.LANCZOS)

        # Create a new transparent image for the grid
        new_image = Image.new('RGBA', (image_size, image_size), (255, 255, 255, 0))

        # Paste the resized emoji in each cell of the grid
        for y_index in range(grid_size):
            for x_index in range(grid_size):
                x_pos = x_index * cell_size + margin
                y_pos = y_index * cell_size + margin
                new_image.paste(emoji_resized, (x_pos, y_pos), emoji_resized)

        # Output filename based on sequence
        output_filename = f'{index}.png'
        output_path = os.path.join(output_folder, output_filename)

        # Save the new image
        new_image.save(output_path)
        print(f"Emoji grid for '{emoji_filename}' saved as '{output_path}'")

# Example usage:
# generate_emoji_grid('path_to_emoji_folder', 'path_to_output_folder')
