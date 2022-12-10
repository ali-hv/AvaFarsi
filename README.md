<p align="center">
<img width="100" src="https://raw.githubusercontent.com/Ali-Hosseinverdi/Music-downloader/main/resources/ui/widgets_img/app_icon.ico">
<h2 align="center">AvaFarsi</h2>
</p>

<p align="center">
<img alt="windows" src="https://img.shields.io/badge/windows-red?style=flat&logo=windows">
<img alt="linux" src="https://img.shields.io/badge/Linux-red?style=flat&logo=linux">
<img alt="gpl-3.0" src="https://img.shields.io/badge/License-GPL%203.0-blue.svg">
<img alt="python" src="https://img.shields.io/badge/Made%20with-Python%203.8-green.svg?logo=python">
<img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/Ali-Hosseinverdi/AvaFarsi?color=purple">
</p>

<p align="center"><kbd><img src="https://raw.githubusercontent.com/Ali-Hosseinverdi/Music-downloader/main/screenshots/menu_img.png"></kbd></p>

**AvaFarsi** is an open-source graphical app which helps you to find and download the songs of iranian singers easily. This app downloads songs from the [upmusics](https://upmusics.com) and [music-fa](https://music-fa.com) sites.

## Table of contents

* [Features](#features)
* [Overview](#overview)
* [Installation](#installation)
  + [Windows](#windows)
  + [Linux](#linux)
  + [Other operating systems](#other-operating-systems)
* [Contributing](#contributing)
* [License](#license)

## Features

<p align="center"><kbd><img src="https://raw.githubusercontent.com/Ali-Hosseinverdi/Music-downloader/main/screenshots/inside_img.png"></kbd></p>

AvaFarsi provides the following features:

- Download song by giving the name of the singer
- Download song by giving the name of the song
- Download song by giving the text of a part of the song
- Download all the songs at once
- Download a certain number of songs by giving a number

## Overview

AvaFarsi doesn't have any host and database of songs for himself and it just crawl the music sites to get the songs link and names.

## Installation

### Windows
Just download the setup file from [here](https://github.com/Ali-Hosseinverdi/AvaFarsi/releases/download/2.0.0/AvaFarsi-2.0.0.exe) and install the program.

### Linux
First of all, make sure you have python3 and pip and git installed. Then open your terminal and enter the following commands in order:

``` bash
git clone https://github.com/Ali-Hosseinverdi/AvaFarsi.git
cd AvaFarsi
pip3 install -r requirements.txt
chmod +x install
sudo ./install
```

Now you can run the AvaFarsi from your apps menu or you can just enter the app name in your terminal:
```
avafarsi
```

### Other operating systems
On other Unix-based operating systems such as Mac, the installation steps on linux should install the program just fine. But I didn't test it so if it doesn't install properly, create an issue and tell me your OS and some details.

## Contributing

if you can imporve this program with adding a new feature or if you found a bug in this program or even if you have an idea that can make this app better, just send a pull-request or create an issue.
You can also send me an email:<br>
[alihv5000@gmail.com](mailto:alihv5000@gmail.com)

## License

[GPL-3.0](https://github.com/Ali-Hosseinverdi/AvaFarsi/blob/main/LICENSE)
