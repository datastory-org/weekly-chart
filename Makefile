.PHONY: init raw clean export copy test reports

##############################################################
# PHONY TARGETS                                              #
##############################################################

init:
	pipenv install

raw:
	# TODO: Add rule

clean:
	# TODO: Add rule

export: raw
	@jupyter nbconvert --execute \
	--ExecutePreprocessor.timeout=None \
	notebooks/exports/Exports.ipynb

	rm notebooks/exports/*.html

copy:
	# TODO: Add rule

test:
	python -m unittest

reports: notebooks/reports/*.ipynb
	jupyter nbconvert --to pdf $< --output-dir reports
