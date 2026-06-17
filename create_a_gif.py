import os
from PIL import Image

# Initialize images list
images = []
target_size = None

# Get all PNG and JPG files in the current directory
for filename in sorted(os.listdir('.')):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        img = Image.open(filename)
        
        # Convert to RGB (removes transparency and ensures consistent format)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Set target size from first image
        if target_size is None:
            target_size = img.size
            print(f"Image size: {target_size}")
        
        # Resize to match first image size
        img = img.resize(target_size)
        images.append(img)
        print(f"Added: {filename}")

# Create GIF
if images:
    images[0].save(
        'output.gif',
        save_all=True,
        append_images=images[1:],
        duration=800,  # duration in milliseconds
        loop=0
    )
    print("GIF created successfully: output.gif")
else:
    print("No images found in the directory")