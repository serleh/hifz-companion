def interpret_alignment(operations):
    feedback = []

    for operation in operations:
        if operation[0] == "skip":
            feedback.append(
                {
                    "type": "possible_skip",
                    "expected_word": operation[1],
                }
            )

        elif operation[0] == "extra":
            feedback.append(
                {
                    "type": "possible_extra",
                    "recognized_word": operation[1],
                }
            )


        elif operation[0] == "substitute":
            feedback.append(
                {
                    "type": "possible_substitution",
                    "expected_word": operation[1],
                    "recognized_word": operation[2],
                }
            )

        

    return feedback