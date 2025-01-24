# coding = utf-8
# @Time    : 2024-12-10  12:42:03
# @Author  : zhaosheng@lyxxkj.com.cn
# @Describe: VAD Model and Iterator definition.

import math
from functools import partial
from pathlib import Path
from typing import Union
import os
import numpy as np
import soundfile as sf
from tqdm import tqdm

from dguard.vad.frame_queue import FrameQueue
from dguard.vad.pickable_session import vad_session
from pydub import AudioSegment
import math

import librosa
import time

def _adjust_audio_length(audio_file):
    # 加载音频文件
    #audio = AudioSegment.from_file(audio_file)
    with open(audio_file, 'rb') as file:
        audio = AudioSegment.from_file(file)
    # 获取音频长度（毫秒）
    length_ms = len(audio)
    length_s = length_ms / 1000
    if length_s < 5:
        silence_duration_ms = 5 * 1000 - leng_s
    else:
    # 计算补充到下一个10的倍数
        next_length_s = math.ceil(length_s / 10) * 10

    # 计算需要补充的静音部分（单位：毫秒）
        silence_duration_ms = (next_length_s * 1000) - length_ms

    # 创建静音部分并加到音频后面
    silence = AudioSegment.silent(duration=silence_duration_ms)
    adjusted_audio = audio + silence

    # 保存调整后的音频文件
    file_path, file_extension = os.path.splitext(audio_file)
    
    # 构建保存的文件路径
    output_path = os.path.join(os.path.dirname(audio_file), f"adjusted_{os.path.basename(audio_file)}")
    
    # 保存调整后的音频文件，保留原文件扩展名
    with open(output_path, 'wb') as output_file:
        adjusted_audio.export(output_file, format=file_extension[1:])
    print(output_path)
    # 返回保存后的文件路径
    return output_path
def adjust_audio_length(audio_file):
    # 直接使用文件路径加载音频
    audio = AudioSegment.from_file(audio_file)
    
    # 获取音频长度（毫秒）
    length_ms = len(audio)
    length_s = length_ms / 1000

    # 如果音频小于5秒，直接补充到5秒，否则补充到下一个10的倍数
    if length_s <= 5:
        silence_duration_ms = 5 * 1000 - length_ms
    else:
        next_length_s = math.ceil(length_s / 10) * 10
        silence_duration_ms = (next_length_s * 1000) - length_ms

    # 创建静音部分并加到音频后面
    silence = AudioSegment.silent(duration=silence_duration_ms)
    adjusted_audio = audio + silence

    # 获取文件的路径和扩展名
    file_path, file_extension = os.path.splitext(audio_file)
    
    # 构建输出文件路径
    output_path = os.path.join(os.path.dirname(audio_file), f"adjusted_{os.path.basename(audio_file)}")

    # 直接使用 export 保存文件
    adjusted_audio.export(output_path, format=file_extension[1:])

    # 返回输出文件路径
    return output_path

