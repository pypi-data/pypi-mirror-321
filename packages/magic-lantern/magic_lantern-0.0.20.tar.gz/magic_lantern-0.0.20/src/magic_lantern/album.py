# An Album is a collection of images.  They can be displayed in
# random or sequential order.  Iterating through the album yields the
# next image.

import os
import pathlib
import random
import logging as log

from magic_lantern.slide import Slide
from magic_lantern import config
from magic_lantern.config import Order
from magic_lantern import pdf


class Album:
    def __init__(self, order: Order, path: pathlib.Path, weight: int, interval: int):
        self._order = order
        self._path = path
        log.debug(f"Creating Album from {path}.")
        if weight:
            self.weight = weight
        else:
            self.weight = config.weight
        if interval:
            self.interval = interval
        else:
            self.interval = config.interval

        self._slideList = []
        self._slideIndex = 0
        self._slideCount = 0
        # Walk through the source directory and its subdirectories
        for root, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if d not in config.exclude]
            for f in files:
                if "~" in f:
                    log.warning(f"Ignoring {f}")
                    continue

                if f.lower().endswith(".pdf"):
                    log.info(f"{f}  PDF file")
                    for pdfPageImageFile in pdf.convert(root, f):
                        slide = Slide(pdfPageImageFile, self.interval)
                        self._slideList.append(slide)
                    continue

                # Filter out files with unknown extensions
                if f.lower().endswith((".bmp", ".png", ".jpg", ".jpeg")):
                    imageFile = os.path.join(root, f)
                    slide = Slide(imageFile, self.interval)
                    self._slideList.append(slide)
                    continue

                log.warning(f"{f}  Unknown file type")

        # Shuffle or sort the list of slides
        if self._order == Order.RANDOM:
            random.shuffle(self._slideList)
        else:
            self._slideList.sort()

        # Update the slide count
        self._slideCount = len(self._slideList)

    def __iter__(self):
        return self

    def __next__(self):
        if self._slideIndex >= self._slideCount:
            self._slideIndex = 0
            if self._order == Order.ATOMIC:
                raise StopIteration  # We've reached the end; signal caller
        slide = self._slideList[self._slideIndex]
        self._slideIndex += 1
        return slide
