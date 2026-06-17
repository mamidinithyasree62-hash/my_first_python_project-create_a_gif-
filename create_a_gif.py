import os
from PIL import Image

images = []
target_size = None



for filename in sorted(os.listdir('.')):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        img = Image.open(filename)
        
        
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        
        if target_size is None:
            target_size = img.size
            print(f"Image size: {target_size}")
        
        
        img = img.resize(target_size)
        images.append(img)
        print(f"Added: {filename}")


if images:
    images[0].save(
        'output.gif',
        save_all=True,
        append_images=images[1:],
        duration=800,  
        loop=0
    )
    print("GIF created successfully: output.gif")
else:
    print("No images found in the directory")
