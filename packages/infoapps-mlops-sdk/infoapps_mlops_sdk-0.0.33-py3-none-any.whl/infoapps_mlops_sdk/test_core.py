import os
import unittest

import sys
from turihub import User

# Set environment variables programmatically, needed so core code sets up correct logging for testing notebook
os.environ["IN_DEV_MODE"] = "true"  # Set to "false" if not in dev mode
os.environ["USE_BETA_URL"] = "true"  # Set to "true" to use the beta URL

from infoapps_mlops_sdk.src.infoapps_mlops_sdk.core import PlatformType, init_experiment, HubPlatform


class TestHubPlatformReal(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load the API token from an environment variable
        cls.api_token = os.getenv("MLOPS_BIGSUR_TURI_API_KEY")
        cls.project_name = "infoapps_mlops_devel"  # Use a dedicated test project

        # Ensure that the token is available
        if cls.api_token is None:
            raise ValueError("Please set the MLOPS_BIGSUR_TURI_API_KEY environment variable")

        # Initialize the HubPlatform with a real token
        cls.platform = HubPlatform(api_token=cls.api_token)

    @unittest.skip("Skipping test_project_initialization.")
    def test_project_initialization(self):
        # Test the project method with a real API call
        project = self.platform.getHubInstance().project(self.project_name)
        self.assertIsNotNone(project)
        self.assertEqual(project.id, self.project_name)

    @unittest.skip("Skipping test_experiments_through_delegation.")
    def test_experiments_through_delegation(self):
        # Accessing Hub methods directly through delegation
        project = self.platform.project(self.project_name)  # Forwarded to Hub instance
        experiments = project.experiments.experiments()
        self.assertIsNotNone(experiments)
        self.assertGreaterEqual(len(experiments), 0)

    @unittest.skip("Skipping test_user.")
    def test_user(self):
        # Accessing Hub methods directly through delegation
        user = self.platform.user()
        self.assertIsNotNone(user)
        assert isinstance(user, User)

    @unittest.skip("Skipping test_models.")
    def test_models(self):
        # Accessing Hub methods directly through delegation
        project = self.platform.project(self.project_name)
        modelapi = project.models
        # models = modelapi.registered_models()
        self.assertIsNotNone(modelapi)

    @unittest.skip("Skipping test_namespaces.")
    def test_namespaces(self):
        # Accessing Hub methods directly through delegation
        namespaces = self.platform.namespaces()
        self.assertIsNotNone(namespaces)

    @unittest.skip("Skipping test_get_list_experiments.")
    def test_get_list_experiments(self):
        # Test the project method with a real API call
        experiments = self.platform.list_experiments(self.project_name)
        self.assertIsNotNone(experiments)
        self.assertGreaterEqual(len(experiments), 0)

    # def test_tensorboad_callback(self):
    #     from sklearn.model_selection import train_test_split
    #     from sklearn.datasets import load_wine
    #     from tensorflow.keras.models import Sequential
    #     from tensorflow.keras.layers import Dense
    #     from tensorflow.keras.utils import to_categorical
    #     from infoapps_mlops_sdk.core import PlatformType, initialize
    #
    #     # Create an experiment object
    #     experiment = initialize(platform_type=PlatformType.KERAS)
    #
    #     # Load and prepare the dataset
    #     data = load_wine()
    #     X_train, X_test, y_train, y_test = train_test_split(data.data, to_categorical(data.target), test_size=0.2,
    #                                                         random_state=42)
    #
    #     # Define a simple Keras model
    #     model = Sequential([
    #         Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    #         Dense(32, activation='relu'),
    #         Dense(y_train.shape[1], activation='softmax')
    #     ])
    #
    #     model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    #
    #     # Create an instance of MLOpsCallback with the experiment object
    #     mlops_callback = MLOpsTensorflowCallback(experiment)
    #
    #     # Train the model and log metrics with MLOpsCallback
    #     model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, callbacks=[mlops_callback])
    #
    #     # Test the project method with a real API call
    #     # project = self.platform.project(self.project_name)
    #     # callback = project.keras_callback()
    #     self.assertIsNotNone(mlops_callback)

    @unittest.skip("Skipping test_keras_callback.")
    def test_keras_callback(self):
        from sklearn.model_selection import train_test_split
        from sklearn.datasets import load_wine
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.layers import Dense
        from tensorflow.keras.utils import to_categorical
        import tensorflow as tf
        from tensorflow.keras.metrics import AUC, Precision, Recall, TopKCategoricalAccuracy
        from ..src.infoapps_mlops_sdk.integrations.keras_callback import MLOpsKerasCallback

        # Create an experiment object
        experiment = init_experiment(
            experiment_name="my_tensorflow_experiment_high_epoch3",
            platform_type=PlatformType.KERAS,
            owner_email="renaldo_williams@apple.com",
            USE_BETA_URL=True
        )

        # Load and prepare the dataset
        data = load_wine()
        X_train, X_test, y_train, y_test = train_test_split(data.data, to_categorical(data.target), test_size=0.2,
                                                            random_state=42)

        # Define a simple Keras model
        model = Sequential([
            Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
            Dense(32, activation='relu'),
            Dense(y_train.shape[1], activation='softmax')
        ])

        # Compile model with correct metric specifications
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=[
            'accuracy',  # Standard accuracy
            Precision(),  # Precision
            Recall(),  # Recall
            AUC(),  # AUC
            TopKCategoricalAccuracy(k=3)  # Top-3 accuracy
        ])

        print("Metrics being tracked:", model.metrics_names)

        # Create an instance of MLOpsCallback with the experiment object
        mlops_callback = MLOpsKerasCallback(experiment, epochs=100)

        # Train the model and log metrics with MLOpsCallback
        model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100, callbacks=[mlops_callback])

        experiment.done()
        # Test the project method with a real API call
        # project = self.platform.project(self.project_name)
        # callback = project.keras_callback()
        self.assertIsNotNone(mlops_callback)

    @unittest.skip("Skipping test_pytorch_callback.")
    def test_pytorch_with_keras_callback3(self):
        import os
        os.environ["KERAS_BACKEND"] = "torch"

        from keras import backend
        print(backend.backend())

        from sklearn.datasets import load_wine
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import StandardScaler
        from keras.models import Sequential
        from keras.layers import Dense, Dropout
        from keras.utils import to_categorical
        from keras.optimizers import Adam
        from keras.metrics import Precision, Recall
        from ..src.infoapps_mlops_sdk.core import PlatformType, init_experiment
        from ..src.infoapps_mlops_sdk.integrations.keras_callback import MLOpsKerasCallback

        try:
            # Step 1: Initialize an Experiment
            experiment = init_experiment(
                experiment_name="wine_experiment_keras_pytorch",
                platform_type=PlatformType.KERAS,
                owner_email="renaldo_williams@apple.com",
                USE_BETA_URL=True
            )

            # Step 2: Load and prepare the dataset
            data = load_wine()
            X_train, X_val, y_train, y_val = train_test_split(data.data, to_categorical(data.target), test_size=0.2,
                                                              random_state=42)

            # Standardize the features
            scaler = StandardScaler()
            X_train = scaler.fit_transform(X_train)
            X_val = scaler.transform(X_val)

            # Step 3: Define the Model
            model = Sequential([
                Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
                Dropout(0.2),
                Dense(32, activation='relu'),
                Dense(y_train.shape[1], activation='softmax')
            ])
            model.compile(optimizer=Adam(learning_rate=1e-3), loss='categorical_crossentropy',
                          metrics=['accuracy', Precision(), Recall()])

            # Step 4: Initialize the custom callback
            mlops_callback = MLOpsKerasCallback(experiment, epochs=10)

            # Step 5: Train the model
            model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10, callbacks=[mlops_callback])

            # Mark experiment as done
            experiment.done()

        except Exception as e:
            print(e)
            self.fail("Test failed")

    # - `ReLU` (Rectified Linear Unit) is an activation function used in neural networks.
    # It applies the function `f(x) = max(0, x)` to each element of the input tensor, introducing
    # non-linearity to the model.
    #
    # - `torch.optim.Adam` is an optimizer in PyTorch that implements the Adam algorithm.
    # It is used to update the model parameters based on the gradients computed during backpropagation.
    # Adam combines the advantages of two other extensions of stochastic gradient descent: AdaGrad and RMSProp.
    #
    # - `CrossEntropyLoss` is a loss function used for classification tasks. It combines `LogSoftmax` and `NLLLoss`
    # in one single class. It is used to measure the performance of a classification model whose output is a
    # probability value between 0 and 1.
    # @unittest.skip("Skipping test_pytorch_callback.")
    def test_pytorch_callback4(self):
        from sklearn.datasets import load_wine
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import StandardScaler
        import torch
        from torch import nn
        from torch.utils.data import DataLoader, TensorDataset
        # Set environment variables programmatically, needed so core code sets up correct logging for testing notebook
        os.environ["IN_DEV_MODE"] = "true"  # Set to "false" if not in dev mode
        os.environ["USE_BETA_URL"] = "true"  # Set to "true" to use the beta URL

        from infoapps_mlops_sdk.src.infoapps_mlops_sdk.core import PlatformType, init_experiment
        # from ..src.infoapps_mlops_sdk.integrations.pytorch_callback import MLOpsPyTorchCallback

        # from infoapps_mlops_sdk.integrations.pytorch_callback import MLOpsPyTorchCallback

        try:
            # Step 1: Initialize an Experiment
            experiment = init_experiment(
                experiment_name="wine_experiment_pytorch",
                platform_type=PlatformType.PYTORCH,
                owner_email="renaldo_williams@apple.com",
                # USE_BETA_URL=True,
                IN_DEV_MODE=True
            )

            # Log a single value
            # Specify a field name ("seed") inside the run and assign a value to it
            experiment["seed"] = 0.42

            # Log a series of values
            from random import random

            epochs = 10
            offset = random() / 5

            for epoch in range(epochs):
                acc = 1 - 2 ** -epoch - random() / (epoch + 1) - offset
                loss = 2 ** -epoch + random() / (epoch + 1) + offset

                experiment["accuracy"].append(acc)
                experiment["loss"].append(loss)

            # print("current directory is: ", os.getcwd())

            file_dir = os.path.dirname(os.path.abspath(__file__))

            print("directory of the file is: ", os.path.dirname(os.path.abspath(__file__)))

            dasaset_dir = file_dir + "/datasets/sample_data.csv"
            image_dir = file_dir + "/images/sample_logo.png"

            # Upload an image
            experiment["single_image"].upload(image_dir)

            # experiment["train/dataset"].track_files(dasaset_dir)

            return

            # Step 2: Load and prepare the dataset
            data = load_wine()
            X_train, X_val, y_train, y_val = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

            # Standardize the features
            scaler = StandardScaler()
            X_train = scaler.fit_transform(X_train)
            X_val = scaler.transform(X_val)

            # Convert to PyTorch tensors
            X_train = torch.tensor(X_train, dtype=torch.float32)
            y_train = torch.tensor(y_train, dtype=torch.long)
            X_val = torch.tensor(X_val, dtype=torch.float32)
            y_val = torch.tensor(y_val, dtype=torch.long)

            # Create TensorDatasets
            train_ds = TensorDataset(X_train, y_train)
            val_ds = TensorDataset(X_val, y_val)

            # Create DataLoaders
            train_loader = DataLoader(train_ds, batch_size=32, shuffle=True)
            val_loader = DataLoader(val_ds, batch_size=32)

            # Step 3: Define the Model
            class WineModel(nn.Module):
                def __init__(self, input_dim, num_classes=3):
                    super(WineModel, self).__init__()
                    self.model = nn.Sequential(
                        nn.Linear(input_dim, 64),
                        nn.ReLU(),
                        nn.Dropout(0.2),
                        nn.Linear(64, 32),
                        nn.ReLU(),
                        nn.Linear(32, num_classes)
                    )

                def forward(self, x):
                    return self.model(x)

            model = WineModel(input_dim=X_train.shape[1])
            optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
            criterion = nn.CrossEntropyLoss()

            # Step 4: Initialize the custom callback
            mlops_callback = MLOpsPyTorchCallback(experiment, epochs=10)

            # Step 5: Training loop
            for epoch in range(10):
                model.train()
                epoch_logs = {"loss": 0.0, "accuracy": 0.0}
                total_correct = 0
                total_samples = 0

                for batch_idx, (X_batch, y_batch) in enumerate(train_loader):
                    optimizer.zero_grad()
                    outputs = model(X_batch)
                    loss = criterion(outputs, y_batch)
                    loss.backward()
                    optimizer.step()

                    # Update logs
                    _, predicted = torch.max(outputs, 1)
                    total_correct += (predicted == y_batch).sum().item()
                    total_samples += y_batch.size(0)
                    batch_logs = {
                        "step": epoch * len(train_loader) + batch_idx,
                        "loss": loss.item(),
                        "accuracy": total_correct / total_samples
                    }

                    # Call batch end callback
                    # mlops_callback.on_batch_end(batch_idx, batch_logs)

                    epoch_logs["loss"] += loss.item()
                    epoch_logs["accuracy"] = total_correct / total_samples

                # Average loss for the epoch
                epoch_logs["loss"] /= len(train_loader)
                epoch_logs["accuracy"] = total_correct / total_samples

                # Call epoch end callback
                mlops_callback.on_epoch_end(epoch_logs)

            # Clean up
            experiment.done()

        except Exception as e:
            print(e)
            self.fail("Test failed")

    @unittest.skip("Skipping test_pytorch_callback4_with_precision_recall.")
    def test_pytorch_callback4_with_precision_recall(self):
        from sklearn.datasets import load_wine
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import StandardScaler
        import torch
        from torch import nn
        from torch.utils.data import DataLoader, TensorDataset
        from torchmetrics import Precision, Recall
        from ..src.infoapps_mlops_sdk.core import PlatformType, init_experiment
        from ..src.infoapps_mlops_sdk.integrations.pytorch_callback import MLOpsPyTorchCallback

        try:
            # Step 1: Initialize an Experiment
            experiment = init_experiment(
                experiment_name="wine_experiment_pytorch",
                platform_type=PlatformType.PYTORCH,
                owner_email="renaldo_williams@apple.com",
                USE_BETA_URL=True
            )

            # Step 2: Load and prepare the dataset
            data = load_wine()
            X_train, X_val, y_train, y_val = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

            # Standardize the features
            scaler = StandardScaler()
            X_train = scaler.fit_transform(X_train)
            X_val = scaler.transform(X_val)

            # Convert to PyTorch tensors
            X_train = torch.tensor(X_train, dtype=torch.float32)
            y_train = torch.tensor(y_train, dtype=torch.long)
            X_val = torch.tensor(X_val, dtype=torch.float32)
            y_val = torch.tensor(y_val, dtype=torch.long)

            # Create TensorDatasets
            train_ds = TensorDataset(X_train, y_train)
            val_ds = TensorDataset(X_val, y_val)

            # Create DataLoaders
            train_loader = DataLoader(train_ds, batch_size=32, shuffle=True)
            val_loader = DataLoader(val_ds, batch_size=32)

            # Step 3: Define the Model
            class WineModel(nn.Module):
                def __init__(self, input_dim, num_classes=3):
                    super(WineModel, self).__init__()
                    self.model = nn.Sequential(
                        nn.Linear(input_dim, 64),
                        nn.ReLU(),
                        nn.Dropout(0.2),
                        nn.Linear(64, 32),
                        nn.ReLU(),
                        nn.Linear(32, num_classes)
                    )
                    self.precision = Precision(num_classes=num_classes, average='macro', task='multiclass')
                    self.recall = Recall(num_classes=num_classes, average='macro', task='multiclass')

                def forward(self, x):
                    return self.model(x)

                def training_step(self, batch):
                    x, y = batch
                    logits = self.forward(x)
                    loss = nn.CrossEntropyLoss()(logits, y)
                    preds = torch.argmax(logits, dim=1)
                    precision = self.precision(preds, y)
                    recall = self.recall(preds, y)
                    return loss, precision, recall

            model = WineModel(input_dim=X_train.shape[1])
            optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

            # Step 4: Initialize the custom callback
            mlops_callback = MLOpsPyTorchCallback(experiment, epochs=10, log_on_batch=True)

            # Step 5: Training loop
            for epoch in range(10):
                model.train()
                epoch_logs = {"loss": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0}
                total_correct = 0
                total_samples = 0

                for batch_idx, (X_batch, y_batch) in enumerate(train_loader):
                    optimizer.zero_grad()
                    loss, precision, recall = model.training_step((X_batch, y_batch))
                    loss.backward()
                    optimizer.step()

                    # Update logs
                    outputs = model(X_batch)
                    _, predicted = torch.max(outputs, 1)
                    total_correct += (predicted == y_batch).sum().item()
                    total_samples += y_batch.size(0)
                    batch_logs = {
                        "step": epoch * len(train_loader) + batch_idx,
                        "loss": loss.item(),
                        "accuracy": total_correct / total_samples,
                        "precision": precision.item(),
                        "recall": recall.item()
                    }

                    # Call batch end callback
                    mlops_callback.on_batch_end(batch_idx, batch_logs)

                    epoch_logs["loss"] += loss.item()
                    epoch_logs["accuracy"] = total_correct / total_samples
                    epoch_logs["precision"] += precision.item()
                    epoch_logs["recall"] += recall.item()

                # Average metrics for the epoch
                epoch_logs["loss"] /= len(train_loader)
                epoch_logs["accuracy"] = total_correct / total_samples
                epoch_logs["precision"] /= len(train_loader)
                epoch_logs["recall"] /= len(train_loader)

                # Call epoch end callback
                mlops_callback.on_epoch_end(epoch_logs)

            # Clean up
            mlops_callback.close()
            experiment.done()

        except Exception as e:
            print(e)
            self.fail("Test failed")

    @unittest.skip("Skipping test_pytorchlightening_callback3.")
    def test_pytorchlightening_callback3(self):
        from pytorch_lightning import Trainer, LightningModule
        from torch.utils.data import DataLoader, TensorDataset, random_split
        from sklearn.datasets import load_wine
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import StandardScaler
        import torch
        from torch import nn
        from ..src.infoapps_mlops_sdk.core import PlatformType, init_experiment
        from ..src.infoapps_mlops_sdk.integrations.pytorchlightening_callback import MLOpsLightningCallback

        try:
            # Step 1: Initialize an Experiment
            experiment = init_experiment(
                experiment_name="wine_experiment",
                platform_type=PlatformType.PYTORCH_LIGHTNING,
                owner_email="renaldo_williams@apple.com",
                USE_BETA_URL=True
            )

            # Step 2: Load and prepare the dataset
            data = load_wine()
            X_train, X_val, y_train, y_val = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

            # Standardize the features
            scaler = StandardScaler()
            X_train = scaler.fit_transform(X_train)
            X_val = scaler.transform(X_val)

            # Convert to PyTorch tensors
            X_train = torch.tensor(X_train, dtype=torch.float32)
            y_train = torch.tensor(y_train, dtype=torch.long)
            X_val = torch.tensor(X_val, dtype=torch.float32)
            y_val = torch.tensor(y_val, dtype=torch.long)

            # Create TensorDatasets
            train_ds = TensorDataset(X_train, y_train)
            val_ds = TensorDataset(X_val, y_val)

            # Create DataLoaders
            train_loader = DataLoader(train_ds, batch_size=32, shuffle=True)
            val_loader = DataLoader(val_ds, batch_size=32)

            # Step 3: Define the Model
            class WineModel(LightningModule):
                def __init__(self, input_dim, num_classes=3, learning_rate=1e-3):
                    super(WineModel, self).__init__()
                    self.save_hyperparameters()
                    self.model = nn.Sequential(
                        nn.Linear(input_dim, 64),
                        nn.ReLU(),
                        nn.Dropout(0.2),
                        nn.Linear(64, 32),
                        nn.ReLU(),
                        nn.Linear(32, num_classes)
                    )
                    self.loss_fn = nn.CrossEntropyLoss()

                def forward(self, x):
                    return self.model(x)

                def training_step(self, batch, batch_idx):
                    x, y = batch
                    logits = self.forward(x)
                    loss = self.loss_fn(logits, y)
                    preds = torch.argmax(logits, dim=1)
                    self.log('train_loss', loss, on_epoch=True)
                    return {'loss': loss, 'preds': preds, 'targets': y}

                def validation_step(self, batch, batch_idx):
                    x, y = batch
                    logits = self.forward(x)
                    loss = self.loss_fn(logits, y)
                    preds = torch.argmax(logits, dim=1)
                    self.log('val_loss', loss, on_epoch=True)
                    return {'loss': loss, 'preds': preds, 'targets': y}

                def configure_optimizers(self):
                    return torch.optim.Adam(self.parameters(), lr=self.hparams.learning_rate)

            # Step 4: Set Up the MLOps Callback
            mlops_callback = MLOpsLightningCallback(experiment=experiment, epochs=100, num_classes=3)

            # Step 5: Train the Model
            trainer = Trainer(max_epochs=100, callbacks=[mlops_callback])
            trainer.fit(WineModel(input_dim=X_train.shape[1]), train_loader, val_loader)

            # Mark experiment as done
            experiment.done()

        except Exception as e:
            print(e)
            self.fail("Test failed")

    @unittest.skip("Skipping test_pytorchlightening_callback2.")
    def test_pytorchlightening_callback2(self):
        from pytorch_lightning import Trainer
        from torch.utils.data import DataLoader, random_split
        from torchvision import datasets, transforms
        from ..src.infoapps_mlops_sdk.core import PlatformType, init_experiment
        from ..src.infoapps_mlops_sdk.integrations.pytorchlightening_callback import MLOpsLightningCallback

        try:
            # Step 1: Initialize an Experiment
            experiment = init_experiment(
                experiment_name="mnist_experiment2",
                platform_type=PlatformType.PYTORCH_LIGHTNING,
                owner_email="renaldo_williams@apple.com",
                USE_BETA_URL=True
            )

            # Step 2: Prepare Data
            transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
            dataset = datasets.MNIST(root='data', train=True, transform=transform, download=True)
            train_size = 10000
            val_size = 1000
            dataset_size = len(dataset)

            # Adjust sizes to ensure the sum matches
            train_size = min(train_size, dataset_size)
            val_size = dataset_size - train_size

            train_ds, val_ds = random_split(dataset, [train_size, val_size])
            train_loader = DataLoader(train_ds, batch_size=3000, shuffle=True)
            val_loader = DataLoader(val_ds, batch_size=16000)

            # Step 3: Define the Model
            class MyModelCode(LightningModule):
                def __init__(self, num_classes=10, learning_rate=1e-3):
                    super(MyModelCode, self).__init__()
                    self.save_hyperparameters()
                    self.model = nn.Sequential(
                        nn.Flatten(),
                        nn.Linear(28 * 28, 128),
                        nn.ReLU(),
                        nn.Dropout(0.2),
                        nn.Linear(128, 64),
                        nn.ReLU(),
                        nn.Linear(64, num_classes)
                    )
                    self.loss_fn = nn.CrossEntropyLoss()

                def forward(self, x):
                    return self.model(x)

                def training_step(self, batch, batch_idx):
                    x, y = batch
                    logits = self.forward(x)
                    loss = self.loss_fn(logits, y)
                    preds = torch.argmax(logits, dim=1)
                    self.log('train_loss', loss, on_epoch=True)
                    return {'loss': loss, 'preds': preds, 'targets': y}

                def validation_step(self, batch, batch_idx):
                    x, y = batch
                    logits = self.forward(x)
                    loss = self.loss_fn(logits, y)
                    preds = torch.argmax(logits, dim=1)
                    self.log('val_loss', loss, on_epoch=True)
                    return {'loss': loss, 'preds': preds, 'targets': y}

                def configure_optimizers(self):
                    return torch.optim.Adam(self.parameters(), lr=self.hparams.learning_rate)

            # Step 4: Set Up the MLOps Callback
            mlops_callback = MLOpsLightningCallback(experiment=experiment, epochs=5, num_classes=10)

            # Step 5: Train the Model
            trainer = Trainer(max_epochs=5, callbacks=[mlops_callback])
            trainer.fit(MyModelCode(num_classes=10), train_loader, val_loader)

            # Mark experiment as done
            experiment.done()

        except Exception as e:
            print(e)
            self.fail("Test failed")

    @unittest.skip("Skipping test_pytorchlightening_callback.")
    def test_pytorchlightening_callback(self):
        from pytorch_lightning import Trainer
        from torch.utils.data import DataLoader, random_split
        from torchvision import datasets, transforms
        from ..src.infoapps_mlops_sdk.core import PlatformType, init_experiment
        from ..src.infoapps_mlops_sdk.integrations.pytorchlightening_callback import MLOpsLightningCallback

        try:
            # Experiment setup (assuming init_experiment is defined)
            experiment = init_experiment(
                experiment_name="mnist_experiment",
                platform_type=PlatformType.PYTORCH_LIGHTNING,
                owner_email="renaldo_williams@apple.com",
                USE_BETA_URL=True
            )

            # Prepare MNIST Data
            transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
            dataset = datasets.MNIST(root='data', train=True, transform=transform, download=True)
            # train_ds, val_ds = random_split(dataset, [10000, 1000]) #instead of 50,000 and 10,000 for testing

            train_size = 10000
            val_size = 1000
            dataset_size = len(dataset)

            if train_size + val_size > dataset_size:
                raise ValueError("Split sizes exceed dataset size!")

            # Adjust sizes to ensure the sum matches
            train_size = min(train_size, dataset_size)
            val_size = dataset_size - train_size

            train_ds, val_ds = random_split(dataset, [train_size, val_size])

            train_loader = DataLoader(train_ds, batch_size=32, shuffle=True)
            val_loader = DataLoader(val_ds, batch_size=32)

            # Model
            model = DemoMNISTModel(num_classes=10)

            # MLOps Callback
            mlops_callback = MLOpsLightningCallback(experiment=experiment, epochs=3, num_classes=10)

            # Trainer
            trainer = Trainer(max_epochs=3, callbacks=[mlops_callback])
            trainer.fit(model, train_loader, val_loader)

            # Mark experiment as done
            experiment.done()

        except Exception as e:
            print(e)
            self.fail("Test failed")


