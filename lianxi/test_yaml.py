import yaml

# print(yaml.load("""
# - a
# - b
# - c
# - d
# """,Loader=yaml.FullLoader))

#转换成字典
print(yaml.load("""
a: 1
""",Loader=yaml.FullLoader))

print(yaml.load(open("demo.yaml")))