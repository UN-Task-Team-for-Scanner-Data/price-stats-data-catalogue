# Contributing to the catalogue

If you have a dataset that you would like to register on the catalogue, the following process outlines how to do this.

# Before you start

## Requirements to contribute to the data catalogue

In order to contribute to the catalogue, the following criteria must be met:

-   **The dataset must be real.** We recommend that synthetic not be registered in the dataset but instead the code that generated it be made publicly available as part of that research projects' [research compendium](https://un-task-team-for-scanner-data.github.io/reproducibility-project/docs/reproducibility-guidance/intro.html).
-   **The dataset must be publicly available for researchers**. There are proprietary datasets that could in theory also be listed, however until the price statistics reproducibility project figures out the process for this, we request that only fully open datasets are registered. We woulds till love to hear from you if you have a valuable proprietary dataset that should be registered, however we will not register it until we flush out this process.
-   T**he dataset must be related to the price statistics discipline**. Price statisticians most typically track change in prices, such as through price index methods - thus the dataset should support this use case. Other use cases, such as for machine learning applications when it comes to classification, can also be submitted, but should be as close to the needs of the discipline as possible.
-   **Be of value to the discipline**. Many data catalogues that are too loose with the registration process become filled with many datasets of incremental value. As a result, users start to struggle to find highly valuable datasets among the smaller and incremental ones, which eventually causes the catalogue to be unused and thus of little value. To avoid this, the value of the dataset to researchers in the discipline should be clearly and sufficiently outlined.
-   **The contributor must document the dataset in full when the dataset is to be registered**. Having partially documented datasets on the catalogue will take away from user experience and will thus takeaway from the push to be open.

## Where to host the dataset

As the price statistics data catalogue describes datasets already hosted elsewhere (in other words it is not a data repository), the first step is to host the dataset somewhere. This is fundamentally up to the researcher and the institution they work at. Ideally a data repository is used that mints a Digitial Object Identifier (DOI) so that the dataset can be easily cited and found. Data repositories often allow a researcher to host private datasets and lock down access but still create a DOI. Regardless of where, the DOI should be ready when the dataset is registered in the catalogue so that researchers can find the dataset itself and know how to cite the dataset.

Read more about [data repositories in the Turing Way](https://book.the-turing-way.org/reproducible-research/rdm/rdm-repository#rr-rdm-repository-select).

# How to register a dataset on the catalogue?

The catalogue uses the open-source python package [`datacontract-cli`](https://cli.datacontract.com/) to render the simple to use static site. Each dataset is stored as a `yaml` file following the structure of this package is saved in the `/datasets/` directory of this GitHub repository. Contributors have the following options:

### Request to add a new dataset yourself (or modify a dataset that exists):

The best way is to directly propose a dataset and start the process of registering it (such as by fully describing the dataset).

1.  Fork [the catalogue repo](https://github.com/UN-Task-Team-for-Scanner-Data/price-stats-data-catalogue) and mock up a new dataset in the `/datasets/` directory of your fork.
2.  Submit a PR to request that we add it to the catalogue. Please tag it to the [dataset](https://github.com/UN-Task-Team-for-Scanner-Data/price-stats-data-catalogue/labels/dataset) label.
3.  We will review your request and coordinate with you as appropriate (such as if we need more info) or help further flush out the metadata so that the dataset is well defined before it is published.

When we are ready, we will either merge your PR and thus register your dataset or reject the dataset if it is not appropriate.

### Request that we add a new dataset:

You could also just give us a ping to let us know that a good dataset exists and we can review and register it when we get a chance.

1.  Create [a new issue](https://github.com/UN-Task-Team-for-Scanner-Data/price-stats-data-catalogue/issues/new) and describe the dataset you wish that we register. Include the relevant details that we can use to find out more about the dataset. Please also tag the issue with the [dataset](https://github.com/UN-Task-Team-for-Scanner-Data/price-stats-data-catalogue/labels/dataset) label.