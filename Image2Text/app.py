from dotenv import load_dotenv
from transformers import pipeline
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf
from datasets import load_dataset

load_dotenv()
captioner = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")
result = captioner("https://i.ytimg.com/vi/BM2RNOytvpc/sddefault.jpg")
print(f'caption = {result[0]["generated_text"]}')

generator = pipeline('text-generation', model = 'gpt2')
result = generator(result[0]['generated_text'], max_length = 30, num_return_sequences=3)
print(result)


processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

inputs = processor(text=result[0]['generated_text'], return_tensors="pt")
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)
sf.write("speech.wav", speech.numpy(), samplerate=16000)