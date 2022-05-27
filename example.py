fruit={"orange","mango","apples"}
print(fruit)
print(fruit)
print(fruit)

def outputName(a):
    print("hi",a)
outputName("shee")

# funtion to replace character in a string
def replace(phrase):
      word=""
      for letter in phrase:
          if letter.lower() in "aeiou":
                  word=word+"g"
          else:
             word=word+letter
      return word
print(replace_in (input("enter a phrase:")))