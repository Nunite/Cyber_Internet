import sys

project_root_path = "project_root"  # 根据实际情况替换为你的项目根路径

if project_root_path in sys.path:
    print(f"{project_root_path} is in module search path.")
else:
    print(f"{project_root_path} is not in module search path.")
