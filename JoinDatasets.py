import shutil
import os

labels = ["Healthy", "Powdery", "Rust"]
sets = ["Test", "Train", "Validation"]


def join_data_sets(main_dir, output_dir):
    for label in labels:
        for set in sets:
            dir_path = os.path.join(main_dir, set, set, label)
            files = os.listdir(dir_path)
            for file in files:
                src = os.path.join(dir_path, file)
                dst = os.path.join(output_dir, label)
                if not os.path.exists(dst):
                    os.mkdir(dst)

                shutil.copy2(src, dst)

            pass
