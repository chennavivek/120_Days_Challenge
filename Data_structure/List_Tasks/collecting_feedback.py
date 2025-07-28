feedback = ["Great", "Good", "Better", "Excellent", "Very Good"]
feedback.append("okok!")

# Counting specific feedback (case-insensitive check)
positive_feedback_count = sum(
    1 for comment in feedback 
    if "great" in comment.lower() or "excellent" in comment.lower()
)

print(f"Positive feedback count: {positive_feedback_count}")
print("User Feedback:")
for comment in feedback:
    print(f"- {comment}")