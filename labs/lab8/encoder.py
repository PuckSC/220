def encode_better(message, key):
    # message and keyword modifications
    mess = message.replace(' ', '')
    key_word = key.replace(' ', '')
    # repeating then fixing length of key
    key_factor = len(mess) // len(key_word) + 1
    key_seq = key_word * key_factor
    key_code = key_seq[:len(mess)]
    # key maker
    key_list = []
    for ltr in key_code.upper():
        unicode = ord(ltr)
        key_list.append(unicode)
    # message to unicode to re-indexed to A = 0
    mess_code = []
    for ltr in mess.upper():
        unicode = ord(ltr)
        mess_code.append(unicode)
    # output section
    output = []
    for num in range(len(mess_code)):
        keycode = ((mess_code[num] + key_list[num]) + 26) % 26
        keycode = keycode + ord('A')
        output.append(chr(keycode))
    result = ''.join(output)
    return result
