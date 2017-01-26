def test_cases(number):
    return test_cases[number]

testCases = [
    # [severity, description]
    ['Blocker','Main Navigation Bar should be displayed'],
    ['Blocker', 'Valid user should be able to login'],
    ['Blocker', 'Invalid user should not be able to login'],
    ['Blocker', 'Invalid user with only username should not be able to login'],
    ['Blocker', 'Invalid user with only password should not be able to login'],
    ['Blocker', 'Invalid user without any credentials should not be able to login'],
]