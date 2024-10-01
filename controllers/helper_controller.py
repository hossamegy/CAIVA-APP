import random

# Define a function to select a random phrase
def get_random_noise_phrase():
    noise_phrases = [
        "I'm having trouble hearing you; there's a lot of background noise.",
        "It sounds like there's noise around you, and I can't hear you clearly.",
        "Your voice is hard to hear because of some surrounding noise.",
        "There's too much noise around you; I can't hear you properly.",
        "I can't hear you well with all the noise in the background.",
        "There's background noise that's making it difficult to hear you.",
        "It's tough to hear you due to the noise around you.",
        "The noise around you is making it hard to understand you.",
        "I can barely hear you over the noise in the background.",
        "There’s too much noise; I’m struggling to hear you.",
        "It’s noisy around you, and I can’t hear what you’re saying.",
        "I can’t hear you clearly because of the background noise.",
        "All the noise is making it difficult to hear your voice.",
        "Your voice is being drowned out by noise around you.",
        "With all that noise, I can't hear you very well.",
        "The noise near you is making it hard for me to hear.",
        "It sounds noisy around you, and I’m having trouble hearing you.",
        "There’s too much background noise; I can’t hear you properly.",
        "I'm finding it hard to hear you over the noise around you.",
        "It’s difficult to understand you because of the noise."
    ]
    return random.choice(noise_phrases)

def slice_string_to_40_words(input_string): 
    # Split the string into words
    words = input_string.split()
    # Initialize an empty list to store the sliced strings
    sliced_dict_with_emotion = {}
    sliced_dict = {}
        # Iterate through the words and slice into chunks of 40 words
    for i in range(0, len(words), 40):
        sliced_words = ' '.join(words[i:i+40])
       # emotion = predict_emotion(sliced_words)
        sliced_dict[len(sliced_dict) + 1] = sliced_words
        #sliced_dict_with_emotion[len(sliced_dict_with_emotion) + 1] = emotion + " " + sliced_words
        #sliced_dict_with_emotion[len(sliced_dict_with_emotion)] = sliced_dict_with_emotion[len(sliced_dict_with_emotion)] + " <emotion Neutral intensity 80>"
        sliced_dict_with_emotion[len(sliced_dict_with_emotion) + 1] = sliced_words
        sliced_dict_with_emotion[len(sliced_dict_with_emotion)] = sliced_dict_with_emotion[len(sliced_dict_with_emotion)] + " <emotion Neutral intensity 80>"
    
    return sliced_dict_with_emotion, sliced_dict