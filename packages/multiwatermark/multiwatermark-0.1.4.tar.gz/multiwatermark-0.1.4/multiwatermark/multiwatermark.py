import random
from PIL import Image, ImageDraw, ImageFont

# TODO FUTURE UPDATES
# add custom font, 
# add number of watermarks, 
# add support for watermark image
# add support for output file types

def add_watermark(image_path, text, output_path, font_size=36, opacity=128, watermark_count=5):
    """
    Adds custom watermark to an image and saves the result.

    :param image_path: Path to the input image.
    :param text: Watermark text to be added.
    :param output_path: Path to save the watermarked image.
    :param font_size: Size of the watermark text.
    :param opacity: Opacity of the watermark (0-255).
    :param watermark_count: number of watermarks to overlay
    """

    try:
        image = Image.open(image_path).convert("RGBA")
        
        txt_overlay = Image.new("RGBA", image.size, (255,255,255,0))
        
        font = ImageFont.load_default()

        draw = ImageDraw.Draw(txt_overlay)

        text_width = draw.textlength(text, font=font)
        text_height = font_size

        # Generate random non-overlapping positions
        positions = []
        attempts = 0
        max_attempts = 100

        while len(positions) < watermark_count and attempts < max_attempts:
            x = random.randint(0, image.size[0] - int(text_width))
            y = random.randint(0, image.size[1] - int(text_height))
            new_position = (x, y)

            # Check for overlap with existing positions
            overlap = False
            for pos in positions:
                if abs(pos[0] - x) < text_width and abs(pos[1] - y) < text_height:
                    overlap = True
                    break

            if not overlap:
                positions.append(new_position)
            attempts += 1

        # Add text to the overlay at the calculated positions
        for position in positions:
            draw.text(position, text, font=font, fill=(255, 255, 255, opacity))

        watermarked = Image.alpha_composite(image, txt_overlay)

        watermarked.convert("RGB").save(output_path, "JPEG")

        print(f"Watermarked image saved to {output_path}")

    except Exception as e:
        print(f"Error: {e}")
        raise e

if __name__ == "__main__":
    image_path = "test.jpeg"
    text = "Matt Burns 2025"
    output_path = "output.jpeg"

    add_watermark(image_path=image_path, text=text, output_path=output_path)