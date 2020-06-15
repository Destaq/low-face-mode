# low-face-mode

This program uses `opencv` and `osascript` to **brighten or dim your monitor screen** (currently only on MacOS) **based on whether or not you are behind your computer**.

By doing this, it **preserves battery life**, as the screen is dimmed down to zero when a face has not been detected by the computer's webcamera for some time. However, **as soon as a face is detected again, the screen is once more brightened** with the help of applescript commands executed from python.

It also fully supports **custom face recognition**. This means that it will only brighten/dim the screen if it is *your* face that is in front of the screen.

## Usage

`low-face-mode` utilizes the `argparse` library to **run commands directly from terminal**. This means that there is **no need to run in an IDE**.

The command-line commands are laid out as follows. You can run this code by typing `python3 low_face_mode.py` followed by the arguments you need (outline below). As an example, the simplest command for simple face detection is `python3 low_face_mode.py -r False -u <yourname>`. **Make sure that you are in the current directory of the low_face_mode.py file before beginning.**

```
usage: low_face_mode.py [-h] [-r RECOGNITION] [-d DATABASE] [-y YOURNAME] [-u USERS [USERS ...]]

optional arguments:
  -h, --help            show this help message and exit
  -r RECOGNITION, --recognition RECOGNITION
                        whether custom recognition is True/False
  -d DATABASE, --database DATABASE
                        create facial database; True/False
  -y YOURNAME, --yourname YOURNAME
                        name used for creating custom face database, MUST be same as in --users
  -u USERS [USERS ...], --users USERS [USERS ...]
                        list of verified users to brighten screen
```

With all of the listed arguments, we can either use a dash and the letter (e.g. -r' or two dashes and the name (shown on right, e.g. --recognition). We will use the shorter letters for simplicity and ease in this tutorial.

The `-r` tag means whether or not facial recognition is on. It is defaulted to `True`, and it is a *necessary* argument. Keep in mind that you MUST first set up your facial database before running, as otherwise the screen will always dim.

The `-d` tag is an *optional* argument; you can choose to ignore it and it is set to `False` by default. If you choose to set it to `True`, a startup script will intialize that will ask you to take some pictures of yourself. It will display a small window with your face in it, outlined in green. Now, you MUST make various faces and then press the `k` key. This creates samples of your face which are used with deep learning to later check it is you. When you are done taking photos, press the `q` key and wait a bit for them to be processed. **Suggested image count: 5-10**.

The `y` tag is an *optional* argument. It is set to `none` by default. However, if you are setting up your face database, it MUST be set to your name. This is because the database creates a folder with images of your name in it, and it will also later compare this name against the list of verified users. Example: `python3 low_face_mode.py -r True -d True -y Simon -u Simon`. If you set it to a previously unadded name, the image database will run again, and another user will be *added* to the facial database.

The `u` tag is *required*. You MUST include it, even if you are not running custom facial recognition. The `u` tag is the list of authorized users, ones who have the power to brighten/dim your screen. **Make sure that your name is set to this**. This list can be multiplefold long. Examples: `... -u Simon` or `... -u Simon Frank`. Ensure that this is your *last* argument.

If you are confused, you can type `python3 low_face_mode.py -h` to get the overview, which is also shown above.

## Requirements
*There's a lot to support the custom face recognition, if you just want face detection, don't worry about this.*

`opencv`
`osascript`
`argparse`
`pickle`
`imutils`
`face_recognition`

## Code in Action!

![Example GIF](https://github.com/Destaq/low-face-mode/blob/master/data/sample.gif)
