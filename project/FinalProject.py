import urllib
import requests
from _ast import Pass

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    return radix_sort(book_to_words())                              #take in the book and return words sorted
    
def radix_sort(lst):
    char =0                                                         #position of the letter we are comparing
    end = len(lst)-1                                                #the end minus 1 to prevent Indexing error
    while char !=longest(lst):                                      # while there is still characters to compare
        while True:                                                 #to continue the loop
            swap =0                                                 #value of how many times two words have swapped
            for i in range(end):                                    #looping over all words
                LW = fun(lst,i,char)                                #taking ascii value and transforming it of left word
                RW = fun(lst,i+1,char)                              #taking ascii value for right word
                if char ==0:                                        #first pass in the sort
                    if LW > RW:                                     #checking if the words should swap
                        lst[i], lst[i+1] = lst[i+1], lst[i]         #swapping words
                        swap+=1                                     #words have swapped, add 1 to value
                if char >0:                                         #for every other pass in the sort
                    LWP = fun(lst,i,char-1)                         #left previous word ascii value
                    RWP = fun(lst,i+1,char-1)                       #right previous word ascii value
                    if LWP == RWP:                                  #if the two words have same previous character, check if we should swap them
                        if LW > RW:                                 #comparing next character since the previous character is the same
                            lst[i], lst[i+1] = lst[i+1], lst[i]     #swapping
                            swap+=1                                 #again swap value increases
            if swap == 0:                                           #went through whole iteration and all are sorted for that character, therefore break while loop
                break                                   
        char+=1                                                     #increase to next character, begin sort again
    words = []                                                      #new array
    for i in range(len(lst)):                                       #looping over list of all words
         words.append(lst[i].decode('ascii'))                       #decoding back to strings to get rid of the b' 
    return words                                                    #returning new list all perfectly sorted :)

def fun(lst, i, char):                                              #my fun function to get rid of anomolies
    try:                                                            #test to see if there is a letter present
        value = lst[i][char]                                        #yay theres a letter, get the ascii code for that letter
        if value > 64 and value <123:                               #the value is a letter and not like a ? or ! or ", etc
            temp =  value % 64                                      #A starts at 65, dividing by 64 will shift the letters to positions 1-26
            if temp > 26:                                           #we are dealing with lowercase letters in 97-122, b/c 97 % 64> 26
                return temp -32                                     #shifting these lowercase letters to overlap the uppercase letters
            else:                                                   #letters are capital and dont need to shift therefore return them
                return temp
        else:                                                       #ascii code is not for letters, return as is, this will allow the random 
            return value                                            #characters and numbers to sort themselves outside of the first 26
    except:                                                         #there is no value aka letter is not there, return 0, this helps with cases 
        return 0                                                    #like comparing the word pickle and pickles
    
def longest(lst):                                                   #finding longest word
    longest = 0                                                     #start with 0
    for i in lst:                                                   #looping over whole list
        if len(i) > longest:                                        #if length of word is longer than previous longest
            longest = len(i)                                        #set new longest
    return longest                                                  #pretty self explanatory 

def main():
    templst = book_to_words()[:100]                                 #i use this for testing, the 100 is the first 100 words, getting rid 
    print(radix_sort(templst))                                      #print the nice and fancy organized list 
    #print(radix_a_book())                                           #note sorting the whole book takes a bit longer, be patient, like REALLLLLLY PATIENT

if __name__ == '__main__':
    main()    