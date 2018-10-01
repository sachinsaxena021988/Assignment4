# define input value 
input1 =["sachin","saxena","as","SAdadad","puneetsrivastava"]

# define filter_long_words
def filter_long_words(n,input1):
    return list(filter(lambda x:len(x) > n,input1))
    
# call function to calculate   
filter_long_words(7,input1)