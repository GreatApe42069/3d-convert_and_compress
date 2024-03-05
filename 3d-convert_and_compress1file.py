import os
import subprocess
import shutil

def convert_to_gltf(input_file, output_file):
    print(f"Converting {input_file} to {output_file}")
    try:
        # Get the absolute path to the "npx" command
        npx_path = shutil.which("npx")

        # Ensure gltf-pipeline is in your system's PATH or provide the full path if not
        subprocess.run([npx_path, "gltf-pipeline", "-i", input_file, "-o", output_file, "--embed", "--draco.compressMeshes"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error converting {input_file} to gltf: {e}")
    else:
        print("Conversion complete")

def main():
    input_folder = r"C:\Doginals-main\Dogemap-Dogs"  # Set your input folder here
    output_folder = r"C:\Doginals-main\Dogemap-Dogs\Converted"  # Set your output folder here

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")

    for file in os.listdir(input_folder):
        if file.lower().endswith((".obj", ".fbx", ".usdz", ".glb", ".mp4", ".png")):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".gltf")

            print(f"Processing: {input_path}")
            convert_to_gltf(input_path, output_path)
            print(f"Conversion of {input_path} complete. Output: {output_path}")

if __name__ == "__main__":
    main()
