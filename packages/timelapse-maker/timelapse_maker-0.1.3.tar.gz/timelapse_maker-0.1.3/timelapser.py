import cv2
import numpy as np
from multiprocessing import Pool, cpu_count
import math
from tqdm import tqdm
import os
import time

def get_target_duration():
    while True:
        try:
            hours = int(input("Enter hours (0 or more): "))
            minutes = int(input("Enter minutes (0-59): "))
            seconds = int(input("Enter seconds (0-59): "))
            
            if hours < 0 or minutes < 0 or seconds < 0:
                print("Please enter non-negative values.")
                continue
            if minutes > 59 or seconds > 59:
                print("Minutes and seconds must be between 0 and 59.")
                continue
                
            return hours * 3600 + minutes * 60 + seconds
        except ValueError:
            print("Please enter valid numbers.")

def get_optimal_cores():
    try:
        available_cores = cpu_count()
        # Use all cores except 2, but ensure at least 1 core is used
        optimal_cores = max(1, available_cores - 2)
        return optimal_cores
    except:
        # Fallback to a conservative default if detection fails
        return 4

def process_chunk(args):
    video_path, frame_indices, chunk_id, target_duration, total_target_frames = args
    cap = cv2.VideoCapture(video_path)
    
    # Calculate seconds per frame
    seconds_per_frame = target_duration / total_target_frames
    start_time = time.time()
    frames_processed = 0
    
    # Create progress bar for this chunk
    pbar = tqdm(
        total=len(frame_indices),
        desc=f"Core {chunk_id}",
        position=chunk_id + 1,  # +1 to leave room for main bar at position 0
        unit=" frames",
        leave=True,  # Changed to True for better visibility
        dynamic_ncols=True,
        mininterval=0.5,  # Increased to reduce update frequency
        maxinterval=2.0
    )
    
    frames = []
    try:
        for idx in frame_indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
            ret, frame = cap.read()
            if ret:
                frames.append(frame)
                frames_processed += 1
                
                # Update progress bar with speed info
                elapsed = time.time() - start_time
                if elapsed > 0:
                    timelapse_seconds = frames_processed * seconds_per_frame
                    speed = timelapse_seconds / elapsed
                    pbar.set_description(f"Core {chunk_id} [{speed:.1f}x]")
                
                pbar.update(1)
    finally:
        pbar.close()
        cap.release()
    
    return frames

def create_timelapse(video_path, output_path, target_duration=None, target_fps=60, cores=None, batch_size=32):
    # Validate input file exists
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Input video file not found: {video_path}")
    
    # Get target duration from user if not specified
    if target_duration is None:
        target_duration = get_target_duration()
    
    # Get optimal core count if not specified
    if cores is None:
        cores = get_optimal_cores()
    
    # Open video
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    original_fps = cap.get(cv2.CAP_PROP_FPS)
    original_duration = total_frames / original_fps
    cap.release()
    
    # Validate target duration
    if target_duration > original_duration:
        raise ValueError(f"Target duration ({target_duration}s) cannot be longer than original duration ({original_duration:.2f}s)")

    # Calculate compression details
    target_frames = target_duration * target_fps
    compression_ratio = original_duration / target_duration
    step = total_frames / target_frames

    # Print information
    print(f"Original video duration: {original_duration:.2f} seconds")
    print(f"Target duration: {target_duration} seconds")
    print(f"Compression ratio: {compression_ratio:.2f}x")
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
        for i in range(0, len(frame_indices), batch_size * cores):
            # Clear previous iteration's progress bars
            for j in range(cores):
                print("\033[1A\033[K" * 2)  # Move up and clear line
            
            batch_indices = frame_indices[i:i + batch_size * cores]
            chunks = np.array_split(batch_indices, cores)
            args = [(video_path, chunk.copy(), j, target_duration, target_frames) for j, chunk in enumerate(chunks)]
            
            # Process batch in parallel
            with Pool(cores) as p:
                batch_results = list(p.imap(process_chunk, args))
                
                # Write frames from this batch
                for chunk in batch_results:
                    chunk_size = len(chunk)
                    total_frames_processed += chunk_size
                    
                    elapsed = time.time() - start_time
                    if elapsed > 0:
                        timelapse_seconds = total_frames_processed * (target_duration / target_frames)
                        speed = timelapse_seconds / elapsed
                        overall_pbar.set_description(f"Total Progress [{speed:.1f}x]")
                    
                    overall_pbar.update(chunk_size)
                    
                    for frame in chunk:
                        out.write(frame)
                    
                del batch_results
            
            del chunks
            del args
            
    finally:
        # Clear all progress bars
        print("\n" * (cores + 1))  # Move past all progress bars
        overall_pbar.close()
        out.release()
        print(f"\nProcessing complete. Output saved to: {output_path}")

# Move the usage examples inside a main guard
if __name__ == '__main__':
    try:
        video_path = input("Enter input video path: ")
        # Generate output path by adding "_timelapse" before the extension
        base, ext = os.path.splitext(video_path)
        output_path = f"{base}_timelapse{ext}"
        create_timelapse(video_path, output_path)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

