import pypdf
import pdfminer
def top_words(file_path,num):
    text=pypdf.process_page(file_path)
    from collections import Counter
    import re
    list_words=re.findall("\w+",text)
    ctr=Counter(list_words)
    result=dict()
    result=ctr.most_common(num)
    return result
