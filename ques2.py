import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."

mat1 = re.findall('b\w+' , text)
print(mat1)

mat2 = re.findall("B\w+",text)
print(mat2)