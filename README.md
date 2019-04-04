# Datastory Weekly Chart
This repository contains data and analysis for the [Datastory Weekly Charts](https://datastory.org/sv/veckans-graf) which are posted on Datastory.org and on social media.

## Installation

To run the notebooks, you need to install the packages listed in the `Pipfile`. The easiest way is to use [Pipenv](https://pipenv.readthedocs.io/en/latest/): `pipenv install`. This will install all dependencies as well as the local `src` package that contain some utility functions that are used in various notebooks.

An additional dependency (ImageMagick) is needed to generate GIFs. Please refer to the ImageMagick website for installation documentation.

## Data
Data is collected from a variety of sources. Each notebook contains a source reference and a date for when the data was originally obtained.

## Licensing and use

- **Open source:** All code in this repository is available under the [MIT License](https://github.com/datastory-org/weekly-chart/blob/master/LICENSE).

- **Attribution:** If you adapt and republish the charts in this repository, the following attribution should be visible in close proximity to the graphics: "Inspiration via datastory.org". Datastory.org charts are generally available under [CC-BY License](https://creativecommons.org/licenses/by-sa/3.0/).

- **The Datastory Brand:** The Logo of Datastory and any other product names, trademarks or service marks are proprietary and are protected by applicable trademark and copyright laws. Nothing contained in this code base should be construed as granting any license or right to use any of the Datastory Marks without the express written permission of the owner of such Marks.

## Styling
To create your own style, make a copy of the `assets/datastory.mplstyle` stylesheet to the location of your local matplotlib configuration directory (which can be found with `matplotlib.get_configdir()`). Assuming the config dir is located at `~/.matplotlib/`, move the stylesheet to `~/.matplotlib/stylelib/your-name.mplstyle`. Now you can use `plt.style.use("your-style")` to create custom styled charts.

Unfortunately, some styling options are not customizable via stylesheets and have to be configured in code, which is what the `ds_plot` (in src/plot) function is for. Whenever possible, initialize your plots with the command `fig, ax = ds_plot()` and all basic styling should be set up appropriately.

