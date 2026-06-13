# Student Performance Predictor 

students = [
    {"hours": 1, "attendance": 60, "score": 40, "passed": 0},
    {"hours": 2, "attendance": 70, "score": 45, "passed": 0},
    {"hours": 3, "attendance": 75, "score": 50, "passed": 0},
    {"hours": 4, "attendance": 80, "score": 55, "passed": 1},
    {"hours": 5, "attendance": 85, "score": 60, "passed": 1},
    {"hours": 6, "attendance": 90, "score": 65, "passed": 1},
    {"hours": 7, "attendance": 95, "score": 70, "passed": 1},
    {"hours": 8, "attendance": 100, "score": 75, "passed": 1},
    {"hours": 2, "attendance": 65, "score": 42, "passed": 0},
    {"hours": 3, "attendance": 72, "score": 48, "passed": 0},
    {"hours": 4, "attendance": 78, "score": 52, "passed": 1},
    {"hours": 5, "attendance": 82, "score": 58, "passed": 1},
    {"hours": 6, "attendance": 88, "score": 62, "passed": 1},
    {"hours": 7, "attendance": 92, "score": 67, "passed": 1},
    {"hours": 8, "attendance": 98, "score": 72, "passed": 1},
    {"hours": 9, "attendance": 100, "score": 80, "passed": 1},
    {"hours": 1, "attendance": 55, "score": 35, "passed": 0},
    {"hours": 2, "attendance": 62, "score": 38, "passed": 0},
    {"hours": 3, "attendance": 68, "score": 44, "passed": 0},
    {"hours": 4, "attendance": 75, "score": 49, "passed": 0},
    {"hours": 5, "attendance": 80, "score": 54, "passed": 1},
    {"hours": 6, "attendance": 85, "score": 59, "passed": 1},
    {"hours": 7, "attendance": 90, "score": 64, "passed": 1},
    {"hours": 8, "attendance": 94, "score": 69, "passed": 1},
    {"hours": 9, "attendance": 99, "score": 78, "passed": 1},
    {"hours": 10, "attendance": 100, "score": 85, "passed": 1},
    {"hours": 2, "attendance": 58, "score": 36, "passed": 0},
    {"hours": 3, "attendance": 65, "score": 42, "passed": 0},
    {"hours": 4, "attendance": 72, "score": 48, "passed": 0},
    {"hours": 5, "attendance": 78, "score": 53, "passed": 1},
    {"hours": 3, "attendance": 70, "score": 46, "passed": 0},
    {"hours": 4, "attendance": 76, "score": 51, "passed": 0},
    {"hours": 5, "attendance": 81, "score": 56, "passed": 1},
    {"hours": 6, "attendance": 86, "score": 61, "passed": 1},
    {"hours": 7, "attendance": 91, "score": 66, "passed": 1},
    {"hours": 8, "attendance": 96, "score": 71, "passed": 1},
    {"hours": 9, "attendance": 100, "score": 79, "passed": 1},
    {"hours": 10, "attendance": 100, "score": 88, "passed": 1},
    {"hours": 1, "attendance": 50, "score": 30, "passed": 0},
    {"hours": 2, "attendance": 55, "score": 34, "passed": 0},
    {"hours": 3, "attendance": 60, "score": 38, "passed": 0},
    {"hours": 4, "attendance": 65, "score": 42, "passed": 0},
    {"hours": 5, "attendance": 70, "score": 46, "passed": 0},
    {"hours": 6, "attendance": 75, "score": 50, "passed": 0},
    {"hours": 7, "attendance": 80, "score": 54, "passed": 1},
    {"hours": 8, "attendance": 85, "score": 58, "passed": 1},
    {"hours": 9, "attendance": 90, "score": 62, "passed": 1},
    {"hours": 10, "attendance": 95, "score": 66, "passed": 1},
    {"hours": 1, "attendance": 52, "score": 32, "passed": 0},
    {"hours": 2, "attendance": 57, "score": 36, "passed": 0},
    {"hours": 3, "attendance": 62, "score": 40, "passed": 0},
    {"hours": 4, "attendance": 67, "score": 44, "passed": 0},
    {"hours": 5, "attendance": 72, "score": 48, "passed": 0},
    {"hours": 6, "attendance": 77, "score": 52, "passed": 1},
    {"hours": 7, "attendance": 82, "score": 56, "passed": 1},
    {"hours": 8, "attendance": 87, "score": 60, "passed": 1},
    {"hours": 9, "attendance": 92, "score": 64, "passed": 1},
    {"hours": 10, "attendance": 97, "score": 68, "passed": 1},
    {"hours": 2, "attendance": 63, "score": 40, "passed": 0},
    {"hours": 3, "attendance": 69, "score": 45, "passed": 0},
    {"hours": 4, "attendance": 74, "score": 50, "passed": 0},
    {"hours": 5, "attendance": 79, "score": 55, "passed": 1},
    {"hours": 6, "attendance": 84, "score": 60, "passed": 1},
    {"hours": 7, "attendance": 89, "score": 65, "passed": 1},
    {"hours": 8, "attendance": 94, "score": 70, "passed": 1},
    {"hours": 9, "attendance": 99, "score": 75, "passed": 1},
    {"hours": 10, "attendance": 100, "score": 82, "passed": 1},
    {"hours": 1, "attendance": 58, "score": 38, "passed": 0},
    {"hours": 2, "attendance": 64, "score": 43, "passed": 0},
    {"hours": 3, "attendance": 71, "score": 48, "passed": 0},
    {"hours": 4, "attendance": 77, "score": 53, "passed": 1},
    {"hours": 5, "attendance": 83, "score": 58, "passed": 1},
    {"hours": 6, "attendance": 89, "score": 63, "passed": 1},
    {"hours": 7, "attendance": 94, "score": 68, "passed": 1},
    {"hours": 8, "attendance": 99, "score": 73, "passed": 1},
    {"hours": 9, "attendance": 100, "score": 81, "passed": 1},
    {"hours": 10, "attendance": 100, "score": 90, "passed": 1},
    {"hours": 2, "attendance": 66, "score": 41, "passed": 0},
    {"hours": 3, "attendance": 73, "score": 47, "passed": 0},
    {"hours": 4, "attendance": 79, "score": 52, "passed": 1},
    {"hours": 5, "attendance": 84, "score": 57, "passed": 1},
    {"hours": 6, "attendance": 90, "score": 62, "passed": 1},
    {"hours": 7, "attendance": 95, "score": 67, "passed": 1},
    {"hours": 8, "attendance": 99, "score": 72, "passed": 1},
    {"hours": 9, "attendance": 100, "score": 80, "passed": 1},
    {"hours": 10, "attendance": 100, "score": 85, "passed": 1},
    {"hours": 1, "attendance": 54, "score": 34, "passed": 0},
    {"hours": 2, "attendance": 60, "score": 39, "passed": 0},
    {"hours": 3, "attendance": 66, "score": 44, "passed": 0},
    {"hours": 4, "attendance": 72, "score": 49, "passed": 0},
    {"hours": 5, "attendance": 77, "score": 54, "passed": 1},
    {"hours": 6, "attendance": 82, "score": 59, "passed": 1},
    {"hours": 7, "attendance": 87, "score": 64, "passed": 1},
    {"hours": 8, "attendance": 92, "score": 69, "passed": 1},
    {"hours": 9, "attendance": 97, "score": 74, "passed": 1},
    {"hours": 10, "attendance": 100, "score": 84, "passed": 1},
]

# Simple formula: score + attendance/2 + hours*5
def predict(hours, attendance, score):
    total = score + (attendance / 2) + (hours * 5)
    if total >= 100:
        return "PASS"
    else:
        return "FAIL"

# Test predictions
tests = [[4, 80, 55], [2, 65, 42], [7, 95, 70], [3, 70, 48], [6, 88, 62], [9, 100, 80], [10, 100, 85]]

print("Predictions:")
for t in tests:
    result = predict(t[0], t[1], t[2])
    print(t, "->", result)

# Calculate accuracy
correct = 0
for s in students:
    result = predict(s["hours"], s["attendance"], s["score"])
    expected = "PASS" if s["passed"] == 1 else "FAIL"
    if result == expected:
        correct += 1

print("\nAccuracy:", round((correct / len(students)) * 100, 2), "%")
print("Total students:", len(students))