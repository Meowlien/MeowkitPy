import sys
import toml

args = sys.argv[1:] # 獲取除脚本名之外的所有參數内容
file_path = "../MeowkitPy/pyproject.toml"
version_file = "version.txt"

def execute() -> bool:
    if (len(args) != 3): return False
    try:
        update_major = int(args[0])
        update_minor = int(args[1])
        update_patch = int(args[2])
        print(f'Version Mask: {update_major}.{update_minor}.{update_patch}')
    except Exception as e:
        print(f'{str(e)}')
        return False

    def update_version():
        try:
            # Read File
            with open(version_file, 'r', encoding="utf-8") as f:
                curr_ver = f.read().strip()
                major = str(int(curr_ver.split('.')[-3]) + update_major) # 主版號
                minor = str(int(curr_ver.split('.')[-2]) + update_minor) # 次版號
                patch = str(int(curr_ver.split('.')[-1]) + update_patch) # 修訂版號
                new_ver = f"{major}.{minor}.{patch}"
                print(f'Version Update: {curr_ver} -> {new_ver}')

            # Write File
            with open(version_file, 'w', encoding="utf-8") as f:
                f.write(new_ver)

            update_version_in_pyproject(new_ver)

        except Exception as e:
            print(f'Error reading version from version.txt: {str(e)}')

    def update_version_in_pyproject(version):
        try:
            # Read File
            with open(file_path, 'r', encoding="utf-8") as f:
                data = toml.load(f)
            # Write File
            with open(file_path, 'w', encoding="utf-8") as f:
                data["project"]["version"] = version
                toml.dump(data, f)
            print(f'Version Update: pyproject.toml -> {version}')

        except Exception as e:
            print(f'Error updating version in pyproject.toml: {str(e)}')


    update_version()
    return True

if __name__ == "__main__":
    execute()
    print('--------------------------------')