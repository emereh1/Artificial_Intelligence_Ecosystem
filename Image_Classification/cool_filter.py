from PIL import Image
import matplotlib.pyplot as plt
import os

# Paths to accessory images (with transparent backgrounds)
SUNGLASSES_PATH = "sunglasses.png"
CHAIN_PATH = "gold_chain.png"
HAT_PATH = "hat.png"

def apply_accessory_filter(image_path, output_path=None):
    try:
        # Open main image
        img = Image.open(image_path).convert("RGBA")
        img_resized = img.resize((512, 512))  # resize for consistency

        # Open accessory images
        sunglasses = Image.open(SUNGLASSES_PATH).convert("RGBA").resize((200, 60))
        chain = Image.open(CHAIN_PATH).convert("RGBA").resize((250, 100))
        hat = Image.open(HAT_PATH).convert("RGBA").resize((300, 150))

        # Calculate positions
        sunglasses_pos = (156, 200)  # roughly over the eyes
        chain_pos = (131, 380)       # roughly around the neck
        hat_pos = (106, 0)           # roughly on top of the head

        # Overlay accessories
        img_resized.paste(sunglasses, sunglasses_pos, sunglasses)
        img_resized.paste(chain, chain_pos, chain)
        img_resized.paste(hat, hat_pos, hat)

        # Default output path if none provided
        if not output_path:
            base, _ = os.path.splitext(image_path)
            output_path = f"{base}_accessory.png"  # always save as PNG

        # Save and show
        img_resized.save(output_path)  
        plt.imshow(img_resized)
        plt.axis('off')
        plt.show()

        print(f"Processed image saved as '{output_path}'.")

    except Exception as e:
        print(f"Error processing image: {e}")


if __name__ == "__main__":
    print("Accessory Filter Processor (type 'exit' to quit)\n")
    while True:
        image_path = input("Enter image filename (or 'exit' to quit): ").strip()
        if image_path.lower() == 'exit':
            print("Goodbye!")
            break
        if not os.path.isfile(image_path):
            print(f"File not found: {image_path}")
            continue

        apply_accessory_filter(image_path)
