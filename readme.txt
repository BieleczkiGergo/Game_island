I will try to make parts of the program separate from eachother, like it has to be. That means we will always be able to modify them without rewriting it all.

Short description to the parts (that are made already):
  frame:
    This contains only one class, which is the main frame of the game, the window its in. It mainly consists of two parts, the canvas and the "frame" element,
    that basically holds everything else. It creates a window for itself when initializing, so you don't have to give it any arguments when doing so.
    Current workers: Geri
    
  sprites:
    This would contains the sprites for the game, including moving and non-moving objects. Images are also imported here. The background is not a sprite.
    Current workers: Gabi
