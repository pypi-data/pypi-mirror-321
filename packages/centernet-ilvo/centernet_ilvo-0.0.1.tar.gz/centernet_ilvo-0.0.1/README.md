# CenterNet ILVO

## Introduction

This python package can be used to run the CenterNet model for plant centre detection.
The plant CenterNet model is presented in the following paper:

```
Willekens, A., Callens, B., Pieters, J., Wyffels, F., & Cool, S. (2025). 
Cauliflower centre detection and 3-dimensional tracking for robotic intrarow weeding. 
Precision Agriculture. Springer.
 ```

An example for usage is provided on the [Hugging Face - CenterNet ILVO](https://huggingface.co/axelwillekens/centernet_ilvo)

## Installation

1. Install [pytorch (torch and torchvision)](https://pytorch.org/get-started/locally/)
2. Install dependencies and the package
```bash
pip install numpy opencv-python scikit-image
pip install cams-ilvo-utils
pip install centernet-ilvo
``` 

## Licence

This project is under the ``ILVO LICENCE``.

```
Copyright (c) 2024 Flanders Research Institute for Agriculture, Fisheries and Food (ILVO)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

When the Software, including modifications and extensions, is used for:
- commercial or non-commercial machinery: the ILVO logo has to be clearly
   visible on the machine or on any promotion material which may be used in any
   agricultural fair or conference, in a way it is clear that ILVO contributed
   to the development of the software for the machine.
- a scientific or vulgarising publication: a reference to ILVO must be made as
   well as to the website of the living lab Agrifood Technology of ILVO:
   https://www.agrifoodtechnology.be

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```