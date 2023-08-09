# 0x03-shell_variables_expansions

## 103-water_and_stir

### Bash Script Explanation

The following bash script showcases a series of operations that involve character manipulation, number conversion, and arithmetic calculations. Environment variables are utilized to achieve the desired outcome.

```bash
export STIR="ti.itirtrtr"
export WATER="ewwatratewa"

echo $( printf "%o" $(( $(( 5#$( echo $WATER | tr 'water' '01234' ) )) + $(( 5#$( echo $STIR | tr 'stir.' '01234') )) )) | tr '01234567' 'bestchol' )
```

### Step-by-Step Breakdown:

1. **Defining Environment Variables:**
   - The script initializes two environment variables:
     - `STIR` is assigned the value `"ti.itirtrtr"`.
     - `WATER` is assigned the value `"ewwatratewa"`.

2. **Calculations and Transformations:**

   a. Conversion of `WATER` Variable:
      - The command `echo $WATER` outputs `"ewwatratewa"`.
      - Subsequently, the `tr 'water' '01234'` command translates 'w', 'a', 't', 'e', and 'r' to '0', '1', '2', '3', and '4' respectively.
      - Result: `"30012412301"`

   b. Conversion of `STIR` Variable:
      - The command `echo $STIR` outputs `"ti.itirtrtr"`.
      - The `tr 'stir.' '01234'` command translates 's', 't', 'i', 'r', and '.' to '0', '1', '2', '3', and '4' respectively.
      - Result: `"12421231313"`

   c. Arithmetic Calculation:
      - The numerical strings from previous steps are interpreted as base-5 numbers using the `5#` prefix.
      - These base-5 numbers are converted to decimal and then added together.
      - The resulting decimal number is `44834284`.

   d. Octal Conversion:
      - The decimal number `44834284` is formatted as an octal (base 8) number using `printf %o`.
      - The octal representation is `"253016754"`.

   e. Character Translation:
      - The octal number `"253016754"` is processed by `tr '01234567' 'bestchol'` to convert octal digits to corresponding characters.
      - Result: `"shtbeolhc"`

3. **Output:**
   - The script employs `echo` to display the final result of all operations, which is `"shtbeolhc"`.

In summary, this script creatively employs character manipulation, number conversion, and arithmetic operations to generate the output string `"shtbeolhc"`.