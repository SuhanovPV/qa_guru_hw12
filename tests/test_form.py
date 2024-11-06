import allure

from student_registration_form.pages.registration_page import RegistrationPage

@allure.feature('Student registration')
@allure.title('Submit student registration form')
def test_fill_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page \
        .fill_first_name('Pavel') \
        .fill_last_name('Sukhar') \
        .fill_email('sukhar@mail.com') \
        .select_gender('Male') \
        .fill_mobile('8800535653') \
        .fill_date_of_birth('1988', '3', '05') \
        .fill_subjects('Maths') \
        .fill_subjects('Computer Science') \
        .select_hobbies('Sports') \
        .select_hobbies('Music') \
        .fill_current_address('Bawana Rd, Shahabad Daulatpur, Shahabad Daulatpur Village, Rohini') \
        .upload_picture('pic.png') \
        .select_state('Rajasthan') \
        .select_city('Jaipur') \
        .submit()

    # THEN
    registration_page.should_have_register_user_with(
        ('Student Name','Pavel Sukhar'),
        ('Student Email','sukhar@mail.com'),
        ('Gender','Male'),
        ('Mobile', '8800535653'),
        ('Date of Birth', '05 April,1988'),
        ('Subjects','Maths, Computer Science'),
        ('Hobbies', 'Sports, Music'),
        ('Picture', 'pic.png'),
        ('Address', 'Bawana Rd, Shahabad Daulatpur, Shahabad Daulatpur Village, Rohini'),
        ('State and City','Rajasthan Jaipur')
    )
