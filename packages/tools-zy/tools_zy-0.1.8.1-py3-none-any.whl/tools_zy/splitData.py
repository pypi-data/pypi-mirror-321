import os
import random
import time
import shutil
from . import utils

def check_sequential_folders(folder_path):
    folder_list = sorted(os.listdir(folder_path))
    count = 0
    for _, folder_name in enumerate(folder_list):
        expected_name = str(count)
        if folder_name == expected_name:
            count += 1
    return count

def split_classifid_images(top_folder, out_folder, split_ratio, format=".bmp", num_class=None):
    """
    top_folder: 图片文件夹的根目录，里面有多个数字命名的子文件夹
    """
    if num_class is None:
        num_class = check_sequential_folders(top_folder)
        print(f"{top_folder} has num_class: {num_class}")
    # 创建输出文件夹 
    train_path = os.path.join(out_folder, "train")
    val_path = os.path.join(out_folder, "val")
    test_path = os.path.join(out_folder, "test")
    os.makedirs(train_path, exist_ok=True)
    os.makedirs(val_path, exist_ok=True)
    os.makedirs(test_path, exist_ok=True)
    # 
    train, val, test = split_ratio
    for i in range(num_class):
        class_num = str(i)
        img_folder = os.path.join(top_folder, class_num)
        all_name = os.listdir(img_folder)
        random.shuffle(all_name)  # 打乱顺序
        train_names = all_name[:int(train * len(all_name))]
        val_names = all_name[int(train * len(all_name)):int((train + val) * len(all_name))]
        test_names = all_name[int((train + val) * len(all_name)):]
        utils.copy_files(img_folder, "/".join([train_path, class_num]), train_names, format)
        utils.copy_files(img_folder, "/".join([val_path, class_num]), val_names, format)
        utils.copy_files(img_folder, "/".join([test_path, class_num]), test_names, format)



def split_labelmes(labelme_folder: str, split_ratio: tuple = (0.85, 0.1, 0.05), format='.jpg'):
    random.seed(time.time())

    # 获取源文件夹中的所有JPG文件
    pics = [f for f in os.listdir(labelme_folder) if f.endswith(format)]
    # 随机打乱并划分JPG文件列表
    random.shuffle(pics)
    total_files = len(pics)
    train_ratio, val_ratio, test_ratio = split_ratio
    train_cnt, val_cnt = int(total_files * train_ratio), int(total_files * val_ratio)
    train_imgs = pics[:train_cnt]
    val_imgs = pics[train_cnt:train_cnt + val_cnt]
    test_imgs = pics[train_cnt + val_cnt:]
    train_json = [pic.replace(pic.split('.')[-1], 'json') for pic in train_imgs]
    val_json = [pic.replace(pic.split('.')[-1], 'json') for pic in val_imgs]
    test_json = [pic.replace(pic.split('.')[-1], 'json') for pic in test_imgs]

    # 移动文件到相应的目标文件夹
    split_folder = labelme_folder + '_split'
    utils.copy_files(labelme_folder, split_folder + '/train', train_imgs)
    utils.copy_files(labelme_folder, split_folder + '/train', train_json)
    utils.copy_files(labelme_folder, split_folder + '/val', val_imgs)
    utils.copy_files(labelme_folder, split_folder + '/val', val_json)
    utils.copy_files(labelme_folder, split_folder + '/test', test_imgs)
    utils.copy_files(labelme_folder, split_folder + '/test', test_json)

    print(f"split pic and json to:\n"
          f"==>{split_folder}")
    return split_folder
