# Project: 0x04. Loops, Conditions, and Parsing

## Description

This directory contains a series of scripts that demonstrate the use of loops, conditions, and parsing in shell scripting. These scripts are designed to help users understand and practice fundamental shell operations related to control flow, conditional statements, and text parsing.

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Additional Notes](#additional-notes)

## Resources

### Read or watch

- [The for loop](https://www.gnu.org/software/bash/manual/html_node/Looping-Constructs.html)
- [Variable assignment and arithmetic](https://tldp.org/LDP/abs/html/ops.html)
- [Comparison operators](https://tldp.org/LDP/abs/html/comparison-ops.html)
- [File test operators](https://tldp.org/LDP/abs/html/fto.html)
- [Make your scripts portable](https://www.cyberciti.biz/tips/finding-bash-shell-portable-code.html)

## Learning Objectives

### General

- How to create SSH keys
- What is the advantage of using `#!/usr/bin/env bash` over `#!/bin/bash`
- How to use `while`, `until`, and `for` loops
- How to use `if`, `else`, `elif`, and `case` condition statements
- How to use the `cut` command
- What are file and other comparison operators, and how to use them

## Tasks

| Task                            | Description                                                                                                                                                         | File                                                             |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| 0. Create a SSH RSA key pair    | Create a SSH RSA key pair                                                                                                                                           | [0-RSA_public_key.pub](./0-RSA_public_key.pub)                   |
| 1. For Best School loop         | Write a script that displays `Best School` 10 times using a `for` loop                                                                                              | [1-for_best_school](./1-for_best_school)                         |
| 2. While Best School loop       | Write a script that displays `Best School` 10 times using a `while` loop                                                                                            | [2-while_best_school](./2-while_best_school)                     |
| 3. Until Best School loop       | Write a script that displays `Best School` 10 times using an `until` loop                                                                                           | [3-until_best_school](./3-until_best_school)                     |
| 4. If 9, say Hi!                | Write a script that displays `Best School` 10 times, but for the 9th iteration, displays `Hi` instead                                                               | [4-if_9_say_hi](./4-if_9_say_hi)                                 |
| 5. 4 bad luck, 8 is your chance | Write a script that loops from 1 to 10 and displays `bad luck` for the 4th iteration, `good luck` for the 8th iteration, and `Best School` for the other iterations | [5-4_bad_luck_8_is_your_chance](./5-4_bad_luck_8_is_your_chance) |
| 6. Superstitious numbers        | Write a script that displays numbers from 1 to 20 and labels them as `bad luck` for 4, `good luck` for 8, and `Best School` for 12                                  | [6-superstitious_numbers](./6-superstitious_numbers)             |
| 7. Clock                        | Write a script that displays the time for 12 hours and 59 minutes                                                                                                   | [7-clock](./7-clock)                                             |
| 8. For ls                       | Write a script that lists files in the current directory                                                                                                            | [8-for_ls](./8-for_ls)                                           |
| 9. To file, or not to file      | Write a script that gives information about the `school` file                                                                                                       | [9-to_file_or_not_to_file](./9-to_file_or_not_to_file)           |
| 10. FizzBuzz                    | Write a script that displays numbers from 1 to 100, replacing multiples of 3 with `Fizz`, multiples of 5 with `Buzz`, and multiples of both with `FizzBuzz`         | [10-fizzbuzz](./10-fizzbuzz)                                     |
| 11. Read and cut                | Write a script that displays the content of the `/etc/passwd` file, but only the username, user id, and home directory fields                                       | [100-read_and_cut](./100-read_and_cut)                           |
| 12. Tell the story of passwd    | Write a script that displays the content of the `/etc/passwd` file, but only the username, user id, and home directory fields, sorted by user id                    | [101-tell_the_story_of_passwd](./101-tell_the_story_of_passwd)   |
| 13. Let's parse Apache logs     | Write a script that parses an Apache log file and displays the IP addresses that made requests to the server                                                        | [102-lets_parse_apache_logs](./102-lets_parse_apache_logs)       |
| 14. Dig the data                | Write a script that parses an Apache log file and displays the IP addresses that made requests to the server, sorted by the number of requests                      | [103-dig_the-data](./103-dig_the-data)                           |

## Additional Notes

- Ensure you have the necessary permissions to execute the scripts.
- Test the scripts in a safe environment to avoid any unintended changes to your system.
- Refer to the resources provided for a deeper understanding of each command and its options.
