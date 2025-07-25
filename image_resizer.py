import os
from PIL import Image
input_folder = r'C:\Users\91700\Bhub\task7\images'
output_folder = r'C:\Users\91700\Bhub\task7\resized_images'
target_size = (300, 600)
print("Script running from:", os.getcwd())
if not os.path.exists(input_folder):
    print(f"Input folder does not exist: {input_folder}")
    exit()
os.makedirs(output_folder, exist_ok=True)
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        try:
            with Image.open(input_path) as img:
                img_resized = img.resize(target_size)
                img_resized.save(output_path)
                print(f"Resized: {filename}")
        except Exception as e:
            print(f"Error {filename}: {e}")
