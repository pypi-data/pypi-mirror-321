# coding = utf-8
# @Time    : 2024-12-10  12:42:42
# @Author  : zhaosheng@lyxxkj.com.cn
# @Describe: Pickable session for VAD.

import os
import onnxruntime as ort
from functools import partial
from dguard.vad.vad_tools.dguardvad import DGUARDVad

class PickableSession:
    """
    This is a wrapper to make the current InferenceSession class pickable.
    """
    def __init__(self, onnx_path=None):
        if onnx_path is None:
            DGUARD_MODEL_PATH = os.environ.get("DGUARD_MODEL_PATH")
            if not DGUARD_MODEL_PATH:
                raise ValueError(
                    "Please set the environment variable DGUARD_MODEL_PATH or specify the onnx_path."
                )
            onnx_path = os.path.join(DGUARD_MODEL_PATH, "dguard_vad.onnx")
        self.model_path = onnx_path
        providers = [
            (
                "CANNExecutionProvider",
                {
                    "device_id": 0,
                    "arena_extend_strategy": "kNextPowerOfTwo",
                    "npu_mem_limit": 2 * 1024 * 1024 * 1024,
                    "enable_cann_graph": True,
                },
            ),
            "CPUExecutionProvider",
        ]
        self.init_session = partial(
            ort.InferenceSession,
            providers=providers
        )
        try:
            self.sess = self.init_session(self.model_path)
        except Exception as e:
            raise RuntimeError(f"Failed to initialize InferenceSession with model at {self.model_path}: {e}")

    def run(self, *args):
        return self.sess.run(None, *args)

    def __getstate__(self):
        return {"model_path": self.model_path}

    def __setstate__(self, values):
        self.model_path = values["model_path"]
        self.sess = self.init_session(self.model_path)

vad_session = DGUARDVad()