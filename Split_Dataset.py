import random
import os
import shutil


def split_dataset(data, num_splits, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    split_datasets = []

    for i in range(num_splits):
        # Shuffle the dataset
        shuffled_data = data[:]
        random.shuffle(shuffled_data)

        # Calculate split sizes
        total_samples = len(shuffled_data)
        training_size = int(total_samples * 0.8)
        validation_size = int(total_samples * 0.1)
        test_size = total_samples - training_size - validation_size

        # Split the dataset
        training_set = shuffled_data[:training_size]
        validation_set = shuffled_data[training_size:training_size + validation_size]
        test_set = shuffled_data[training_size + validation_size:]

        # Store the splits
        split_datasets.append((training_set, validation_set, test_set))

        # Save splits to files
        save_split(training_set, os.path.join(output_dir, f'training_set_{i + 1}.txt'))
        save_split(validation_set, os.path.join(output_dir, f'validation_set_{i + 1}.txt'))
        save_split(test_set, os.path.join(output_dir, f'test_set_{i + 1}.txt'))

    return split_datasets


def save_split(data_split, file_path):
    with open(file_path, 'w') as f:
        for item in data_split:
            f.write(f"{item}\n")


# Example usage
if __name__ == "__main__":
    # Load your dataset (this example assumes a list of file paths or data points)
    dataset = [f"sample_{i}" for i in range(1000)]  # Replace with actual data loading

    # Number of splits to create
    num_splits = 5

    # Directory to save the split datasets
    output_dir = 'dataset_splits'

    # Perform the splits
    split_datasets = split_dataset(dataset, num_splits, output_dir)

    print(f"Dataset has been split into {num_splits} sets and saved in '{output_dir}'.")
