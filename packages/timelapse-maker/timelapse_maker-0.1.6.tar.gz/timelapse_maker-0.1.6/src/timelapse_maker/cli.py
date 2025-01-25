import argparse
from .core import create_timelapse

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

def parse_duration(duration_str):
    """Parse duration string in format HH:MM:SS"""
    try:
        h, m, s = map(int, duration_str.split(':'))
        return h * 3600 + m * 60 + s
    except:
        raise argparse.ArgumentTypeError("Duration must be in format HH:MM:SS")

def main():
    parser = argparse.ArgumentParser(description='Create a timelapse video.')
    parser.add_argument('-i', '--input', default='input.mp4',
                      help='input video file path (default: input.mp4)')
    parser.add_argument('-o', '--output', default='output.mp4',
                      help='output video file path (default: output.mp4)')
    parser.add_argument('-d', '--duration', type=parse_duration,
                      help='Target duration in format HH:MM:SS (if not provided, will prompt interactively)')
    parser.add_argument('--fps', type=int, default=60,
                      help='Target frames per second (default: 60)')

    args = parser.parse_args()
    
    try:
        # If duration not provided via CLI, get it interactively
        target_duration = args.duration if args.duration is not None else get_target_duration()
        
        create_timelapse(
            video_path=args.input,
            output_path=args.output,
            target_duration=target_duration,
            target_fps=args.fps
        )
        return 0
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

if __name__ == "__main__":
    exit(main()) 