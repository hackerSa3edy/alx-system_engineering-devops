# Project: 0x06. Regular Expressions

## Description

This directory contains a series of scripts that demonstrate the use of regular expressions (regex) in various programming tasks. Regular expressions are powerful tools for pattern matching and text manipulation. These scripts are designed to help users understand and practice fundamental operations related to regex, including matching, searching, and replacing text patterns.

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Additional Notes](#additional-notes)

## Resources

### Read or watch

- [Regular Expressions - Basics](https://www.regular-expressions.info/tutorial.html)
- [Regular Expressions - Advanced](https://www.regular-expressions.info/advanced.html)
- [Rubular - A Ruby-based Regular Expression Editor](https://rubular.com/)
- [Regular Expressions 101](https://regex101.com/)
- [Learn Regex with Simple, Interactive Exercises](https://regexone.com/)

## Learning Objectives

### General

- Understand the basic concepts of regular expressions
- Learn how to use regular expressions for pattern matching
- Understand how to use regular expressions for searching and replacing text
- Learn how to use regular expressions in different programming languages
- Understand the syntax and structure of regular expressions

## Tasks

| Task                         | Description                                                                                                                                                                                                                          | File                                                             |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| 0. Simply matching School    | Write a Ruby script that accepts one argument and passes it to a regular expression matching method. The regular expression must match the word "School".                                                                            | [0-simply_match_school.rb](./0-simply_match_school.rb)           |
| 1. Repetition Token #0       | Write a Ruby script that accepts one argument and passes it to a regular expression matching method. The regular expression must match the pattern `hbt{2,5}n`.                                                                      | [1-repetition_token_0.rb](./1-repetition_token_0.rb)             |
| 2. Repetition Token #1       | Write a Ruby script that accepts one argument and passes it to a regular expression matching method. The regular expression must match the pattern `hb?tn`.                                                                          | [2-repetition_token_1.rb](./2-repetition_token_1.rb)             |
| 3. Repetition Token #2       | Write a Ruby script that accepts one argument and passes it to a regular expression matching method. The regular expression must match the pattern `hbt+n`.                                                                          | [3-repetition_token_2.rb](./3-repetition_token_2.rb)             |
| 4. Repetition Token #3       | Write a Ruby script that accepts one argument and passes it to a regular expression matching method. The regular expression must match the pattern `hbt*n`.                                                                          | [4-repetition_token_3.rb](./4-repetition_token_3.rb)             |
| 5. Not quite HBTN yet        | Write a Ruby script that accepts one argument and passes it to a regular expression matching method. The regular expression must match a string that starts with `h` and ends with `n` and can have any single character in between. | [5-beginning_and_end.rb](./5-beginning_and_end.rb)               |
| 6. Call me maybe             | Write a Ruby script that accepts one argument and passes it to a regular expression matching method. The regular expression must match a 10-digit phone number.                                                                      | [6-phone_number.rb](./6-phone_number.rb)                         |
| 7. OMG WHY ARE YOU SHOUTING? | Write a Ruby script that accepts one argument and passes it to a regular expression matching method. The regular expression must match only uppercase letters.                                                                       | [7-OMG_WHY_ARE_YOU_SHOUTING.rb](./7-OMG_WHY_ARE_YOU_SHOUTING.rb) |
| 8. Textme                    | Write a Ruby script that accepts one argument and passes it to a regular expression matching method. The script should output: `[SENDER],[RECEIVER],[FLAGS]` where each part is extracted from the argument string.                  | [100-textme.rb](./100-textme.rb)                                 |

## Additional Notes

- Ensure you have the necessary permissions to execute the scripts.
- Test the scripts in a safe environment to avoid any unintended changes to your system.
- Refer to the resources provided for a deeper understanding of each command and its options.
- Regularly practice writing and testing regular expressions to improve your proficiency.
