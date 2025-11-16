def main():
    import sys

    def process_cases(lines, case_num=0, results=None):
        if results is None:
            results = []
        if not lines or case_num == int(lines[0]):
            return results
        x = int(lines[case_num * 2 + 1])
        yns = lines[case_num * 2 + 2].split()
        if len(yns) != x:
            results.append(-1)
        else:
            nums = list(map(int, yns))
            def sum_powers(nums):
                if not nums:
                    return 0
                y = nums[0]
                if y > 0:
                    return sum_powers(nums[1:])
                return y ** 4 + sum_powers(nums[1:])
            results.append(sum_powers(nums))
        return process_cases(lines, case_num + 1, results)

    lines = list(map(str.strip, sys.stdin.readlines()))
    output = process_cases(lines)
    for res in output:
        print(res)

if __name__ == "__main__":
    main()
