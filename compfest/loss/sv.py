import itertools
import string

def check(code: str) -> bool:
    if len(code) < 170 or len(code) > 181:
        return False

    if "CF=16" not in code and "dist=0" not in code:
        return False

    if sum(int(ch) for ch in code if ch.isdigit()) != 0xCF:
        return False

    blacklist = ["use", "std"]
    return all(bl not in code for bl in blacklist)

def brute_force_code():
    digits = '0123456789'
    base_code = "CF=16\n"  # Add a required string to ensure it's present
    target_sum = 0xCF  # 207 in decimal

    for length in range(170, 182):
        for combination in itertools.product(digits, repeat=length - len(base_code)):
            candidate = base_code + ''.join(combination)
            if check(candidate):
                print("Valid code found:")
                print(candidate)
                return

    print("No valid code found.")

if __name__ == "__main__":
    brute_force_code()
