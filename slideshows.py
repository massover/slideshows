import argparse
import os
import sys

from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.concatenate import concatenate

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = f'{BASE_DIR}/imgs'
IMAGE_CLIP_DURATION = 5


def get_default_image_filenames():
    return [f'{IMG_DIR}/{file}' for file in os.listdir(IMG_DIR)] * 4


def get_default_audio_filename():
    return f'{BASE_DIR}/halo.mp3'


def get_default_output_filename():
    return f'{BASE_DIR}/bruce_the_bulldog.mp4'


def create(images_filenames, audio_filename, output_filename):
    image_clips = []
    for image in images_filenames:
        image_clip = ImageClip(image)
        image_clip = image_clip.set_duration(IMAGE_CLIP_DURATION)
        image_clips.append(image_clip)

    audio_clip = AudioFileClip(audio_filename)
    audio_clip = audio_clip.set_end(IMAGE_CLIP_DURATION * len(images_filenames))

    video_clip = concatenate(image_clips, method='compose')
    video_clip = video_clip.set_audio(audio_clip)
    video_clip.write_videofile(output_filename, fps=10)


def main():
    parser = argparse.ArgumentParser(description='Generate a slideshow for a collection of images')
    parser.add_argument("create")
    parser.add_argument("--images", nargs='*', default=get_default_image_filenames())
    parser.add_argument("--audio_filename", default=get_default_audio_filename())
    parser.add_argument("--output_filename", default=get_default_output_filename())
    args = parser.parse_args()
    files = args.images + [args.audio_filename]
    for file_ in files:
        if not os.path.isfile(file_):
            sys.exit(f'Invalid image file {file_}')

    create(args.images, args.audio_filename, args.output_filename)


if __name__ == '__main__':
    main()
