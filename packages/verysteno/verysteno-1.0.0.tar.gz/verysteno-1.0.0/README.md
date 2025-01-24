# VerySteno
VerySteno lets you encode hidden text in sound and images.
## Usage
VerySteno is simple to use. To encode in an image:
```python
from verysteno import EncodeInImage, DecodeFromImage

EncodeInImage("input.png", "This message is secret.")
decoded_message = DecodeFromImage("input_encoded.png")
print(decoded_message)
```
To encode in an sound:
```python
from verysteno import EncodeInSound, DecodeFromSound

EncodeInSound("input.wav", "This is a secret message.")
decoded_message = DecodeFromSound("input_encoded.wav")
print(decoded_message)
```
And to use passwords:
```python
from verysteno import EncodeInSound, DecodeFromSound

EncodeInSound("input.wav", "This secret message has a password!", "verypassword")
decoded_message = DecodeFromSound("input_encoded.wav", "verypassword")
print(decoded_message)
```

