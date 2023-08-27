def concat_dico(dict1, dict2):
    dict3 = None
    repeat_key = False
    dict3 = dict1.copy()
        
    for keys, values in dict2.items():
        
        for old_keys in dict3:
            
            if old_keys == keys:
                dict3[keys] = [dict3[old_keys], values]
                repeat_key = True
                
        if repeat_key == False :
            dict3[keys] = values
            
    return(dict3)



