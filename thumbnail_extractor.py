# From https://jacopodaeli.medium.com/from-video-to-thumbnails-with-python-and-opencv-ce5983cbb76a
import os
import cv2

def run_example():
  """Extract frames from the video and creates thumbnails for one of each"""
  # Extract frames from video
  print("Extract frames from video")
  # frames = video_to_frames('/home/anley1/aa20/Dataset/Videos/%s' % video_name)

  # Walk through all files in directory
  target_dir = "C:\\Users\\aleye\\Swin-Transformer-Object-Detection\\data" \
               "\\video"

  for subdir, dirs, files in os.walk(target_dir):
      for file in files:
          # print os.path.join(subdir, file)
          filepath = subdir + os.sep + file

          if filepath.endswith(".MP4") or filepath.endswith(".mp4") or \
                  filepath.endswith(".avi"):
              print(filepath)
              frames = video_to_frames(filepath)
              # Generate and save thumbs
              print("Generate and save thumbs")
              for i in range(len(frames)):
                thumb = image_to_thumbs(frames[i])
                os.makedirs('frames/%s/%d' % (file, i))
                for k, v in thumb.items():
                  cv2.imwrite('frames/%s/%d/%s.png' % (file, i, k), v)

def video_to_frames(video_filename):
    """Extract frames from video"""
    cap = cv2.VideoCapture(video_filename)
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print(video_length)
    frames = []
    if cap.isOpened() and video_length > 0:
        frame_ids = [0]
        if video_length >= 4:
            frame_ids = [0,
                         round(video_length * 0.25),
                         round(video_length * 0.5),
                         round(video_length * 0.75),
                         video_length - 1]
        # print(frame_ids)
        # count = 0
        # success, image = cap.read()
        # while success or count < video_length:
        #     if count in frame_ids and success:
        #         frames.append(image)
        #     success, image = cap.read()
        #     # print(count)
        #     # print(success)
        #     count += 1

        for frame_id in frame_ids:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_id-1)
            success, image = cap.read()
            if success:
                frames.append(image)

    return frames

def image_to_thumbs(img):
    """Create thumbs from image"""
    height, width, channels = img.shape
    thumbs = {"original": img}
    sizes = [640, 320, 160]
    for size in sizes:
        if (width >= size):
            r = (size + 0.0) / width
            max_size = (size, int(height * r))
            thumbs[str(size)] = cv2.resize(img, max_size, interpolation=cv2.INTER_AREA)
    return thumbs

if __name__ == '__main__':
    run_example()
