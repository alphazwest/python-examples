from PIL import Image, ImageDraw, ImageFont
import textwrap
from string import ascii_letters


class TextWrapper(object):
    """
    A class to provide basic text-wrapping functionality such
    that custom fonts, font-sizes, and texts can be overlaid on
    images in a flexible manner. Uses the standard textwrap library
    and the Pillow library.
    """
    def __init__(self, image: Image, text: str, font: ImageFont):
        self.image = image
        self.text = text
        self.font = font
        self.draw = ImageDraw.Draw(im=self.image)

    @staticmethod
    def scaled_text_wrap(text: str, width: int or float, font: ImageFont) -> str:
        """
        Creates a text wrapped string to fit within a specified width by
        calculating the average width of a character and converting that
        to a maximum number of characters to be used with Pythons
        textwrap.fill() function.
        Args:
            text: The string of text to which the wrapping effect is
             to be applied
            width: The width, as an integer pixel value, for the
             maximum line to span.
            font: The ImageFont object from which our average character
             length measure is derived.

        Returns:
            A string split into lines of a <width> maximum length scaled
        """
        # Calculates the average character width of a font to translate
        # to a max character count such that the textwrap.fill's width
        # argument can be appropriately used.
        avg_char_width = sum(font.getsize(char)[0]
                             for char in ascii_letters) / len(ascii_letters)

        return textwrap.fill(text=text, width=int(width / avg_char_width))

    def wrap_text(self, width: int, position: tuple = None,
                  color: str = "#ffffff", anchor: str = 'mm'):
        """
        Adds text to the image located at the <position> argument as x, y
        image-relative pixel coordinates. Text color is set via the <color>
        argument which can take a hexadecimal value or verbose color name
        specified by the Pillow TextDraw module. The text is positioned via
        the anchor argument that signifies the desired position relative
        to ImageDraw text anchor parameters.

        References:
            color:  https://pillow.readthedocs.io/en/stable/reference/ImageColor.html#color-names
            anchor: https://pillow.readthedocs.io/en/stable/handbook/text-anchors.html
        Args:
            width: int value representing maximum pixel width at which
             to wrap the text.
            position: x,y tuple coordinates in pixel value for text placement
            color: str argument for text color
            anchor: str argument for text placement relative to position
        """
        # Restrict max image width to image width
        if width > self.image.size[0]:
            width = self.image.size[0]

        # Center text to image unless otherwise specified
        if not position:
            position = (self.image.size[0] / 2, self.image.size[1] / 2)

        # Draw a scaled version of the text on the image
        self.draw(
            xy=(position[0], position[1]),
            text=self.scaled_text_wrap(text=self.text, width=width, font=self.font),
            font=self.font,
            fill=color,
            anchor=anchor
        )

    def show(self, **kwargs):
        """
        Convenience wrapper for the Image object's show() method. Displays
        the current image state via system standard photo viewer.
        """
        self.image.show(kwargs)

    def save(self, filepath: str, **kwargs):
        """
        Convenience function for the Image object's save() method. Saves
        the current image state to a specified filepath location.
        Args:
            filepath: str filepath to which the image is saved.
        """
        self.image.save(filepath, kwargs)
