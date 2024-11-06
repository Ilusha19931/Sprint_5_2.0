import random
import  string

letters = string.ascii_letters
random_string = ''.join(random.choice(letters) for _ in range(5))

random_pass_uncorrect = random.randint(100, 999)
random_pass_correct = random.randint(100000, 999999)

random_email = f"{random_string}@15{random_pass_uncorrect}.ru"
random_pass =  f"{random_pass_uncorrect}{random_string}"

email_login = "ilya.mzokov15151@yandex.ru"
pass_login = "tayesthecat"