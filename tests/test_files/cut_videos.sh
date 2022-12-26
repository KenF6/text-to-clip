#!/bin/bash

# Check that the start time, end time, input directory, and output directory arguments are provided
if [ $# -ne 4 ]; then
  echo "Usage: cut_videos.sh start_time end_time input_directory output_directory"
  exit 1
fi

# Set the start time and end time for the cut
start_time=$1
end_time=$2

input_dir=$3
output_dir=$4

# Convert the input and output directories to their absolute paths
input_dir=$(realpath "$input_dir")
output_dir=$(realpath "$output_dir")

# Convert the start time and end time to Unix timestamps
start_timestamp=$(date -d "$start_time" +%s)
end_timestamp=$(date -d "$end_time" +%s)

# Subtract the start time from the end time
difference=$((end_timestamp - start_timestamp))

# Convert the difference to a timestamp string with milliseconds
duration=$(date -u -d @"$difference" +"%T.%3N")

# Loop through all files in the input directory
for file in "$input_dir"/*; do
  if ffprobe -v error -show_streams "$file" > /dev/null; then
    # Cut the media file using FFmpeg
	filename=$(basename "$file")
    ffmpeg -ss "$start_time" -i "$file"  -t "$duration" -c copy "$output_dir/cut-$filename"
  fi
done
