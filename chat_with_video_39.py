from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled, VideoUnavailable

def get_transcript(video_id, preferred_language="en"):
    try:
        # Get list of all transcripts for the video
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        print("Available transcripts:")
        for transcript in transcript_list:
            print(f"Language: {transcript.language}, Code: {transcript.language_code}")

        # Try to get the preferred language (e.g., English)
        try:
            transcript = transcript_list.find_transcript([preferred_language])
        except NoTranscriptFound:
            print(f"No transcript in '{preferred_language}' found. Using the first available transcript.")
            transcript = next(iter(transcript_list))

        # Fetch the actual transcript data
        transcript_data = transcript.fetch()
        text = " ".join([item["text"] for item in transcript_data])

        # Save to file
        with open(f"transcript_{video_id}.txt", "w", encoding="utf-8") as f:
            f.write(text)

        print(f"\nTranscript saved to transcript_{video_id}.txt")
        return text

    except VideoUnavailable:
        print("Error: The video is unavailable.")
    except TranscriptsDisabled:
        print("Error: Transcripts are disabled for this video.")
    except NoTranscriptFound:
        print("Error: No transcripts found for this video.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage with a video known to have captions
video_id = "iG9CE55wbtY"  # TED Talk
transcript_text = get_transcript(video_id)
print("\nSample transcript snippet:")
print(transcript_text)  # Print first 500 characters
