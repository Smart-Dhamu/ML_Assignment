#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise
Google's Python class
The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.
1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...
Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.
2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.
Use str.split() (no arguments) to split on all whitespace.
Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.
Optional: define a helper function to avoid code duplication inside
print_words() and print_top().
"""

import sys

def helper(t):
    text=open(t,'r')
    f=[]
    for i in text:
        f.append(i)

    f=''.join(f)
    f=f.lower()

    for i in range(len(f)):
        if(f[i].isalnum()==False):
            if(f[i]!=' ' and f[i]!='\n'):
                f=f.replace(f[i],'$')
              
    f=list(f)
    while(f.count('$')!=0):
        f.remove('$')
    f=''.join(f)

    f=f.split()
    d=[]
    for i in f:
        if i not in d:
            d.append(i)
    s=[]
    for i in d:
        s.append([i,f.count(i)])
    return(s)     

def print_words(filename):
    a=helper(filename)
    a.sort()
    for i in a:
        print(i[0],' ',i[1])



def print_top(filename):
    a=helper(filename)
    def Lout(a):
        return a[1]
    a=sorted(a,reverse=True,key=Lout)
    for i in range(20):
        print(a[i][0],' ',a[i][1])
    
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
