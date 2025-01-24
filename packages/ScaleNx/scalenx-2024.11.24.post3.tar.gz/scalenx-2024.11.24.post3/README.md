# Pixel Art Scaling - Scale2x and Scale3x

## Overview

[**Scale2x** and **Scale3x**](https://github.com/amadvance/scale2x) (aka **AdvMAME2x** and **AdvMAME3x**) algorithms were developed by [Andrea Mazzoleni](https://www.scale2x.it/) for sole purpose of scaling up small graphics like icons and game sprites.

However, apparently it appeared to be useful for scaling up text scans with low resolution before OCR, to improve OCR quality.

For this, current general purpose pure Python implementation of Scale2x and Scale3x was developed. Current implementation does not use any import, neither Python standard nor third party, and therefore is quite cross-platform and onmicompatible.

For examples of practical programs utilizing this module, with GUI, multiprocessing etc., please visit [ScaleNx at Github](https://github.com/Dnyarri/PixelArtScaling). PNG support in these programs is based on [PyPNG](https://gitlab.com/drj11/pypng), and PPM and PGM support - on [PyPNM](https://pypi.org/project/PyPNM/), both of the above being pure Python modules as well.

## Installation

`pip install ScaleNx`, then `from scalenx import scale2x` or `from scalenx import scale3x`.

## Usage

`scaled_image = scale2x(source_image)`

where both images are of 3D nested list (image) of lists (rows) of lists (pixels) of int (channel values) type.

## Copyright and redistribution

Current Python implementation was written by [Ilya Razmanov](https://dnyarri.github.io/) and may be freely used, copied and improved. In case of making substantial improvements it's almost obligatory to share your work with the developer and lesser species.

## References

1. [Scale2x and Scale3x](https://www.scale2x.it/algorithm) algorithms description by the inventor, Andrea Mazzoleni.

2. [Pixel-art scaling algorithms](https://en.wikipedia.org/wiki/Pixel-art_scaling_algorithms) review at Wikipedia.

3. [ScaleNx at Github](https://github.com/Dnyarri/PixelArtScaling/) - current ScaleNx at Github, containing main programs for single and batch image processing.
