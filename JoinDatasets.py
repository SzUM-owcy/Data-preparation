import shutil
import os
import multiprocessing
import Normalisation
import tqdm
from skimage import io 


def process_image(dir_path,file,output_dir,label,copy_version,image_shape):
    src = os.path.join(dir_path, file)
    dst = os.path.join(output_dir, label)
    if not os.path.exists(dst):
        os.makedirs(dst)

    #Copy unchanged
    if(copy_version == "unchanged"):
        shutil.copy2(src, dst)
        return

    #Copy Resized
    if(copy_version == "resize"):
        img = Normalisation.Resize(src,image_shape[0],image_shape[1])
    
    #Copy Cropped
    if(copy_version == "crop"):
        img = Normalisation.CropFromMiddle(src,image_shape[0],image_shape[1]) 
    #io.imshow(img)
    io.imsave(os.path.join(dst,file), img, check_contrast=False)

def join_datasets_with_shape_normalisation(main_dir, output_dir, copy_version, image_shape = (0,0)):
    labels = ["Healthy", "Powdery", "Rust"]
    sets = ["Test", "Train", "Validation"]
    for label in labels:
        for set in sets:
            dir_path = os.path.join(main_dir, set, set, label)
            files = os.listdir(dir_path)
            parallel_input = [(dir_path,file,output_dir,label,copy_version,image_shape) for file in files]
            
            #Parallel
            with multiprocessing.Pool(6) as pool:
                if copy_version != "resized": 
                    parallel_input = tqdm.tqdm(parallel_input, total = len(parallel_input))
                pool.starmap(process_image, parallel_input, chunksize=2)

            #Sequential
            # for inp in parallel_input:
            #     process_image(*inp)
        

# if __name__ == '__main__':
#     path = os.getcwd()
#     join_datasets_with_shape_normalisation(os.path.join(path,"data"), os.path.join(path,"merged-data","unchanged"), "unchanged")
#     print("Finished copying")
#     join_datasets_with_shape_normalisation(os.path.join(path,"data"), os.path.join(path,"merged-data","cropped"), "crop", (2421,1728)) # 2592,1728
#     print("Finished cropping")
#     join_datasets_with_shape_normalisation(os.path.join(path,"data"), os.path.join(path,"merged-data","resized"), "resize", (3982,2700))
#     print("Finished resizing")