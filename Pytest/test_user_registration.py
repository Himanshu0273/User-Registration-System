import pytest
from user_registration_system import valid_name, valid_email, valid_number, valid_password
from faker import Faker
import random
import string
from loguru import logger

logger.add("failed_testcases.log", level="ERROR")
fake = Faker()

#----------------NAME----------------

def generate_valid_name():
    name = fake.first_name()
    while len(name) <= 2 or not name[0].isupper() or not name.isalpha():
        name = fake.first_name()
    
    return name

def generate_invalid_name():
    invalids=[
        fake.word().lower(),
        fake.word().upper(),
        fake.pystr(min_chars=1, max_chars=2),
        fake.password(length=5, special_chars=True, digits=True, lower_case=True, upper_case=False)
    ]
    return random.choice(invalids)


#----------------PHONE----------------

def generate_valid_phone():
    return f"{fake.random_number(digits=2, fix_len =True)} {fake.random_number(digits=10, fix_len=True)}"

def generate_invalid_phone():
    invalids=[
        lambda: fake.msisdn(),
        lambda: fake.random_number(digits=12, fix_len=True),
        lambda: ''.join(random.choices(string.ascii_lowercase, k=10)),
        lambda: f"{fake.random_number(digits=3, fix_len=True)} {fake.random_number(digits=5, fix_len=True)}",
        lambda: f"{fake.random_number(digits=2, fix_len=True)}-{fake.random_number(digits=10, fix_len=True)}",
        lambda: f"{fake.random_number(digits=2, fix_len=True)} {fake.random_number(digits=12, fix_len=True)}",
    ]
    return random.choice(invalids)()

#----------------EMAIL----------------

def generate_valid_email():
    domains = ["gmail.com", "yahoo.com", "abc.co.in"]
    return f"{fake.user_name()}@{random.choice(domains)}"

def generate_invalid_email():
    invalids = [
        fake.word(), "abc.com", "abc@com", "@gmail.com", "abc@gmail", "abc@.com"
    ]
    return random.choice(invalids)

# ----------------PASSWORD----------------

def generate_valid_password():
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special_char = random.choice("!@#$%^&*")
    rest=''.join(random.choices(string.ascii_letters+string.digits, k=5))
    
    password = list(upper+digit+special_char+rest)
    random.shuffle(password)
    return ''.join(password)

def generator_invalid_password():
    invalids=[
        fake.password(length=random(1,7)),
        fake.password(length=10,special_chars=False, upper_case=False, digits=False),
        fake.password(length=10, special_chars=True, upper_case=True, digits=True)+"!",
        fake.password(length=10, special_chars=False, digits=True, upper_case=True)        
    ]    
    return random.choice(invalids)

#----------------Test Data Generation----------------

def generate_test_data():
    positive=[]
    negative=[]
    for _ in range(1000):
        valid_entry={
            "first_name": generate_valid_name(),
            "second_name": generate_valid_name(),
            "phone": generate_valid_phone(),
            "email": generate_valid_email(),
            "password": generate_valid_password()
        }
        positive.append(valid_entry)
        
        invalid_entry={
            "first_name": generate_invalid_name(),
            "second_name": generate_valid_name(),
            "phone": generate_invalid_phone(),
            "email": generate_invalid_email(),
            "password": generate_valid_password()
        }
        
        negative.append(invalid_entry)
        
    return {"positive": positive, "negative": negative}

#----------------Simple Validator----------------

def validate_input(data):
    first_name=data["first_name"]
    second_name=data["second_name"]
    phone=data["phone"]
    email=data["email"]
    password=data["password"]
    
    #Rules for first name
    if len(first_name)<=2 or not first_name[0].isupper() or not first_name.isalpha():
        return False
    
    #Rules for second name
    if len(second_name)<=2 or not second_name[0].isupper() or not second_name.isalpha():
        return False
    
    #Rules for email
    if "@" not in email or "." not in email.split("@")[-1]:
        return False
    
    #Rules for phone number
    parts = str(phone).split(" ")
    if len(parts[0]) != 2 or not (parts[0].isdigit() and parts[1].isdigit()) or len(parts[1]) != 10:
        return False
    
    #Rules for password
    specials = "!@#$%^&*"
    special_count = sum(1 for c in password if c in specials)
    if special_count != 1:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if len(password) < 8:
        return False
    
    return True
    
#----------------Test Cases----------------

test_data = generate_test_data()

@pytest.mark.parametrize("input_data", test_data["positive"])
def test_positive_cases(input_data):
    result = validate_input(input_data)
    try:
        assert result == True
    except AssertionError as e:
        logger.error(f"[Positive Test Case Failed!!] Case:{input_data}\nReason:{e}")
    
@pytest.mark.parametrize("input_data", test_data["negative"])
def test_negative_cases(input_data):
    result = validate_input(input_data)
    try:
        assert result==False
    except AssertionError as e:
        logger.error(f"[Negative Test Case Failed!!] Case:{input_data}\nReason:{e}")