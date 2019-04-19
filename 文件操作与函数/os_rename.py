import os
src_file="new_modify_file"
dst_file="modify_file"
# 在windows下，如果dst是一个存在的目录, 将抛出OSError
# [WinError 183] 当文件已存在时，无法创建该文件
os.rename(src_file,dst_file)