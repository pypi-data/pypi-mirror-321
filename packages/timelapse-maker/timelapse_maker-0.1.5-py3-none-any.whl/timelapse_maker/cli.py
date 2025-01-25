import argparse
import os
from .core import create_timelapse

def parse_duration(duration_str: str) -> float:
    """Parse duration string in format 'HH:MM:SS' to seconds."""
    try:
        parts = [int(x) for x in duration_str.split(':')]
        if len(parts) == 3:
            hours, minutes, seconds = parts
            return hours * 3600 + minutes * 60 + seconds
        raise ValueError
    except ValueError:
        raise argparse.ArgumentTypeError("Duration must be in format HH:MM:SS")

def main():
    parser = argparse.ArgumentParser(description="Compress videos into timelapses")
    parser.add_argument(
        "-i", "--input",
        help="input video file path (default: input.mp4)",
        default="input.mp4"
    )
    parser.add_argument(
        "-o", "--output",
        help="output video file path (default: output.mp4)",
        default="output.mp4"
    )
    parser.add_argument(
        "-d", "--duration",
        type=parse_duration,
        help="Target duration in format HH:MM:SS"
    )
    parser.add_argument(
        "--fps",
        type=int,
        default=60,
        help="Target frames per second (default: 60)"
    )
    
    args = parser.parse_args()
    
    # Get absolute directory path of input file
    input_dir = os.path.dirname(os.path.abspath(args.input))
    
    # Get absolute directory path of output file
    output_dir = os.path.dirname(os.path.abspath(args.output))
    
    if not args.output:
        base, ext = os.path.splitext(args.input)
        args.output = f"{base}_timelapse{ext}"
    
    try:
        create_timelapse(
            input_dir,
            output_dir,
            target_duration=args.duration,
            target_fps=args.fps
        )
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main()) 