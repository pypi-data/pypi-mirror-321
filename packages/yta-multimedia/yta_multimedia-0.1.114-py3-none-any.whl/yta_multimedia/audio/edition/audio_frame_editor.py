from yta_general_utils.programming.parameter_validator import PythonValidator

import numpy as np


class AudioFrameEditor:
    """
    Class to simplify and encapsulate all the functionality
    related to audio frame edition (audio frame is a numpy).
    """

    @staticmethod
    def modify_volume(audio_frame: np.ndarray, factor: int = 100):
        return change_audio_volume(audio_frame, factor)
    
def change_audio_volume(audio_frame: np.ndarray, factor: int = 100):
    """
    Change the 'audio_frame' volume by applying the
    given 'factor'.

    Based on:
    https://github.com/Zulko/moviepy/blob/master/moviepy/audio/fx/MultiplyVolume.py
    """
    if not PythonValidator.is_numpy_array(audio_frame):
        raise Exception('The provided "audio" is not a numpy array.')
    
    number_of_channels = len(list(audio_frame))

    def multiply_stereo_volume(get_frame, t):
        return np.multiply(
            get_frame(t),
            np.array([factor for _ in range(number_of_channels)]).T,
        )

    def multiply_mono_volume(get_frame, t):
        return np.multiply(get_frame(t), factor)

    return multiply_mono_volume if number_of_channels == 1 else multiply_stereo_volume