"""
დაწერეთ პროგრამა რომელიც მომხმარებლის შემოყვანილ ტექსტს დაშიფრავს ან
განშიფრავს და დაბეჭდავს ეკრანზე. ნებისმიერი სიმბოლო რომელიც არ მიეკუთვნება
a-z დატოვეთ უცვლელი.
დაშიფვრის ლოგიკა ასეთია: ყოველი დაბალი რეგისტრის სიმბოლო (a-z) უნდა
შეიცვალოს კლავიატურაზე მის მარჯვნივ მდგომი სიმბოლოთი. თუ სიმბოლოს
მარჯვნივ კლავიატურაზე ინგლისური სიმბოლო არ არის, მაშინ უნდა გადავიდეს
პირველ სიმბოლოში ამ სტრიქონიდან. მაგალითად: p -> q, l -> a და ა.შ. პროგრამამ
უნდა გარდაქმნას მხოლოდ დაბალი რეგისტრის ინგლისური ასოები a-z, ხოლო
ყველა დანარჩენი სიმბოლო შეუცვლელი დატოვოს.
განშიფვრის ლოგიკა არის ზემოთ აღწერილი დაშიფვრით მიღებული ტექსტის
აღდგენა, ანუ მისი შებრუნებული პროცესი.
პროგრამამ ტექსტის გარდა უნდა მოგვთხოვოს e ან d-ს შეყვანა, სადაც e ნიშნავს
დაშიფვრის ბრძანებას, ხოლო d ნიშნავს განშიფვრის ბრძანებას. სხვა სიმბოლოს
შეყვანის შემთხვევაში მოგვთხოვოს თავიდან შეყვანა.

მაგ. 1:
Enter action (e/d): e
Enter text: power IS THE power
qpert IS THE qpert
მაგ. 2:
Enter action (e/d): d
Enter text: quyjpm IS COOL
python IS COOL
"""

lines = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

action = input('Enter action (e/d): ')
input_text = input('Enter text: ')

def encode_text(text):
    output_text = ''

    for i, c in enumerate(text):
        if ord(c) < ord('a') or ord(c) > ord('z'):
            output_text += c
        else:
            for line in lines:
                char_index = line.find(c)
                if char_index != -1:
                    if char_index == len(line) - 1:
                        output_text += line[0]
                    else:
                        output_text += line[char_index + 1]

    return output_text

def decode_text(text):
    output_text = ''

    for i, c in enumerate(text):
        if ord(c) < ord('a') or ord(c) > ord('z'):
            output_text += c
        else:
            for line in lines:
                char_index = line.find(c)
                if char_index != -1:
                    if char_index == 0:
                        output_text += line[-1]
                    else:
                        output_text += line[char_index - 1]

    return output_text

if action == 'e':
    print(encode_text(input_text))
elif action == 'd':
    print(decode_text(input_text))
