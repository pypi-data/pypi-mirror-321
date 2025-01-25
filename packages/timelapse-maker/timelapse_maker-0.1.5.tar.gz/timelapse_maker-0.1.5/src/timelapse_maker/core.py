import cv2
import numpy as np
from multiprocessing import Pool, cpu_count
from typing import List, Tuple, Optional
from tqdm import tqdm
import os
import time

def get_optimal_cores() -> int:
    """Calculate the optimal number of CPU cores to use."""
    try:
        available_cores = cpu_count()
        return max(1, available_cores - 2)
    except:
        return 4

def process_chunk(args: Tuple) -> List[np.ndarray]:
    """Process a chunk of video frames."""
    video_path, frame_indices, chunk_id, target_duration, total_target_frames = args
    # [Rest of the process_chunk function]
    # Copy from original lines 38-79

def create_timelapse(
    video_path: str,
    output_path: str,
    target_duration: Optional[float] = None,
    target_fps: int = 60,
    cores: Optional[int] = None,
    batch_size: int = 32
) -> None:
    """
    Create a timelapse video from an input video file.
    
    Args:
        video_path: Path to input video file
        output_path: Path where the output video will be saved
        target_duration: Desired duration in seconds
        target_fps: Target frames per second for output video
        cores: Number of CPU cores to use
        batch_size: Number of frames to process in each batch
    
    Raises:
        FileNotFoundError: If input video file doesn't exist
        ValueError: If target duration is longer than original video
        RuntimeError: If video frame cannot be read
    """
    # [Rest of the create_timelapse function]
    # Copy from original lines 82-191 