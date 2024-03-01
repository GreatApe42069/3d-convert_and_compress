import os
import subprocess

def convert_to_gltf(input_file, output_file):
    subprocess.run(["gltfpack", "-i", input_file, "-o", output_file])

def main():
    input_folder = "C:\Doginals-main\Ape-srtact-Apes"  # Set your input folder here
    output_folder = "C:\Doginals-main\Ape-srtact-Apes\Converted"  # Set your output folder here

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(input_folder):
        if file.endswith((".obj", ".fbx", ".usdz")):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".gltf")

            convert_to_gltf(input_path, output_path)

if __name__ == "__main__":
    main()
