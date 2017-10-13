"""Script to call the credit-risk API
"""
import firefly

api = firefly.Client("https://credit-scoring-demo.rorocloud.io/")

row = { 
    'delinq_2yrs': 0.0,
    'delinq_2yrs_zero': 1.0,
    'dti': 8.7200000000000006,
    'emp_length_num': 0,
    'grade': 'F',
    'home_ownership': 'RENT',
    'inq_last_6mths': 3.0,
    'last_delinq_none': 1,
    'last_major_derog_none': 1,
    'open_acc': 2.0,
    'payment_inc_ratio': 4.5,
    'pub_rec': 0.0,
    'pub_rec_zero': 1.0,
    'purpose': 'vacation',
    'revol_util': 98.5,
    'short_emp': 0,
    'sub_grade_num': 1.0
}

result = api.predict(row=row)
print(result)
