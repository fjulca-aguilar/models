from create_graphics_tf_record import generate_tf_record_for_files

dataset_directories = ['object_detection/data/math768_min_sides'] #['object_detection/data/math768', 'object_detection/data/math1024']
file_names = ['math_train_set', 'math_val_set' , 'math_test_set']
outputs_end = ['_train.record', '_val.record' , '_test.record']
label_map_path = 'object_detection/data/math_label_map.pbtxt'

for ds in dataset_directories:
    print(ds)
    for i, fn in enumerate(file_names):
        print(fn)
        generate_tf_record_for_files(ds + outputs_end[i], label_map_path, file_names[i], ds)


