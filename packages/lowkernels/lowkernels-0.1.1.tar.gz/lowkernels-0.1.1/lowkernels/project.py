import os
import shutil

def create_project(name):
    """
    Creates a new LowKernels project with predefined templates.

    Args:
        name (str): Project name.
    """
    os.makedirs(name, exist_ok=True)
    os.makedirs(os.path.join(name, "src"), exist_ok=True)
    os.makedirs(os.path.join(name, "build"), exist_ok=True)

    # Copy templatestemplate_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "templates"))
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "templates"))

    shutil.copy(os.path.join(template_dir, "bootloader.asm"), os.path.join(name, "src", "bootloader.asm"))
    shutil.copy(os.path.join(template_dir, "kernel.c"), os.path.join(name, "src", "kernel.c"))

    print(f"Project '{name}' created successfully.")
