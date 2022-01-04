#Look-and-say sequence

par 116 chars - Jackson

https://en.wikipedia.org/wiki/Look-and-say_sequence

output the first 20 elements of the Look-and-say sequence starting with 1, each on their own line.

To generate a member of the sequence from the previous member, read off the digits of the previous member, counting the number of digits in groups of the same digit. For example:

    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.

1  
11  
21  
1211  
111221  
312211  
13112221  
1113213211  
...  