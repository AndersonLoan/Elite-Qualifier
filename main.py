import time

# load dictionary words from file
def load_words():
  all_words = []
  start_time = time.time()
  
  with open('safedict_simple.txt', 'r') as f:
    for line in f:
      all_words.append(line.rstrip())
  end_time = time.time()

  elapsed_time = end_time - start_time
  # log words loaded and elapsed time
  print('Loaded ' + str(len(all_words)) + ' words in ' + f'{elapsed_time:.2f}' + ' seconds.')

  return all_words



def suggest(text, all_words):

  if text in all_words:
    print(text + ' is a word')
  else:
    prompt = " "
    list_1 = []
    list_2 = []
    char_num = 3 
    num_string = "three"
    corrected = False

    if len(prompt) <= 3:
      char_num = 3
      num_string = "three"
    elif len(prompt) >= 4:
      char_num = 4
      num_string = "four"

    for text in all_words:
      if prompt != text:
        for i in all_words[all_words.index(text)]:
          if len(list_1) < char_num:
            list_1.append(i)
        for i in prompt:
          if len(list_2) < char_num:
            list_2.append(i)

        if list_1 == list_2:
          corrected = True
          prompt += text
          list_1.clear()
          list_2.clear()
          break
        elif list_1 != list_2:
          list_1.clear()
          list_2.clear()
def main():
    all_words = load_words()
    print('Type some text, or type \"quit\" to stop')
    while True:
        text = input(':> ').lower()
        if ('quit' == text):
          break
        suggest(text, all_words)

if __name__ == "__main__":
    main()

