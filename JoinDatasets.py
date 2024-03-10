import shutil
import os

main_dir = f"D:\\Informatyka\\Mgr\\SEM1\\SZUM\\archive" #input()
output = f"D:\\Informatyka\\Mgr\\SEM1\\SZUM\\prepared" #input()


labels = ["Healthy","Powdery","Rust"]
for label in labels:
    for set in ["Test","Train","Validation"]:
        dir_path = os.path.join(main_dir,set,set,label)    
        files = os.listdir(dir_path)
        for file in files:
            src = os.path.join(dir_path,file)
            dst = os.path.join(output,label)
            if not os.path.exists(dst):
                os.mkdir(dst)
            
            
            shutil.copy2(src,dst)
            
        pass