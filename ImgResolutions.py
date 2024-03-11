import os
from collections import Counter

def res_image (filename):
    with open(filename, 'rb') as file_image:
            file_image.seek (163)
            a = file_image.read (2)
            height = (a [0] << 8) + a [1]
            a = file_image.read (2)
            width = (a [0] << 8) + a [1]
            return (width,height)
            print("The resolution of the given image is:", width, "x", height)

main_dir = "merged-data"
labels = ["Healthy","Powdery","Rust"]

all_widths = []
all_heights = []

for label in labels:
    dir_path = os.path.join(main_dir,label)    
    files = os.listdir(dir_path)
    widths = []
    heights = []
    for file in files:
        src = os.path.join(dir_path,file)
        w, h = res_image(src)
        widths.append(w)
        heights.append(h)
        all_widths.append(w)
        all_heights.append(h)
        
    print(label, " Mean Width:", sum(widths)/len(widths))
    print(label, "Mean Height:", sum(heights)/len(heights))
    print(label, "Widths Count:",Counter(widths))
    print(label, "Heights Count:",Counter(heights))

print("Mean Width:", sum(all_widths)/len(all_widths))
print("Mean Height:", sum(all_heights)/len(all_heights))
print("Widths Count:",Counter(all_widths))
print("Heights Count:",Counter(all_heights))