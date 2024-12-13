import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D, MaxPooling2D, Flatten, Dense,
    Dropout, BatchNormalization
)
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    precision_recall_curve,
    average_precision_score,
    precision_score,
    recall_score,
    f1_score,
    roc_curve,
    roc_auc_score
)
import os
import cv2


class CheckFraudDetectionMetrics:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.X = None
        self.y = None
        self.model = None

    def load_and_preprocess_data(self, img_size=(256, 256)):
        """
        Load and preprocess check images
        """
        images = []
        labels = []

        # Load images from legitimate and fake folders
        for category in ['legitimate', 'fake']:
            category_path = os.path.join(self.data_dir, category)
            label = 0 if category == 'legitimate' else 1

            for img_name in os.listdir(category_path):
                img_path = os.path.join(category_path, img_name)
                try:
                    # Read image
                    img = cv2.imread(img_path)
                    img = cv2.resize(img, img_size)
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                    images.append(img)
                    labels.append(label)
                except Exception as e:
                    print(f"Error processing {img_path}: {e}")

        # Convert to numpy arrays
        self.X = np.array(images) / 255.0
        self.y = np.array(labels)

        return self.X, self.y

    def create_model(self, input_shape=(256, 256, 3)):
        """
        Create CNN model for check fraud detection
        """
        model = Sequential([
            # Feature extraction layers
            Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
            BatchNormalization(),
            MaxPooling2D((2, 2)),

            Conv2D(64, (3, 3), activation='relu'),
            BatchNormalization(),
            MaxPooling2D((2, 2)),

            Conv2D(128, (3, 3), activation='relu'),
            BatchNormalization(),
            MaxPooling2D((2, 2)),

            Flatten(),

            # Dense layers for classification
            Dense(128, activation='relu'),
            Dropout(0.5),
            Dense(64, activation='relu'),
            Dropout(0.3),
            Dense(1, activation='sigmoid')  # Binary classification
        ])

        # Compile model
        model.compile(
            optimizer=Adam(learning_rate=0.0001),
            loss='binary_crossentropy',
            metrics=['accuracy',
                     tf.keras.metrics.Precision(),
                     tf.keras.metrics.Recall()]
        )

        self.model = model
        return model

    def train_model(self, test_size=0.2, random_state=42):
        """
        Train the model with data augmentation
        """
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=random_state,
            stratify=self.y
        )

        # Data augmentation
        datagen = ImageDataGenerator(
            rotation_range=20,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True
        )

        # Train model
        history = self.model.fit(
            datagen.flow(X_train, y_train, batch_size=32),
            epochs=20,
            validation_data=(X_test, y_test),
            verbose=1
        )

        return history, X_test, y_test

    def comprehensive_evaluation(self, X_test, y_test):
        """
        Comprehensive model performance evaluation
        """
        # Predictions
        y_pred_proba = self.model.predict(X_test).flatten()
        y_pred = (y_pred_proba > 0.5).astype(int)

        # 1. Basic Metrics
        print("\n1. Basic Performance Metrics:")
        print(classification_report(y_test, y_pred))

        # 2. Precision and Recall
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        print("\n2. Detailed Precision and Recall:")
        print(f"Precision: {precision:.4f}")
        print(f"Recall: {recall:.4f}")
        print(f"F1 Score: {f1:.4f}")

        # 3. Precision-Recall Curve
        precision_curve, recall_curve, thresholds = precision_recall_curve(y_test, y_pred_proba)
        avg_precision = average_precision_score(y_test, y_pred_proba)

        plt.figure(figsize=(10, 5))
        plt.subplot(121)
        plt.plot(recall_curve, precision_curve, label=f'AP={avg_precision:.2f}')
        plt.title('Precision-Recall Curve')
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.legend()

        # 4. ROC Curve
        fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
        roc_auc = roc_auc_score(y_test, y_pred_proba)

        plt.subplot(122)
        plt.plot(fpr, tpr, label=f'ROC curve (AUC = {roc_auc:.2f})')
        plt.plot([0, 1], [0, 1], 'k--')
        plt.title('Receiver Operating Characteristic')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.legend()

        plt.tight_layout()
        plt.show()

        # 5. Confusion Matrix
        cm = confusion_matrix(y_test, y_pred)
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title('Confusion Matrix')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.show()

        return {
            'precision': precision,
            'recall': recall,
            'f1_score': f1,
            'avg_precision': avg_precision,
            'roc_auc': roc_auc
        }

    def feature_importance(self, X_test):
        """
        Visualize feature importance using activation maps
        """
        # Get first convolutional layer
        first_layer = self.model.layers[0]

        # Create intermediate model to get feature maps
        feature_model = tf.keras.Model(
            inputs=self.model.inputs,
            outputs=[layer.output for layer in self.model.layers[:3]]
        )

        # Get feature maps
        feature_outputs = feature_model.predict(X_test[:5])

        # Visualize feature maps
        plt.figure(figsize=(15, 5))
        for i, feature_map in enumerate(feature_outputs[0][:16]):
            plt.subplot(4, 4, i + 1)
            plt.imshow(feature_map, cmap='viridis')
            plt.title(f'Feature Map {i + 1}')
            plt.axis('off')
        plt.tight_layout()
        plt.show()


def main():
    # Set random seeds for reproducibility
    np.random.seed(42)
    tf.random.set_seed(42)

    # Initialize detection system
    # Replace with your generated image dataset path
    detector = CheckFraudDetectionMetrics('check_images')

    # Load and preprocess data
    X, y = detector.load_and_preprocess_data()

    # Create model
    model = detector.create_model()

    # Train model
    history, X_test, y_test = detector.train_model()

    # Comprehensive evaluation
    metrics = detector.comprehensive_evaluation(X_test, y_test)

    # Feature importance visualization
    detector.feature_importance(X_test)


if __name__ == '__main__':
    main()