import torch
from torch import nn
from torch.nn import functional as F
from torchmetrics import Accuracy, Precision, Recall, AUROC
from pytorch_lightning import LightningModule


class DemoMNISTModel(LightningModule):
    def __init__(self, num_classes=10, learning_rate=1e-3):
        super(DemoMNISTModel, self).__init__()
        self.save_hyperparameters()

        # Define the model architecture
        self.model = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28 * 28, 128),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, num_classes)
        )

        # Define loss function
        self.loss_fn = nn.CrossEntropyLoss()
        #
        # # Define metrics
        # self.accuracy = Accuracy(num_classes=num_classes, average='macro')
        # self.precision = Precision(num_classes=num_classes, average='macro')
        # self.recall = Recall(num_classes=num_classes, average='macro')
        # self.auroc = AUROC(num_classes=num_classes, average='macro')

    def forward(self, x):
        return self.model(x)

    def training_step(self, batch, batch_idx):
        x, y = batch
        logits = self.forward(x)
        loss = self.loss_fn(logits, y)

        # Log metrics
        # Collect predictions and targets
        preds = torch.argmax(logits, dim=1)
        self.log('train_loss', loss, on_epoch=True)

        return {'loss': loss, 'preds': preds, 'targets': y}

        # self.log('train_accuracy', self.accuracy(preds, y), on_epoch=True)
        # self.log('train_precision', self.precision(preds, y), on_epoch=True)
        # self.log('train_recall', self.recall(preds, y), on_epoch=True)
        # self.log('train_auroc', self.auroc(logits, y), on_epoch=True)

    def validation_step(self, batch, batch_idx):
        x, y = batch
        logits = self.forward(x)
        loss = self.loss_fn(logits, y)

        # Log metrics
        # Collect predictions and targets
        preds = torch.argmax(logits, dim=1)
        self.log('val_loss', loss, on_epoch=True)

        return {'loss': loss, 'preds': preds, 'targets': y}
        # self.log('val_accuracy', self.accuracy(preds, y), on_epoch=True)
        # self.log('val_precision', self.precision(preds, y), on_epoch=True)
        # self.log('val_recall', self.recall(preds, y), on_epoch=True)
        # self.log('val_auroc', self.auroc(logits, y), on_epoch=True)

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=self.hparams.learning_rate)
