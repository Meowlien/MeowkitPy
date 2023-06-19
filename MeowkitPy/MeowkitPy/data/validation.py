from enum import Enum, auto

# 字符串匹配類型
class StringMatchType(Enum):
    Complete = 0,           # 完整比對
    StartsWith = auto(),    # 以...開頭
    EndsWith = auto()       # 以...結束

'''
**前置檢查-資料頭**
- parameter: 需要驗證的欄位名稱 {
    範例： parameter = @"A,B..."; 檢查請求正文是否擁有欄位 A, B...
    注意： parameter = @"A,B,C..."; 欄位之間不可以有空格
}
- return: 是否存在必要資料欄位
'''
def check_valid_data(collection: dict, params: str, default_value: str='', condition_check: bool=False):

    # 無需檢查 >> 直接返回
    if params == '':
        return True, collection
    
    for param_ori in params.split(','):

        # 啓動條件檢查
        if condition_check == True:
            symbol_len = 2 # 條件標簽長度
            if len(param_ori) > (symbol_len + 1):      # 長度不足開啓條件檢查則無意義
                param = param_ori[:-(symbol_len)]      # 截去字串最後兩位字元
                token = param_ori[-(symbol_len):]      # 截取字串結尾兩位字元
        else:
            token = '{}'


        #for key in collection:
        key = collection.get(param, default_value)




        # 比對
        is_pass = False
        if token == '{}':
            if key == param:            is_pass = True # 全匹配
        elif token == '<<':     
            if key.startswith(param):   is_pass = True # 開頭匹配即可
        elif token == '>>':     
            if key.endswith(param):     is_pass = True # 結尾匹配即可
        #elif token == '--':     
            #if key:                     is_pass = True # 中間匹配即可

        # 任意一個 key 不匹配，均視爲失敗
        if is_pass == False:
            return False, None

    return True, collection

# 字典過濾器
def dict_filtered(collection: dict[str, any], param: str, match_type: StringMatchType) -> dict[str, any]:
    if match_type == StringMatchType.Complete:
        return {key: value for key, value in collection.items() if key == param}
    elif match_type == StringMatchType.StartsWith:
        return {key: value for key, value in collection.items() if str(key).startswith(param)}
    elif match_type == StringMatchType.EndsWith:
        return {key: value for key, value in collection.items() if str(key).endswith(param)}