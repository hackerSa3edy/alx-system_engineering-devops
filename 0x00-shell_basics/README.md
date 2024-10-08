# 0x00-shell_basics

## Description

This directory contains a series of scripts that demonstrate basic shell commands and their usage. These scripts are designed to help users understand and practice fundamental shell operations, including navigation, file manipulation, and system information retrieval.

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Additional Notes](#additional-notes)

## Resources

### Read or watch

- [Linux Command Line Basics](https://www.learnlinux.org/en/Command_Line)
- [Introduction to Shell](https://www.geeksforgeeks.org/introduction-to-shell/)
- [Shell Scripting Tutorial](https://www.shellscript.sh/)

## Learning Objectives

### General

- Understand the basic concepts of the shell
- Navigate the file system using shell commands
- Manipulate files and directories
- Use common shell utilities and commands
- Understand and use shell scripting basics

## Tasks

| Task                                        | Description                                                                                                                                                                                                                                             | File                                                         |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| 0. Where am I?                              | Print the absolute path name of the current working directory                                                                                                                                                                                           | [0-current_working_directory](./0-current_working_directory) |
| 1. What’s in there?                         | Display the contents list of your current directory                                                                                                                                                                                                     | [1-listit](./1-listit)                                       |
| 2. There is no place like home              | Change the working directory to the user’s home directory                                                                                                                                                                                               | [2-bring_me_home](./2-bring_me_home)                         |
| 3. The long format                          | Display current directory contents in a long format                                                                                                                                                                                                     | [3-listfiles](./3-listfiles)                                 |
| 4. Hidden files                             | Display current directory contents, including hidden files                                                                                                                                                                                              | [4-listmorefiles](./4-listmorefiles)                         |
| 5. I love numbers                           | Display current directory contents with user and group IDs displayed numerically                                                                                                                                                                        | [5-listfilesdigitonly](./5-listfilesdigitonly)               |
| 6. Welcome                                  | Create a directory named `my_first_directory` in the `/tmp/` directory                                                                                                                                                                                  | [6-firstdirectory](./6-firstdirectory)                       |
| 7. Betty in my first directory              | Move the file `betty` from `/tmp/` to `/tmp/my_first_directory`                                                                                                                                                                                         | [7-movethatfile](./7-movethatfile)                           |
| 8. Bye bye Betty                            | Delete the file `betty`                                                                                                                                                                                                                                 | [8-firstdelete](./8-firstdelete)                             |
| 9. Bye bye My first directory               | Delete the directory `my_first_directory` that is in the `/tmp` directory                                                                                                                                                                               | [9-firstdirdeletion](./9-firstdirdeletion)                   |
| 10. Back to the future                      | Change the working directory to the previous one                                                                                                                                                                                                        | [10-back](./10-back)                                         |
| 11. Lists                                   | List all files (even ones with names beginning with a period character) in the current directory and the parent of the working directory and the `/boot` directory (in this order), in long format                                                      | [11-lists](./11-lists)                                       |
| 12. File type                               | Print the type of the file named `iamafile`                                                                                                                                                                                                             | [12-file_type](./12-file_type)                               |
| 13. We are symbols, and inhabit symbols     | Create a symbolic link to `/bin/ls`, named `__ls__`                                                                                                                                                                                                     | [13-symbolic_link](./13-symbolic_link)                       |
| 14. Copy HTML files                         | Copy all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory | [14-copy_html](./14-copy_html)                               |
| 15. Let’s move                              | Move all files beginning with an uppercase letter to the directory `/tmp/u`                                                                                                                                                                             | [100-lets_move](./100-lets_move)                             |
| 16. Clean Emacs                             | Delete all files in the current working directory that end with the character `~`                                                                                                                                                                       | [101-clean_emacs](./101-clean_emacs)                         |
| 17. Tree                                    | Create the directories `welcome/`, `welcome/to/`, and `welcome/to/school` in the current directory                                                                                                                                                      | [102-tree](./102-tree)                                       |
| 18. Life is a series of commas, not periods | List all the files and directories of the current directory, separated by commas (`,`), including hidden files, but excluding the current and parent directories. The listing should be in alphabetical order, with directories listed first            | [103-commas](./103-commas)                                   |

## Additional Notes

- Ensure you have the necessary permissions to execute the scripts.
- Test the scripts in a safe environment to avoid any unintended changes to your system.
- Refer to the resources provided for a deeper understanding of each command and its options.
