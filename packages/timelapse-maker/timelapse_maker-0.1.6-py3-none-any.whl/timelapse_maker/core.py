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
    
    frames = []
    cap = cv2.VideoCapture(video_path)
    
    # Create chunk progress bar
    chunk_pbar = tqdm(
        total=len(frame_indices),
        desc=f"Chunk {chunk_id}",
        position=chunk_id + 1,  # Position below main bar
        unit=" frames",
        leave=False
    )
    
    try:
        for frame_idx in frame_indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
            ret, frame = cap.read()
            if not ret:
                raise RuntimeError(f"Could not read frame {frame_idx}")
            frames.append(frame)
            chunk_pbar.update(1)
    finally:
        cap.release()
        chunk_pbar.close()
    
    return frames

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
    """
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Input video file not found: {video_path}")
    
    # Initialize video capture
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    original_fps = cap.get(cv2.CAP_PROP_FPS)
    original_duration = total_frames / original_fps
    
    # Calculate target frames
    if target_duration is None:
        target_duration = original_duration / 10  # Default to 10x speedup
    
    if target_duration > original_duration:
        raise ValueError("Target duration cannot be longer than original video")
    
    target_frames = int(target_duration * target_fps)
    step = total_frames / target_frames
    
    # Set number of cores
    if cores is None:
        cores = get_optimal_cores()
    
    print(f"Processing {target_frames} frames out of {total_frames} total frames")
    print(f"Using {cores} CPU cores")

    # Calculate frame indices needed
    frame_indices = [int(i * step) for i in range(int(target_frames))]
    
    # Create output video writer early
    cap = cv2.VideoCapture(video_path)
    ret, sample_frame = cap.read()
    cap.release()
    if not ret:
        raise RuntimeError("Could not read sample frame from video")
        
    out = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*'mp4v'),
        target_fps,
        (sample_frame.shape[1], sample_frame.shape[0])
    )

    # Process in batches
    print("Processing frames...")
    start_time = time.time()
    total_frames_processed = 0
    
    # Create overall progress bar
    overall_pbar = tqdm(
        total=len(frame_indices),
        desc="Total Progress",
        position=0,  # Main bar at top
        unit=" frames",
        dynamic_ncols=True,
        mininterval=0.5,
        maxinterval=2.0,
        leave=True
    )
    
    try:
        with Pool(cores) as pool:
            for batch_start in range(0, len(frame_indices), batch_size):
                batch_indices = frame_indices[batch_start:batch_start + batch_size]
                
                # Prepare arguments for each process
                chunk_args = []
                for i, chunk_indices in enumerate(np.array_split(batch_indices, cores)):
                    if len(chunk_indices) > 0:  # Only process non-empty chunks
                        chunk_args.append((
                            video_path,
                            chunk_indices.tolist(),
                            i,
                            target_duration,
                            target_frames
                        ))
                
                # Process chunks in parallel
                results = pool.map(process_chunk, chunk_args)
                
                # Write frames to output
                for chunk_frames in results:
                    for frame in chunk_frames:
                        out.write(frame)
                        total_frames_processed += 1
                
                # Update overall progress
                overall_pbar.update(len(batch_indices))
                
    finally:
        overall_pbar.close()
        out.release()
    
    end_time = time.time()
    print(f"\nProcessed {total_frames_processed} frames in {end_time - start_time:.2f} seconds")
    print(f"Output saved to: {output_path}") 