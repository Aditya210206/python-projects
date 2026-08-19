alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(original_text,shift_amt,encode_or_decode):
    output_text=""
    if encode_or_decode=="decode":
        shift_amt*=-1
    for letter in original_text:
        if letter not in alphabets:
            output_text+=letter
        else:
            
            shifted_position=alphabets.index(letter)+shift_amt
            shifted_position%=len(alphabets)
            output_text+=alphabets[shifted_position]
    print(f"Here is your {encode_or_decode}d text: {output_text}")

game_over=True
while game_over:
    direction=input("Enter 'encode' to encrypt, and 'decode' to decrypt: ").lower()
    text=input("Type your message: ").lower()
    shift=int(input("Enter the number of shifts: "))
    caesar(text,shift,direction)
    restart=input("Type 'yes' if you want to continue and 'no' if you dont want to continue: ").lower()
    if restart=="no":
        game_over=False
        print("Goodbye!")
    else:
        game_over=True
