import os

import slideshows

TEST_OUTPUT_FILENAME = f'{slideshows.BASE_DIR}/test_bruce_the_bulldog.mp4'

def test_create():
    image_filenames = slideshows.get_default_image_filenames()
    audio_filename = slideshows.get_default_audio_filename()
    slideshows.create(image_filenames, audio_filename, TEST_OUTPUT_FILENAME)
    assert os.path.isfile(TEST_OUTPUT_FILENAME)

def teardown_module(module):
    try:
        os.remove(TEST_OUTPUT_FILENAME)
    except OSError:
        pass

