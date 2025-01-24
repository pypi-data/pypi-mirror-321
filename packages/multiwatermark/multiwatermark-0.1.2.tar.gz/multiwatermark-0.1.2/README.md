# MultiWatermark
## *By Matt Burns*

## Installation
```pip install multiwatermark```

## Usage
```
from multiwatermark import multiwatermark

image_path = "some/path/input.jpeg"
text = "Example Text"
output_path = "some/path/output.jpeg"

multiwatermark.add_watermark(image_path, text, output_path, font_size=36, opacity=128, watermark_count=5):
```

### Options
image_path: Path to the input image.
text: Watermark text to be added.
output_path: Path to save the watermarked image.
font_size: Size of the watermark text.
opacity: Opacity of the watermark (0-255).
watermark_count: number of watermarks to overlay

## Source Code
