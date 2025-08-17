import os
import importlib.util
import re

STUB_FILE = "AvalonPasm.py"  # Your main loader file
ROOT_FOLDER = "APasm_ROOT"

def get_all_exports(folder):
    exports = {}
    for dirpath, _, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(".py") and not filename.startswith("__"):
                filepath = os.path.join(dirpath, filename)
                mod_name = f"{ROOT_FOLDER}.{os.path.relpath(filepath, ROOT_FOLDER)[:-3].replace(os.sep, '.')}"
                spec = importlib.util.spec_from_file_location(mod_name, filepath)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                for k, v in vars(module).items():
                    if not k.startswith("_"):
                        exports[k] = v
    return exports

def generate_stub_lines(exports):
    lines = []
    for name, val in exports.items():
        if callable(val):
            # Function stub
            lines.append(f"def {name}(*args, **kwargs): ...")
        elif isinstance(val, dict):
            lines.append(f"{name}: dict | None = None")
        elif isinstance(val, int):
            lines.append(f"{name}: int | None = None")
        else:
            lines.append(f"{name}: {type(val).__name__} | None = None")
    return lines

def update_stub_section(lines):
    with open(STUB_FILE, "r") as f:
        content = f.read()

    new_stub_block = "# --- AUTO-GENERATED IntelliSense stubs ---\n" + "\n".join(lines) + "\n# --------------------------------------"

    # Replace old stub block or insert if missing
    if "# --- AUTO-GENERATED IntelliSense stubs ---" in content:
        content = re.sub(
            r"# --- AUTO-GENERATED IntelliSense stubs ---.*?# --------------------------------------",
            new_stub_block,
            content,
            flags=re.S
        )
    else:
        content = new_stub_block + "\n\n" + content

    with open(STUB_FILE, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    exports = get_all_exports(ROOT_FOLDER)
    stub_lines = generate_stub_lines(exports)
    update_stub_section(stub_lines)
    print("IntelliSense stubs updated in", STUB_FILE)
