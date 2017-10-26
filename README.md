# slideshows

## System Requirements

```
python 3.6
```

## Quickstart

```
git clone git@github.com:massover/slideshows.git

python3 -m venv venv # or make your virtualenv
source venv/bin/activate # or activate your virtualenv
pip install -r requirements.txt
python -c 'import imageio; imageio.plugins.ffmpeg.download()'

slideshows create

# There's a codec issue with quicktime, use chrome instead.
chrome bruce_the_bulldog.mp4
```
## Usage

### API

```python
import slideshows

slideshows.create(image_filenames=['file.jpg'], audio_filename='audio_file.mp4',
                  output_filename='output_file.mp4')
```

## CLI

```bash
slideshows create  --images file1.jpg file2.jpg \
                   --audio_filename audio_file.mp4 \
                   --outputfile outputfile.mp4
```

## Testing

```
pytest
```