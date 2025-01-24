"""VerySteno Library

VerySteno provides functionality to encode and decode hidden messages in sound and images.

Functions:
    - EncodeInSound: Encodes messages into sound files.
    - DecodeFromSound: Decodes messages from sound files.
    - EncodeInImage: Encodes messages into image files.
    - DecodeFromImage: Decodes messages from image files.

Each encoding and decoding function supports password-protected and passwordless variants.
"""

import wave
import numpy as np
from PIL import Image
import hashlib
import itertools


def hash_password(password):
    """Hashes the password for added security."""
    return hashlib.sha256(password.encode()).digest() if password else None


def EncodeInSound(audio_path, message, password=None):
    """Encodes a message into a sound file, optionally using a password."""
    with wave.open(audio_path, "rb") as audio:
        frames = bytearray(list(audio.readframes(audio.getnframes())))
    
    message += "###"  # Delimiter to indicate end of message
    if password:
        message = ''.join(chr(ord(c) ^ k) for c, k in zip(message, itertools.cycle(hash_password(password))))
    
    bits = ''.join(f'{ord(c):08b}' for c in message)
    
    for i, bit in enumerate(bits):
        frames[i] = (frames[i] & 0xFE) | int(bit)
    
    with wave.open(audio_path.replace(".wav", "_encoded.wav"), "wb") as output:
        output.setparams(audio.getparams())
        output.writeframes(bytes(frames))


def DecodeFromSound(audio_path, password=None):
    """Decodes a message from a sound file, optionally using a password."""
    with wave.open(audio_path, "rb") as audio:
        frames = list(audio.readframes(audio.getnframes()))
    
    bits = [str(frame & 1) for frame in frames]
    chars = [chr(int(''.join(bits[i:i+8]), 2)) for i in range(0, len(bits), 8)]
    message = ''.join(chars).split("###")[0]
    
    if password:
        message = ''.join(chr(ord(c) ^ k) for c, k in zip(message, itertools.cycle(hash_password(password))))
    
    return message


def EncodeInImage(image_path, message, password=None):
    """Encodes a message into an image file, optionally using a password."""
    img = Image.open(image_path)
    pixels = np.array(img)
    
    message += "###"
    if password:
        message = ''.join(chr(ord(c) ^ k) for c, k in zip(message, itertools.cycle(hash_password(password))))
    
    bits = ''.join(f'{ord(c):08b}' for c in message)
    
    flat_pixels = pixels.flatten()
    for i, bit in enumerate(bits):
        flat_pixels[i] = (flat_pixels[i] & 0xFE) | int(bit)
    
    new_pixels = flat_pixels.reshape(pixels.shape)
    encoded_img = Image.fromarray(new_pixels)
    encoded_img.save(image_path.replace(".png", "_encoded.png"))


def DecodeFromImage(image_path, password=None):
    """Decodes a message from an image file, optionally using a password."""
    img = Image.open(image_path)
    pixels = np.array(img).flatten()
    
    bits = [str(p & 1) for p in pixels]
    chars = [chr(int(''.join(bits[i:i+8]), 2)) for i in range(0, len(bits), 8)]
    message = ''.join(chars).split("###")[0]
    
    if password:
        message = ''.join(chr(ord(c) ^ k) for c, k in zip(message, itertools.cycle(hash_password(password))))
    
    return message


__all__ = [
    "EncodeInSound",
    "DecodeFromSound",
    "EncodeInImage",
    "DecodeFromImage"
]
