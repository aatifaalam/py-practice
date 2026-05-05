s = "A man, a plan, a canal: Panama"
s1 = ""
for ch in s:
    if ch.isalnum():      # sirf letters aur digits allow
        s1 += ch.lower()  # lowercase me convert