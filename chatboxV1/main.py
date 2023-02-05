import re
import long_responses as long


def chance(user_input, known_words, one_word=False, required_words=[]):
    current_phrase = 0
    needed_word_present = True

    # Counts how many words are present in each predefined message
    for word in user_input:
        if word in known_words:
            current_phrase += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(current_phrase) / float(len(known_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_input:
            needed_word_present = False
            break

    # Must either have the required words, or be a single response
    if needed_word_present or one_word:
        return int(percentage * 100)
    else:
        return 0


def all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def reply(bot_response, list_of_words, one_word=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = chance(message, list_of_words, one_word, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    reply('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], one_word=True)
    reply('See you!', ['bye', 'goodbye'], one_word=True)
    reply('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    reply('You\'re welcome!', ['thank', 'thanks'], one_word=True)
    reply('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    reply('Sorry to hear that, would you like me to try and help?', ['I', 'am', 'feeling', 'overwhelmed'], required_words=['overwhelmed'])
    reply('Ok, please try doing you daily health routine', ['yes'], one_word=True)

    # Longer responses
    reply(long.R_ADVICE, ['give', 'advice', 'on', 'staying', 'motivated'], required_words=['advice'])
    reply(long.R_GF, ['Do', 'you', 'have', 'a', 'gf'], required_words=['have', 'gf'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    reply = all_messages(split_message)
    return reply


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))