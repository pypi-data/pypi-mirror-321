# Copyright (C) 2024,2025 Kian-Meng Ang
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""Halftone subcommand."""

import argparse
import logging
import math

from PIL import Image, ImageDraw

from fotolab import save_image

log = logging.getLogger(__name__)


def build_subparser(subparsers) -> None:
    """Build the subparser."""
    halftone_parser = subparsers.add_parser(
        "halftone", help="halftone an image"
    )

    halftone_parser.set_defaults(func=run)

    halftone_parser.add_argument(
        dest="image_filenames",
        help="set the image filename",
        nargs="+",
        type=str,
        default=None,
        metavar="IMAGE_FILENAMES",
    )


def run(args: argparse.Namespace) -> None:
    """Run halftone subcommand.

    Args:
        config (argparse.Namespace): Config from command line arguments

    Returns:
        None
    """
    log.debug(args)

    for image_filename in args.image_filenames:
        original_image = Image.open(image_filename)
        grayscale_image = original_image.convert("L")
        width, height = original_image.size

        halftone_image = Image.new("L", (width, height), "black")
        draw = ImageDraw.Draw(halftone_image)

        # modified from the circular halftone effect processing.py example from
        # https://tabreturn.github.io/code/processing/python/2019/02/09/processing.py_in_ten_lessons-6.3-_halftones.html
        coltotal = 50
        cellsize = width / coltotal
        rowtotal = math.ceil(height / cellsize)

        col = 0
        row = 0

        for _ in range(int(coltotal * rowtotal)):
            x = int(col * cellsize)
            y = int(row * cellsize)
            col += 1

            if col >= coltotal:
                col = 0
                row += 1

            x = int(x + cellsize / 2)
            y = int(y + cellsize / 2)

            brightness = grayscale_image.getpixel((x, y))
            amp = 10 * brightness / 200
            draw.ellipse(
                [x - amp / 2, y - amp / 2, x + amp / 2, y + amp / 2], fill=255
            )

        save_image(args, halftone_image, image_filename, "halftone")
