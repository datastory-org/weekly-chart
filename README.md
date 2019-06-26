[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/datastory-org/weekly-chart/master?urlpath=%2Flab%2Ftree%2Fnotebooks)

# Datastory Weekly Chart
This repository contains data and analysis for the [Datastory Weekly Charts](https://datastory.org/sv/veckans-graf) which are posted on Datastory.org and on social media.

## Run the code in the cloud
The Jupyter notebooks within this repository can be run using mybinder.org, just
press the 'launch: binder' button above.

## Installation
To work with the notebooks on your own computer, we recommend to [download and
install Python as part of the anaconda
distribution](https://www.anaconda.com/distribution/). That way, you get `git`
to fetch the source code from this repository and Jupyter installed for you.

To install the Python dependencies required for this project, do the following
from a terminal or command prompt.

```sh
# get the content of this git repository
git clone https://github.com/datastory-org/weekly-chart

# enter the weekly-chart directory
cd weekly-chart

# install pipenv (https://pipenv.readthedocs.io)
pip install pipenv

# install the Python dependencies from the Pipfile
pipenv install

# enter the environment
pipenv shell

# start jupyter lab to work with the notebooks
jupyter lab
```

> **NOTE:** You also need [ImageMagick](https://imagemagick.org) to generate
> GIFs, see their instructions on how to install it.

## Data
Data is collected from a variety of sources. Each notebook contains a source reference and a date for when the data was originally obtained.

## Licensing and use

- **Open source:** All code in this repository is available under the [MIT License](https://github.com/datastory-org/weekly-chart/blob/master/LICENSE).

- **Attribution:** If you adapt and republish the charts in this repository, the following attribution should be visible in close proximity to the graphics: "Inspiration via datastory.org". Datastory.org charts are generally available under [CC-BY License](https://creativecommons.org/licenses/by-sa/3.0/).

- **The Datastory Brand:** The Logo of Datastory and any other product names, trademarks or service marks are proprietary and are protected by applicable trademark and copyright laws. Nothing contained in this code base should be construed as granting any license or right to use any of the Datastory Marks without the express written permission of the owner of such Marks.

## Styling
To adjust the style of the plots, modify `assets/datastory.mplstyle`.

Unfortunately, some styling options are not customizable via stylesheets and have to be configured in code, which is what the `ds_plot` (in src/plot) function is for. Whenever possible, initialize your plots with the command `fig, ax = ds_plot()` and all basic styling should be set up appropriately.

