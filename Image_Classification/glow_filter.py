from PIL import Image, ImageFilter, ImageOps, ImageDraw
import matplotlib.pyplot as plt
import os
import random

def cyberpunk_filter(image_path, output_path=None):
    try:
        img = Image.open(image_path).convert("RGB")
        img_resized = img.resize((512, 512))

        # Step 1: Create neon color overlay
        neon_colors = [(255, 0, 255), (0, 255, 255), (255, 255, 0)]
        overlay = Image.new("RGB", img_resized.size)
        for y in range(img_resized.height):
            for x in range(img_resized.width):
                r, g, b = img_resized.getpixel((x, y))
                # Mix original color with random neon
                nr, ng, nb = random.choice(neon_colors)
                overlay.putpixel((x, y), (int((r+nr)/2), int((g+ng)/2), int((b+nb)/2)))

        # Step 2: Add glitch lines
        draw = ImageDraw.Draw(overlay)
        for _ in range(20):
            y = random.randint(0, img_resized.height-1)
            draw.line([(0, y), (img_resized.width, y)], fill=random.choice(neon_colors), width=1)

        # Step 3: Add glow blur
        final_img = overlay.filter(ImageFilter.GaussianBlur(radius=2))

        # Step 4: Save
        if not output_path:
            base, _ = os.path.splitext(image_path)
            output_path = f"{base}_cyberpunk.png"

        final_img.save(output_path)
        plt.imshow(final_img)
        plt.axis('off')
        plt.show()
        print(f"Cyberpunk filter applied and saved as '{output_path}'.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        image_path = input("Enter image filename (or 'exit' to quit): ").strip()
        if image_path.lower() == 'exit':
            break
        if not os.path.isfile(image_path):
            print(f"File not found: {image_path}")
            continue
        cyberpunk_filter(image_path)