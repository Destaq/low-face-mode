# low-face-mode

This program uses `opencv` and `osascript` to brighten or dim your monitor screen (on MacOS) based on whether or not you are behind your computer.

By doing this, it preserves battery life, as the screen is dimmed down to zero when a face has not been detected by the computer's webcamera for some time. However, as soon as a face is detected again, the screen is once more brightened with the help of applescript commands executed from python.

## Requirements
*There's a lot to support the custom face recognition, if you just want face detection, don't worry about this.*
`opencv`
`osascript`
`numpy`
`argparase`
`pickle`
`imutils`
`face_recognition`

## Code in Action!

![Example GIF](https://github.com/Destaq/low-face-mode/blob/master/data/sample.gif)
