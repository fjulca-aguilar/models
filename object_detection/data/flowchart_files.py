import numpy as np

train_fraction = 0.8
np.random.seed(1)

with open('object_detection/data/flowchart_train.txt') as f:
	train_files = f.readlines()

train_files = [x.strip() for x in train_files]
num_train = int(train_fraction * len(train_files))
np.random.shuffle(train_files)
train_set = train_files[:num_train]
val_set = train_files[num_train:]

with open('object_detection/data/flowchart_test.txt') as f:
	test_set = f.readlines()
test_set = [x.strip() for x in test_set]


if __name__ == '__main__':

	print(len(train_set))
	print(len(val_set))
	print(len(test_set))
	print(train_set[:10])
	print(val_set[:10])
	print(test_set[:10])





