from behave import *
from funcs import *
use_step_matcher("re")


@given('a calculator')
def step_impl(context):
    pass


@when(r'User inputs a parameter (?P<numbers>(?:\d*\.?\d*))')
def step_impl(context, numbers):
    context.a = numbers


@then(r"outputs (?P<numbers>(?:\d*\.?\d*))")
def step_impl(context, numbers):
    assert trignometry.cos(context.a) == float(numbers)
