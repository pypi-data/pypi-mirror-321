[![Notebooker](https://raw.githubusercontent.com/man-group/notebooker/master/docs/images/notebooker_cropped.jpg)](https://notebooker.readthedocs.io/en/latest/)

Productionise and schedule your Jupyter Notebooks, just as interactively as you wrote them. Notebooker is a webapp which can execute and parametrise Jupyter Notebooks as soon as they have been committed to git. The results are stored in MongoDB and searchable via the web interface, essentially turning your Jupyter Notebook into a production-style web-based report in a few clicks.


[![CircleCI](https://dl.circleci.com/status-badge/img/gh/man-group/notebooker/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/man-group/notebooker/tree/master)
[![Documentation Status](https://readthedocs.org/projects/notebooker/badge/?version=latest)](https://notebooker.readthedocs.io/en/latest/?badge=latest)

## Run a Jupyter notebook as a report with parameters
![Screenshot of "Run A Report" dialog](https://raw.githubusercontent.com/man-group/notebooker/master/docs/images/nbkr_run_report.png)

## Execute Jupyter notebooks either on the webservice or command line
![Screenshot of Executing a notebook](https://raw.githubusercontent.com/man-group/notebooker/master/docs/images/nbkr_running_report.png)

## View the output of notebooks as static HTML
![Screenshot of some notebook results](https://raw.githubusercontent.com/man-group/notebooker/master/docs/images/nbkr_results.png)

## All results are accessible from the home page
![Screenshot of the Notebooker homepage](https://raw.githubusercontent.com/man-group/notebooker/master/docs/images/nbkr_homepage.png)

## Drill down into each template's results
![Screenshot of result listings](https://raw.githubusercontent.com/man-group/notebooker/master/docs/images/nbkr_results_listing.png)


## Getting started
See the documentation at [https://notebooker.readthedocs.io/](https://notebooker.readthedocs.io/) for installation instructions.

Notebooker has been tested on Linux, Windows 10, and OSX; the webapp has been tested on Google Chrome.

If you want to explore an example right away, you can use docker-compose:
```sh
cd docker
docker-compose up
```
That will expose Notebooker at http://localhost:8080/ with the example templates.

# Contributors
Notebooker has been actively maintained at Man Group since late 2018, with the original concept built by 
[Jon Bannister](https://github.com/jonbannister). 
It would not have been possible without contributions from:

* [Douglas Bruce](https://github.com/douglasbruce88)
* [Franek Jemiolo](https://github.com/FranekJemiolo)
* [Sam Ratcliff](https://github.com/sparks1372)
* [Matthew Dodds](https://github.com/doddsiedodds)
* [Dominik Christ](https://github.com/DominikMChrist)

And these fantastic projects:

* [Jupytext](<https://github.com/mwouts/jupytext>)
* [papermill](<https://github.com/nteract/papermill>)
* [nbconvert](<https://github.com/jupyter/nbconvert>)
* [Fomantic-UI](<https://github.com/fomantic/Fomantic-UI>)




