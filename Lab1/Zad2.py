n = 'There is no do..while :('
while n != 0:
  try:
    print('Type N (type 0 to exit):')
    n = int(input())
    if n == 0:
      break;
    automorphs = []
    for i in range(1, n):
      n_str = str(i)
      n_pow_str = str(i**2)
      n_str_len = len(n_str)
      n_pow_str_len = len(n_pow_str)
      len_diff = n_pow_str_len - n_str_len
      if n_pow_str[len_diff:] == n_str:
        automorphs.append(i)
    if automorphs:
      print('Automorhps:')
      for a in automorphs:
        print(str(a))
    else:
      print('There is no automorphs')
  except ValueError:
    print('Input type error')
    break;
