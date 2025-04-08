def add_many_numbers(numbers) ->int:

  total_sum: int = 0
  for number in numbers:
    total_sum += number
  return total_sum


def main():

  numbers: list[int] = [1,2,3,4,5]
  sum_of_numbers: int = add_many_numbers(numbers)
  print(sum_of_numbers)


if __name__ == "__main__":
  main()