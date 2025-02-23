import pdfplumber #pip install pdfplumber
import os
from gtts import gTTS #pip install gtts
from moviepy import * #pip install moviepy

def extract_text_from_pdf(pdf_path): #needs to be in pdf, turns it into a huge string
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + " "
    return text

def split_text(text, chunk_size=16): #splits text to 5 words on the video at a time
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

def generate_tts(text, output_audio): #text to speech
    tts = gTTS(text)
    tts.save(output_audio)

def create_video(text, bg_video, output_video):
    phrases = split_text(text)
    font = "/Users/daniel/Documents/coding_stuff/novaSpy/project_website/static/arial.ttf" #FONT MUST BE GIVEN
    audio_path = "temp_audio.mp3"
    generate_tts(" ".join(phrases), audio_path)
    audio_clip = AudioFileClip(audio_path)
    
    video = VideoFileClip(bg_video).subclipped(0, audio_clip.duration) #cuts video to length of audio
    clips = [video]

    
    duration_per_text = audio_clip.duration / len(phrases) #makes each batch of words appear for an even amount of time to last the whole video
    current_time = 0
    
    for phrase in phrases:
        txt_clip = TextClip(font = font, 
                            text = phrase, 
                            font_size=25, #adjustable
                            size=(video.w, video.h - 75), #decrease video.h to move text higher 
                            color="#fff", #adjustable
                            method = "caption",
                            text_align = "center", 
                            horizontal_align = "center", 
                            vertical_align = "bottom", 
                            duration = duration_per_text)
        
        txt_clip = txt_clip.with_start(current_time) #tells the txtclip to appear after a set time
        clips.append(txt_clip)
        current_time += duration_per_text
    
    final_video = CompositeVideoClip(clips)
    final_video = final_video.with_audio(audio_clip)
    final_video.write_videofile(output_video, fps=24)
    
    # os.remove(audio_path) #clean up

# Example usage
# create_video("text", "1min30video.mp4", "output.mp4")
