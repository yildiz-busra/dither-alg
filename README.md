# Floyd-Steinberg Dithering Algorithm

A Python repository implementing the Floyd-Steinberg dithering algorithm for image processing.

## Overview

This repository provides a Python implementation of the Floyd-Steinberg dithering algorithm. Dithering is used to convert grayscale images to black-and-white while preserving perceived image quality by distributing quantization errors to neighboring pixels. This technique is commonly used in image processing, printing, and display technologies.

## Features

- Implements the Floyd-Steinberg dithering algorithm
- Processes images using Pillow (PIL) and NumPy
- Converts images to dithered (black-and-white) versions
- Useful for education, research, and practical image processing

## Usage

### Prerequisites

- Python 3.x
- Pillow (`pip install pillow`)
- NumPy (`pip install numpy`)

### Running the Code

1. Clone the repository:
   ```
   git clone https://github.com/yildiz-busra/dither-alg.git
   cd dither-alg
   ```

2. Run the script:
   ```
   python floyd_steinberg.py
   ```
   - Make sure to specify your input image path as required in the script.
   - The output will be a dithered image file.

### Example

```python
from PIL import Image
import numpy as np

def floyd_steinberg_dither(image_path):
    image = Image.open(image_path).convert('L')
    # ... dithering algorithm ...
    image.save('output.png')
```

## Algorithm Included

- Floyd-Steinberg Dithering

## Author

[Busra Yildiz](https://github.com/yildiz-busra)

---

*For educational and research use. Contributions and feedback are welcome!*
