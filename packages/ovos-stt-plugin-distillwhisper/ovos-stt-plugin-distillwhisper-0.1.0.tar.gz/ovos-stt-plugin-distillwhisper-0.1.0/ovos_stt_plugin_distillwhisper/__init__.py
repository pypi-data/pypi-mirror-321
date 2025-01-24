from ovos_plugin_manager.templates.stt import STT
from ovos_stt_plugin_whisper import WhisperSTT
from ovos_utils.log import LOG


class DistillWhisperSTT(STT):
    MODELS = ["distil-whisper/distil-small.en",
              "distil-whisper/distil-medium.en",
              "distil-whisper/distil-large-v2",
              "distil-whisper/distil-large-v3"]

    def __init__(self, config=None):
        super().__init__(config)
        model_id = self.config.get("model") or "distil-whisper/distil-medium.en"
        if model_id == "small":
            model_id = "distil-whisper/distil-small.en"
        elif model_id == "medium":
            model_id = "distil-whisper/distil-medium.en"
        elif model_id == "large-v2":
            model_id = "distil-whisper/distil-large-v2"
        elif model_id == "large" or model_id == "large-v3":
            model_id = "distil-whisper/distil-large-v3"

        self.config["model"] = model_id
        self.config["lang"] = "en"
        self.config["ignore_warnings"] = True
        valid_model = model_id in self.MODELS
        if not valid_model:
            LOG.info(f"{model_id} is not default model_id ({self.MODELS}), "
                     f"assuming huggingface repo_id or path to local model")
        self.stt = WhisperSTT(self.config)

    def execute(self, audio, language=None):
        return self.stt.execute(audio, language)

    @property
    def available_languages(self) -> set:
        return {"en"}

