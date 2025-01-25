from setuptools import setup, find_packages
import platform

cuda_version = "cu118"  # Adjust to the desired CUDA version
system = platform.system()
# Set PyTorch dependency based on the OS
if system == "Windows":
    torch_package = f"torch==2.5.1+{cuda_version} @ https://download.pytorch.org/whl/{cuda_version}/torch-2.0.1%2B{cuda_version}-cp{python_version}-cp{python_version}-win_amd64.whl"
    torchvision_package = f"torchvision==0.15.2+{cuda_version} @ https://download.pytorch.org/whl/{cuda_version}/torchvision-0.15.2%2B{cuda_version}-cp{python_version}-cp{python_version}-win_amd64.whl"
    torchaudio_package = f"torchaudio==2.0.2+{cuda_version} @ https://download.pytorch.org/whl/{cuda_version}/torchaudio-2.0.2%2B{cuda_version}-cp{python_version}-cp{python_version}-win_amd64.whl"
elif system == "Linux":
    torch_package = f"torch==2.5.1+{cuda_version} @ https://download.pytorch.org/whl/{cuda_version}/torch-2.0.1%2B{cuda_version}-cp{python_version}-cp{python_version}-linux_x86_64.whl"
    torchvision_package = f"torchvision==0.15.2+{cuda_version} @ https://download.pytorch.org/whl/{cuda_version}/torchvision-0.15.2%2B{cuda_version}-cp{python_version}-cp{python_version}-linux_x86_64.whl"
    torchaudio_package = f"torchaudio==2.0.2+{cuda_version} @ https://download.pytorch.org/whl/{cuda_version}/torchaudio-2.0.2%2B{cuda_version}-cp{python_version}-cp{python_version}-linux_x86_64.whl"
elif system == "Darwin":  # macOS
    # macOS uses CPU-only builds
    torch_package = "torch==2.5.1"
    torchvision_package = "torchvision==0.15.2"
    torchaudio_package = "torchaudio==2.0.2"
else:
    raise RuntimeError("Unsupported platform. This setup.py script supports Windows, Linux, and macOS only.")

requirements = [i.strip() for i in open("./requirements.txt").readlines()]
requirements.append(torch_package)
print(requirements)
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
	name='deepadapter',
	version='1.0.7',
	author='MJ Zhang',
	author_email='mengji.zhang0809@gmail.com',
	description=long_description,
	packages=(
        find_packages() +
        find_packages(where="./deepadapter/deepadapter") +
        find_packages(where="./deepadapter/models") +
        find_packages(where="./deepadapter/params") +
        find_packages(where="./deepadapter/utils")
    ),
    license='BSD-3',
	classifiers=[
	'Programming Language :: Python :: 3',
	'Operating System :: OS Independent',
	],
	python_requires='>=3.9',
	install_requires=requirements
)

