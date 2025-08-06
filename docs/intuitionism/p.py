import re

def remove_p_tags(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 替换 <p></p> 标签为其内部内容
    updated_content = re.sub(r'<p>(.*?)</p>', lambda match: match.group(1).replace('\n', ' ').strip(), content, flags=re.DOTALL)
    
    # 覆盖写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

# 测试文件路径
file_path = 'hello-logic\docs\intuitionism\math.md'
remove_p_tags(file_path)
print(f"File '{file_path}' has been updated.")
