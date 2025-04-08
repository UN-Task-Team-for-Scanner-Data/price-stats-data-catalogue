# Contributing

## Requirements to contribute to the data catalogue

In order to contribute to the catalogue, the following criteria must be met:

-   The dataset must be real. We recommend that synthetic not be registered in the dataset but instead the code that generated it be made publicly available as part of that research projects' [research compendium](https://un-task-team-for-scanner-data.github.io/reproducibility-project/docs/reproducibility-guidance/intro.html).
-   The dataset must be publicly available for researchers. There are proprietary datasets that could in theory also be listed, however until the price statistics reproducibility project figures out the process for this, we request that only fully open datasets are registered. We woulds till love to hear from you if you have a valuable proprietary dataset that should be registered, however we will not register it until we flush out this process.
-   The dataset must be related to the price statistics discipline. Price statisticians most typically track change in prices, such as through price index methods - thus the dataset should support this use case. Other use cases, such as for machine learning applications when it comes to classification, can also be submitted, but should be as close to the needs of the discipline as possible.
-   Be of value to the discipline. Many data catalogues that are too loose with the registration process become filled with many datasets of incremental value. As a result, users start to struggle to find highly valuable datasets among the smaller and incremental ones, which eventually causes the catalogue to be unused and thus of little value. To avoid this, the value of the dataset to researchers in the discipline should be clearly and sufficiently outlined.
-   The contributor must document the dataset in full when the dataset is to be registered. Having partially documented datasets on the catalogue will take away from user experience and will thus takeaway from the push to be open.

## How to Contribute

The catalogue uses the open-source python package [`datacontract-cli`](https://cli.datacontract.com/) . Each dataset is stored as a `yaml` file following the structure of this package is saved in the `/datasets/` directory of this GitHub repository. Contributors have the following options:

### Request to add a new dataset yourself (or modify a dataset that exists):

1.  Fork the repo and mock up a new dataset in the `/datasets/` directory of your fork
2.  Submit a PR to request that we add it to the catalogue. Please tag it to the [dataset](https://github.com/UN-Task-Team-for-Scanner-Data/price-stats-data-catalogue/labels/dataset) label.
3.  We will review your request and coordinate with you as appropriate (such as if we need more info).

### Request that we add a new dataset:

1.  Create [a new issue](https://github.com/UN-Task-Team-for-Scanner-Data/price-stats-data-catalogue/issues/new) and describe the dataset you wish that we register. Include the relevant details that we can use to find out more about the dataset. Please also tag the issue with the [dataset](https://github.com/UN-Task-Team-for-Scanner-Data/price-stats-data-catalogue/labels/dataset) label.