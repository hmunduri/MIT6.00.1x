#MIT6.00.1x
My solutions for MIT 6.00.1x course on edX.

##l3p9.py
In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

Here is a transcript of an example session:
```
Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 87?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 81?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 84?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 82?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 83?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 83
```

Your program should use bisection search. So think carefully what that means. What will the first guess always be? How should you calculate subsequent guesses?

## l4p5.py
Write a Python function, `clip(lo, x, hi)` that returns `lo` if `x` is less than `lo`; `hi` if `x` is greater than `hi`; and `x` otherwise. For this problem, you can assume that `lo < hi`.

Don't use any conditional statements for this problem. Instead, use the built in Python functions min and max. You may wish to read the documentation on min and the documentation on max, and play around with these functions a bit in your interpreter, before beginning this problem.

This function takes in three numbers and returns a single number.
