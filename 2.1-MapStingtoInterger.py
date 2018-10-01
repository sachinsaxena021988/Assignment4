# define input value 
input1 =["sachin","saxena","as","SAdadad","puneetsrivastava"]

# define map_words_lenght
def map_words_lenght(input1):
    return list(map(lambda x:len(x),input1))
    
# call function to calculate   
map_words_lenght(input1)