class VAD:
    def __init__(
        self,
        sample_rate: int = 16000,
        threshold: float = 0.5,
        min_silence_duration_ms: int = 300,
        speech_pad_ms: int = 100
    ):
        """
        Init silero VAD model

        Parameters
        ----------
        sample_rate: int (default - 16000)
            sample rate of the input audio
        threshold: float (default - 0.5)
            Speech threshold. Silero VAD outputs speech probabilities for each audio
            chunk, probabilities ABOVE this value are considered as SPEECH. It is
            better to tune this parameter for each dataset separately, but "lazy"
            0.5 is pretty good for most datasets.
        min_silence_duration_ms: int (default - 300 milliseconds)
            In the end of each speech chunk wait for min_silence_duration_ms before
            separating it.
        speech_pad_ms: int (default - 100 milliseconds)
            Final speech chunks are padded by speech_pad_ms each side.
        """

        self.session = vad_session
        self.threshold = threshold
        self.sample_rate = sample_rate

        self.speech_pad_samples = speech_pad_ms * sample_rate // 1000
        self.min_silence_samples = min_silence_duration_ms * sample_rate // 1000
        self.model_sample_rate = sample_rate if sample_rate in [8000, 16000] else 16000

        self.state = np.zeros((2, 1, 128), dtype=np.float32)
        self.context_size = 64 if self.model_sample_rate == 16000 else 32
        self.context = np.zeros((1, self.context_size), dtype=np.float32)

        self.num_samples = 512 if self.model_sample_rate == 16000 else 256
        self.queue = FrameQueue(
            self.num_samples,
            self.sample_rate,
            self.speech_pad_samples,
            out_rate=self.model_sample_rate,
        )

        self.segment = 0

    def reset(self):
        self.segment = 0
        self.queue = FrameQueue(
            self.num_samples,
            self.sample_rate,
            self.speech_pad_samples,
            out_rate=self.model_sample_rate,
        )
        self.state = np.zeros((2, 1, 128), dtype=np.float32)
        self.context = np.zeros((1, self.context_size), dtype=np.float32)

    def __call__(self, x, sr):
        x = np.concatenate((self.context, x[np.newaxis, :]), axis=1)
        self.context = x[:, -self.context_size :]
        ort_inputs = {
            "input": x,
            "state": self.state,
            "sr": np.array(sr, dtype=np.int64),
        }
        output, self.state = self.session.run(ort_inputs)
        return output

    def add_chunk(self, chunk, is_last=False):
        return self.queue.add_chunk(chunk, is_last)

    def read_audio(self, wav_path: Union[str, Path]):
        audio, sample_rate = sf.read(wav_path, dtype=np.float32)
        if sample_rate != self.sample_rate:
            raise ValueError(
                "Sample rate mismatch.\n"
                "Reinitialize SileroVAD(sample_rate=sr) with the correct sample rate."
            )
        if len(audio.shape) > 1:
            raise ValueError("Only supported mono wav.")
        dur_ms = len(audio) * 1000 / sample_rate
        if dur_ms < 32:
            raise ValueError("Input audio is too short.")
        return audio, sample_rate, dur_ms

    def get_speech_probs(self, wav_path: Union[str, Path]):
        """
        Getting speech probabilities of audio frames (32ms/frame)

        Parameters
        ----------
        wav_path: wav path

        Returns
        ----------
        speech_probs: list of speech probabilities
        """
        self.reset()
        audio, _, dur_ms = self.read_audio(wav_path)
        progress_bar = tqdm(
            total=math.ceil(dur_ms / 32),
            desc="VAD processing",
            unit="frames",
            bar_format="{l_bar}{bar}{r_bar} | {percentage:.2f}%",
        )
        for _, _, frame in self.add_chunk(audio, True):
            progress_bar.update(1)
            yield np.around(self(frame, self.model_sample_rate)[0][0], 2)

    def process_segment(self, segment, wav, save_path, flat_layout, return_seconds):
        index = segment["segment"]
        start = max(segment["start"] - self.speech_pad_samples, 0)
        end = min(segment["end"] + self.speech_pad_samples, len(wav))
        if save_path is not None:
            wav = wav[start:end]
            if flat_layout:
                sf.write(str(save_path) + f"_{index:05d}.wav", wav, self.sample_rate)
            else:
                save_path = Path(save_path)
                if not save_path.exists():
                    save_path.mkdir(parents=True, exist_ok=True)
                sf.write(str(save_path / f"{index:05d}.wav"), wav, self.sample_rate)
        if return_seconds:
            start = round(start / self.sample_rate, 3)
            end = round(end / self.sample_rate, 3)
        return {"segment": index, "start": start, "end": end}

    def get_speech_timestamps(
        self,
        wav_path: Union[str, Path],
        save_path: Union[str, Path] = None,
        flat_layout: bool = True,
        min_speech_duration_ms: int = 250,
        max_speech_duration_s: float = float("inf"),
        return_seconds: bool = False,
    ):
        #import time
        #start = time.time()
        new_path = adjust_audio_length(wav_path)
        #end = time.time()
        #print(end-start)
        segments = self.session.segments_offline(Path(new_path))
        ms = 1000
        formatted_segments = [
                            {
            "segment": i,
            "start": round(segment[0] / ms, 3),
            "end": round(segment[1] / ms, 3),                                                                                                                                                              }
        for i, segment in enumerate(segments)
                            ]
        if os.path.exists(new_path):
            os.remove(new_path)
        return formatted_segments

    def get_speech_timestamps_energy(
            self,
            wav_path: str,
            save_path: str = None,
            float_layout: bool = True,
            energy_threshold: float = 0.02,
            frame_length: int = 1024,
            hop_length: int = 512,
            min_speech_duration_ms: int = 250,
            merge_close_segments_ms: int = 100,
            return_seconds: bool = True,
            max_speech_duration_s: int = 9999
    ):
        """
        基于音频能量的快速 VAD 实现，并支持合并相近语音段。
        
        Args:
            wav_path (str): 输入音频文件路径（支持 WAV 格式）。
            energy_threshold (float): 能量阈值，用于区分语音与静音。
            frame_length (int): 帧长度。
            hop_length (int): 帧移长度。
            min_speech_duration_ms (int): 最短语音段长度，单位毫秒。
            merge_close_segments_ms (int): 合并间隔小于此毫秒数的相邻语音段。
            return_seconds (bool): 是否返回秒为单位的时间戳。

        Returns:
            list: 每段语音的起止时间，格式为 [{'segment': idx, 'start': time1, 'end': time2}, ...]。
        """
        y, sr = librosa.load(wav_path, sr=None)
        frame_duration_ms = (frame_length / sr) * 1000
        
        energy = np.array([
            np.sum(np.abs(y[i:i + frame_length]**2))
            for i in range(0, len(y) - frame_length + 1, hop_length)
        ])
        
        is_speech = energy > energy_threshold
        speech_frames = np.where(is_speech)[0]
        
        if len(speech_frames) == 0:
            return []

        segments = []
        start = speech_frames[0]
        for i in range(1, len(speech_frames)):
            if speech_frames[i] != speech_frames[i - 1] + 1:
                end = speech_frames[i - 1]
                segments.append((start, end))
                start = speech_frames[i]
        segments.append((start, speech_frames[-1]))
        
        min_speech_frames = int((min_speech_duration_ms / frame_duration_ms))
        formatted_segments = []
        for start, end in segments:
            if end - start + 1 >= min_speech_frames:
                start_time = start * hop_length / sr
                end_time = (end + 1) * hop_length / sr
                formatted_segments.append((start_time, end_time))
        
        merged_segments = []
        current_start, current_end = formatted_segments[0]
        for start, end in formatted_segments[1:]:
            if start - current_end <= merge_close_segments_ms / 1000:
                current_end = end
            else:
                merged_segments.append((current_start, current_end))
                current_start, current_end = start, end
        merged_segments.append((current_start, current_end))
        
        result_segments = [
            {
                "segment": i,
                "start": round(start if return_seconds else start * 1000, 3),
                "end": round(end if return_seconds else end * 1000, 3),
            }
            for i, (start, end) in enumerate(merged_segments)
        ]
        if save_path:
            # 保存拼接后的只有有效音的音频到文件
            combined_audio = []
            for start, end in merged_segments:
                start_sample = int(start * sr)
                end_sample = int(end * sr)
                segment_audio = y[start_sample:end_sample]
                combined_audio.append(segment_audio)
            combined_audio = np.concatenate(combined_audio)
            sf.write(save_path, combined_audio, sr)
        return result_segments
        

    def _get_speech_timestamps(
        self,
        wav_path: Union[str, Path],
        save_path: Union[str, Path] = None,
        flat_layout: bool = True,
        min_speech_duration_ms: int = 250,
        max_speech_duration_s: float = float("inf"),
        return_seconds: bool = False,
    ):
        """
        Splitting long audios into speech chunks using silero VAD

        Parameters
        ----------
        wav_path: wav path
        save_path: string or Path (default - None)
            whether the save speech segments
        flat_layout: bool (default - True)
            whether use the flat directory structure
        min_speech_duration_ms: int (default - 250 milliseconds)
            Final speech chunks shorter min_speech_duration_ms are thrown out
        max_speech_duration_s: int (default - inf)
            Maximum duration of speech chunks in seconds
            Chunks longer than max_speech_duration_s will be split at the timestamp
            of the last silence that lasts more than 98ms (if any), to prevent
            agressive cutting. Otherwise, they will be split aggressively just
            before max_speech_duration_s.
        return_seconds: bool (default - False)
            whether return timestamps in seconds (default - samples)

        Returns
        ----------
        speeches: list of dicts
            list containing ends and beginnings of speech chunks (samples or seconds
            based on return_seconds)
        """
        self.reset()
        audio, sample_rate, dur_ms = self.read_audio(wav_path)
        progress_bar = tqdm(
            total=math.ceil(dur_ms / 32),
            desc="VAD processing",
            unit="frames",
            bar_format="{l_bar}{bar}{r_bar} | {percentage:.2f}%",
        )

        min_silence_samples_at_max_speech = 98 * sample_rate // 1000
        min_speech_samples = min_speech_duration_ms * sample_rate // 1000
        max_speech_duration_samples = max_speech_duration_s * sample_rate
        max_speech_samples = max_speech_duration_samples - 2 * self.speech_pad_samples

        fn = partial(
            self.process_segment,
            wav=audio,
            save_path=save_path,
            flat_layout=flat_layout,
            return_seconds=return_seconds,
        )

        current_speech = {}
        neg_threshold = self.threshold - 0.15
        triggered = False
        # to save potential segment end (and tolerate some silence)
        temp_end = 0
        # to save potential segment limits in case of maximum segment size reached
        prev_end = 0
        next_start = 0
        for frame_start, frame_end, frame in self.add_chunk(audio, True):
            progress_bar.update(1)
            speech_prob = self(frame, self.model_sample_rate)
            # current frame is speech
            if speech_prob >= self.threshold:
                if temp_end > 0 and next_start < prev_end:
                    next_start = frame_end
                temp_end = 0
                if not triggered:
                    triggered = True
                    current_speech["start"] = frame_end
                    continue
            # in speech, and speech duration is more than max speech duration
            if triggered and frame_start - current_speech["start"] > max_speech_samples:
                # prev_end larger than 0 means there is a short silence in the middle avoid aggressive cutting
                if prev_end > 0:
                    current_speech["end"] = prev_end
                    current_speech["segment"] = self.segment
                    self.segment += 1
                    yield fn(current_speech)
                    current_speech = {}
                    # previously reached silence (< neg_thres) and is still not speech (< thres)
                    if next_start < prev_end:
                        triggered = False
                    else:
                        current_speech["start"] = next_start
                    prev_end = 0
                    next_start = 0
                    temp_end = 0
                else:
                    current_speech["end"] = frame_end
                    current_speech["segment"] = self.segment
                    self.segment += 1
                    yield fn(current_speech)
                    current_speech = {}
                    prev_end = 0
                    next_start = 0
                    temp_end = 0
                    triggered = False
                    continue
            # in speech, and current frame is silence
            if triggered and speech_prob < neg_threshold:
                if temp_end == 0:
                    temp_end = frame_end
                # record the last silence before reaching max speech duration
                if frame_end - temp_end > min_silence_samples_at_max_speech:
                    prev_end = temp_end
                if frame_end - temp_end >= self.min_silence_samples:
                    current_speech["end"] = temp_end
                    # keep the speech segment if it is longer than min_speech_samples
                    if (
                        current_speech["end"] - current_speech["start"]
                        > min_speech_samples
                    ):
                        current_speech["segment"] = self.segment
                        self.segment += 1
                        yield fn(current_speech)

                    current_speech = {}
                    prev_end = 0
                    next_start = 0
                    temp_end = 0
                    triggered = False

        # deal with the last speech segment
        if current_speech and len(audio) - current_speech["start"] > min_speech_samples:
            current_speech["end"] = len(audio)
            current_speech["segment"] = self.segment
            yield fn(current_speech)


