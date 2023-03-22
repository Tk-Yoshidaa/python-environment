from sklearn.model_selection import StratifiedKFold
from torch.utils.data import Dataset, Subset

import numpy as np

N = 10
solution_data_nor = np.empty((N, 3))
score_size_Tmean = np.empty((N, 5))
score_weight = np.empty((N, 1))
score_data = np.empty((N, 3))
label = np.array(range(N)) % 3 == 0

class NEDO(Dataset):
    def __init__(self, data, condition, weight, score, label):

        self.data = data.astype('float32')
        self.weight = weight.astype('float32')
        self.condition = condition.astype('float32')
        self.score = score.astype('float32')
        self.label = label.astype('float32')
        self.outdata = []

        for i in range(self.data.shape[0]):
          self.outdata.append([self.data[i], self.condition[i], self.weight[i], self.score[i], self.label[i]])
        
    def __getitem__(self, index):
        transform = transforms.Compose([transforms.ToTensor()])
        outdata1 = transform(self.outdata[index][0])
        outdata2 = torch.Tensor(self.outdata[index][1])
        outdata3 = torch.FloatTensor([self.outdata[index][2]])
        outdata4 = torch.FloatTensor([self.outdata[index][3]])
        outdata5 = torch.LongTensor([self.outdata[index][4].astype(int)])
        return outdata1, outdata2, outdata3, outdata4, outdata5

    def __len__(self):
        """csv の行数を返す。
        """
        return len(self.outdata)

dataset = NEDO(solution_data_nor, score_size_Tmean, score_weight, score_data, label)

hyperparamer_list = [
    {'learning_rate': 0.5, 'num_epochs': 10},
    {'learning_rate': 0.4, 'num_epochs': 10},
    {'learning_rate': 0.3, 'num_epochs': 3},
    {'learning_rate': 0.2, 'num_epochs': 2},
]

cv = StratifiedKFold(n_splits=5)
for i, (train_index_outer, test_index) in enumerate(cv.split(dataset, label)):

    print('outer:', i, train_index_outer, test_index)

    train_dataset_outer = Subset(dataset, train_index_outer)
    label_outer = label[train_index_outer]

    cv_inner = StratifiedKFold(n_splits=4)

    for j, (train_index_inner, valid_index) in enumerate(cv_inner.split(train_dataset_outer, label_outer)):

        print('inner:', j, train_index_inner, valid_index)

        train_dataset_inner = Subset(train_dataset_outer, train_index_inner)

        print(train_dataset_inner)


        valid_error_list = []
        for k, hyperparamer in enumerate(hyperparamer_list):

            model -= ...
            optimizer = Optimizer(learning_rate=hyperparamer['learning_rate'])

            for epoch in range(num_epochs):

                one_epoch(...)


            valid_error = ...
            valid_error_list.append(valid_error)

        best_hp_index = argmin(valid_error_list)

        break
    break
