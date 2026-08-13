first_name = "optimus"
second_name = "prime"
"""print(first_name+" "+second_name)   first method"""
""" print(f"hi {first_name}")          second method"""
"""third method
sentence = "hi {}"
print(sentence.format(first_name))"""
sentence = "hi {} {}"

print(sentence.format(first_name,second_name))
print(f"i am  {first_name} {second_name}  ")