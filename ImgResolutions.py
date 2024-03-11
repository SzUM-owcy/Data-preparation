import os

def res_image (filename):
    with open(filename, 'rb') as file_image:
            file_image.seek (163)

            a = file_image.read (2)

            height = (a [0] << 8) + a [1]

            a = file_image.read (2)

            width = (a [0] << 8) + a [1]
            print("The resolution of the given image is:", width, "x", height)

res_image("image1.jpeg")
labels = ["Healthy","Powdery","Rust"]
sets = ["Test","Train","Validation"]
for label in labels:
    for set in sets:
        dir_path = os.path.join(main_dir,set,set,label)    
        files = os.listdir(dir_path)
        for file in files:
            src = os.path.join(dir_path,file)
            dst = os.path.join(output,label)
            if not os.path.exists(dst):
                os.mkdir(dst)
            
            
            shutil.copy2(src,dst)
            
        pass