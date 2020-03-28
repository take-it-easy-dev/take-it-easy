import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class OneDimensionalLinearRegression(nn.Module):
    def __init__(self):
        super(OneDimensionalLinearRegression, self).__init__()
        self.linear = nn.Linear(in_features=1, out_features=1, bias=True)

    def forward(self, input: torch.Tensor) -> torch.Tensor:
        return self.linear(input=input)


net = OneDimensionalLinearRegression()
net.zero_grad()
input = torch.linspace(start=0., end=10., steps=500).view(-1, 1)
target = input * 2. + 1.
optimizer = optim.SGD(net.parameters(), lr=0.01)
for i in range(2000):
    optimizer.zero_grad()
    output = net(input)
    loss = F.mse_loss(output, target=target)
    loss.backward()
    optimizer.step()

print(f"i: {i}\nweight: {net.linear.weight}\nloss: {loss}\nbias: {net.linear.bias}\n=======")
