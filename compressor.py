
#© 2020 Kiyokazu Tanaka
#PackBits Function

def PackBits(string):

    original_text = string

    compressed_text = ''

    current_char = original_text[0]
    countup = 0
    decom =0
    decom_char = ''


    for character in original_text:
        if current_char == character:
            if decom < 0:
                compressed_text +=  str(decom)+str(decom_char)
                decom_char =''
                decom = 0
            countup+=1
        else:
            if countup > 1:
                compressed_text += str(countup)+ str(current_char)
            if countup == 1:
                decom -= 1
                decom_char += current_char
            countup=1
            current_char = character

    if countup > 1:
        compressed_text +=  str(countup)+str(current_char)
    else:
        decom -= 1
        decom_char += current_char
        compressed_text +=  str(decom)+str(decom_char)
    return compressed_text

#Decompressor for Compressed Data(PackBits)
def PackBits_Decompressor(string):

    decompressed_text = ''
    compressed_text = string
    minus_flag = False
    count_stock = ''
    digit_counter = -1
    sum_cn = 0
    for i in range(len(compressed_text)) :
        if compressed_text[i] == "-":
            minus_flag = True
            continue;
        if compressed_text[i].isalpha() == True:
            digit_counter = -1
            sum_cn = 0
            if minus_flag == True:
                count_stock = "1"
                minus_flag = False
            decompressed_text += compressed_text[i]*int(count_stock)
        else:
            digit_counter+=1
            sum_cn += int(compressed_text[i])*(10**digit_counter)
            count_stock = sum_cn

    return decompressed_text

#FUNCTION SAMPLE
original     = "ODAMURA"
com_result   = PackBits(original)
decom_result = PackBits_Decompressor(com_result)

#OUTPUTS
print("Original Data     : ",format(original))
print("Compressed Data   : ",format(com_result))
print("Decompressed Data : ",format(decom_result))
