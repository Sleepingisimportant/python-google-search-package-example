# Google Search Query Script

## Overview

This script performs a Google search for a specified query and retrieves a specified number of search result URLs. The results are saved in a CSV file, where each URL is associated with a key consisting of the query and the current date.

## Requirements

The following Python libraries are requiredt:
```
pip install pandas googlesearch-python
```


# How the Script Works
## Define Search Query:
You specify the item or phrase you want to search for by modifying the query variable (e.g., "3M Scotch Super 88").

## Specify Number of Results:
Modify the countResult variable to set how many Google search results you want to retrieve (e.g., 60).

## Perform Google Search:
The script performs a Google search and retrieves the URLs for the search results. The number of URLs retrieved is controlled by the countResult variable.

## Save Results to CSV:
The results are saved into a CSV file with a name based on the query and the current date. The CSV file contains the URLs of the search results.





