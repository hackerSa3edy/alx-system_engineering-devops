# Project: 0x16. API Advanced

## Description

This project focuses on advanced concepts and techniques for working with APIs (Application Programming Interfaces). APIs allow different software systems to communicate with each other. This project provides hands-on experience with making API requests, handling responses, working with pagination, and performing recursive API calls.

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Additional Notes](#additional-notes)

## Resources

### Read or watch

- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [Query String](https://en.wikipedia.org/wiki/Query_string)
- [REST API Tutorial](https://restfulapi.net/)
- [JSON Data Format](https://www.json.org/json-en.html)
- [Python Requests Library](https://docs.python-requests.org/en/latest/)

## Learning Objectives

### General

- How to read API documentation to find the endpoints you’re looking for
- How to use an API with pagination
- How to parse JSON results from an API
- How to make a recursive API call
- How to sort a dictionary by value

## Tasks

| Task              | Description                                                                                                                                      | File                           |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------ |
| 0. How many subs? | Write a Python script that queries the Reddit API and returns the number of subscribers for a given subreddit                                    | [0-subs.py](./0-subs.py)       |
| 1. Top Ten        | Write a Python script that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit                   | [1-top_ten.py](./1-top_ten.py) |
| 2. Recurse it!    | Write a recursive Python function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit | [2-recurse.py](./2-recurse.py) |
| 3. Count it!      | Write a recursive Python function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords | [100-count.py](./100-count.py) |

## Additional Notes

- Ensure you have the necessary permissions to execute the scripts.
- Test the scripts in a safe environment to avoid any unintended changes to your system.
- Refer to the resources provided for a deeper understanding of each concept and its practical applications.
- Regularly review and update your scripts to maintain compatibility with the latest API changes.
