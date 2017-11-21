# PGE Bill Fetcher
_Note: this is an older project and will be ported to Python 3 at a later date_

This script was developed as a stop-gap solution to download and archive PG&E bills for all of my university's properties while I get the OAuth credentials secured to use PG&E's official API to pull data.

## Usage

This script is meant to be run on a server on a scheduled basis, with little regard to performance. This iteration of the script is made to download historical data too (not just the current bill), so if your intention is to only fetch the latest bill, I may create a modified version of this script that only downloads the current bill.

However, this would also require the user to store their password somehow, which isn't the most secure thing to do. For now it's best that the user ssh into the server they're running the script on and run it manually every so often (about once or twice a month should be enough).

This script is self-contained so long as you specify the appropriate folder names in the script so it could really be run from just about anywhere.


### Prerequisites

This script has a few dependencies that need to be installed.


```
sudo apt-get install xvfb
```
Please be sure to download the latest version of Firefox geckodriver and set it in PATH. In Linux, this could be done by copying the extracted geckodriver file and copying it into the `/usr/local/bin/` folder.


If you do not have pip installed, the linux command for installing it is:



```
sudo apt-get install python-pip
```

The python packages we will be using in this script are Selenium and pyvirutaldisplay. Selenium powers the whole web scraping process, and pyvirtualdisplay allows the script to run headless (for ssh and performance reasons).
These are installed by running  
```
pip install selenium
```
and
```
pip install pyvirtualdisplay
```


### Usage

