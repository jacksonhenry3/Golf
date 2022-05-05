# Parenthesis matching

Suppose you've made a series of very poor life choices and now have a hobby that involves parsing programming languages.
At first it was light-hearted experimentation with regular expressions but now you're hooked and starting on the hard stuff.
It's 1am and you're experimenting with a simplified lisp variant.

## variant 1: are the parentheses balanced?

Lisp expressions are all about the parentheses.
However, before you get too far, you want to check that your parentheses are balanced -- if not, you've written invalid lisp.

**Write a program that takes in an arbitrary string and outputs whether/not the parentheses are matched.**

```py
def parens_are_balanced(lisp: str) -> bool:...
```
It should produce
```lisp
 ()        ; ok, the parens are balanced
 (())      ; ok
 ()()      ; ok
 (()())()  ; ok
 (()(())() ; bad
 (()())))  ; bad
```

### scores
Steven: 85B
Jackson: 49 charachters (not sure how to measure bytes) 

## variant 2:

There are a lot of parentheses and you keep wasting time on syntax errors.
You want to write a function that identifies where you went wrong, like

```py
def find_mistake(lisp: str) -> str:
    return "get out of computer science, it's a trap"
```
No, wait, more like
```py
def where_it_all_went_wrong(lisp: str) -> datetime.datetime:
    return datetime.datetime.fromisoformat("2019-04-18")
    # It was a brisk day in April when I picked up an article on parser combinators...
```
Focus! The desired function signature is:
```py
def find_first_unmatched_paren(lisp: str) -> int:
    "Return the index of the first unmatched paren in the string, or -1 if balanced"
    ...
```

```lisp
 ()        ; -1
 (())      ; -1
 ()()      ; -1
 (()())()  ; -1
 (()(())() ; 0
;^ no matching bracket
 (()())))  ; 5
;      ^^ no matching brackets
```
###scores 
Jackson: 164 charachters

## variant 3: parentheses and brackets and curly braces, oh my!

The sun is now shining.
Not on you yet though, it's 4am and you got wild with lex and yacc and now your lisp variant has started to vary pretty widely from the other implementations.
It now needs to balance pairs of parentheses, brackets, and curly braces.

You promise yourself you'll sleep after you write a function

```py
def is_balanced(lang: str) -> bool: ...
```
That can tell if all the nested parentheses, brackets, and curly braces are balanced:
```
([)] => false
({[][](())}) => true
```
