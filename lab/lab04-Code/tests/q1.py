test = {
  'name': 'Question 1: Lists',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> s = [7//3, 5, [4, 0, 1], 2]
          >>> s[0]
          2
          >>> s[2]
          [4, 0, 1]
          >>> s[-1]
          2
          >>> len(s)
          4
          >>> 4 in s
          False
          >>> 4 in s[2]
          True
          >>> s + [3 + 2, 9]
          [2, 5, [4, 0, 1], 2, 5, 9]
          >>> s[2] * 2
          [4, 0, 1, 4, 0, 1]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> x = [1, 2, 3, 4]
          >>> x[1:3]
          [2, 3]
          >>> x[:2]
          [1, 2]
          >>> x[1:]
          [2, 3, 4]
          >>> x[-2:3]
          [3]
          >>> x[-2:4]
          [3, 4]
          >>> x[0:4:2]
          [1, 3]
          >>> x[::-1]
          [4, 3, 2, 1]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
