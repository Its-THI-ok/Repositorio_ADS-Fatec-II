# Solving problem

def transpose_two_strings(arr):
  returner = ''
  maxElement = len(arr[0]) if (len(arr[0]) >= len(arr[1])) else len(arr[1])
  limit = 0
  try:
    for i in range(0, maxElement):
      returner += f'{arr[0][i]} {arr[1][i]}'
      if i < maxElement - 1: returner += '\n'
  
  except (IndexError):
    limit = len(arr[0]) if (len(arr[0]) < len(arr[1])) else len(arr[1])

    while True:
      if limit > maxElement: break

      if(len(arr[0]) > limit):
        returner += f'{arr[0][limit]}  '
        
      elif (len(arr[1]) > limit):
        returner += f'  {arr[1][limit]}'

      limit += 1
      if limit < maxElement: returner += '\n'

  return returner

print(transpose_two_strings(["Hello","World"]))