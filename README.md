# 3D File to GLTF Converter Script

This Python script is designed to convert various 3D file formats (e.g., .obj, .fbx, .usdz) to GLTF (.gltf) using the `gltfpack` tool. The goal is to achieve a file size of around 65KB without compromising the integrity of the pixels. The script utilizes the `gltfpack` tool for efficient compression. By specifying the desired dependencies in the `requirements.txt` file, users can easily manage and install the required packages, making the conversion process seamless. Customize the script to fit your specific needs and contribute to its improvement for efficient 3D model processing in AR/VR applications.

## Prerequisites

- Before using the script, ensure you have the following dependencies installed:

  - Python (>=3.6)
  - Pip
  - GLTFPack (Installation details provided below)
  - NPX (for running local npm packages)
  - Zlib (Compression library, installation details provided below)
  - C:\Tools directory (Creation details provided below)

## Installing Dependencies

### Python Dependencies:

- Create a `requirements.txt` file:

  - Create a file named `requirements.txt` in the root directory of your project and add the following lines to specify the required Python packages and their versions:


tripy
Pillow==8.4.0
imageio==2.14.0


  - Install Python dependencies by running the following command:

`pip install -r requirements.txt`


### GLTFPack:

#### Command For Linux:

`sudo apt-get install -y gltfpack`


#### Command For macOS (using Homebrew):

`brew install gltfpack`


#### For Windows:
**If you have Node.js, run the following command:**

`npm install gltfpack`

-After the installation is complete, try running gltfpack from the local node modules:

`npx gltfpack --version`

***The npx command ensures that you're using the locally installed version of gltfpack.***

**If you encounter an error (Unrecognized option --version), run the following command to execute gltfpack without any options. This should output information about the available commands and the version:**

`npx gltfpack`

-Alternatively, download the executable from the official GitHub releases page:

https://github.com/zeux/meshoptimizer/releases

## You will also need Zlib For Windows:

-Download the Zlib binaries from the official 
website: https://zlib.net/

-Create `C:\Tools` Directory:

Create a folder in root dir named Tools example: `C:\Tools` directory on your system

-Extract the downloaded ZIP file and copy the contents" (DLL files) to `C:\Tools`


# Usage:

**Clone the Repository:**

git clone https://github.com/GreatApe42069/3d-convert_and_compress.git
cd 3d-to-gltf-converter

**Set up Input and Output Folders:**

Open the 3d-convert_and_compress.py file and update the input_folder and output_folder variables with the appropriate paths.
Run the Script:

**Call the file path of your project:**

cd C:\Doginals-main\Doge-Art

**Execute the script using the following command:**

`C:\Python312\python.exe .\3d-convert_and_compress.py`

This script will convert all supported 3D files in the input folder to GLTF and save them in the output folder.

## Additional Notes:
Ensure that your 3D files are located in the specified input folder.

The script uses the gltfpack tool for compression.

Adjust the parameters within the script or experiment with gltfpack options for customization.

Feel free to modify the script based on your specific needs or contribute to its improvement.

# Happy converting!
