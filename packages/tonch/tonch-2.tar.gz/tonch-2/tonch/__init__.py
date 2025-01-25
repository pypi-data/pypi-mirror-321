import pyperclip as pc

class torcn:
    def imports():
        s = '''import pandas as pd
    import numpy as np

    import torch
    from torch import nn, optim
    import torch.nn.functional as F
    from torch.utils.data import Dataset, DataLoader, TensorDataset, random_split
    from torchvision import transforms
    from torchvision.datasets import ImageFolder

    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler, OneHotEncoder
    from sklearn.compose import ColumnTransformer
    from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, f1_score


    import matplotlib.pyplot as plt
        '''
        return pc.copy(s)

    def image_dataset_load():
        s = '''transform = transforms.Compose([transforms.ToTensor(),
                                    transforms.Resize((300, 300))
                                    ])
    dataset = ImageFolder(root='images/cat_breeds_4', transform=transform)
    dataloader = DataLoader(dataset, batch_size = 32, shuffle = False)
        '''
        return pc.copy(s)

    def image_dataset_normalization():
        s = '''mean = torch.zeros(3)
    std = torch.zeros(3)
    total_images = 0

    for images, labels in dataloader:
    batch_samples = images.size(0)
    images = images.flatten(2)
    mean += images.mean(2).sum(0)
    std += images.std(2).sum(0)
    total_images += batch_samples
    mean /= total_images
    std /= total_images

    transform = transforms.Compose([transforms.ToTensor(),
                                    transforms.Resize((300, 300)),
                                    transforms.Normalize(mean = mean, std = std)])
    dataset = ImageFolder(root='images/cat_breeds_4', transform=transform)
    dataloader = DataLoader(dataset, batch_size = 32, shuffle = False)
        '''
        return pc.copy(s)

    def image_accuracy():
        s = '''def accuracy(data_loader, model, device):
        y_pred = []
        y_true = []

        model.eval()
        with torch.no_grad():
        for X_batch, y_batch in data_loader:
            X_batch, y_batch = X_batch.to(device), y_batch.to(device)
            outputs = model(X_batch)
            predicted = torch.argmax(outputs, 1)
            y_pred.extend(predicted.cpu().numpy())
            y_true.extend(y_batch.cpu().numpy())
        return accuracy_score(y_true, y_pred)
        '''
        return pc.copy(s)

    def train_with_accuracy():
        s = '''optimizer = optim.Adam(model.parameters(), lr = 0.00001)
    loss_function = nn.CrossEntropyLoss()
    train_losses = []
    test_accuracy = []
    train_accuracy = []
    model.train()
    for epoch in range(10):
        loss_for_epoch = 0
        for X_batch, y_batch in train_loader:
            X_batch, y_batch = X_batch.to(device), y_batch.to(device)
            predict = model(X_batch)
            loss = loss_function(predict, y_batch)
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
            loss_for_epoch += loss.item()
        loss_for_epoch /= len(train_loader)
        train_losses.append(loss_for_epoch)
        train_accuracy_for_epoch = accuracy(train_loader, model, device)
        test_accuracy_for_epoch = accuracy(test_loader, model, device)
        train_accuracy.append(train_accuracy_for_epoch)
        test_accuracy.append(test_accuracy_for_epoch)
        if epoch % 1 == 0:
            print(f"Epoch: {epoch} | Train loss for epoch: {loss_for_epoch} | Train accuracy: {train_accuracy_for_epoch} | Test accuracy: {test_accuracy_for_epoch}")
        '''
        return pc.copy(s)

    def parameters_count():
        s = '''print(sum(p.numel() for p in model.parameters() if p.requires_grad))
        '''
        return pc.copy(s)


    def show_images_with_predict():
        s = '''def show_examples(model, dataloader, mean, std, k = 5):
        data_iter = iter(dataloader)
        images, y_true = next(data_iter)
        images, y_true = images.to(device), y_true.to(device)
        classes = test_dataset.dataset.classes
        denormalize = transforms.Normalize((-1 * mean / std), (1.0 / std))

        model.eval()
        with torch.no_grad():
            outputs = model(images)
            predicted = torch.argmax(outputs, 1)

        num_images = k
        plt.figure(figsize=(11, 11))
        for i in range(num_images):
            plt.subplot(2, 3, i + 1)
            plt.imshow(denormalize(images[i].cpu()).clamp(0, 1).numpy().transpose(1, 2, 0))
            plt.axis('off')
            plt.title(f'True: {classes[y_true[i].item()]} \nPredict: {classes[predicted[i].item()]}')
        plt.show()
        '''
        return pc.copy(s)

    def cnn_model():
        s = '''model = nn.Sequential(
        nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2, stride=2),

        nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2, stride=2),

        nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2, stride=2),

        nn.Flatten(),
        nn.Linear(64 * 37 * 37, 128),
        nn.ReLU(),
        nn.Linear(128, 64),
        nn.ReLU(),
        nn.Linear(64, 4)
    ).to(device)
        '''
        return pc.copy(s)

    def visualize_conv1_activations():
        s = '''def visualize_conv1_activations(model, dataloader):
        model.eval()
        with torch.no_grad():
            for input_images, labels in dataloader:
                input_image = input_images[0]  # Берем первую картинку в батче

                activations = model[0](input_image.unsqueeze(0).to(device))

                num_filters = activations.size(1)
                fig = plt.figure(figsize = (20, 10))
                for i in range(num_filters):
                    plt.subplot(4, 4, i + 1)
                    plt.imshow(activations[0][i].cpu(), cmap = 'gray')
                    plt.axis('off')
                plt.show()
                break

    visualize_conv1_activations(model, test_loader)
        '''
        return pc.copy(s)

    def cnn_dropout_model():
        s = '''model = nn.Sequential(
        nn.Conv2d(3, 32, kernel_size = 5),
        nn.MaxPool2d(2),
        nn.ReLU(),
        nn.Conv2d(32, 64, kernel_size = 5),
        nn.Dropout2d(0.5),
        nn.MaxPool2d(2),
        nn.ReLU(),
        nn.Flatten(1),
        nn.Linear(64 * 22 * 22, 50),
        nn.ReLU(),
        nn.Dropout(0.5),
        nn.Linear(50, 25),
        nn.ReLU(),
        nn.Dropout(0.5),
        nn.Linear(25, 10)
    ).to(device)
        '''
        return pc.copy(s)

    def test_loss():
        s = '''def test_loss(model, test_loader, device):
    model.eval()
    loss_for_epoch = 0
    with torch.no_grad():
    for X_batch, y_batch in test_loader:
    X_batch, y_batch = X_batch.to(device), y_batch.to(device)
    predict = model(X_batch)
    loss = loss_function(predict, y_batch)
    loss_for_epoch += loss.item()
    loss_for_epoch /= len(test_loader)
    return loss_for_epoch
        '''
        return pc.copy(s)


    def collect_y_pred_y_true():
        s = '''y_pred = []
    y_true = []

    model.eval()
    with torch.no_grad():
        for X_batch, y_batch in test_loader:
            X_batch, y_batch = X_batch.to(device), y_batch.to(device)
            outputs = model(X_batch)
            predicted = torch.argmax(outputs, 1)
            y_pred.extend(predicted.cpu().numpy())
            y_true.extend(y_batch.cpu().numpy())
    y_pred = torch.tensor(y_pred)
    y_true = torch.tensor(y_true)
        '''
        return pc.copy(s)

    def heatmap():
        s = '''y_pred = []
    y_true = []

    model.eval()
    with torch.no_grad():
        for X_batch, y_batch in test_loader:
            X_batch, y_batch = X_batch.to(device), y_batch.to(device)
            outputs = model(X_batch)
            predicted = torch.argmax(outputs, 1)
            y_pred.extend(predicted.cpu().numpy())
            y_true.extend(y_batch.cpu().numpy())
    y_pred = torch.tensor(y_pred)
    y_true = torch.tensor(y_true)
    sns.heatmap(confusion_matrix(y_true, y_pred), annot = True)
    print(classification_report(y_true, y_pred))
        '''
        return pc.copy(s)
        
    def save_load_model():
        s = '''torch.save(model.state_dict(), 'model.pth')
    torch.save(optimizer.state_dict(), 'optimizer.pth')

    model.load_state_dict(torch.load('model.pth', weights_only=True))
        '''
        return pc.copy(s)    

    def create_dataset():
        s = '''class DiamondsDataset(Dataset):
    def __init__(self, data):
        for col in data.columns:
        if data[col].dtype not in ('float64', 'int64'):
            data = data.drop(col, axis = 1)
        self.X = torch.tensor(data.drop('price', axis = 1).values, dtype = torch.float)
        self.y = torch.tensor(data['price'].values, dtype = torch.float)

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

    dataset = DiamondsDataset(df)
    train_size = int(0.8 * len(dataset))  # 80% для обучения
    test_size = len(dataset) - train_size  # 20% для тестирования
    train_dataset, test_dataset = random_split(dataset, [train_size, test_size])
    print(len(train_dataset))
    dataloader = DataLoader(train_dataset, 256, shuffle = True)
    print(len(dataloader))
        '''
        return pc.copy(s)    

    def create_dataset_with_transform():
        s = '''class DiamondsDataset(Dataset):
    def __init__(self, data, transform):
        self.transform = transform
        self.X = data.drop('price', axis = 1).values
        self.y = data['price'].values

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        sample = (self.X[idx], self.y[idx])
        if self.transform:
        sample = self.transform(sample)
        return sample

    class ToTensorTransform:
    def __call__(self, sample):
        X, y = sample
        # <преобразование X и y в тензоры>
        X = torch.from_numpy(X).type(torch.float)
        y = torch.tensor(y, dtype = torch.float)
        return X, y

    to_tensor = ToTensorTransform()
    dataset = DiamondsDataset(df, transforms.Compose([to_tensor]))
    dataloader = DataLoader(dataset, 256, shuffle = True)
        '''
        return pc.copy(s)   

    def labelencoder_to_string_cols():
        s = '''label_encoder = LabelEncoder()
    for col in df:
    if df[col].dtype == object:
        df[col] = label_encoder.fit_transform(df[col])
    df.head()
        '''
        return pc.copy(s)    

    def standardscaler_to_num_cols():
        s = '''standard_scaler = StandardScaler()
    for col in df:
    if df[col].dtype == 'float':
        df[col] = standard_scaler.fit_transform(np.array(df[col]).reshape(-1, 1))
    df.head()
        '''
        return pc.copy(s)    

    def get_dummies():
        s = '''df_one_hot_encoded = pd.get_dummies(df, columns = ['cut', 'color', 'clarity'], dtype = int)
    df_one_hot_encoded.head()
        '''
        return pc.copy(s)    

    def linear_model_batch_normalization():
        s = '''my = nn.Sequential(
        nn.Linear(dataloader.dataset.dataset.X.shape[1], 250),
        nn.BatchNorm1d(250),
        nn.ReLU(),
        nn.Linear(250, 500),
        nn.BatchNorm1d(500),
        nn.ReLU(),
        nn.Linear(500, 250),
        nn.BatchNorm1d(250),
        nn.ReLU(),
        nn.Linear(250, 50),
        nn.BatchNorm1d(50),
        nn.ReLU(),
        nn.Linear(50, 1)
    ).to(device)
        '''
        return pc.copy(s)    

    def pretrained_model_import():
        s = '''import torchvision.models as models
    model = models.vgg16(weights='IMAGENET1K_V1')
    print(model, '\n')

    layers_count = sum(1 for module in model.modules() if (isinstance(module, nn.Conv2d) or isinstance(module, nn.Linear)))
    print(f'Кол-во слоев: {layers_count}\n')

    params_count = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f'Количество настраиваемых параметров: {params_count}')
        '''
        return pc.copy(s)   

    def pretrained_model_freeze_all():
        s = '''for param in model.parameters():
        param.requires_grad = False
        '''
        return pc.copy(s)   

    def pretrained_model_freeze_all_conv():
        s = '''# Заморозить все сверточные слои, кроме последнего
    for i, layer in enumerate(model.features):
        if isinstance(layer, torch.nn.Conv2d):
            if i < (len(model.features) - 1):  # Все слои, кроме последнего Conv
                for param in layer.parameters():
                    param.requires_grad = False
        '''
        return pc.copy(s)   

    def cnn_full_solution():
        s = '''import pandas as pd
    import numpy as np

    import torch
    from torch import nn, optim
    from torch.utils.data import Dataset, DataLoader, TensorDataset

    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler, OneHotEncoder
    from sklearn.compose import ColumnTransformer
    from sklearn.metrics import accuracy_score
    from tqdm import tqdm

    import matplotlib.pyplot as plt

    data_dir = 'chars'

    # Предобработка изображений
    transform = transforms.Compose([
        transforms.Resize([128, 128]),
        transforms.ToTensor()
    ])

    # Загрузка данных
    full_dataset = ImageFolder(data_dir, transform=transform)

    train_size = int(0.7 * len(full_dataset))
    test_size = len(full_dataset) - train_size
    train_dataset, test_dataset = torch.utils.data.random_split(full_dataset, [train_size, test_size])

    device = torch.device('cpu')

    model = nn.Sequential(
        nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2, stride=2),

        nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2, stride=2),

        nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2, stride=2),

        nn.Flatten(),
        nn.Linear(16384, 128),
        nn.ReLU(),
        nn.Dropout(),
        nn.Linear(128, 64),
        nn.ReLU(),
        nn.Dropout(),
        nn.Linear(64, 2)
    ).to(device)

    def accuracy(data_loader, model, device):
        y_pred = []
        y_true = []

        model.eval()
        with torch.no_grad():
        for X_batch, y_batch in data_loader:
            X_batch, y_batch = X_batch.to(device), y_batch.to(device)
            outputs = model(X_batch)
            predicted = torch.argmax(outputs, 1)
            y_pred.extend(predicted.cpu().numpy())
            y_true.extend(y_batch.cpu().numpy())
        return accuracy_score(y_true, y_pred)

    batch_size = 32
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size)

    num_epochs = 40
    print_every = 1

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.AdamW(params=model.parameters(), lr = 0.001)
    train_losses = []
    test_accuracy = []
    train_accuracy = []
    model.train()
    for epoch in tqdm(range(num_epochs)):
        loss_for_epoch = 0
        for X_batch, y_batch in train_loader:
            X_batch, y_batch = X_batch.to(device), y_batch.to(device)
            predict = model(X_batch)
            loss = criterion(predict, y_batch)
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
            loss_for_epoch += loss.item()
        loss_for_epoch /= len(train_loader)
        train_losses.append(loss_for_epoch)
        train_accuracy_for_epoch = accuracy(train_loader, model, device)
        test_accuracy_for_epoch = accuracy(test_loader, model, device)
        train_accuracy.append(train_accuracy_for_epoch)
        test_accuracy.append(test_accuracy_for_epoch)
        if epoch % 1 == 0:
            print(f"Epoch: {epoch} | Train loss for epoch: {loss_for_epoch} | Train accuracy: {train_accuracy_for_epoch} | Test accuracy: {test_accuracy_for_epoch}")
        '''
        return pc.copy(s)


    def pretrained_model_import():
        s = '''import torchvision.models as models
    model = models.vgg16(weights='IMAGENET1K_V1')
    print(model, '\n')

    layers_count = sum(1 for module in model.modules() if (isinstance(module, nn.Conv2d) or isinstance(module, nn.Linear)))
    print(f'Кол-во слоев: {layers_count}\n')

    params_count = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f'Количество настраиваемых параметров: {params_count}')
        '''
        return pc.copy(s)   

    def adam_model_train():
        s = '''batch_size = 32
    epochs = 100
    print_every = 20

    criterion = nn.MSELoss()
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    adamw_model = nn.Sequential(
        nn.Linear(train_dataset.tensors[0].shape[1], 64),
        nn.ReLU(),
        nn.Linear(64, 256),
        nn.ReLU(),
        nn.Linear(256, 128),
        nn.ReLU(),
        nn.Linear(128, 32),
        nn.ReLU(),
        nn.Linear(32, 1)
    )

    adamw_optimizer = optim.Adam(params=adamw_model.parameters(), lr = 0.001)
    adamw_losses = []
    for epoch in range(epochs):
        epoch_loss = 0
        model.train()
        for batch_X, batch_y in train_loader:
            adamw_optimizer.zero_grad()
            outputs = adamw_model(batch_X)
            loss = criterion(outputs, batch_y.reshape(-1, 1))
            loss.backward()
            adamw_optimizer.step()
            epoch_loss += loss.item()
        epoch_loss /= len(train_loader)
        adamw_losses.append(epoch_loss)

        if (epoch + 1) % print_every == 0:
            y_true, y_pred = collect(adamw_model, train_loader)
            y_true_test, y_pred_test = collect(adamw_model, test_loader)
            
            train_r2 = r2_score(y_true, y_pred)
            test_r2 = r2_score(y_true_test, y_pred_test)
            
            train_mae = mean_absolute_error(y_true, y_pred)
            test_mae = mean_absolute_error(y_true_test, y_pred_test)
            print(f'Epoch {epoch+1}/{epochs}, Loss: {epoch_loss:.8f}, Train R2: {train_r2}, Test R2: {test_r2}, Train MAE: {train_mae}, Test MAE: {test_mae}')
        '''
        return pc.copy(s)   

    def class_weights():
        s = '''from sklearn.utils.class_weight import compute_class_weight

    classes = np.array([0, 1])  

    # Compute class weights
    class_weights = compute_class_weight(class_weight='balanced', classes=classes, y=y)

    for i, weight in enumerate(class_weights):
        print(f"Class {classes[i]}: {weight}")
        '''
        return pc.copy(s)  
