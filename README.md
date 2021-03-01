# Python sudoku puzzle collector

This script is just a simple code which uses python selenium to collect specified number images which contain sudoku puzzles.

<br>

## Install the required python packages: 

In order to install the python packages, you just need to run the command bellow:

```bash
pip install -r requirements.txt
```
<br>

## Install selenium driver for firefox
to install the driver of selenium which is used for firefox browser. You can download and install other appropriate drivers to use other browsers.


```bash
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
```
Extract the file with:

```bash
tar -xvzf geckodriver:
```
Make it executable:

```bash
chmod +x geckodriver
```
Add the driver to your PATH so other tools can find it:
```bash
export PATH=$PATH:/path-to-extracted-file/.
```

