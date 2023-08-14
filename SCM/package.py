import toml

file_path = "../MeowkitPy/pyproject.toml"
version_file = "version.txt"

def update_version_in_pyproject(version):
    try:
        # Read File
        with open(file_path, 'r', encoding="utf-8") as f:
            data = toml.load(f)
        # Write File
        with open(file_path, 'w', encoding="utf-8") as f:
            data["project"]["version"] = version
            toml.dump(data, f)
        print(f'Updated version in pyproject.toml to {version}')

    except Exception as e:
        print(f'Error updating version in pyproject.toml: {str(e)}')

try:
    # Read File
    with open(version_file, 'r', encoding="utf-8") as f:
        curr_ver = f.read().strip()
        ver = ".".join(curr_ver.split(".")[:-1])
        patch = str(int(curr_ver.split('.')[-1]) + 1)
        new_ver = f"{ver}.{patch}"
    # Write File
    with open(version_file, 'w', encoding="utf-8") as f:
        f.write(new_ver)

    update_version_in_pyproject(new_ver)

except Exception as e:
    print(f'Error reading version from version.txt: {str(e)}')
