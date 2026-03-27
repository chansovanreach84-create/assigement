trigger_words = ["urgent", "winner", "free", "money", "click", "guarantee", "act", "prize"]

email_1 = """
URGENT: You are a winner! Click here to claim your free money guarantee.
This is not a scam, it is 100% free. Act now to get your prize!
"""

email_2 = """
Hey team, just a quick reminder about the meeting tomorrow at 10 AM.
Please bring your project updates. Thanks!
"""

email_3 = """
I am writing to see if you have any free time this weekend.
I owe you money for lunch, so let me buy you a pizza!
"""

emails = [email_1, email_2, email_3]

for i, email in enumerate(emails, 1):
    
    email = email.lower()
    print(f"\n Processing Email_{i}.....")
    
    for ch in ".,!?%:":
        email = email.replace(ch, "")
    
    words = email.split()
    
    total_words = len(words)
    trigger_count = 0
    
    for word in words:
        if word in trigger_words:
            trigger_count += 1
    
    if total_words > 0:
        spam_score = (trigger_count / total_words) * 100
    else:
        spam_score = 0
    
    print(f"Total words: {total_words}")
    print(f"Trigger words: {trigger_count}")
    print(f"Spam Score: {spam_score:.2f}%")