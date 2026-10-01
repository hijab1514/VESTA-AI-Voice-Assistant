"""Central configuration for the audio acquisition module.

Keeping these values here, rather than inline in audio/microphone.py,
means swapping the target device or capture backend later is a one-line
config change, not a hunt through consumer code.
"""

# Substring used to find the ReSpeaker XVF3800 among sounddevice's
# reported input devices (case-insensitive match against device name).
# The exact ALSA/PortAudio name string for the XVF3800 has not been
# confirmed on real hardware yet - update this hint after running
# device discovery once on the Raspberry Pi 5.
DEVICE_NAME_HINT = "ReSpeaker"

# Target capture format. 16 kHz mono 16-bit PCM matches what the wake
# word and STT engines planned for later phases expect. If the XVF3800
# does not support this rate/channel combination directly, that will
# surface as a stream_start_failed error in the logs - do not assume
# support until verified against the hardware.
TARGET_SAMPLE_RATE = 16000
CHANNELS = 1
DTYPE = "int16"

# Number of frames per audio block delivered by the capture callback.
BLOCK_SIZE = 1024

# Max blocks buffered between the audio callback and consumers before
# the oldest block is dropped, to bound memory use if a consumer stalls.
QUEUE_MAX_BLOCKS = 50

LOG_LEVEL = "INFO"
