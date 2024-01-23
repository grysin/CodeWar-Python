# 1-22-24 
 # Instructions 

# Count how often sign changes in array.

# number from 0 to ... . Empty array returns 0

# example

# /*
# | elem | count |
# |------|-------|
# |  1   |  0    |
# | -3   |  1    |
# | -4   |  1    |
# |  0   |  2    |
# |  5   |  2    |
# */

# catch_sign_change(arr) == 2;


def catch_sign_change(arr):
    if not arr:
        return 0
    
    # initialize previous sign and sign change count
    previous_sign=None
    sign_change_count = 0

    for each in arr: 
        # figure out whether current number is positive or negative
        if each >=0:
            current_sign = "positive"
        else:
            current_sign= "negative"

        # test print
        #print(f"Number:{each} \n Previous sign {previous_sign} \n Current sign {current_sign}")

        # check to make sure that previous_sign exists, only compare after 1st integer
        if previous_sign is not None:
            # compare current sign to previous sign
                if current_sign == "positive" and previous_sign == "negative" or current_sign=="negative" and previous_sign=="positive":
                    sign_change_count = sign_change_count + 1
        
        previous_sign=current_sign
    
    return sign_change_count
