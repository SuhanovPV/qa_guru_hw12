from selene import browser, be, have, command

from student_registration_form import resources


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)
        return self

    def select_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()
        return self

    def fill_mobile(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element(f'.react-datepicker__year-select > option[value="{year}"]').click()
        browser.element(f'.react-datepicker__month-select > option[value="{month}"]').click()
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value)
        browser.element('#subjectsContainer div[id^="react-select"]').click()
        return self

    def scroll_to_page(self):
        browser.element('#subjectsInput').perform(command.js.scroll_into_view)
        return self

    def select_hobbies(self, value):
        browser.all('[id^=hobbies-checkbox-]+label').element_by(have.exact_text(value)).click()
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def upload_picture(self, value):
        browser.element("#uploadPicture").send_keys(resources.path(value))
        return self

    def select_state(self, value):
        browser.element('#state').click()
        browser.all('#state div[id^="react-select-"]').element_by(have.text(value)).click()
        return self

    def select_city(self, value):
        browser.element('#city').click()
        browser.all('#city div[id^="react-select-"]').element_by(have.text(value)).click()
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def should_have_register_user_with(self, *verification_data):

        for field, value in verification_data:
            browser.element(f'//td[preceding-sibling::td="{field}"]').should(have.exact_text(value))

