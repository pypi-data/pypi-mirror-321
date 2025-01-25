import subprocess
import os

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {command}\n{result.stderr.decode()}")
    print(f"Command succeeded: {command}")

def build_os(project_dir):
    src_dir = os.path.join(project_dir, "src")
    build_dir = os.path.join(project_dir, "build")
    os.makedirs(build_dir, exist_ok=True)

    # Compile bootloader
    bootloader_src = os.path.join(src_dir, "bootloader.asm")
    bootloader_bin = os.path.join(build_dir, "bootloader.bin")
    run_command(f"nasm -f bin {bootloader_src} -o {bootloader_bin}")

    # Compile kernel
    kernel_src = os.path.join(src_dir, "kernel.c")
    kernel_obj = os.path.join(build_dir, "kernel.o")
    run_command(f"gcc -m32 -ffreestanding -c {kernel_src} -o {kernel_obj}")

    # Link kernel (PE/COFF format)
    kernel_bin = os.path.join(build_dir, "kernel.bin")
    run_command(f"ld -m i386pe -Ttext 0x1000 -o {kernel_bin} {kernel_obj}")

    # Convert to binary
    run_command(f"objcopy -O binary {kernel_bin} {kernel_bin}")

    # Create .img
    os_img = os.path.join(project_dir, "my_os.img")
    with open(os_img, "wb") as img:
        with open(bootloader_bin, "rb") as bl:
            img.write(bl.read())
        with open(kernel_bin, "rb") as krnl:
            img.write(krnl.read())

    print(f"OS successfully built! Bootable image created: {os_img}")
