A d20-friendly Visual Novel prototype realized with Ren'Py and AI-generated graphics

Releases can be found on [my Itch.io channel](https://sprintingkiwi.itch.io/)

Graphics realized with Stable Diffusion

# LICENSES:
* The **code** is under GNU GPL 3 License, except for [dnd_character python library](https://github.com/tassaron/dnd-character) which credits go to [tassaron](https://github.com/tassaron), and it comes with its own license.
* The **images** are licensed [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/)
* Credits and licenses for the **audio** files are specified inside the audio folder

# CREDITS:
A special thanks to:
* [tassaron](https://github.com/tassaron) for the very useful dnd_character python library
* [kevin macleod](https://incompetech.com/music/royalty-free/music.html) for producing a lot of beautiful royalty free music

# NOTES:
* Set visual studio code editor ruler at 120 for correct line breaking, two lines for dialogue.
* For Android builds: put the dnd_character python library folder inside "renpy-8.2.1-sdk\lib\python3.*" so that the Renpy Android packager can properly add it among the python libraries that will be packaged in the APK file. Do not put it inside the "game" directory, otherwise the build will search it there during execution but will not find the json cache files inside, because for some reasons they are not packaged together with it, returning an error.
