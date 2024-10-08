# 0x03-shell_variables_expansions

## Description

This directory contains a series of scripts that demonstrate shell variable usage and expansions. These scripts are designed to help users understand and practice fundamental shell operations related to variable assignment, arithmetic operations, and various types of expansions including parameter expansion, command substitution, and arithmetic expansion.

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Additional Notes](#additional-notes)

## Resources

### Read or watch

- [Shell Parameter Expansion](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html)
- [Shell Arithmetic](https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html)
- [Bash Variable Basics](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_02.html)
- [Bash Variable Expansion](https://tldp.org/LDP/abs/html/parameter-substitution.html)

## Learning Objectives

### General

- Understand the basic concepts of shell variables and expansions
- Learn how to assign values to variables
- Understand how to perform arithmetic operations in the shell
- Learn how to use parameter expansion to manipulate variable values
- Understand command substitution and how to use it in scripts
- Learn how to use arithmetic expansion for calculations

## Tasks

| Task                                                                                              | Description                                                                                                                                            | File                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| 0. alias                                                                                          | Create a script that creates an alias                                                                                                                  | [0-alias](./0-alias)                                       |
| 1. Hello you                                                                                      | Create a script that prints `hello user`, where user is the current Linux user                                                                         | [1-hello_you](./1-hello_you)                               |
| 2. The path to success is to take massive, determined action                                      | Add `/action` to the `PATH`. `/action` should be the last directory the shell looks into when looking for a program                                    | [2-path](./2-path)                                         |
| 3. If the path be beautiful, let us not ask where it leads                                        | Create a script that counts the number of directories in the `PATH`                                                                                    | [3-paths](./3-paths)                                       |
| 4. Global variables                                                                               | Create a script that lists environment variables                                                                                                       | [4-global_variables](./4-global_variables)                 |
| 5. Local variables                                                                                | Create a script that lists all local variables and environment variables, and functions                                                                | [5-local_variables](./5-local_variables)                   |
| 6. Local variable                                                                                 | Create a script that creates a new local variable                                                                                                      | [6-create_local_variable](./6-create_local_variable)       |
| 7. Global variable                                                                                | Create a script that creates a new global variable                                                                                                     | [7-create_global_variable](./7-create_global_variable)     |
| 8. Every addition to true knowledge is an addition to human power                                 | Write a script that prints the result of the addition of 128 with the value stored in the environment variable `TRUEKNOWLEDGE`, followed by a new line | [8-true_knowledge](./8-true_knowledge)                     |
| 9. Divide and rule                                                                                | Write a script that prints the result of `POWER` divided by `DIVIDE`, followed by a new line                                                           | [9-divide_and_rule](./9-divide_and_rule)                   |
| 10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath | Write a script that displays the result of `BREATH` to the power `LOVE`                                                                                | [10-love_exponent_breath](./10-love_exponent_breath)       |
| 11. There are 10 types of people in the world -- Those who understand binary, and those who don't | Write a script that converts a number from base 2 to base 10                                                                                           | [11-binary_to_decimal](./11-binary_to_decimal)             |
| 12. Combination                                                                                   | Create a script that prints all possible combinations of two letters, except `oo`                                                                      | [12-combinations](./12-combinations)                       |
| 13. Floats                                                                                        | Write a script that prints a number with two decimal places, followed by a new line                                                                    | [13-print_float](./13-print_float)                         |
| 14. Decimal to Hexadecimal                                                                        | Write a script that converts a number from base 10 to base 16                                                                                          | [100-decimal_to_hexadecimal](./100-decimal_to_hexadecimal) |
| 15. Everyone is a proponent of strong encryption                                                  | Write a script that encodes and decodes text using the rot13 encryption                                                                                | [101-rot13](./101-rot13)                                   |
| 16. The eggs of the brood need to be an odd number                                                | Write a script that prints every other line from the input, starting with the first line                                                               | [102-odd](./102-odd)                                       |
| 17. I'm an instant star. Just add water and stir.                                                 | Write a script that adds the two numbers stored in the environment variables `WATER` and `STIR` and prints the result                                  | [103-water_and_stir](./103-water_and_stir)                 |

## Additional Notes

- Ensure you have the necessary permissions to execute the scripts.
- Test the scripts in a safe environment to avoid any unintended changes to your system.
- Refer to the resources provided for a deeper understanding of each command and its options.
