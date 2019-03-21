# Datastory Weekly Chart
This repository contains data and analysis for the [Datastory Weekly Charts](https://datastory.org/sv/veckans-graf) which are posted on Datastory.org and on social media.

## Installation

To run the notebooks, you need to install the packages listed in the `Pipfile`. The easiest way is to use [Pipenv](https://pipenv.readthedocs.io/en/latest/): `pipenv install`. This will install all dependencies as well as the local `src` package that contain some utility functions that are used in various notebooks.

An additional dependency (ImageMagick) is needed to generate GIFs. Please refer to the ImageMagick website for installation documentation.

## Data
Data is collected from a variety of sources. Each notebook contains a source reference and a date for when the data was originally obtained.

# Styling
In order to use `plt.style.use("datastory")`, you need to move the `assets/datastory.mplstyle` stylesheet to the location of your local matplotlib configuration directory (which can be found with `matplotlib.get_configdir()`). Assuming the config dir is located at `~/.matplotlib/`, move the stylesheet to `~/.matplotlib/stylelib/datastory.mplstyle`.

Unfortunately, some styling options are not customizable via stylesheets and have to be configured in code, which is what the `ds_plot` (in src/plot) function is for. Whenever possible, initialize your plots with the command `fig, ax = ds_plot()` and all basic styling should be set up appropriately.

## Licensing
All code in this repository is available under the MIT License.