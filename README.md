# DPA-2 预训练模型使用指南

预训练模型的具体使用方法及训练数据，可以在 DPA-2 预训练模型官网找到：
[访问 DPA-2 预训练模型官网](https://aissquare.com/models/detail?pageType=models&name=DPA-2.2.0-v3.0.0b3&id=272)

目前脚本和预训练模型均基于 **DeePMD-Kit v3.0.0b3**，请确保预训练模型版本与 DeePMD-Kit 版本一致。
[访问 DeePMD-Kit v3.0.0b3 发布版本](https://github.com/deepmodeling/deepmd-kit/releases/tag/v3.0.0b3)

## 快速使用

### 1. 描述符参数

请不要修改描述符的参数。如果需要更换预训练模型，请使用 `parma.py` 脚本输出预训练模型的参数，并根据输出的参数自行修改。我提供的 JSON 脚本已经包含了与预训练模型匹配的参数，可以直接使用。

### 2. Multitask JSON 与普通任务 JSON

Multitask 的 JSON 与普通任务 JSON 的核心结构一致，区别在于 `model_dict` 和 `loss_dict` 变成了多个分支的组合。从 `model_dict` 模块开始，您可以根据需要修改任务。
- `"pureknachar"` 是我的任务部分，可以根据您的实际情况进行修改。
- `"Domain_ANI"` 是预训练模型中的一个分支，您可以在 DPA-2 预训练模型官网找到不同分支的名称及训练细节，根据您的实际任务选择。

后续的 `loss_dict` 会与 `model_dict` 一一对应，按需修改即可。

### 3. 训练数据准备

预训练模型的训练数据也可以在官网获取，这些数据已转换为 `dpdata` 格式。如果您在 Multitask 训练中想使用这些数据进行辅助训练（我强烈推荐使用这些数据来辅助训练，避免在训练自己分支时出现过拟合），可以使用我提供的 `path.py` 脚本读取并输出当前目录下所有符合要求的 `dpdata` 文件路径，并保存为 `path.txt`，符合 JSON 输入格式。

随后，您可以使用 `split.py` 脚本将 `path.txt` 分割成训练集和验证集。直接复制这些脚本即可使用。

### 4. 训练或微调（Finetune）

如果您要直接训练，可以使用以下命令：
```bash
dp --pt train input_torch_multitask.json
```
如果是进行微调（finetune），则在命令后添加 --finetune 参数，并指定微调模型的检查点文件：
```bash
dp --pt train input_torch_multitask.json --finetune xxxx.pt
```

由于我们使用的是 Multitask 模型，因此无需在命令中指定使用哪个分支，因为在 JSON 文件中已经显式地指定了所用的分支。

### 注意：DeePMD 的微调模式目前只支持调整模型的最后一层参数，意味着 DPA-2 描述符部分将共享预训练模型中的参数。这也是为什么描述符部分的参数必须与预训练模型中的参数一致。如果出现错误，大多数情况下是由于 DPA-2 描述符参数不一致，请仔细检查。
