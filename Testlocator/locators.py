class l_forgot:
    pwd_link = '//*[@class="orangehrm-login-forgot"]/p'
    user = 'username'
    forgot_btn = 'button[class*="forgot-password-button--reset"]'
    success_msg = 'h6[class*="forgot-password-title"]'


class Login:
    # Login
    username_input_box = "username"
    password_input_box = "password"
    submit_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    invalid_msg = "//*[contains(@class,'alert-content-text')]"
    header_text = "//h6[contains(@class,'topbar-header')]"


class option:
    admin_opt = '//ul[@class="oxd-main-menu"]//li[1]//a'
    navig = '//nav[@class="oxd-topbar-body-nav"]/ul//li'


class menu:
    opt = '//ul[@class="oxd-main-menu"]//li'
