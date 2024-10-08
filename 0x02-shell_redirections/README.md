# 0x02-shell_redirections

## Description

This directory contains a series of scripts that demonstrate shell redirections and filters. These scripts are designed to help users understand and practice fundamental shell operations related to input/output redirection, piping, and text processing using various shell utilities.

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Additional Notes](#additional-notes)

## Resources

### Read or watch

- [Shell Redirections](https://www.gnu.org/software/bash/manual/html_node/Redirections.html)
- [Piping in Unix/Linux](https://www.geeksforgeeks.org/piping-in-unix-or-linux/)
- [Text Processing Commands](https://www.tecmint.com/12-awesome-linux-tools-for-every-linux-user/)
- [Understanding Shell Script](https://www.shellscript.sh/)

## Learning Objectives

### General

- Understand the basic concepts of input/output redirection
- Learn how to use pipes to connect multiple commands
- Understand how to use common text processing commands such as `cat`, `grep`, `cut`, `sort`, `uniq`, `awk`, and `sed`
- Learn how to create and execute shell scripts that utilize redirections and filters

## Tasks

| Task                                                               | Description                                                                                                                             | File                                             |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| 0. Hello World                                                     | Write a script that prints "Hello, World"                                                                                               | [0-hello_world](./0-hello_world)                 |
| 1. Confused smiley                                                 | Write a script that displays a confused smiley `"(Ôo)'`                                                                                 | [1-confused_smiley](./1-confused_smiley)         |
| 2. Let's display a file                                            | Display the content of the `/etc/passwd` file                                                                                           | [2-hellofile](./2-hellofile)                     |
| 3. What about 2?                                                   | Display the content of `/etc/passwd` and `/etc/hosts`                                                                                   | [3-twofiles](./3-twofiles)                       |
| 4. Last lines of a file                                            | Display the last 10 lines of `/etc/passwd`                                                                                              | [4-lastlines](./4-lastlines)                     |
| 5. I'd prefer the first ones actually                              | Display the first 10 lines of `/etc/passwd`                                                                                             | [5-firstlines](./5-firstlines)                   |
| 6. Line #2                                                         | Display the third line of the file `iacta`                                                                                              | [6-third_line](./6-third_line)                   |
| 7. It is a good file that cuts iron without making a noise         | Write a shell script that creates a file named exactly `\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)` containing the text `Best School`       | [7-file](./7-file)                               |
| 8. Save current state of directory                                 | Write a script that writes into the file `ls_cwd_content` the result of the command `ls -la`                                            | [8-cwd_state](./8-cwd_state)                     |
| 9. Duplicate last line                                             | Write a script that duplicates the last line of the file `iacta`                                                                        | [9-duplicate_last_line](./9-duplicate_last_line) |
| 10. No more javascript                                             | Write a script that deletes all the regular files with a `.js` extension in the current directory and all its subfolders                | [10-no_more_js](./10-no_more_js)                 |
| 11. Don't just count your directories, make your directories count | Write a script that counts the number of directories and sub-directories in the current directory                                       | [11-directories](./11-directories)               |
| 12. What’s new                                                     | Create a script that displays the 10 newest files in the current directory                                                              | [12-newest_files](./12-newest_files)             |
| 13. Being unique is better than being perfect                      | Create a script that takes a list of words as input and prints only words that appear exactly once                                      | [13-unique](./13-unique)                         |
| 14. It must be in that file                                        | Display lines containing the pattern "root" from the file `/etc/passwd`                                                                 | [14-findthatword](./14-findthatword)             |
| 15. Count that word                                                | Display the number of lines that contain the pattern "bin" in the file `/etc/passwd`                                                    | [15-countthatword](./15-countthatword)           |
| 16. What's next?                                                   | Display lines containing the pattern "root" and 3 lines after them in the file `/etc/passwd`                                            | [16-whatsnext](./16-whatsnext)                   |
| 17. I hate bins                                                    | Display all the lines in the file `/etc/passwd` that do not contain the pattern "bin"                                                   | [17-hidethisword](./17-hidethisword)             |
| 18. Letters only please                                            | Display all lines of the file `/etc/ssh/sshd_config` starting with a letter                                                             | [18-letteronly](./18-letteronly)                 |
| 19. A to Z                                                         | Replace all characters `A` and `c` from input to `Z` and `e` respectively                                                               | [19-AZ](./19-AZ)                                 |
| 20. Without C, you would live in hiago                             | Create a script that removes all letters `c` and `C` from input                                                                         | [20-hiago](./20-hiago)                           |
| 21. esreveR                                                        | Write a script that reverse its input                                                                                                   | [21-reverse](./21-reverse)                       |
| 22. DJ Cut Killer                                                  | Write a script that displays all users and their home directories, sorted by users                                                      | [22-users_and_homes](./22-users_and_homes)       |
| 23. Empty casks make the most noise                                | Write a command that finds all empty files and directories in the current directory and all sub-directories                             | [100-empty_casks](./100-empty_casks)             |
| 24. A gif is worth ten thousand words                              | Write a script that lists all the files with a `.gif` extension in the current directory and all its sub-directories                    | [101-gifs](./101-gifs)                           |
| 25. Acrostic                                                       | Create a script that decodes acrostics that use the first letter of each line                                                           | [102-acrostic](./102-acrostic)                   |
| 26. The biggest fan                                                | Write a script that parses web server logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests | [103-the_biggest_fan](./103-the_biggest_fan)     |

## Additional Notes

- Ensure you have the necessary permissions to execute the scripts.
- Test the scripts in a safe environment to avoid any unintended changes to your system.
- Refer to the resources provided for a deeper understanding of each command and its options.
