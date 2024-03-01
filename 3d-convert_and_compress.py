import os
import subprocess

def convert_to_gltf(input_file, output_file):
    print(f"Converting {input_file} to {output_file}")
    try:
        # Redirect subprocess output to a file
        with open('conversion_log.txt', 'a') as log_file:
            subprocess.run(["npx", "gltfpack", "-i", input_file, "-o", output_file], stdout=log_file, stderr=log_file)
    except subprocess.CalledProcessError as e:
        print(f"Error converting {input_file} to gltf: {e}")
    else:
        print("Conversion complete")

def main():
    input_folder = r"C:\Doginals-main\Doge-Art"  # Set your input folder here
    output_folder = r"C:\Doginals-main\Doge-Art\Converted"  # Set your output folder here

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(input_folder):
        if file.endswith((".obj", ".fbx", ".usdz", ".glb")):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".gltf")

            convert_to_gltf(input_path, output_path)

if __name__ == "__main__":
    main()
