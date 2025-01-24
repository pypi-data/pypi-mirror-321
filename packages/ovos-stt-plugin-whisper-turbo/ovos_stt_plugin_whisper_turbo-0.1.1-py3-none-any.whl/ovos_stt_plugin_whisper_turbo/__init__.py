from ovos_plugin_manager.templates.stt import STT
from ovos_stt_plugin_whisper import WhisperSTT
from ovos_utils.log import LOG


class WhisperTurboSTT(STT):
    MODELS = ["openai/whisper-large-v3-turbo"]

    def __init__(self, config=None):
        super().__init__(config)
        model_id = "openai/whisper-large-v3-turbo"
        self.config["model"] = model_id
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
        return self.stt.available_languages
