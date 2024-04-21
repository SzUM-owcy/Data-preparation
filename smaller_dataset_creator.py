from PIL import Image
import os

labels = ["Healthy", "Powdery", "Rust"]
sets = ["test", "train", "val"]

# BEFORE RUNNING THIS CODE, CREATE THE DIRECTORIES (splitX_new) and then inside it all the needed directories!!!!!!


def read_files(src_dir, new_dir):
    for label in labels:
        for set in sets:
            dir_path = src_dir + set + '/' + label
            files = os.listdir(dir_path)
            os.makedirs(new_dir + set + '/' + label,exist_ok=True)
            for file in files:
                src = dir_path + '/' + file

                foo = Image.open(src)

                # downsize the image with an ANTIALIAS filter (gives the highest quality)
                foo = foo.resize((225, 225), Image.LANCZOS)

                new_filepath = new_dir + set + '/' + label + '/' + file
                foo.save(new_filepath, optimize=True, quality=95)


main_dir = 'splits/split3/'
new_dir = 'splits/split3_new/'

read_files(main_dir, new_dir)
