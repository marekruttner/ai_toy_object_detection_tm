import os
import time
import shutil
import zipfile
import glob

dir_path = '/media/pi/' #path to where OS automount USB drives
target_copy_dir = '/home/pi/ai_toy_object_detection_tm/' #where it will be coppied to
name_of_file = ''.join(glob.glob('./converted_keras???.zip')) #starting characters in name of our file eg our file is named "testfile1.txt" we want every file that starts with "testfile" this file will be selected

infinite_loop = 1 #make zero to stop after one filecopy

#look through the usb file for desired file == name_of_file
"""
def look_through (directory): #look through the newly dicovered flash drive for our file
    file_list = os.listdir(directory)
    print(file_list)
    found_file = ""
    for file in file_list:
        if (file.startswith(name_of_file)):
            found_file = file
            print(found_file)
            return found_file
    return 0
"""
name_of_file = found_file

def delete_copy(target_to_copy): #target must be a complete path
    #first scan target directory for files with same name and delete them
    scan_result = look_through(target_copy_dir)
    print('delete copy scan result: ' + str(scan_result))
    while ( 0 != scan_result):
        print('found: ' + scan_result)
        scan_result_path = target_copy_dir + scan_result
        if os.path.isfile(scan_result_path):
            os.remove(scan_result_path)
            print('file has been deleted')
        else:
            print(scan_result_path + ' is not a path')
            print(os.path.isfile(scan_result_path))
        scan_result = look_through(target_copy_dir)
    
    #now copy the file to the prepared directory
    shutil.copy2(target_to_copy, target_copy_dir)
    with zipfile.ZipFile(name_of_file, 'r') as zip_ref:
        zip_ref.extractall(target_copy_dir)
    print('copied')



cycle_counter = 0

dir_list_old = []
dir_list_new = []
usb_dir = ""
new_item = 1



while new_item == 1: 
    
    #list the whole dir_path directory
    res = os.listdir(dir_path)
    
    #only look for sdX items
    for word in res:
        #if word.startswith('sd'):
            #append the sd items to a list
        dir_list_new.append(word)
    
    #firts run fill both lists
    if cycle_counter == 0:
        dir_list_old = dir_list_new
    
    #compare new and old lists
    for nword in dir_list_new:
        matches = 0
        #print(nword)
        for oword in dir_list_old:
            
            if oword == nword:
                matches = 1
                #print(nword + " vs " + oword + " res = " + str(matches))
                break
            #print(nword + " vs " + oword + " res = " + str(matches))
            
        if matches == 0:
            #found new item
            
            print("new item found")
            usb_dir=nword
            print(usb_dir)
            found_file = look_through(dir_path + "/" + usb_dir)
            if(found_file == 0):
                print('no target file in USB directory')
            else:
                delete_copy(dir_path + "/" + usb_dir + "/" + found_file) 
            new_item = infinite_loop
            break
        #print("------------------")

    dir_list_old = dir_list_new
    dir_list_new = []
    cycle_counter += 1
    time.sleep(1)
    print(cycle_counter)
  
print("finsihed")


