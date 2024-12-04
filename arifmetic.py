class Segment:
    def __init__(self, left, right, character):
        self.left = left
        self.right = right
        self.character = character

def define_segments(letters, probabilities):
    sorted_letters_with_probs = sorted(zip(letters, probabilities), key=lambda x: x[1])
    segments = []
    l = 0.0
    for letter, prob in sorted_letters_with_probs:
        right = l + prob
        segments.append(Segment(l, right, letter))
        l = right
    return segments

def arithmetic_encoding(text, letters, probabilities):
    segments = define_segments(letters, probabilities)
    left, right = 0.0, 1.0
    print(f"Начальные границы: {left:.16} - {right:.16}")

    for char in text:
        for segment in segments:
            if segment.character == char:
                range_width = right - left
                right = left + range_width * segment.right
                left = left + range_width * segment.left
                print(f"Символ: '{char}' - Левая граница: {left:.16f}, Правая граница: {right:.16f}")
                break

    encoded_value = (left + right) / 2
    return encoded_value

text = "бастрыгинтимофейсергеевич"
letters = ['а', 'б', 'в', 'й', 'м', 'н', 'о', 'ф', 'ч', 'ы', 'г', 'р', 'с', 'т', 'и', 'е']
probabilities = [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.08, 0.08, 0.08, 0.08, 0.12, 0.16]

encoded_value = arithmetic_encoding(text, letters, probabilities)

print(f"\nЗакодированное значение: {encoded_value:.16f}")
