"""Module that defines the PictorRectangle class."""

from PIL import ImageDraw
from src.pictor_lib.pictor_box import PictorBox
from src.pictor_lib.pictor_drawable import PictorDrawable


class PictorRectangle(PictorDrawable):
    """Drawable rectangle shape."""

    def __init__(self, bbox: PictorBox):
        self._bbox = bbox

    def draw(self, draw: ImageDraw.Draw):
        pass

    def copy(self) -> 'PictorRectangle':
        """Create a new instance by copying all fields."""

        return PictorRectangle(bbox=self._bbox.copy())