class VADIterator(VAD):
    def __init__(
        self,
        sample_rate: int = 16000,
        threshold: float = 0.5,
        min_silence_duration_ms: int = 300,
        speech_pad_ms: int = 100,
    ):
        """
        Class for stream imitation
        """
        super().__init__(
            sample_rate,
            threshold,
            min_silence_duration_ms,
            speech_pad_ms,
        )
        self.segment = 0
        self.temp_end = 0
        self.triggered = False
        # for offline asr
        self.speech_samples = np.empty(0, dtype=np.float32)
        self.reset()

    def reset(self):
        super().reset()
        self.segment = 0
        self.temp_end = 0
        self.triggered = False
        self.speech_samples = np.empty(0, dtype=np.float32)

    def get_frame(self, speech_padding=False):
        frame = self.queue.get_frame(speech_padding)
        if speech_padding:
            self.speech_samples = np.empty(0, dtype=np.float32)
        self.speech_samples = np.concatenate((self.speech_samples, frame))
        return frame

    def __call__(self, chunk, is_last=False, return_seconds=False):
        """
        chunk: audio chunk

        is_last: bool (default - False)
            whether is the last audio chunk
        return_seconds: bool (default - False)
            whether return timestamps in seconds (default - samples)
        """
        for frame_start, frame_end, frame in self.add_chunk(chunk, is_last):
            speech_prob = super().__call__(frame, self.model_sample_rate)

            is_start = False
            if speech_prob >= self.threshold:
                self.temp_end = 0
                # triggered = True means the speech has been started
                if not self.triggered:
                    is_start = True
                    self.triggered = True
                    speech_start = max(frame_start - self.speech_pad_samples, 0)
                    if return_seconds:
                        speech_start = round(speech_start / self.sample_rate, 3)
                    yield {"start": speech_start}, self.get_frame(True)
            elif speech_prob < self.threshold - 0.15 and self.triggered:
                if not self.temp_end:
                    self.temp_end = frame_end
                if frame_end - self.temp_end >= self.min_silence_samples:
                    speech_end = self.temp_end + self.speech_pad_samples
                    if return_seconds:
                        speech_end = round(speech_end / self.sample_rate, 3)
                    self.temp_end = 0
                    self.triggered = False
                    yield {"end": speech_end, "segment": self.segment}, self.get_frame()
                    self.segment += 1
            if not is_start and self.triggered:
                yield {}, self.get_frame()

        if is_last and self.triggered:
            speech_end = self.queue.current_sample
            if return_seconds:
                speech_end = round(speech_end / self.sample_rate, 3)
            yield {"end": speech_end, "segment": self.segment}, self.get_frame()
            self.reset()
