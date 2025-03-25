# Price Statistics Data Catalogue

Welcome to the *Price Statistics Data Catalogue* project repository!

<p align="center">
  <a href="[url](https://un-task-team-for-scanner-data.github.io/price-stats-data-catalogue/)">
    <b>Browse the catalogue</b>
  </a>
</p>

<p align="center">[*Find out more about the project and how to register new datasets!*](https://un-task-team-for-scanner-data.github.io/reproducibility-project/docs/datasets-guidance/intro.html)</p>

# *Raison d'être*

## Status quo in the price statistics discipline

There are many datasets that researchers in the field price statistics can use to do empirical research. Specifically, they can use

1.  internal (such as to a National Statistical Office) datasets that only they and their colleagues have access to,
2.  proprietary datasets (i.e. available to researchers at a cost) that may be too expensive for other researchers to acquire, or
3.  openly available or public datasets.

If researchers use the first two types of datasets, *replicability* is a challenge for the discipline as others may not be able to easily get access to the same datasets to validate or replicate the results. Researchers who may wish to try to use the third type of datasets with the aim of making their research reproducible (or even [replicable, or robust](https://book.the-turing-way.org/reproducible-research/overview/overview-definitions#table-of-definitions-for-reproducibility)) may be dissuaded from trying if it is too challenging to find applicable datasets or if the datasets that are available are poorly documented, requiring researchers to document the dataset for others as part of their project. Our observation is that currently in the price statistics discipline, most research is done with internal or proprietary datasets for this reason.

## Purpose of the price statistics data catalogue

The aim of this data catalogue is to considerably simplify the process outlined above and make it easy to find and use open datasets in price statistics. Our hope is that with this process considerably simplified, more research will tend towards open datasets, allowing better reproducibility in the discipline. Thus the catalogue lists the main datasets that are availible within the discipline and describes how to download them, as well as outlines how they are structured to provide a common interface for researchers. We accept two types of datasets:

-   Open datasets that are available to others - includes datasets that are made available by various researchers or organizations for research purposes.
-   Proprietary but free datasets - includes datasets that are 'owned' by someone else but are summarized here so that they are easily discoverable to researchers.

## Note on this version of the catalogue

This data catalogue is a proof of concept. We are aiming to use this version to demonstrate the use and add value to the discipline. If this proves a success, we will look for a more permanent and powerful catalogue.

# Contributing a dataset:

To contribute a dataset to this catalogue, please submit either an issue to this repository outlining the dataset and why it should be added to the catalogue, or a pull request with the proposed changes for us to review and approve.

## Technical context

We are exploring the use of [data contract cli](https://cli.datacontract.com/) as a way to document and track datasets as the python library comes with a [data catalog](https://datacontract.com/examples/index.html).

## Who are we?

This project is led by a workstream of the [UN Task Team on Scanner and web scraped data](https://unstats.un.org/bigdata/task-teams/scanner/index.cshtml), a part of the [UN Committee of Experts on Big Data and Data Science for Official Statistics (UN-CEBD)](https://unstats.un.org/bigdata/about/index.cshtml). As part of the replicability project, our workstream is also working on a white paper on FAIR and reproducible research for price statistics.
