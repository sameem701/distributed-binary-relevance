"""
Milestone 1: Binary Relevance Multi-Label Classification
Using parallel and distributed computing approaches
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import hamming_loss, accuracy_score, f1_score
import concurrent.futures
import time
from pathlib import Path

# Configuration
TRAIN_DATA = Path("eurlex.csv")
TEST_DATA = Path("eurlex_test.csv")
RANDOM_STATE = 42
NUM_WORKERS = 4
TEST_SIZE = 0.2

def load_data():
    """Load training and test datasets"""
    print("Loading data...")
    train_df = pd.read_csv(TRAIN_DATA)
    test_df = pd.read_csv(TEST_DATA)
    
    # Extract features and labels
    train_features = train_df.iloc[:, 1:-1].values  # Skip row_id and labels
    train_labels_raw = train_df.iloc[:, -1].values
    test_features = test_df.iloc[:, 1:].values  # Skip row_id
    
    # Parse multi-label strings (sparse format: "label_idx:value label_idx:value ...")
    train_labels = []
    for label_str in train_labels_raw:
        if isinstance(label_str, str) and label_str.strip():
            labels = []
            for pair in label_str.split():
                if ':' in pair:
                    label_idx, value = pair.split(':')
                    if int(value) == 1:  # Only include labels with value 1
                        labels.append(int(label_idx))
            train_labels.append(labels)
        else:
            train_labels.append([])
    
    print(f"Train shape: {train_features.shape}")
    print(f"Test shape: {test_features.shape}")
    print(f"Number of samples: {len(train_labels)}")
    
    return train_features, train_labels, test_features


def convert_to_binary_matrix(labels_list, num_labels):
    """Convert list of label indices to binary matrix"""
    n_samples = len(labels_list)
    binary_matrix = np.zeros((n_samples, num_labels), dtype=int)
    
    for i, labels in enumerate(labels_list):
        for label_idx in labels:
            if 0 <= label_idx < num_labels:
                binary_matrix[i, label_idx] = 1
    
    return binary_matrix


def train_binary_classifier(args):
    """Train a single binary classifier for one label"""
    label_idx, X_train, y_train, X_val, y_val = args
    
    # Check if label has both classes in training data
    unique_classes = np.unique(y_train)
    if len(unique_classes) < 2:
        # Label is imbalanced, skip training
        return label_idx, None, 0.0, 0.0
    
    clf = LogisticRegression(max_iter=1000, random_state=RANDOM_STATE, verbose=0)
    clf.fit(X_train, y_train)
    
    train_acc = clf.score(X_train, y_train)
    val_acc = clf.score(X_val, y_val)
    
    return label_idx, clf, train_acc, val_acc


def train_parallel_binary_relevance(X_train, y_train, num_labels):
    """Train binary relevance classifiers in parallel"""
    print(f"\nTraining {num_labels} binary classifiers in parallel...")
    
    # Split train/val for training phase
    X_tr, X_val, y_tr, y_val = train_test_split(
        X_train, y_train, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )
    
    classifiers = {}
    start_time = time.time()
    
    # Prepare arguments for parallel training
    train_args = [
        (label_idx, X_tr, y_tr[:, label_idx], X_val, y_val[:, label_idx])
        for label_idx in range(num_labels)
    ]
    
    # Train classifiers in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
        results = list(executor.map(train_binary_classifier, train_args))
    
    train_time = time.time() - start_time
    
    # Collect results
    total_train_acc = 0
    total_val_acc = 0
    trained_count = 0
    skipped_count = 0
    
    for label_idx, clf, train_acc, val_acc in results:
        if clf is not None:  # Only store trained classifiers
            classifiers[label_idx] = clf
            total_train_acc += train_acc
            total_val_acc += val_acc
            trained_count += 1
        else:
            skipped_count += 1
    
    avg_train_acc = total_train_acc / trained_count if trained_count > 0 else 0
    avg_val_acc = total_val_acc / trained_count if trained_count > 0 else 0
    
    print(f"Training completed in {train_time:.2f}s")
    print(f"Classifiers trained: {trained_count}/{num_labels}")
    print(f"Labels skipped (insufficient data): {skipped_count}")
    print(f"Average train accuracy: {avg_train_acc:.4f}")
    print(f"Average validation accuracy: {avg_val_acc:.4f}")
    
    return classifiers, train_time


def predict_parallel(X_test, classifiers):
    """Make predictions using trained classifiers in parallel"""
    print(f"\nMaking predictions with {len(classifiers)} trained classifiers in parallel...")
    
    num_samples = X_test.shape[0]
    # Find max label index to determine matrix size
    max_label_idx = max(classifiers.keys()) if classifiers else 0
    num_labels = max_label_idx + 1
    
    predictions = np.zeros((num_samples, num_labels), dtype=int)
    
    start_time = time.time()
    
    # Prepare prediction arguments
    pred_args = [
        (label_idx, classifier, X_test)
        for label_idx, classifier in classifiers.items()
    ]
    
    # Make predictions in parallel
    def predict_single_label(args):
        label_idx, clf, X = args
        if clf is not None:
            return label_idx, clf.predict(X)
        else:
            return label_idx, np.zeros(X.shape[0], dtype=int)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
        results = list(executor.map(predict_single_label, pred_args))
    
    for label_idx, preds in results:
        predictions[:, label_idx] = preds
    
    pred_time = time.time() - start_time
    print(f"Prediction completed in {pred_time:.2f}s")
    
    return predictions, pred_time


def evaluate_predictions(y_true, y_pred):
    """Evaluate multi-label predictions"""
    print("\nEvaluation Metrics:")
    print("=" * 50)
    
    hamming = hamming_loss(y_true, y_pred)
    print(f"Hamming Loss: {hamming:.4f}")
    
    # Exact match accuracy (all labels must match)
    exact_match = accuracy_score(y_true, y_pred)
    print(f"Exact Match Accuracy: {exact_match:.4f}")
    
    # Micro-averaged F1 score
    f1_micro = f1_score(y_true, y_pred, average='micro', zero_division=0)
    print(f"F1 Score (Micro): {f1_micro:.4f}")
    
    # Macro-averaged F1 score
    f1_macro = f1_score(y_true, y_pred, average='macro', zero_division=0)
    print(f"F1 Score (Macro): {f1_macro:.4f}")
    
    # Per-label statistics
    label_accuracies = np.mean(y_true == y_pred, axis=0)
    print(f"\nLabel Accuracy - Min: {label_accuracies.min():.4f}, "
          f"Max: {label_accuracies.max():.4f}, "
          f"Mean: {label_accuracies.mean():.4f}")


def main():
    print("=" * 60)
    print("Binary Relevance Classification with Parallel Training")
    print("=" * 60)
    
    # Load and prepare data
    X_train, labels_train, X_test = load_data()
    
    # Determine number of labels from training data
    all_labels = set()
    for labels in labels_train:
        all_labels.update(labels)
    num_labels = max(all_labels) + 1 if all_labels else 1
    print(f"Number of labels: {num_labels}")
    
    # Convert to binary matrix
    y_train_binary = convert_to_binary_matrix(labels_train, num_labels)
    print(f"Training binary matrix shape: {y_train_binary.shape}")
    print(f"Label distribution (training):")
    label_counts = y_train_binary.sum(axis=0)
    print(f"  Min: {label_counts.min()}, Max: {label_counts.max()}, "
          f"Mean: {label_counts.mean():.1f}")
    
    # Normalize features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train binary relevance classifiers in parallel
    classifiers, train_time = train_parallel_binary_relevance(
        X_train_scaled, y_train_binary, num_labels
    )
    
    # Make predictions in parallel
    y_pred, pred_time = predict_parallel(X_test_scaled, classifiers)
    
    # Evaluate on training set predictions for insight
    print("\n" + "=" * 60)
    print("Training Set Predictions Analysis:")
    y_train_pred, _ = predict_parallel(X_train_scaled, classifiers)
    evaluate_predictions(y_train_binary, y_train_pred)
    
    # Print performance summary
    print("\n" + "=" * 60)
    print("Performance Summary:")
    print("=" * 60)
    print(f"Training time (parallel): {train_time:.2f}s")
    print(f"Prediction time (parallel): {pred_time:.2f}s")
    print(f"Number of workers: {NUM_WORKERS}")
    print(f"Test set predictions shape: {y_pred.shape}")
    print(f"Test set predictions saved for further analysis")
    
    # Save predictions
    np.save("test_predictions.npy", y_pred)
    print("\nTest predictions saved to: test_predictions.npy")
    
    return classifiers, scaler


if __name__ == "__main__":
    classifiers, scaler = main()
    print("\n" + "=" * 60)
    print("Milestone 1 Completed Successfully!")
    print("=" * 60)
