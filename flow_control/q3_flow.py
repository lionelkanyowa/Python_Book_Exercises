# Q.3 Without running the following code, what does it print? Why?

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')
            
bar_code_scanner('113')
bar_code_scanner(142)
 
#This would print 'Product2' and 'Product not found!' bacause the integer 142 isn't part of the case statement.               