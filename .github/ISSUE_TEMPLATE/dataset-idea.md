---
name: Dataset idea
about: Template to walk a person through documenting a new dataset idea
title: IDEA
labels: ''
assignees: sergegoussev
body:
- type: markdown
  attributes:
    value: |
      Thank you for telling us about a new idea for the catalogue! 
- type: input
  id: dataset-name
  attributes:
    label: Dataset Name
    description: First off, how would you name this dataset?
    placeholder: ex. ABC-country-scanner-grocery-dataset
  validations:
    required: false
- type: textarea
  id: dataset-description
  attributes:
    label: Tell us a bit about the dataset
    description: Cover anything that would help someone underststand the dataset from a few sentences. 
    placeholder: Full scanner dataset from country ABC
  validations:
    required: true
- type: dropdown
  id: dataset-type
  attributes:
    label: Dataset type
    description: How would you categorize the dataset?
    options:
      - web scraped dataset
      - scanner dataset
      - administrative dataset
      - field/survey dataset
      - other (specify below)
  validations:
    required: true
---
