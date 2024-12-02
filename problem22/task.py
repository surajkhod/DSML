# Compute Accuracy, Error rate, Precision, Recall for the following
# confusion matrix.

# Actual Class\Predicted class
# cancer =yes
# cancer = no 
# Total

# cancer = yes 90 210 300
# cancer = no 140 9560 9700
# Total 230 9770 10000


# Given values
TP = 90  # True Positives
FP = 140 # False Positives
FN = 210 # False Negatives
TN = 9560 # True Negatives
Total = 10000 # Total instances

# Accuracy
accuracy = (TP + TN) / Total

# Error Rate
error_rate = (FP + FN) / Total

# Precision (for class "Yes")
precision = TP / (TP + FP)

# Recall (for class "Yes")
recall = TP / (TP + FN)

print(f"Accuracy: {accuracy:.4f}")
print(f"Error Rate: {error_rate:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")