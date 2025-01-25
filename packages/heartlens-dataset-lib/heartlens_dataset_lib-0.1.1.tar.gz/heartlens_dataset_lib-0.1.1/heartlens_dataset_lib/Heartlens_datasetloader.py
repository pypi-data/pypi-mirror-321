
 
from torch.utils.data import Dataset, DataLoader
 
from torch.utils.data.distributed import DistributedSampler   

import numpy as np  
import torch     
import zarr  

 
class HeartlensDataset(Dataset):
    """
    Custom PyTorch Dataset to handle Heartlens Zarr data.
    """

    def __init__(self, zarr_path, norm_min_max=False):
        """
        Initialize the dataset.
        :param zarr_path: Path to the Zarr file containing the dataset.
        :param norm_min_max: Boolean flag to decide whether to apply min-max normalization.
        """
        # Open the Zarr file in read mode
        self.zarr = zarr.open(zarr_path, mode="r")
        # Access the 'data' array in the Zarr dataset
        self.zarr_data = self.zarr['data']
        # Store the normalization preference
        self.norm_min_max = norm_min_max
        # Access the slice and bag metadata
        self.slice_metadata = self.zarr['slice_metadata']
        self.bag_metadata = self.zarr['bag_metadata']
        # Calculate the total number of samples in the dataset
        self.zarr_len = self.zarr_data.shape[0]

    def __len__(self):
        """
        Return the total number of samples in the dataset.
        """
        return self.zarr_len

    def normalize_(self, image, MIN_B=-1024.0, MAX_B=3071.0):
        """
        Normalize the image to the range [0, 1] using fixed min and max bounds.
        :param image: Input image array.
        :param MIN_B: Minimum bound for normalization.
        :param MAX_B: Maximum bound for normalization.
        :return: Normalized image array.
        """
        image = (image - MIN_B) / (MAX_B - MIN_B)
        return image

    def normalize_min_max(self, image_tensor):
        """
        Normalize the image to the range [0, 1] using min-max normalization based on the tensor's values.
        :param image_tensor: Input image array.
        :return: Normalized image array.
        """
        # Find the minimum and maximum values in the tensor
        orig_min = np.amin(image_tensor)
        orig_max = np.amax(image_tensor)
        # Small constant to avoid division by zero
        epsilon = 1e-7
        # Normalize the tensor
        normalized_tensor = (image_tensor - orig_min) / (orig_max - orig_min + epsilon)
        return normalized_tensor

    def __getitem__(self, idx):
        """
        Retrieve a single sample from the dataset.
        :param idx: Index of the sample to retrieve.
        :return: Tuple (image, bag_id, idx).
        """
        # Get metadata for the specific slice
        slice_metadata = self.slice_metadata[idx]
        # Extract bag index from the slice metadata
        bag_index = int(slice_metadata[0])
        # Get bag ID from the bag metadata
        bag_id = int(self.bag_metadata[bag_index][0])
        
        # Retrieve and preprocess the image
        img = self.zarr_data[idx] - 1024.0  # Shift the pixel values by -1024
        if self.norm_min_max:
            img = self.normalize_min_max(img)  # Apply min-max normalization
        else:
            img = self.normalize_(img)  # Apply fixed normalization
        
        # Scale the image to range [-1, 1]
        img = (img * 2) - 1
        # Convert the image to a PyTorch tensor and add a channel dimension
        img = torch.tensor(img, dtype=torch.float32).unsqueeze(0)
        
        return img, bag_id, idx  # Return the processed image, bag ID, and index


class HeartlensDatasetLoader:
    """
    Loader class to initialize a DataLoader for the HeartlensDataset.
    """

    def __init__(self, batch_size, rank=0, shuffle=True, zarr_path="dataset/uk_heartlens_v1", is_DDP=True):
        """
        Initialize the DataLoader.
        :param batch_size: Number of samples per batch.
        :param rank: Rank for distributed training (default: 0).
        :param shuffle: Whether to shuffle the dataset.
        :param zarr_path: Path to the Zarr dataset.
        :param is_DDP: Boolean flag for Distributed Data Parallel (DDP) training.
        """
        # Initialize the dataset
        segDataset = HeartlensDataset(zarr_path=zarr_path)
        # Create the DataLoader with the appropriate configuration
        self.data_loader = DataLoader(
            segDataset,
            batch_size=batch_size,
            pin_memory=True,  # Use pinned memory for faster data transfer to GPU
            shuffle=False if is_DDP else shuffle,  # Disable shuffle for DDP
            sampler=DistributedSampler(segDataset, seed=42, rank=rank, shuffle=shuffle) if is_DDP else None
        )