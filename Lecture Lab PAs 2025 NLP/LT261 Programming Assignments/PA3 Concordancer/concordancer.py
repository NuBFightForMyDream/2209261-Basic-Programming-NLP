# import library
import nltk # for tokenizing words
import string # for punctuations
from nltk.tokenize import wordpunct_tokenize

class Concordancer:

    left_context_length = 50
    right_context_length = 50

    def __init__(self):
        """
        - Create list for storing messages in each line
        """
        self.allText = [] 


    def read_tokens(self, file_name):
        """
        Goal : tokenize each word then store into list in initial method
        """
        # read file first 
        filename_in = open(file_name , 'r') # read file
        
        # loop each line then token then store to list of line
        for each_line in filename_in :
            # tokenize line (string) into list 
            tokenized_words = nltk.wordpunct_tokenize(each_line)
            # append to list of line
            self.allText.append( tokenized_words )
            
        filename_in.close()

    def find_concordance(self, query, num_words):
        """
        Goal : find words nearby N words then print word found
        Don't forget to format query word to the center
        
        Steps :
        1) for loop , found word
        2) get list of words nearby
        3) limit spaces
        4) print word
        """
        
        # create bool checking if found word
        found_query_word = False
        
        # for loop , find word 
        for word_list in self.allText : # word_list = list of tokenized words in each line
            
            for pos in range(len(word_list)) :
                
                # check if each word is query word (word finding)
                if query == word_list[pos] :
                    
                    # change bool found to True
                    found_query_word = True
                    
                    # find concordance text range 
                    concordance_text = " ".join(word_list[pos - num_words : pos + (num_words + 1)]) # join word
                    
                    # find position of word in concordance_text 
                    leftbound_query_pos = concordance_text.find(query) - 1 # bound of word like | word |
                    rightbound_query_pos = concordance_text.find(query) + len(query) 
                    
                    # count then check for spaces
                    leftbound_count = len(concordance_text[0 : leftbound_query_pos])
                    rightbound_count = len(concordance_text[rightbound_query_pos + 1 : ])
    
                    # limit zone and add some spaces
                    if leftbound_count > self.left_context_length :
                        # cut only latest N characters
                        concordance_text = concordance_text[ leftbound_count - self.left_context_length : ]
                        left_spaces = "" # no spaces
                    else :
                        left_spaces = " " * (self.right_context_length - leftbound_count) # add spaces (left corcordance still same)
                        
                    if rightbound_count > self.right_context_length :
                        # cut only latest N characters
                        concordance_text = concordance_text[ : len(concordance_text) - (rightbound_count - self.right_context_length) ] # all - right_bound
                        right_spaces = "" # no spaces
                    else :
                        right_spaces = " " * (self.right_context_length - rightbound_count) # add spaces (right concordance still same)
                        
                    # print out messages
                    print( left_spaces + concordance_text + right_spaces )
                    
        # if word not found in all text 
        if found_query_word == False :
            print("Query not found...")
                                        
    def find_concordance_ngram(self, ngram_query, num_words):
        """
        Goal : find words nearby N words then print query_tokens found
        Don't forget to format query word to the center
        
        Steps :
        1) for loop , found word
        2) get list of words nearby
        3) limit spaces
        4) print word
        """
        
        # create bool checking if found word
        self.query_tokens = ngram_query.split() # split into list -> got word sublist
        found_query_word = False
        
        # for loop , find word 
        for word_list in self.allText : # word_list = list of tokenized words in each line
            
            for pos in range(0 , len(word_list) - len(self.query_tokens)): 
                
                # check if each word is query word (word finding)
                if self.query_tokens == word_list[pos : pos + len(self.query_tokens)] :
                    
                    # change bool found to True
                    found_query_word = True
                    
                    # find concordance text range
                    concordance_text = " ".join(word_list[pos - num_words : pos + len(self.query_tokens) + (num_words)])
                    
                    ngram_phrase = " ".join(self.query_tokens)
                    query_pos = concordance_text.find(ngram_phrase)
                    
                    # find position of word in concordance_text 
                    leftbound_query_pos =  query_pos - 1 # bound of word like | word |
                    rightbound_query_pos = query_pos + len(ngram_phrase)
                    
                    # count then check for spaces
                    leftbound_count = len(concordance_text[0 : leftbound_query_pos])
                    rightbound_count = len(concordance_text[rightbound_query_pos + 1 : ])
    
                    # limit zone and add some spaces
                    if leftbound_count > self.left_context_length :
                        # cut only latest N characters
                        concordance_text = concordance_text[ leftbound_count - self.left_context_length : ]
                        left_spaces = "" # no spaces
                    else :
                        left_spaces = " " * (self.right_context_length - leftbound_count) # add spaces (left corcordance still same)
                        
                    if rightbound_count > self.right_context_length :
                        # cut only latest N characters
                        concordance_text = concordance_text[ : len(concordance_text) - (rightbound_count - self.right_context_length) ] # all - right_bound
                        right_spaces = "" # no spaces
                    else :
                        right_spaces = " " * (self.right_context_length - rightbound_count) # add spaces (right concordance still same)
                        
                    # print out messages
                    print( left_spaces + concordance_text + right_spaces )
                
        # if word not found in all text 
        if found_query_word == False :
            print("Query not found...")    
                    

    def compute_bigram_stats(self, query, output_file_name):
        """
        Goal : count frequency of nearby query words
        
        Steps
        - 1) for loop , find query word
        - 2) get nearby words then check frequency in dict
        - 3) if word in dict , add frequency , otherwise add new key: (remember to add frequency as negative for descending order)
        - 4) change dict to list of tuples
        - 5) reverse key:val then sort
        - 6) write file with each pair of key:val (change frequency back to positive number)
        """
        # create dict for storing word frequency
        self.bigram_frequency = {}
        
        # for loop , find word 
        for word_list in self.allText : # word_list = list of tokenized words in each line
            
            for pos in range(len(word_list)) : # pos = each_word position
                
                if query == word_list[pos] : # if found query word
                    
                    # get nearby words (left & right)
                    word_before_query , word_after_query = word_list[pos - 1] ,  word_list[pos + 1] 
                    
                    # check punctuation for 2 words
                    if word_before_query not in (string.punctuation + ' -- ?" ." ') : # clean punctuations 1-2 chars out
                        # check if word never appear in dict
                        if word_before_query not in self.bigram_frequency :
                            self.bigram_frequency[ word_before_query ] = -1 # start freq from -1 to sort frequency descending but alphabetically
                        else :
                            self.bigram_frequency[ word_before_query ] -= 1
                            
                    if word_after_query not in (string.punctuation + ' -- ?" ." ') : # clean punctuations 1-2 chars out
                        # check if word never appear in dict
                        if word_after_query not in self.bigram_frequency :
                            self.bigram_frequency[ word_after_query ] = -1
                        else :
                            self.bigram_frequency[ word_after_query ] -= 1 
                
        # turn dit into list of tuples
        self.bigram_frequency_list = list(self.bigram_frequency.items())
        
        # swap count and word for sorting then sort -> get list of tuples
        self.bigram_frequency_list = sorted([ (negative_count , word) for (word , negative_count) in self.bigram_frequency_list ])
        
        # write into files
        with open(output_file_name , "w") as filename : # write file
           for (negative_count , word) in self.bigram_frequency_list :
               filename.write( f"{query} {word} {-negative_count}\n" )
    
"""
# test class
cc = Concordancer() # create object

## -------------------------------- Test all methods --------------------------------
print("-" * 35 + "Testing `read_tokens` Function" + "-" * 35) 
cc.read_tokens('jane.txt') # testing file path = ./test/jane_mini.txt
print("Done reading tokens , added to list already." + " Now testing filepath is : " + "jane.txt")

print("\n" + "-" * 32 + "Testing `find_concordance` Function " + "-" * 32)  
cc.find_concordance("good", 5)

print("\n" + "-" * 30 + "Testing `compute_bigram_stats` Function " + "-" * 30)
cc.compute_bigram_stats("good" , "good_bigram.txt")

bigram_output = open("good_bigram.txt" , "r")
for line in bigram_output :
    print(line.strip("\n"))
bigram_output.close()

print("\n" + "-" * 29 + "Testing `find_concordance_ngram` Function " + "-" * 29)
cc.find_concordance_ngram("my book" , 3)
"""