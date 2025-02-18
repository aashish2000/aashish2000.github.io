---
title: "See-Do-Ku: Playing Sudoku with Computer Vision"
date: 2020-09-11
categories: ["Uncategorized"]
---

Seedoku is a Computer Vision based interactive Sudoku Game using Hand Detection and Tracking for moving numbers across the frame. This project opens a game of sudoku on the screen and allows you to move the numbers to their appropriate location using your hands. The location of your hand is tracked in real time through your webcam feed. You will be able to move the pointer, pick up numbers and drop them in their respective places without needing a mouse or keyboard. 

For selecting a number, keep your pointer on a number and bring it closer. Once your hand gets close enough, the color of the cursor changes and the number gets selected. Similarly for dropping a number in its appropriate place, bring your hand closer with your pointer at the intended location. To move numbers around the screen without selecting and dropping, bring your hand farther away from the screen and move the pointer wherever you want.

The area of the bounding boxes of your hand increases as the hand comes closer to the camera and vice versa when you pull you hand farther away. This gives the select and drop functionality.

{{< video "seedoku-demo.m4v" "my-5" >}}

The Hand Tracking functionality is achieved through a SSD based Hand Position detector. This detector was adapted from the open source Mediapipe Framework by Google Research. This model is based on TFLite, and is capable of performing Hand Detection at around 30fps on modern Edge Devices.

The game is available as a CLI utility distributed via PyPi.

To install and run the game: 
```sh
pip install seedoku
seedoku
```
## Packages Used
- TensorFlow 2
- OpenCV

To check out the source code in Github, click [here](https://github.com/aashish2000/SeeInDark).
