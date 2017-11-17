# Project Title

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
Please be sure to download the latest version of Firefox geckodriver. In linux, this could be done by copying the extracted geckodriver file and copying it into the `/usr/local/bin/` folder.


If you do not have pip installed, the linux command for installing it is:



```
sudo apt-get install python-pip
```

The python packages we will be using in this script are Selenium and pyvirutaldisplay. Selenium powers the whole web scraping process, and pyvirtualdisplay allows the script to run headless (for ssh and performance reasons).
These are installed by running
```
pip install selenium`
```
and
```
pip install pyvirtualdisplay
```

you also need to run


### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
