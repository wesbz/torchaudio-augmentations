import pytest
from torchaudio_augmentations import Compose, ComposeMany, RandomResizedCrop

from .utils import generate_waveform

sample_rate = 22050
num_samples = sample_rate * 5


@pytest.mark.parametrize('num_channels', [1, 2])
def test_compose(num_channels):
    audio = generate_waveform(sample_rate, num_samples, num_channels)
    transform = Compose(
        [
            RandomResizedCrop(num_samples),
        ]
    )

    t_audio = transform(audio)
    assert t_audio.shape[0] == num_channels
    assert t_audio.shape[1] == num_samples


@pytest.mark.parametrize('num_channels', [1, 2])
def test_compose_many(num_channels):
    num_augmented_samples = 10

    audio = generate_waveform(sample_rate, num_samples, num_channels)
    transform = ComposeMany(
        [
            RandomResizedCrop(num_samples),
        ],
        num_augmented_samples=num_augmented_samples,
    )

    t_audio = transform(audio)
    assert t_audio.shape[0] == num_augmented_samples
    assert t_audio.shape[1] == num_channels
    assert t_audio.shape[2] == num_samples
