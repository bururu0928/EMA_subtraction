# 將輸入的各位數數字轉成list儲存
def num_int_list(num):
    num_list=list(map(int,str(num)))
    num_list.reverse()
    
    return num_list

# 將各位數的借位，轉成list儲存
def borrow_list(list1, list2):
    
    #建立處理每一位數時，對應的被減數list
    minuend_int_list = list1.copy()

    #建立借位list，其中每個元素都是list，每個位數依序分配一個元素
    borrow_int_list=[]

    #處理借位
    for digit in range(len(list2)):

        #判斷是否借位
        if minuend_int_list[digit] < list2[digit]:

            #尋找最近的非零位數
            for i in minuend_int_list[digit+1:]:
                if i != 0:
                    NotZero = minuend_int_list[digit+1:].index(i)
                    break
            
            #製作該位數對應的小借位list
            minuend_int_list[digit]=10
            for i in range(NotZero):
                minuend_int_list[digit+1+i]=9
            minuend_int_list[digit+1+NotZero]-=1

            #放入大借位list
            borrow_int_list.append(minuend_int_list[digit:digit+2+NotZero])
        else:
            #放入大借位list
            borrow_int_list.append([])
        
    return borrow_int_list

# 計算減法
def calculate(a,b):

    #儲存a,b,ans的數字列表
    a_int_list = num_int_list(a)
    b_int_list = num_int_list(b)
    ans_int_list = num_int_list(a-b)

    #處理和與進位
    borrow_int_list = borrow_list(a_int_list,b_int_list)

    return a_int_list, b_int_list, ans_int_list, borrow_int_list

# 用''把字串列表補足位數
def fill(num_str_list, max_len):
    for i in range(max_len-len(num_str_list)):
        num_str_list.append('')

    num_str_list.reverse()

    return num_str_list

# 將各位數數字、加總(含進位)、進位，轉成字串型態的list儲存
def calculate_str(a,b):
    a_int_list, b_int_list, ans_int_list, borrow_int_list = calculate(a,b)
    a_str_list = list(map(str,a_int_list))
    b_str_list = list(map(str,b_int_list))
    ans_str_list = list(map(str,ans_int_list))

    #季錄各組數字位數
    a_len = len(a_str_list)
    b_len = len(b_str_list)
    ans_len = len(ans_str_list)

    max_len = max(a_len, b_len, ans_len)

    a_str_list = fill(a_str_list, max_len)
    b_str_list = fill(b_str_list, max_len)
    ans_str_list = fill(ans_str_list, max_len)
    
    borrow_str_list = []
    for i in borrow_int_list:
        borrow_str_list.append(list(map(str, i)))

    return a_str_list, b_str_list, ans_str_list, borrow_str_list, max_len
    
if __name__ == '__main__':
    a_str_list, b_str_list, ans_str_list, borrow_str_list, max_len = calculate_str(999,9)
    print(a_str_list, b_str_list, ans_str_list, borrow_str_list, max_len)
    print(type(a_str_list[0]))
