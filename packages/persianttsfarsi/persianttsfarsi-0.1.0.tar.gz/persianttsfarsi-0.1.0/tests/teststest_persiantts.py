import unittest
import os
from persiantts import PersianTTS

class TestPersianTTS(unittest.TestCase):

    def setUp(self):
        self.tts = PersianTTS()
        self.test_text = "این یک متن تستی است."
        self.output_file = "test_output.mp3"

    def test_synthesize_default(self):
        self.tts.synthesize(self.test_text, self.output_file)
        self.assertTrue(os.path.exists(self.output_file))
        self.assertTrue(os.path.exists(self.output_file.replace(".mp3", "_processed.wav")))
        os.remove(self.output_file)
        os.remove(self.output_file.replace(".mp3", "_processed.wav"))
    
    def test_synthesize_custom_voice(self):
        custom_voice = "fa-IR-DelbarNeural"
        self.tts.synthesize(self.test_text, self.output_file, voice = custom_voice)
        self.assertTrue(os.path.exists(self.output_file))
        self.assertTrue(os.path.exists(self.output_file.replace(".mp3", "_processed.wav")))
        os.remove(self.output_file)
        os.remove(self.output_file.replace(".mp3", "_processed.wav"))

    def test_synthesize_custom_settings(self):
        custom_output = "custom_test.mp3"
        self.tts.synthesize(self.test_text, custom_output, pitch="5%", rate="20%", volume="80%")
        self.assertTrue(os.path.exists(custom_output))
        self.assertTrue(os.path.exists(custom_output.replace(".mp3", "_processed.wav")))
        os.remove(custom_output)
        os.remove(custom_output.replace(".mp3", "_processed.wav"))

if __name__ == '__main__':
    unittest.main()