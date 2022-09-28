###

##

# Basic Credit Card Processing Program.

- This program for processing the credit card transaction in batch processing.

- Program will produce the summary of the transaction status in the end.

- All the input cards will be validated with Luhn10 validation.

# Description

## Design decision

- Card_validator module checks the credit card against the Luhn10 validation.
- Data input accepted as file or STDIN
- Processing happens in line by line.
  - Each line controlled based on the control verb.
  - All the "Add" statement with card information will be validated against Luhn10 algorithm.
  - Charge will increase the balance of the user if its an valid card and ignored for invalid cards.
  - Credit will decrease the balance (can go as negative balance too) of the user if its an valid card and ignored for invalid cards.

## Programming Used

- Python 3.x

## Required Dependency.

- No depency with external module.
- Internal impementation of luhn10 is part of this module.

## Build Steps

- run the program in console, no build steps.

## How to run the code.

- refer below how to run the program step.

# Usage - How to Run the Program

## Provide Execute Permission

Add execute permission to the file to run it in the console in MacOS or Linux Machine.

```bash
chmod +x myprogram.py
```

## 1. Run the Program with the input filename passed as ARGUMENT.

```bash
./myprogram.py input.txt
```

## 2. Run the Program with the input file passed as STDIN.

```bash
./myprogram.py < input.txt
```

## Input file Commands

Text input file for the credit card processing. each line will start with control statement for processing decision.

- "Add" will create a new credit card for a given name, card number, and limit
  - Card numbers should be validated using Luhn 10
  - New cards start with a $0 balance
- "Charge" will increase the balance of the card associated with the provided name by the amount specified
  - Charges that would raise the balance over the limit are ignored as if they were declined
  - Charges against Luhn 10 invalid cards are ignored
- "Credit" will decrease the balance of the card associated with the provided name by the amount specified
  - Credits that would drop the balance below $0 will create a negative balance
  - Credits against Luhn 10 invalid cards are ignored

## Input file sample - input.txt

```bash
Add Tom 4111111111111111 $1000
Add Lisa 5454545454545454 $3000
Add Quincy 1234567890123456 $2000
Charge Tom $500
Charge Tom $800
Charge Lisa $7
Credit Lisa $100
Credit Quincy $200
```

## Expected Output - STDOUT

- Output will be the summary after all the transaction processed.
- User name followed up colon and the balance in dollars.
- Users with invalid cards will hav balance as "error"
- User Balance summary dislayed in alphabetical order.

```bash
lisa: $2907
quincy: error
tom: $2300
```

## Input assumptions.

- Empty lines are ignored by the program.
- Each valid line with proper control verb and type of transaction will be processed.
- All the data considered as case insensitive. "Tom" and "tom" considered as same persion.
- Different user can have the same credit card number. balance considered based on user.
- Credit number always in numeric and can vary in length up to 19 characters.
- Each line in the input file considered as one command statment and details as space delimited.
- 3 verb are "Add", "Charge" and "Credit", can be submitted in any order. Program logic handles it.
- card length vary from 1 to 19 characters.

# Usage - How to Run the Test cases

## Unit test on add data and Luhn10 check.

```bash
chmod +x test_myprogram.py
python3 -m unittest test_myprogram.py
```

## Test case.

```
TestCase: Invalid AddData - Passed
.
TestCase:   Valid AddData - Passed
.
TestCase: Invalid Luhn10 Check - Passed
.
TestCase:   Valid Luhn10 Check - Passed
.
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK

```

# Support.

- Please read the read me one more time to understand.

# Roadmap

- Persistance can be added.
- More validations can be added.
- More test cases can be added.

# Contributing

- Not initialised in GITHUB. This is internal program.
- Once opensourced the follwing can be done.
  - Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

# License

[MIT](https://choosealicense.com/licenses/mit/)
