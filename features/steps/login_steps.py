from behave import given, when, then

# Day 4: Contracts only. No Selenium. No requests.
# Day 8: We'll implement these against saucedemo.com
# Day 9: We'll implement these against restful-booker API

@given('a registered user exists with password "{password}"')
def step_impl(context, password):
    """Day 11: This will call db_client.UserRepo.create_user()"""
    context.test_password = password
    # TODO Day 11: Seed user in DB for 50ms setup
    pass

@given('the user is logged in')
def step_impl(context):
    """Day 8: This will call LoginPage.login()"""
    # TODO Day 8: Use Page Object to log in via UI
    pass

@when('the user logs in with valid credentials')
def step_impl(context):
    """Day 8: Calls LoginPage.login(valid_user, valid_pass)"""
    # TODO Day 8: context.login_page.login()
    pass

@when('the user logs in with password "{password}"')
def step_impl(context, password):
    """Day 8: Calls LoginPage.login(valid_user, password)"""
    context.invalid_password = password
    # TODO Day 8: context.login_page.login()
    pass

@when('the user logs out')
def step_impl(context):
    """Day 8: Calls DashboardPage.logout()"""
    # TODO Day 8: context.dashboard_page.logout()
    pass

@then('the user sees their account dashboard')
def step_impl(context):
    """Day 8: Asserts DashboardPage.is_visible()"""
    # TODO Day 8: assert context.dashboard_page.is_visible()
    pass

@then('the user sees a welcome message')
def step_impl(context):
    """Day 8: Asserts DashboardPage.welcome_text()"""
    # TODO Day 8: assert "Welcome" in context.dashboard_page.welcome_text()
    pass

@then('the user sees an authentication error')
def step_impl(context):
    """Day 8: Asserts LoginPage.error_message()"""
    # TODO Day 8: assert context.login_page.error_message() is not None
    pass

@then('the user remains on the login page')
def step_impl(context):
    """Day 8: Asserts LoginPage.is_visible()"""
    # TODO Day 8: assert context.login_page.is_visible()
    pass

@then('the user sees the login page')
def step_impl(context):
    """Day 8: Asserts LoginPage.is_visible()"""
    # TODO Day 8: assert context.login_page.is_visible()
    pass

@then('the user cannot access the dashboard')
def step_impl(context):
    """Day 8: Asserts DashboardPage.is_visible() == False"""
    # TODO Day 8: assert not context.dashboard_page.is_visible()
    pass