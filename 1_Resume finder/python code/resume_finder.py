import docxpy as dx
import os

def search(dir_path,keyword):
    matched_file_list=[]
    all_docx_files=[]
    all_file_list=os.listdir(dir_path)
    for file in all_file_list:
        if(file.endswith('.docx')):
            all_docx_files.append(file)
            text=dx.process(f'{dir_path}/{file}')
            if(keyword.lower() in text.lower()):
                matched_file_list.append(file)
    return all_file_list,all_docx_files,matched_file_list


'''key=input('Enter the keyword to be searched: ')
all_files, docx_files, matched_files=search(key)
 

print(f'Total files found: {len(all_files)}')
print(f'Total docx files found: {len(docx_files)}')
print(f'Total Matched files: {len(matched_files)}')
for res in matched_files:
    print('\t>',res)
'''
