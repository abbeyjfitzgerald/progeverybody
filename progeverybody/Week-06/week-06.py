# using find() and string slicing to extract the number at the end of the line below. Convert the extracted value to a floating point number.

text = "X-DSPAM-Confidence:    0.8475";
number = float(text[text.find('0'):])
print number