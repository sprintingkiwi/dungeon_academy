A 5E compatible Visual Novel prototype realized with Ren'Py and AI-generated graphics

Releases can be found on [my Itch.io channel](https://sprintingkiwi.itch.io/)

Graphics realized with Stable Diffusion

# LICENSES:
* The **code** is under GNU GPL 3 License, except for the content of the [sheet_5e folder](sheet_5e/) which is a fork of [this project](https://github.com/tassaron/dnd-character) by [tassaron](https://github.com/tassaron), and it comes with its own license.
* The **images, the story and the characters** are licensed [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/)
* Credits and licenses for the **audio** files are specified inside the [audio folder](game/audio/)
* This work includes material taken from the System Reference Document 5.1 (“SRD 5.1”) by Wizards of the Coast LLC and available at https://dnd.wizards.com/resources/systems-reference-document. The SRD 5.1 is licensed under the Creative Commons Attribution 4.0 International License available at https://creativecommons.org/licenses/by/4.0/legalcode.
* The [Creative Commons Attribution 4.0 International License (“CC-BY-4.0”)](SRD_CC_v5.1.pdf) mainly refers to the content of the [json_cache folder](json_data_5e/) and the content of [SRD5_system.rpy file](game/SRD5_system.rpy) which implements game mechanics heavily inspired by the SRD5 document. For more informations, please refer to this page: https://www.dndbeyond.com/resources/1781-systems-reference-document-srd

# CREDITS:
A special thanks to:
* [tassaron](https://github.com/tassaron) for the very useful python library to manage 5e characters sheets
* [kevin macleod](https://incompetech.com/music/royalty-free/music.html) for producing a lot of beautiful royalty free music

# NOTES:
* Set visual studio code editor ruler at 120 for correct line breaking, two lines for dialogue.
* For Android builds: put the sheet_5e and json_data_5e folders inside "renpy-8.2.1-sdk\lib\python3.*" so that the Renpy Android packager can properly add it among the python libraries that will be packaged in the APK file. Do not put it inside the "game" directory, otherwise the build will search it there during execution but will not find the json cache files inside, because for some reasons they are not packaged together with it, returning an error.
