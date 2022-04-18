import torch.nn as nn


class FashionMNIST(nn.Module):
    def __init__(self):
        super(FashionMNIST, self).__init__()
        self.conv2 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1)
        self.batchNorm2d = nn.BatchNorm2d(32)
        self.relu = nn.ReLU()
        self.maxPool2d = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = nn.Linear(in_features=169 * 2 * 2 * 2 * 2 * 2, out_features=600)
        self.drop = nn.Dropout2d(0.25)
        self.fc2 = nn.Linear(in_features=600, out_features=120)
        self.fc3 = nn.Linear(in_features=120, out_features=10)

    def forward(self, x):
        out = self.conv2(x)
        out = self.batchNorm2d(out)
        out = self.relu(out)
        out = self.maxPool2d(out)
        out = out.view(out.size(0), -1)
        out = self.fc1(out)
        out = self.drop(out)
        out = self.fc2(out)
        out = self.fc3(out)
        return out